from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile


"""
Initial page
"""
def home(request):
    return render(request, 'index.html', {})


"""
Profile from all users
"""
def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {'profiles': profiles})
    else:
        messages.success(request, ('You must be loggeg in to view this page.'))
        return redirect('home')


"""
Own Profile
Option to follow/unfollow others profiles
"""
def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)

        # Post form logic
        if request.method == 'POST':
            # Get current user
            current_user_profile = request.user.profile
            # Get form data
            action = request.POST['follow']
            # Follow or unfollow
            if action == 'unfollow':
                current_user_profile.follows.remove(profile)
            elif action == 'follow':
                current_user_profile.follows.add(profile)
            # Save the profile
            current_user_profile.save()

        return render(request, 'profile.html', {'profile': profile})
    else:
        messages.success(request, ('You must be loggeg in to view this page.'))
        return redirect('home')
