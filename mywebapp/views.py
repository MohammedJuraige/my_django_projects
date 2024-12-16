from django.shortcuts import render, get_object_or_404, redirect
from .models import Page,Post,Comment
from .forms import CommentForm,PageForm
from django.contrib.auth.decorators import login_required

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    page.views_count += 1
    page.save()
    return render(request, 'page_detail.html', {'page': page})



def homepage(request):
    pages = Page.objects.all()
    posts = Post.objects.all()
    return render(request, 'homepage.html', {'pages': pages, 'posts': posts})




@login_required
def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'page_detail.html', {'page': page})


# Post detail view
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

     # Handle comment form submission
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Save the comment with the current post
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=slug)  # Refresh the page after submitting
    else:
        form = CommentForm()

    # Get all comments for the post
    comments = post.comments.all()

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })

def edit_page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            return redirect('page_detail', slug=page.slug)
    else:
        form = PageForm(instance=page)
    return render(request, 'edit_page.html', {'form': form, 'page': page})


