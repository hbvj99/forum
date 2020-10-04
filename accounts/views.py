from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from accounts.forms import CreateUser, ImageUploadForm, UserDetail
from discussions.models import Discussion


def signup(request):
    if request.method == 'POST':
        user_form = CreateUser(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.save()
            return redirect('/')
    else:
        user_form = CreateUser()
    context = {'user_form': user_form}
    return render(request, 'accounts/signup.html', context)


@login_required()
def dashboard(request):
    logged_in_user = request.user

    post = Discussion.objects.all().order_by('-updated').filter(user=logged_in_user)
    paginator = Paginator(post, 9)  # No of discussions per page

    page = request.GET.get('page')
    post = paginator.get_page(page)

    return render(request, 'discussions/profile.html', {'post': post})


def image_update(request):
    if request.method == 'POST':
        user = get_object_or_404(User, username=request.user)
        user.profile.image = request.FILES.get('image', None)
        user.profile.save()
        return redirect('profile')
    else:
        form = ImageUploadForm(instance=request.user)
        return render(request, 'accounts/change_picture.html', {'form': form})


def edit_account(request):
    if request.method == 'POST':
        form = UserDetail(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your profile.')
            return redirect('profile')
    else:
        form = UserDetail(instance=request.user)
        return render(request, 'accounts/account_edit.html', {'form': form})
