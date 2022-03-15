from unicodedata import name
from django.urls import reverse
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth import authenticate, login as login_ , logout 
from .forms import UserForm,CommentForm
from .models import AllUsers,Post,Comments,Like
from django.contrib.auth.decorators import login_required
from django.db.models import Count

# Main Index
def index_view(request):
    posts = Post.objects.values('id','name__username','post_desc','created').order_by('-created')
    comments = Comments.objects.values('id')
    likes=Like.objects.values('post_id','like')
    liked_number = {}
    disliked_number = {}
    for like in likes:
        if like["like"] is False:
            if like['post_id'] in disliked_number:
                disliked_number[like['post_id']] +=1
            else:
                disliked_number[like['post_id']] = 1
        else:
            
            if like["post_id"] in liked_number:
                liked_number[like["post_id"]] += 1  
                
            else:
                liked_number[like["post_id"]] = 1
   
    comment_count = (Comments.objects.values('post_id').annotate(comments=Count('body')))
    
    context = {
        'posts':posts,
        'comments':comments,
        'dislikes':disliked_number,
        'likes':liked_number,
        'comment_numbers':comment_count,
    }
    return render(request,'posts/index.html',context=context)




# registration 
def register_view(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('posts:login')
    return render (request,'posts/register.html',{'form':form})


# Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username = username,password = password)

        if user:
            login_(request,user)
            return redirect('posts:index')
        else:
            return redirect('posts:login')
    return render (request,'posts/login.html')


# Logout
def logout_view(request):
    logout(request)
    return redirect ('posts:index')

def post_add_view(request):
    if request.method == 'POST':
        user = request.user
        post = request.POST['post_body']
        Post.objects.create(name=user,post_desc = post)
        return redirect('posts:index')


# Comment on Post
@login_required(login_url='posts:login')
def comment_view(request,id):
    print('++++++++++++++++')
    comments = Comments.objects.filter(post_id = id).values('post_id','name','body','post')
    print(comments)
    form = CommentForm()
    user = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.name = request.user
            user.post_id = id
            user.save()
            return redirect('posts:index')
    return render(request,'posts/comments.html',{
        'form':form,
        'comments':comments,

        })


def like_view(request,post_ids):
    if Like.objects.filter(user = request.user,post_id=post_ids).exists():
        return redirect('posts:index')
    else:
        Like.objects.create(user=request.user,post_id=post_ids,like=True)
        return redirect('posts:index')

@login_required(login_url='posts:login')
def dislike_view(request,posts_id):
    if Like.objects.filter(user=request.user,post_id = posts_id).exists():
        return redirect('posts:index')
    else:
        Like.objects.create(user = request.user,post_id=posts_id,like=False)
        return redirect('posts:index')

    
        