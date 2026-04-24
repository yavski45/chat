from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, UserProfileForm
from .models import User, Profile

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inbox')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile(request):
    # Ensure profile exists (safety net)
    profile_obj, _ = request.user.__class__.objects.get_or_create(pk=request.user.pk)
    from .models import Profile
    profile_instance, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile_instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil mis à jour avec succès !")
            return redirect('profile')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label} : {error}")
            for error in form.non_field_errors():
                messages.error(request, error)
    else:
        form = UserProfileForm(instance=profile_instance)

    return render(request, 'accounts/profile.html', {'form': form})

@login_required
def user_profile(request, username):
    viewed_user = get_object_or_404(User.objects.select_related('profile'), username=username)
    return render(request, 'accounts/user_profile.html', {'viewed_user': viewed_user})
