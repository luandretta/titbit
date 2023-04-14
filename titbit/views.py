from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile


def home(request):
    return render(request, 'index.html', {})

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {'profiles':profiles})
    else:
        messages.success(request, ('You must be loggeg in to view this page.'))
        return redirect('home')

