from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post_list, name='post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('art/', views.art_list, name='art'),
    path('paint/', views.paint, name='paint'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
