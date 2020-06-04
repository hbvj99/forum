from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from discussions.forms import CreatePost, CreateComment
from discussions.models import Discussion, Comment
from django.contrib import messages
from django.db.models import F, Count


def homepage(request):
    post = Discussion.objects.all().order_by('-views')
    article_search = request.GET.get("search")
    category = request.GET.get('category')
    tags = request.GET.get('tags')
    author = request.GET.get('author')

    discussion_cat = Discussion.objects.distinct('category')
    if article_search:
        post = post.filter(
            Q(title__icontains=article_search) |
            Q(content__icontains=article_search) |
            Q(category__icontains=article_search) |
            Q(tags__icontains=article_search)
        ).distinct()
    if category:
        post = post.filter(category__icontains=category)
    if author:
        post = post.filter(user__username=author)
    if tags:
        post = post.filter(tags__icontains=tags)

    paginator = Paginator(post, 7)  # Show discussions per page

    page = request.GET.get('page')
    post = paginator.get_page(page)

    return render(request, 'discussions/discussion.html', {'post': post, 'discussion_cat': discussion_cat})


def api_doc(request):
    return render(request, 'discussions/api-doc.html')


@login_required()
def add_vote(request):
    post = get_object_or_404(Discussion, id=request.POST.get('vote_id'))
    if post.votes.filter(id=request.user.id).exists():
        post.votes.remove(request.user)
    else:
        post.votes.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def discussion_detail(request, title):
    Discussion.objects.filter(slug=title).update(views=F('views') + 1)  # Count view
    post = Discussion.objects.get(slug=title)
    is_liked = False
    if post.votes.filter(id=request.user.id):
        is_liked = True

    comment = Comment.objects.filter(post=post).order_by('-timestamp')
    comment_form = CreateComment(request.POST or None)
    if request.method == 'POST':
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            messages.success(request, 'Successfully Posted New Comment.')
            return HttpResponseRedirect(request.path_info)

    return render(request, 'discussions/discussion_detail.html',
                  {'post': post, 'comments': comment,
                   'comment_form': comment_form, 'is_liked': is_liked})


@login_required()
def new_discussion(request):
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Discussion Created Successfully.')
            return redirect('homepage')
    else:
        form = CreatePost()
    return render(request, 'discussions/add_post.html', {'form': form})


@login_required()
def discussion_update(request, title):
    obj = get_object_or_404(Discussion, slug=title)
    form = CreatePost(request.POST or None, request.FILES or None, instance=obj)
    post = Discussion.objects.get(slug=title)
    if request.user != post.user:
        messages.warning(request, 'Error! Not valid user.')
        return redirect('homepage')
    else:
        if form.is_valid():
            form.user = request.user
            form.save()
            messages.info(request, 'Updated! Discussion updated successfully.')
            return redirect('profile')
        template_name = 'discussions/add_post.html'
        context = {"title": f"Update {obj.title}", "form": form}
        return render(request, template_name, context)


@login_required
def discussion_delete(request, title):
    obj = get_object_or_404(Discussion, slug=title)
    template_name = 'discussions/delete.html'
    post = Discussion.objects.get(slug=title)
    if request.user != post.user:
        messages.warning(request, 'Error! Not a valid user.')
        return redirect('homepage')
    else:
        if request.method == 'POST':
            obj.delete()
            messages.warning(request, 'Success! Item has been deleted.')
            return redirect('profile')
        context = {"object": obj}
        return render(request, template_name, context)
