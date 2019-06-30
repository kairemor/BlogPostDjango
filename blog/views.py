from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone
from .models import Post, Comment
from django.template.loader import render_to_string
from django.http import Http404, JsonResponse

# Create your views here.


def index(request):
    delete = request.session.get('delete', None)
    if delete:
        del request.session['delete']
    posts = Post.objects.all().order_by('-id')[:10]
    context = {
        'posts': posts,
        'delete': delete
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        image = ''
        user = request.user
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        content = request.POST['content']
        if request.FILES:
            image = request.FILES['image']

        if title and subtitle and content:
            post = Post.objects.create(
                user=user, title=title, subtitle=subtitle, content=content)
            if image:
                post.image = image
            post.save()
            return redirect('blog:index')

        context = {
            error: 'Veulliez remplir correctement les champs correctement'
        }

        return render(request, 'index.html', context)


def detail(request, id):
    delete = request.session.get('delete', None)
    if delete:
        del request.session['delete']
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all()
    posts = Post.objects.all().order_by('-id').exclude(id=id)[:5]
    if not request.session.get('viewed_post_%s' % id, False) and post.user != request.user:
        post.views_number += 1
        post.save()
        request.session['viewed_post_%s' % id] = True
        request.session.set_expiry(86400)

    if request.user in post.likes.all():
        liked = True
    else:
        liked = False

    context = {
        'post': post,
        'delete': delete,
        'posts': posts,
        'comments': comments
    }
    return render(request, 'detail.html', context)


@login_required
def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    context = {
        'post_liked': liked,
        'post': post,
    }
    if request.is_ajax():
        html = render_to_string('post/like_section.html',
                                context, request=request)
        return JsonResponse({'form': html})


def update(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'update': True,
        'post': post
    }
    return render(request, 'detail.html', context)


def update_confirm(request, id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=id)
        image = ''
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        content = request.POST['content']
        if request.FILES:
            image = request.FILES['image']

        if title and subtitle and content:
            post.title = title
            post.subtitle = subtitle
            post.content = content
            post.update_date = timezone.now()
            if image:
                post.image = image
            post.save()
            return redirect(reverse('blog:detail', args=(post.pk, )))

        context = {
            error: 'Veulliez remplir correctement les champs correctement'
        }

        return render(request, 'index.html', context)


def delete(request, id):
    post = get_object_or_404(Post, id=id)
    if post.user == request.user:
        post.delete()
        request.session['delete'] = 'ok'
        return redirect('blog:index')

    request.session['delete'] = 'error'
    return redirect(reverse('blog:detail', args=(post.pk,)))


def comment(request, id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=id)
        user = request.user
        comment = request.POST['comment']
        comment = Comment.objects.create(user=user, post=post, comment=comment)
        comment.save()
        return redirect(reverse('blog:detail', args=(post.pk, )))
