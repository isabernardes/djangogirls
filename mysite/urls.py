from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Post


# Views

def homepage(request):
	# import pdb
	# pdb.set_trace()

	return render(request, "homepage.html")
	# return HttpResponse("Hello, this is my first django thing")

def latest_post(request):
	return HttpResponse("This is the latest post")

def create(request):
	if request.method != "POST":
		raise Http404("Not your business") 
	post_title = request.POST["title"]
	post_content = request.POST["content"]
	new_post = Post.objects.create(title = post_title, content = post_content)
	
	return redirect('/')

# URL

urlpatterns = [
	url(r'^$', homepage),
	url(r'^latest-post$', latest_post),
	url(r'^create$', create)
]

