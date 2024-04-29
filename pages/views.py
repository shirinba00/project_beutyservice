from django.shortcuts import get_object_or_404, render
from django.views import View

from .models import Category, AboutUS
from django.db.models import Q

# display AbouUs
class AllTypeServiceView(View):
    def get(self, request):
        aboutus = AboutUS.objects.all()
        context = {'aboutus': aboutus}
        return render(request, 'pages/AboutUs.html', context)
