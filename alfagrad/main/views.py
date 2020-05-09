from django.shortcuts import render
from .models import LastProjects, BaseLevel, Location, Contacts

from django.http import HttpResponse
from django.views.decorators.http import require_GET

# Create your views here.

def main(request):
    title = 'Установка заборов под ключ | Альфаград'
    contact_phone = Contacts.objects.first()
    description = f'Заборы под ключ, установка заборов. Строительство, ремонт, монтаж. Киев и киевская область. Качественно не дорого. Звоните {contact_phone.phone}'
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
        'description':description
        }
    return render(request, template, context)


def view(request, pk):
    obj = LastProjects.objects.get(title=pk)
    title = f'{obj.title} - установка, монтаж и хорошее качество | Альфаград'
    contact_phone = Contacts.objects.first()
    description = f'{obj.title} - установка заборов под ключ, ремонт, монтаж. Киев и киевская область. Качественно не дорого. Звоните {contact_phone.phone}'
    location = Location.objects.first()
    contacts = Contacts.objects.all()
    template = 'main/view.html'
    context = {
        'objs' : obj, 
        'location':location,
        'contacts':contacts,
        'title':title,
        'description':description,

        }
    return render(request, template, context)

def about_us(request):
    title = 'Строительстро, монтаж, заборы, не дорого | Альфаград'
    contact_phone = Contacts.objects.first()
    description = f'Заборы под ключ, установка заборов, ремонт, монтаж. Киев и киевская область. Качественно не дорого. Звоните {contact_phone.phone}'
    base_level = BaseLevel.objects.first()
    location = Location.objects.first()
    contacts = Contacts.objects.all()
    template = 'main/about_us.html'
    context = {
        'base_level':base_level,
        'location':location,
        'contacts':contacts,
        'title':title,
        'description':description,

        }
    return render(request, template, context)

def all_projects(request):
    title = 'Заборы не дорого | Альфаград'
    contact_phone = Contacts.objects.first()
    description = f'Заборы под ключ, установка заборов, ремонт, монтаж. Киев и киевская область. Качественно не дорого. Звоните {contact_phone.phone}'
    objs = LastProjects.objects.all()
    location = Location.objects.first()
    contacts = Contacts.objects.all()
    template = 'main/all_project.html'
    context = {
        'objs':objs,
        'location':location,
        'contacts':contacts,
        'title':title,
        'description':description,

        }
    return render(request, template, context)



@require_GET
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow:"
        # "User-Agent: *",
        # "Disallow: /private/",
        # "Disallow: /junk/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

