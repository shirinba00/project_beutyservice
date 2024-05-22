from pages.models import AboutUS

def  aboutus(request):
    return {'aboutus': AboutUS(request)}