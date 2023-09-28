from django.shortcuts import get_object_or_404, render
from .models import Blog
# Create your views here.

def all_blogs(request):
    # blogs = Blog.objects.order_by('-date')[:3]
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog':blog})