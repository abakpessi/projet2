from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts
from .form import PostForm
from django.views import View

# Create your views here.


class List_view(View):
    template_name = 'posts/posts_list.html'
    def get(self, request, *args, **kwargs):
        queryset = Posts.objects.all()
        return render(request, self.template_name, {'object_list': queryset})

class Detail_view(View):
    template_name = 'posts/posts_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        id = self.kwargs.get('pk')
        context = {}
        if id is not None:
            obj = get_object_or_404(Posts, id=id)
            context['object'] = obj
        return render( request, self.template_name, context )
        
class Create_view(View):
    form = PostForm()
    template_name = 'posts/posts_create.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form})
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
class Update_view(View):
    template_name = 'posts/posts_create.html'
    def get_object(self):
        id = self.kwargs.get('pk')
        if id is not None:
            obj = get_object_or_404(Posts, id = id)
        return obj
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        form = PostForm(instance = obj)
        return render(request, self.template_name, {'form':form})
    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        form = PostForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
        return redirect('/')
    
class Delete_view(View):
    template_name = 'posts/posts_delete.html'
    def get_object(self):
        id = self.kwargs.get('pk')
        if id is not None:
            obj = get_object_or_404(Posts, id = id)
        return obj
    
    def get(self,request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return redirect('/')
    
