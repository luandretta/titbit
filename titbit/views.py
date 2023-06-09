from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Profile, Post
from .forms import PostForm, SignUpForm, PictureForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


"""
Initial page
"""
def home(request):
    if request.user.is_authenticated:
        form = PostForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                messages.success(request, ('Your titbit has been posted!'))
                return redirect('home')

        posts = Post.objects.all().order_by('-created_at')
        return render(request, 'index.html', {"posts": posts, 'form': form})
    else:
        posts = Post.objects.all().order_by('-created_at')
        return render(request, 'index.html', {"posts": posts})


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
Own Profile with own posts
Option to follow/unfollow others profiles
"""
def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        posts = Post.objects.filter(user_id=pk).order_by('-created_at')

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

        return render(request, 'profile.html', {'profile': profile,
                                                'posts': posts})
    else:
        messages.success(request, ('You must be loggeg in to view this page.'))
        return redirect('home')


"""
Login
"""
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in!'))
            return redirect('home')
        else:
            messages.success(request, ('ERROR! Please try again'))
            return redirect('login')
    else: 
        return render(request, 'login.html', {})


"""
Logout
"""
def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out.'))
    return redirect('login')


"""
Register
"""
def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Welcome! You have successfully registered!')
            return redirect('home')

    return render(request, 'register.html', {'form': form})


def update_user(request):
    if request.user.is_authenticated:
        # Get the user
        current_user = User.objects.get(id=request.user.id)
        # Get the profile
        profile_user = Profile.objects.get(user_id=request.user.id)
        # Get forms
        user_form = SignUpForm(request.POST or None, request.FILES or None, instance=current_user)
        profile_form = PictureForm(request.POST or None, 
                                request.FILES or None, instance=profile_user)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_user.save()
            login(request, current_user)
            messages.success(request, 'Great! Your profile has been updated!')
            return redirect('home')

        return render(request, 'update_user.html', {'user_form': user_form,
                    'profile_form': profile_form})
    else:
        messages.success(request, 'You must be loggeg in to view this page.')
        return redirect('home')

def post_like(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=pk)
        if post.likes.filter(id=request.user.id):
           post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return redirect('home')
    else:
        messages.success(request, 'You must be loggeg in to view this page.')
        return redirect('home')
