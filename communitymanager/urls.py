from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('communautes', views.communautes.as_view(), name='communautes'),
    path('communautes/<int:pk>', views.communaute.as_view(), name='communaute'),
    path('all_post', views.all_post.as_view(), name='all_post'),
    path('post/<int:pk>', views.post.as_view(), name='post'),
    path('create_post', views.nouveau_post.as_view(), name='create_post'),
    path('modif_post/<int:pk>', views.modif_post.as_view(), name='modif_post'),
]
