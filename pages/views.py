from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.db.models import Q
from django.contrib import messages
from pages.forms import ContactUSForm
from .models import AboutUS, ContactUs, ImageAboutUs

# display AbouUs
class AllAboutUsView(View):
    def get(self, request):
        aboutus = AboutUS.objects.all()
        context = {'aboutus': aboutus,}
        return render(request, 'pages/AboutUs.html', context)


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