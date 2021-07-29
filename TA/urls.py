from django.conf.urls import url

from . import views

urlpatterns = [
    #url('recent/', views.recent),
    url('',views.index, name='image'),
    url('review', views.review, name='review'),
    url('proses', views.prosesImg, name='proses'),
]