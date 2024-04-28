from django.shortcuts import get_object_or_404, render
from django.views import View

from .models import Category, TypeService
from .forms import *
from django.db.models import Q


# display all typeservice
class AllTypeServiceView(View):
    def get(self, request):
        typeservice = TypeService.objects.all()
        context = {'typeservice': typeservice}
        return render(request, 'service/service.html', context)
          

# display detail typeservice
class DetailTypeServiceView(View):
    def get(self, request, slug):
        typeservice = get_object_or_404(TypeService, slug=slug)
        category = Category.objects.filter(sub_cat=False)
        form = SearchTypeService()
        if 'search' in request.GET:
           form = SearchTypeService(request.GET)
        if form.is_valid():
            data = form.cleaned_data['search']
            data = category.filter(Q(name__icontains=data))
           
        if slug:
            typeservice_slug = get_object_or_404(TypeService, slug=slug)
        context = {'typeservice': typeservice,'typeservice_slug': typeservice_slug,
                    'category': category,'form' : form ,}
        return render(request, 'service/detail_service.html', context)


# Display List Category
class CategoryAndSubView(View):
    def get(self, request, slug=None):
        category = Category.objects.filter(sub_cat=False)
        if slug:
            category_slug = get_object_or_404(Category, slug=slug)
        context = {'category': category,'category_slug':category_slug}
        return render(request, 'service/service.html', context)
    



# def category_and_sub(request, slug=None): 
#     category = Category.objects.all()
#     if slug: 
#         category = get_object_or_404(Category, slug=slug) 
#     context = {'category': category} 
#     return render(request, 'service/service.html', context)



  
                                                  

