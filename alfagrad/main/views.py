from django.shortcuts import render
from .models import LastProjects, BaseLevel, Location, Contacts, SubText
from .forms import FormAskQuestions

from django.http import HttpResponse
from django.views.decorators.http import require_GET
import os

# Create your views here.

def main(request):
    form_question = FormAskQuestions(request.POST)
    if form_question.is_valid():
        form_question.save()

    form = FormAskQuestions
    title = 'Установка заборов под ключ | Альфаград'
    contact_phone = Contacts.objects.first()
    description = f'Заборы под ключ, установка заборов. Строительство, ремонт, монтаж. Киев и киевская область. Качественно не дорого. Звоните {contact_phone.phone}'
    obj = LastProjects.objects.all()
    base_level = BaseLevel.objects.first()
    sub_texts = SubText.objects.all()
    location = Location.objects.first()
    contacts = Contacts.objects.all()
    template = 'main/index.html'
    context = {
        'form' : form,
        'objs' : obj, 
        'base_level':base_level,
        'location':location,
        'contacts':contacts,
        'title':title,
        'description':description,
        'url':request.build_absolute_uri(),
        'sub_texts':sub_texts,
        }
    return render(request, template, context)


def view(request, pk):
    form_question = FormAskQuestions(request.POST)
    if form_question.is_valid():
        form_question.save()
    form = FormAskQuestions
    obj = LastProjects.objects.get(slug=pk)
    title = f'{obj.title} - установка, монтаж и хорошее качество | Альфаград'
    contact_phone = Contacts.objects.first()
    description = f'{obj.title} - установка заборов под ключ, ремонт, монтаж. Киев и киевская область. Качественно не дорого. Звоните {contact_phone.phone}'
    location = Location.objects.first()
    contacts = Contacts.objects.all()
    template = 'main/view.html'
    context = {
        'form' : form,
        'url':request.build_absolute_uri(),
        'objs' : obj, 
        'location':location,
        'contacts':contacts,
        'title':title,
        'description':description,

        }
    return render(request, template, context)

def about_us(request):
    form_question = FormAskQuestions(request.POST)
    if form_question.is_valid():
        form_question.save()
    form = FormAskQuestions
    title = 'Строительство, монтаж, заборы, не дорого | Альфаград'
    contact_phone = Contacts.objects.first()
    description = f'Заборы под ключ, установка заборов, ремонт, монтаж. Киев и киевская область. Качественно не дорого. Звоните {contact_phone.phone}'
    base_level = BaseLevel.objects.first()
    sub_texts = SubText.objects.all()
    location = Location.objects.first()
    contacts = Contacts.objects.all()
    template = 'main/about_us.html'
    context = {
        'form' : form,
        'base_level':base_level,
        'sub_texts':sub_texts,
        'location':location,
        'contacts':contacts,
        'title':title,
        'description':description,
        'url':request.build_absolute_uri(),

        }
    return render(request, template, context)

def all_projects(request):
    form_question = FormAskQuestions(request.POST)
    if form_question.is_valid():
        form_question.save()
    form = FormAskQuestions
    title = 'Заборы не дорого | Альфаград'
    contact_phone = Contacts.objects.first()
    description = f'Заборы под ключ, установка заборов, ремонт, монтаж. Киев и киевская область. Качественно не дорого. Звоните {contact_phone.phone}'
    objs = LastProjects.objects.all()
    location = Location.objects.first()
    contacts = Contacts.objects.all()
    template = 'main/all_project.html'
    context = {
        'form' : form,
        'objs':objs,
        'location':location,
        'contacts':contacts,
        'title':title,
        'description':description,
        'url':request.build_absolute_uri(),

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

