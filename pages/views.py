from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.db.models import Q
from django.contrib import messages
from pages.forms import ContactUSForm
from service.forms import ReserveServiceForm
from service.models import TypeService
from .models import AboutUS, ContactUs, ImageAboutUs

# display AbouUs
class AllAboutUsView(View):
    def get(self, request):
        typeservice = TypeService.objects.all()
        reserveservice_form = ReserveServiceForm()
        aboutus = AboutUS.objects.all()
        context = {'aboutus': aboutus,'typeservice': typeservice,'reserveservice_form': reserveservice_form}
        return render(request, 'pages/AboutUs.html', context)
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
          


# display ImageAbouUs
class AllImageView(View):
    def get(self, request):
        image_about = ImageAboutUs.objects.all()
        context = {'image_about': image_about,}
        return render(request, 'pages/AboutUs.html', context)
    

class ContactUsView(View):
    def get(self, request):
        aboutus = AboutUS.objects.all()
        context = {'aboutus': aboutus,}
        url = request.META.get('HTTP_REFERER')
        return render(request, 'pages/contactus.html', context)

    def post(self, request):
        url = request.META.get('HTTP_REFERER')
        contactus_form = ContactUSForm(request.POST)
        # aboutus = AboutUS.objects.all()
        if contactus_form.is_valid():
            data = contactus_form.cleaned_data
            ContactUs.objects.create(fullname=data['fullname'],email=data['email'],
                                      phone=data['phone'], text=data['text'],)
            messages.success(request, 'نظر شما با موفقیت ثبت شد.')
            return redirect(url)
        else:
            messages.error(request, 'ثبت نظر با مشکل مواجه شد لطفا دوباره تلاش کنید.')
            return redirect(url)