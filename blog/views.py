from django.shortcuts import render, get_object_or_404

# Create your views here.
from . models import blog

def home(request):
    all_blogs = blog.objects
    return render(request , 'blog/index.html',{'all_blogs':all_blogs})

def details(request, blog_id):
    detail_blog = get_object_or_404(blog,pk=blog_id)
    return render(request , 'blog/details.html',{'full_blog':detail_blog})

