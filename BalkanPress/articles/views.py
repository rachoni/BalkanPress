from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.views.generic.edit import FormMixin

from BalkanPress.comments.forms import CommentCreateForm

from .forms import (
    ArticleCreateForm,
    ArticleDeleteForm,
    ArticleEditForm,
    ArticleSearchForm,
)
from .models import Article


# Create your views here.
class PublishedArticleQuerysetMixin:
    def get_queryset(self):
        return (
            Article.objects.filter(is_published=True)
            .select_related()
            .prefetch_related("categories", "tags")
            .order_by("-created_at")
        )


class ArticleListView(PublishedArticleQuerysetMixin, ListView):
    model = Article
    template_name = "articles/article-list.html"
    context_object_name = "articles"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = ArticleSearchForm(self.request.GET or None)
        context["search_query"] = self.request.GET.get("q", "")
        return context


class ArticleSearchView(PublishedArticleQuerysetMixin, ListView):
    model = Article
    template_name = "articles/article-list.html"
    context_object_name = "articles"
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = ArticleSearchForm(self.request.GET or None)

        if self.form.is_valid():
            return self.form.filter_queryset(queryset)

        return queryset.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.form
        context["search_query"] = self.request.GET.get("q", "")
        context["is_search"] = True
        return context


# Pass the Search form to the template
class CommentFormMixin(FormMixin):
    form_class = CommentCreateForm

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.save()
        return redirect("articles:detail", slug=self.object.slug)


class ArticleSlugMixin:
    model = Article
    slug_field = "slug"
    slug_url_kwarg = "slug"


class ArticleDetailView(CommentFormMixin, ArticleSlugMixin, DetailView):
    context_object_name = "article"
    template_name = "articles/article-detail.html"

    def get_queryset(self):
        return Article.objects.filter(is_published=True).prefetch_related(
            "comments", "categories", "tags"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.filter(is_approved=True).order_by(
            "-created_at"
        )
        context["form"] = self.get_form()
        return context


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = "articles/article-create.html"
    success_url = reverse_lazy("articles:list")


class ArticleEditView(ArticleSlugMixin, UpdateView):
    form_class = ArticleEditForm
    template_name = "articles/article-edit.html"
    success_url = reverse_lazy("articles:list")


class ArticleDeleteView(ArticleSlugMixin, DeleteView):
    form_class = ArticleDeleteForm
    template_name = "articles/article-delete.html"
    context_object_name = "article"
    success_url = reverse_lazy("articles:list")
