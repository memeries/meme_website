from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .models import Token


def register(request, secret_token):
    # print(secret_token)
    # if Token.objects.filter(secure_token=secret_token).exists():
    #     print("exists")
    #     token_to_delete = Token.objects.get(secure_token=secret_token)
    #     token_to_delete.delete()
    # else:
    #     return redirect('index')

    print("POST awaiting")

    if request.method == 'POST':
        print("Trying to register user")
        form = UserCreationForm(request.POST)
        if form.is_valid() and Token.objects.filter(secure_token=secret_token).exists():
            print("exists")
            token_to_delete = Token.objects.get(secure_token=secret_token)
            token_to_delete.delete()

            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('index')
    else:
        form = UserCreationForm

    context = {'form': form}
    return render(request, 'registration/register.html', context)
    # changed accounts to register in templates name because django looks for registration/login.html