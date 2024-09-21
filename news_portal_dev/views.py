from django.shortcuts import render
from django.views.generic import ListView, DetailView
from  .models import Post



class NewsList(ListView):
    model = Post
    ordering = '-timestamp'
    template_name = 'news_list.html'
    context_object_name = 'news'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lenght'] = len(Post.objects.all())
        return context

class NewsDetail(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'news_detail'



# Create your views here.
