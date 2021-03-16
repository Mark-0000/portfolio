from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm
from django.urls import reverse
from .models import Project, Skill, Service, Gallery
from django.contrib import messages


# Create your views here.
# def home(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             return redirect(reverse('index') + '#contact')
#     else:
#         pass
#
#     context = {
#         'projects': Project.objects.all(),
#         'skills': Skill.objects.all(),
#         'services': Service.objects.all()
#     }
#     return render(request, 'ui/index.html', context)


def gallery(request, project_id):
    my_project = Project.objects.get(id=project_id)

    my_gallery = my_project.gallery_set.last()
    context = {
        'gallery': my_gallery
    }
    return render(request, 'ui/gallery.html', context)


class Index(View):

    def get(self, request):
        context = {
            'projects': Project.objects.all(),
            'skills': Skill.objects.all(),
            'services': Service.objects.all()
        }
        return render(request, 'ui/index.html', context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form': form}
        messages.success(request, f'Message Sent!')
        return redirect(reverse('index') + '#contact', context)
