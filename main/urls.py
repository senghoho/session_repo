from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('',mainpage, name="mainpage"),
    path('second/',secondpage,name="secondpage"),
    path('new/',new,name="new"),
    path('create/',create,name="create"),
    path('<int:id>',detail,name="detail"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>',update, name="update"),
    path('delete/<int:id>',delete, name="delete"),
    # tag 관련 path 추가
    path('tag/', tag_list, name="tag_list"),
    path("tag/<int:tag_id>",tag_blogs, name="tag_blogs"),
]
