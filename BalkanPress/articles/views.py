from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.shortcuts import redirect
from .models import Article
from .forms import ArticleCreateForm, ArticleEditForm, ArticleDeleteForm
from BalkanPress.comments.forms import CommentCreateForm

# Create your views here.
class ArticleBaseView:
    model = Article

class ArticleListView(ArticleBaseView, ListView):
    context_object_name = 'articles'
    template_name = 'articles/article-list.html'

    def get_queryset(self):
        return Article.objects.filter(is_published=True).order_by('-created_at')

class ArticleDetailView(ArticleBaseView, FormMixin, DetailView):
    context_object_name = 'article'
    template_name = 'articles/article-detail.html'
    form_class = CommentCreateForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(
            **kwargs
        )
        context['comments'] = self.object.comments.filter(
            is_approved=True
        )
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.save()
        return redirect('articles:detail', slug=self.object.slug)

class ArticleCreateView(ArticleBaseView, CreateView):
    form_class = ArticleCreateForm
    template_name = 'articles/article-create.html'
    success_url = reverse_lazy('articles:index')

class ArticleEditView(ArticleBaseView, UpdateView):
    form_class = ArticleEditForm
    template_name = 'articles/article-edit.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('articles:index')

class ArticleDeleteView(ArticleBaseView, DeleteView):
    form_class = ArticleDeleteForm
    template_name = 'articles/article-delete.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'article'
    success_url = reverse_lazy('articles:index')