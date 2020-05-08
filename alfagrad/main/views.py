from django.shortcuts import render
from .models import LastProjects, BaseLevel, Location, Contacts



# Create your views here.

def main(request):
    title = 'Альфаград, заборы'
    obj = LastProjects.objects.all()
    base_level = BaseLevel.objects.first()
    location = Location.objects.first()
    contacts = Contacts.objects.all()
    template = 'main/index.html'
    context = {
        'objs' : obj, 
        'base_level':base_level,
        'location':location,
        'contacts':contacts,
        'title':title,
        }
    return render(request, template, context)


def view(request, pk):
    title = 'заборы не дорого, Киев'
    obj = LastProjects.objects.get(title=pk)
    location = Location.objects.first()
    contacts = Contacts.objects.all()
    template = 'main/view.html'
    context = {
        'objs' : obj, 
        'location':location,
        'contacts':contacts,
        'title':title,

        }
    return render(request, template, context)

def about_us(request):
    title = 'заборы не дорого, Киев'
    base_level = BaseLevel.objects.first()
    location = Location.objects.first()
    contacts = Contacts.objects.all()
    template = 'main/about_us.html'
    context = {
        'base_level':base_level,
        'location':location,
        'contacts':contacts,
        'title':title,

        }
    return render(request, template, context)

def all_projects(request):
    title = 'заборы не дорого, Киев'
    objs = LastProjects.objects.all()
    location = Location.objects.first()
    contacts = Contacts.objects.all()
    template = 'main/all_project.html'
    context = {
        'objs':objs,
        'location':location,
        'contacts':contacts,
        'title':title,

        }
    return render(request, template, context)



