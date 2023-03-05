from django.shortcuts import render , redirect , get_object_or_404
from.models import Post
from.forms import CreateBlogForm


def Home(request):
    posts = Post.objects.all().order_by('-id')
    context = {
        'posts' : posts,
        'title' : 'the blog title '

    }
    return render(request , 'blog/index.html' ,context)

def About(request):
    return render(request , 'blog/about.html')


def create_blog(request):
    if request.method == 'POST':
        form = CreateBlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog-home')
    else:
        form = CreateBlogForm()
    context = {
        'form' : form 
    }
    return render(request , 'blog/create-blog.html' , context)


def blog_detail(request , pk):
    blog = Post.objects.get(id =pk)
    context ={
        'post': blog
    }
    return render(request , 'blog/blog-detail.html' , context)


def blog_update(request , pk):
    blog =get_object_or_404(Post , id=pk)
    if request.method == 'POST':
        form = CreateBlogForm(request.POST , instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else :
        form = CreateBlogForm(instance=blog)
    context = {
        'form' : form,
        'blog' : blog
    }
    return render(request , 'blog/blog-update.html' , context)