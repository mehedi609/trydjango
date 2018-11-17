from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Article
from .forms import ArticleModelForm
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    # queryset = Article.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    # queryset = Article.objects.all()
    # success_url = '/' <some path>

    def form_valid(self, form):
        return super().form_valid(form)

    # def get_success_url(self):
    #     return '/' <same path>


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id = id_)

    def form_valid(self, form):
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')
