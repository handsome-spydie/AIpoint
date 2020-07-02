from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Blog 

# Create your views here

def index(request):
    blogs = Blog.objects.all()
    latest_blogs = reversed(blogs)
    params = {
		'blog':blogs,
		'latest_blog':latest_blogs,
	}
    return render(request, 'index.html',params)