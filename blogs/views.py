from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import BlogPost, Profile, Comment
from django.db.models import Count
from django.contrib.auth.decorators import login_required

def home(request):
    # Handle search
    search_query = request.GET.get('search', '')
    if search_query:
        posts = BlogPost.objects.filter(title__icontains=search_query) | BlogPost.objects.filter(content__icontains=search_query)
    else:
        posts = BlogPost.objects.all()

    # Trending posts (top 3 by likes)
    trending_posts = BlogPost.objects.annotate(like_count=Count('like')).order_by('-like_count')[:3]

    # Add liked_by_user to each post in both posts and trending_posts
    for post in posts:
        post.liked_by_user = post.like_set.filter(user=request.user).exists() if request.user.is_authenticated else False
    for post in trending_posts:
        post.liked_by_user = post.like_set.filter(user=request.user).exists() if request.user.is_authenticated else False

    return render(request, 'blogs/home.html', {
        'posts': posts,
        'trending_posts': trending_posts,
        'search_query': search_query,
    })

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('signup')
            user = User.objects.create_user(username=username, password=password1)
            Profile.objects.create(user=user)
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')
    return render(request, 'blogs/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')
        else:
            return render(request, 'blogs/login.html', {'error_message': 'Invalid username or password.'})
    return render(request, 'blogs/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    posts = BlogPost.objects.filter(user=user)
    return render(request, 'blogs/profile.html', {'user': user, 'profile': profile, 'posts': posts})

@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        profile.bio = request.POST['bio']
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
        profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile', username=request.user.username)
    return render(request, 'blogs/edit_profile.html', {'profile': profile})

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        category = request.POST['category']
        tags = request.POST['tags']
        image = request.FILES.get('image')
        post = BlogPost.objects.create(
            user=request.user,
            title=title,
            content=content,
            category=category,
            tags=tags,
            image=image
        )
        messages.success(request, 'Post created successfully!')
        return redirect('home')
    return render(request, 'blogs/create_post.html')

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, user=request.user)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.category = request.POST['category']
        post.tags = request.POST['tags']
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.save()
        messages.success(request, 'Post updated successfully!')
        return redirect('profile', username=request.user.username)
    return render(request, 'blogs/edit_post.html', {'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, user=request.user)
    post.delete()
    messages.success(request, 'Post deleted successfully!')
    return redirect('profile', username=request.user.username)

@login_required
def like_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if post.like_set.filter(user=request.user).exists():
        post.like_set.filter(user=request.user).delete()
    else:
        post.like_set.create(user=request.user)
    return redirect('home')

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        text = request.POST['text']
        Comment.objects.create(post=post, user=request.user, text=text)
        messages.success(request, 'Comment added successfully!')
    return redirect('home')