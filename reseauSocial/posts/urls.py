from django.urls import path
from posts.views import List_view, Create_view, Update_view, Delete_view, Detail_view
from django.conf import settings
from django.conf.urls.static import static



app_name = 'posts/'
urlpatterns = [
    path('', List_view.as_view(), name = 'posts_list'),
    path('des', List_view.as_view(template_name = "posts/posts_list_des.html"), name = 'posts_list_des'),
    path('<int:pk>/detail', Detail_view.as_view(), name = 'posts_detail'),
    path('create', Create_view.as_view(), name = 'posts_create'),
    path('<int:pk>/update', Update_view.as_view(), name = 'posts_create'),
    path('<int:pk>/delete', Delete_view.as_view(), name = 'posts_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT)
    

