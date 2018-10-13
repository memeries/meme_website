from django.http import HttpResponse
from django.shortcuts import render

from .models import Memes, Type


def index(request):
    all_memes = Memes.objects.filter(nsfw=False).order_by('-date_added').all()
    all_types = Type.objects.all()

    context = {'all_memes': all_memes, 'all_types': all_types}
    return render(request, 'memes/index.html', context)


def type(request, type_id):
    type = Type.objects.get(id=type_id)
    all_memes = Memes.objects.filter(type=type).order_by('-date_added').all()
    all_types = Type.objects.all()

    context = {'all_memes': all_memes, 'all_types': all_types}
    return render(request, 'memes/index.html', context)


def un_safe(request):
    all_memes = Memes.objects.filter(nsfw=True).order_by('-date_added').all()
    all_types = Type.objects.all()

    context = {'all_memes': all_memes, 'all_types': all_types}
    return render(request, 'memes/index.html', context)


# TODO: context processor for all_types