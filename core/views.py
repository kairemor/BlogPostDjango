from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect, render

from .models import UserProfile
from blog.models import Post


# Create your views here.
def register(request):
    if request.method == "POST":
        print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            user = User.objects.get(username=username)
            userProfile = UserProfile.objects.create(user=user)
            userProfile.save()
            return redirect('update_profile')
    else:
        form = UserCreationForm()
    args = {
        'form': form,
        'error': 'Le username doit avoir 5 caracteres'
    }
    return render(request, 'register.html', args)


@login_required
def profile(request, username=''):
    if username:
        user = User.objects.get(username=username)
    else:
        user = request.user.username

    posts = Post.objects.filter(user=user).order_by('-id')
    userProfile = UserProfile.objects.get(user=user)
    context = {
        'profile': userProfile,
        'posts': posts
    }
    return render(request, 'profile.html', context)


@login_required
def update_profile(request):
    return render(request, 'update_profile.html')


@login_required
def update_profile_confirm(request):
    if request.method == 'POST':
        image = ''
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        city = request.POST['city']
        email = request.POST['email']
        job = request.POST['job']
        website = request.POST['website']
        phone = request.POST['phone']
        sexe = request.POST['sexe']
        print(request.FILES)
        if request.FILES:
            image = request.FILES['image']

        up = UserProfile.objects.get(user=request.user)
        up.fname = fname
        up.lname = lname
        up.city = city
        up.email = email
        up.website = website
        up.phone = phone
        up.sexe = sexe
        up.job = job
        if image:
            up.image = image

        up.save()

        return redirect(reverse('profile', args=(request.user.username,)))
