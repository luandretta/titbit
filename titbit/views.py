from django.shortcuts import render
from .models import Profile


def home(request):
    return render(request, 'index.html', {})

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'profile_list.html', {'profiles':profiles})

