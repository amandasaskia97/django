from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from about import views as aboutViews
from identify import views as idenViews
from info import views as infoViews


urlpatterns = [
    url('admin/', admin.site.urls),
    url('about', aboutViews.index),
    url('identify', idenViews.index),
    url('hasil', idenViews.prosesImg,name='hasil'),
    url('info', infoViews.index),
    url('', views.index),

]
