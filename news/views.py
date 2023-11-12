from django.shortcuts import render,redirect,get_object_or_404
from news.models import *
from news.forms import PostModelForm,PostUpdateForm,CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='users/login')
def home(request):
    data=PostModel.objects.all()
    if request.method=='POST':
        form=PostModelForm(request.POST)
        # print(form)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('/')
    else:
        form=PostModelForm()
    context={
        'posts':reversed(data),'form':form
    }
    return render(request,'home.html',context)


def post_detail(request,pk):
    post = get_object_or_404(PostModel,id=pk)
    if request.method=='POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance=c_form.save(commit=False)
            instance.user=request.user
            instance.post=post
            instance.save()
            return redirect('post_detail-page',pk=post.id)
    else:
        c_form = CommentForm()
    context={
        'post':post,
        'c_form':c_form,
    }
    return render(request,'post_detail.html',context)

def post_edit(request,pk):
    post = get_object_or_404(PostModel,id=pk)
    if request.method == 'POST':
        form=PostUpdateForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_edit.html',pk=post.id)
        else:
            form=PostUpdateForm(instance=post)
    context={
        'post':post,
        'form':form
    }
    return render(request,'post_edit.html',context)

def post_delete(request,pk):
    post = get_object_or_404(PostModel,id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home-page')
    context={
        'post':post
    }
    return render(request,'post_delete.html',context)