from django.urls import path
from Comments.views import List_view, Create_view, Update_view, Delete_view



app_name = "comments/"
urlpatterns = [
    path('', List_view.as_view(), name = 'comments_list'),
    path('create', Create_view.as_view(), name = 'comments_create'),
    path('<int:pk>/update', Update_view.as_view(), name = 'comments_create'),
    path('<int:pk>/delete', Delete_view.as_view(), name = 'comments_delete'),
]