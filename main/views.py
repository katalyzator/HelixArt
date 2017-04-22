from django.shortcuts import render

from .models import *


def index_view(request):
    arts = Art.objects.all()[:3]
    context = {"arts": arts}
    template = 'main/index.html'

    return render(request, template, context)
