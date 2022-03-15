from django.urls import path
from .import views


app_name = 'posts'


urlpatterns = [
    path('',views.index_view,name='index'),
    path('Register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('<int:id>/Comment/',views.comment_view,name='comment'),
    path('like/<int:post_ids>/',views.like_view,name="like"),
    path('dislike/<int:posts_id>/',views.dislike_view,name="dislike"),
    path('add-newpost/',views.post_add_view,name='postnew'),
    

]