from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib import messages
from .models import Category, ReserveService, Skill, TypeService,PersonService
from .forms import *
from django.db.models import Q
from taggit.models import Tag
from django.core.paginator import Paginator


class PersonServiceView(View):
    personservice = PersonService.objects.all()
    def get(self, request):
        personservice = PersonService.objects.all()
        typeservice = TypeService.objects.all()
        context = {'personservice': personservice,'typeservice':typeservice}
        return render(request, 'service/team.html', context)


def personservice_detail(request, personservice_id,):
    personservice = get_object_or_404(PersonService, id=personservice_id)
    similar = personservice.tags.similar_objects()[:4]
    skill = Skill.objects.all()
    return render(request, 'service/team_detail.html', {'personservice': personservice,
                                                         'similar': similar,
                                                         'skill':skill,
                                                         })



# display all typeservice
class AllTypeServiceView(View):
    typeservice = TypeService.objects.all()
   
    def get(self, request):
        person_service = TypeService.objects.all()
        reserveservice_form = ReserveServiceForm()
        typeservice = TypeService.objects.all()
        context = {'person_service': person_service, 'form': reserveservice_form,'typeservice': typeservice, }
        return render(request, 'service/service.html', context)

    def post(self, request):
        reserveservice_form = ReserveServiceForm(request.POST)
        typeservice = TypeService.objects.all()
        if reserveservice_form.is_valid():
            reserveservice_form.save()
            messages.success(request, 'Your reservation has been successfully submitted.')
            return redirect('service:typeservice')
        else:
            messages.error(request, 'Failed to submit reservation. Please check the form.')
            typeservice = TypeService.objects.all()
            context = {'typeservice': typeservice, 'form': reserveservice_form}
            return render(request, 'service/service.html', context)
          

# display detail typeservice
class DetailTypeServiceView(View):
    typeservice = TypeService.objects.all()
    def get(self, request, slug):
        typeservice = get_object_or_404(TypeService, slug=slug)
        category = Category.objects.filter(sub_cat=False)
        form = SearchTypeService()
        reserveservice_form = ReserveServiceForm()
        typeservice2 = TypeService.objects.all()
        if 'search' in request.GET:
           form = SearchTypeService(request.GET)
        if form.is_valid():
            data = form.cleaned_data['search']
            data = category.filter(Q(name__icontains=data))
           
        if slug:
            typeservice_slug = get_object_or_404(TypeService, slug=slug)
        context = {'typeservice': typeservice,'typeservice_slug': typeservice_slug,
                    'category': category,'form' : form ,
                    'reserveservice_form':reserveservice_form,'typeservice2': typeservice2,}
        return render(request, 'service/detail_service.html', context)
    def post(self, request):
        reserveservice_form = ReserveServiceForm(request.POST)
        typeservice2 = TypeService.objects.all()
        if reserveservice_form.is_valid():
            reserveservice_form.save()
            messages.success(request, 'Your reservation has been successfully submitted.')
            return redirect('service:detail_service')
        else:
            messages.error(request, 'Failed to submit reservation. Please check the form.')
            typeservice2 = TypeService.objects.all()
            context = {'typeservice2': typeservice2, 'form': reserveservice_form}
            return render(request, 'service/service.html', context)
    


# Display List Category
class CategoryAndSubView(View):
    def get(self, request, slug=None):
        typeservice = TypeService.objects.all()
        category = Category.objects.filter(sub_cat=False)
        if slug:
            category_slug = get_object_or_404(Category, slug=slug)
        context = {'category': category,'category_slug':category_slug,'typeservice':typeservice,}
        return render(request, 'service/service.html', context)
    




# display products by tag

from django.core.exceptions import ObjectDoesNotExist

def typeservice_list_by_tag(request, tag_id, slug):
    categories = Category.objects.filter(sub_cat=False)
    try:
        clicked_tag = get_object_or_404(Tag, id=tag_id)
    except ObjectDoesNotExist:
        raise Http404("Tag does not exist")
    
    try:
        data = get_object_or_404(Category, slug=slug)
    except ObjectDoesNotExist:
        raise Http404("Category does not exist")
    
    service = TypeService.objects.filter(tags=clicked_tag)
    
    s_form = SearchTypeService()
    
    paginator = Paginator(service, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if 'search' in request.GET:
        s_form = SearchTypeService(request.GET)
        if s_form.is_valid():
            data = s_form.cleaned_data['search']
            if data.isdigit():
                page_obj = service.filter(Q(name__icontains=data))
            paginator = Paginator(page_obj, 8)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
    
    if slug:
        data = get_object_or_404(Category, slug=slug)
        page_obj = service.filter(category=data)
        paginator = Paginator(page_obj, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    
    return render(request, "service/service.html", {
        'service': page_obj,
        'categories': categories,
        's_form': s_form,
    })