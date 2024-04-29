from django.shortcuts import get_object_or_404, render
from django.views import View

from .models import AboutUS, ImageAboutUs
from django.db.models import Q

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