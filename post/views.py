from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from post.models import Post
from users.models import Profile
from cart.models import Order
from cart.utils import cart_data


# Create your views here.


@login_required()
def file_upload(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('/explore/')
    else:
        form = PostForm

    return render(request, 'post/post_form.html', {'form': form})


def explore(request):
    data = cart_data(request)
    cart_items = data['cartItems']

    posts = Post.objects.all()
    context = {'posts': posts, 'cartItems': cart_items}
    return render(request, 'post/post_list.html', context)


@login_required
def user_posts(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, 'post/user_posts.html', {'posts': posts})


def user_profile(request, pk):
    profile = Profile.objects.filter(user_id=pk)
    posts = Post.objects.filter(user_id=pk)
    context = {'posts': posts, 'profile': profile}
    return render(request, 'post/profile_posts.html', context)


def post_view(request, pk):
    post = Post.objects.filter(id=pk)
    context = {'post': post,}
    return render(request, 'post/post_view.html', context)


def delete_view(request, id):
    context = {}
    obj = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect('/')

    return render(request, 'post/delete_view.html', context)


def modify_post(request, id):
    obj = get_object_or_404(Post, id=id)
    form = PostForm(instance=obj)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context = {'form': form}
    return render(request, 'post/modify_post.html', context)






