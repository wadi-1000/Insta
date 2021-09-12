from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.main, name='main_page'),
    path('new/post', views.new_post, name='new-post'),
    path('(<str:pk>)/', views.update_post, name='updatepost'),
    path('delete_post/(<int:pk>)/', views.delete_post, name='deletepost'),
    path('single/(<int:pk>)/', views.single_post, name = 'single_image'),
    path('search/', views.search_results, name='search_results'),
    path('comment/(<int:pk>)/', views.comments, name='add_comment'),
    path('likes/(<int:pk>)/' , views.like_images, name='likes'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)