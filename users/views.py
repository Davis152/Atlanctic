from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
            form = ExtendedUserCreationForm(request.POST)
            profile_form = UserProfileForm(request.POST)
            if form.is_valid() and profile_form.is_valid():
                user= form.save()

                profile = profile_form.save(commit=False)
                profile.user= user

                profile.save()

                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password = password)
                login(request, user)

                messages.success(request, f'Your account has been created! You are now able to log in')
                return redirect('login')
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()
    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'users/register.html', context)

@login_required # decorate
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been Updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
                  'u_form':u_form,
                  'p_form':p_form
              }
    return render(request,'users/profile.html', context)