from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from BalkanPress.articles.forms import ArticleSearchForm
from BalkanPress.articles.models import Article

from .forms import CategoryCreateForm, CategoryDeleteForm, CategoryEditForm
from .models import Category


# Create your views here.
class BaseFilteredArticleListView(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "articles/article-list.html"
    paginate_by = 5
    filter_model = None
    filter_field = None
    context_object_name_filter = None
    filter_type = None

    def get_queryset(self):
        self.filter_object = get_object_or_404(
            self.filter_model, slug=self.kwargs["slug"]
        )

        return (
            Article.objects.filter(
                **{self.filter_field: self.filter_object}, is_published=True
            )
            .select_related()
            .prefetch_related("categories", "tags")
            .order_by("-created_at")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_object"] = self.filter_object
        context["filter_type"] = self.filter_type
        context["search_form"] = ArticleSearchForm(self.request.GET or None)
        context["search_query"] = self.request.GET.get("q", "")
        return context


class CategoryArticleListView(BaseFilteredArticleListView):
    filter_model = Category
    filter_field = "categories"
    context_object_name_filter = "current_category"
    filter_type = "category"


class CategoryListView(ListView):
    model = Category
    template_name = "categories/category-list.html"
    context_object_name = "categories"
    queryset = Category.objects.order_by("name")


class CategorySlugMixin:
    model = Category
    slug_field = "slug"
    slug_url_kwarg = "slug"


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = "categories/category-create.html"
    success_url = reverse_lazy("categories:list")


class CategoryEditView(CategorySlugMixin, UpdateView):
    form_class = CategoryEditForm
    template_name = "categories/category-edit.html"
    success_url = reverse_lazy("categories:list")


class CategoryDeleteView(CategorySlugMixin, DeleteView):
    form_class = CategoryDeleteForm
    template_name = "categories/category-delete.html"
    success_url = reverse_lazy("categories:list")

    def get_form(self):
        return self.form_class(self.request.POST or None, instance=self.object)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "form" not in context:
            context["form"] = self.form_class(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        self.object.delete()
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
