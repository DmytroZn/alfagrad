from django.shortcuts import render
from .models import LastProjects, BaseLevel, Location, Contacts

# Create your views here.

def main(request):
    obj = LastProjects.objects.all()
    base_level = BaseLevel.objects.first()
    location = Location.objects.first()
    contacts = Contacts.objects.all()


    template = 'main/index.html'
    context = {
        'objs' : obj, 
        'base_level':base_level,
        'location':location,
        'contacts':contacts
        }
    return render(request, template, context)