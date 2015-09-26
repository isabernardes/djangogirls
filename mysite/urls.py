from django.conf.urls import include, url
from django.contrib import admin
from .views import homepage,create


# URL

urlpatterns = [
	url(r'^$', homepage),
	# url(r'^latest-post$', latest_post),
	url(r'^create$', create)
]

