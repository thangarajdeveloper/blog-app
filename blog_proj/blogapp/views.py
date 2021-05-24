from .models import BlogModel, CommentModel
from .forms import SearchForm, CommentForm, BlogForm
from django.shortcuts import render, redirect
from django.http import Http404


def BlogListView(request):
    """
    returns the entire blog list
    """
    dataset = BlogModel.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            blog = BlogModel.objects.get(blog_title=title)
            return redirect(f'/blog/{blog.id}')
    else:
        form = SearchForm()
        context = {
            'dataset': dataset,
            'form': form,
        }
    return render(request, 'blogapp/listview.html', context)


def BlogDetailView(request, id):
    """
    returns the blog details
    """
    try:
        data = BlogModel.objects.get(id=id)
        comments = CommentModel.objects.filter(blog=data)
    except BlogModel.DoesNotExist:
        raise Http404('Data does not exist')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = CommentModel(your_name=form.cleaned_data['your_name'],
                                   comment_text=form.cleaned_data['comment_text'],
                                   blog=data)
            Comment.save()
            return redirect(f'/blog/{id}')
    else:
        form = CommentForm()

    context = {
        'data': data,
        'form': form,
        'comments': comments,
    }
    return render(request, 'blogapp/detailview.html', context)


def BlogAdd(request):
    """
    adding a new blog
    """
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            form.save()
            return redirect(f'/blog/{id}')
    else:
        form = BlogForm()

    context = {
        'form': form,
    }
    return render(request, 'blogapp/addblog.html', context)


def BlogUpdate(request, id):
    """
    update the existing blog
    """
    try:
        book = BlogModel.objects.get(id=id)
        form = BlogForm(instance=book)
    except BlogModel.DoesNotExist:
        raise Http404('Data does not exist')

    if request.method == 'POST':
        update = BlogForm(request.POST, instance=book)
        if update.is_valid():
            update.save()
            return redirect(f'/blog/{id}')

    context = {
        'form': form,
    }
    return render(request, 'blogapp/updateblog.html', context)


def BlogDelete(request, id):
    """
    delete the existing blog
    """
    try:
        blog = BlogModel.objects.get(id=id)
    except BlogModel.DoesNotExist:
        raise Http404('Blog does not exist')

    if request.method == 'GET' and blog:
        blog.delete()
        return redirect(f'/blogs/')

    return render(request, 'blogapp/detailview.html', {'message': 'deleted'})
