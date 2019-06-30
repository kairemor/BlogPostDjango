from django.urls import path
from .views import index, create, detail, update, update_confirm, delete, comment, like_post

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('detail/<int:id>', detail, name="detail"),
    path('update/<int:id>', update, name="update"),
    path('update_confirm/<int:id>', update_confirm, name="update_confirm"),
    path('delete/<int:id>', delete, name="delete"),
    path('comment/<int:id>', comment, name="comment"),
    path('like/', like_post, name="like_post"),
]
