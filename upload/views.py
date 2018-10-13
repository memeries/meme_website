from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import UploadForm
from memes.models import Memes

import pyimgur
import os

CLIENT_ID = "053728db6e717d0"
UPLOAD_TO_LOCATION = "uploadedmemes/newimage"

im = pyimgur.Imgur(CLIENT_ID)

@login_required
def index(request):
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            i = request.FILES['image']
            write_image(i)

            transcribe = form.cleaned_data["transcribe"]
            type = form.cleaned_data["type"]
            nsfw = form.cleaned_data["nsfw"]


            uploaded_image = im.upload_image(UPLOAD_TO_LOCATION, title="memeuploadapp")
            print(uploaded_image.link)

            new_meme = Memes(link=uploaded_image.link,
                             thumbnail=uploaded_image.link_small_thumbnail,
                             transcribe=transcribe,
                             nsfw=nsfw)
            new_meme.save()
            new_meme.type.set(type)

            return redirect('index')

    else:
        form = UploadForm()

    context = {'form': form}
    return render(request, 'upload/index.html', context)


def write_image(i):
    if not os.path.exists('memes/'):
        os.mkdir('memes/')
    with open(UPLOAD_TO_LOCATION, 'wb+') as dest:
        for chunk in i.chunks():
            dest.write(chunk)