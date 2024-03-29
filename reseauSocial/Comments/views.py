from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Comments
from .form import  CommentForm
from django.views import View

# Create your views here.


class List_view(View):
    template_name = 'Comments/comments_list.html'
    def get(self, request, *args, **kwargs):
        queryset = Comments.objects.all()
        return render(request, self.template_name, {'object_list': queryset})
        
class Create_view(View):
    form = CommentForm()
    template_name = 'Comments/comments_create.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form})
    
    def comment(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('comments/')
    
class Update_view(View):
    template_name = 'Comments/comments_create.html'
    def get_object(self):
        id = self.kwargs.get('pk')
        if id is not None:
            obj = get_object_or_404(Comments, id = id)
            return obj
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        form = CommentForm(instance = obj)
        return render(request, self.template_name, {'form':form})
    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        form = CommentForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
        return redirect('/comments/')
    
class Delete_view(View):
    template_name = 'comments/comments_delete.html'
    def get_object(self):
        id = self.kwargs.get('pk')
        if id is not None:
            obj = get_object_or_404(Comments, id = id)
            return obj
    
    def get(self,request, *args, **kwargs):
        return render(request, self.template_name)
    
    def comment(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return redirect('/comments/')
    
