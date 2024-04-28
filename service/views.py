from django.shortcuts import render

from .models import TypeService


# display all typeservice
def all_typeservice(request):
    typeservice = TypeService.objects.all()

    return render(request, 'service/service.html',
                  {'typeservice' :typeservice,
                 
                   })


