from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "core/home.html"

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['title'] = 'Mi Super Web I-LEF'
    #    return context
    
    def get(self, request, *args, **kwargs): # envia variables de contexto
        link = "https://www.udemy.com/course/curso-django-2-practico-desarrollo-web-python-3/learn/lecture/9652712#overview"
        return render(request, self.template_name,{'title':'Mi Super Web I-LEF','link':link})

class SamplePageView(TemplateView):
    template_name = 'core/sample.html'
