from django.urls import path

from . import views

urlpatterns = [
    path('init', views.init, name='init'),
    path('check_update', views.check_update, name='update'),
    path('notice', views.get_notice, name='notice'),
]