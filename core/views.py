from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm


def frontPage(request):
    return render(request, 'core/frontpage.html')


def signUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
        context = {
            'form' : form
        }
        
    else:
        form = SignUpForm()
        context = {
            'form' : form
        }

    return render(request, 'core/signup.html', context)