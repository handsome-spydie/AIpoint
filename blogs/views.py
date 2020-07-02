from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Blog 

# Create your views here

def index(request):
	
	blogs = Blog.objects.all()
	# category = blogs('category')
	# print(category)
	params	=	{
		'blog':blogs
	}
	return render(request,'blogs.html',params)


def blogpost(request):
	blogs = Blog.objects.all()
	params = {
		'blog':blogs
	}
	return render(request, 'blogpost.html',params)