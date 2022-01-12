from django.conf.urls import url
from apipostapp import views

urlpatterns = [
    url(r'^post$', views.postApi),
    url(r'^post/([0-20]+)$', views.postApi),
]