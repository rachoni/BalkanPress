from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from BalkanPress.categories.views import BaseFilteredArticleListView

from .forms import TagCreateForm, TagDeleteForm, TagEditForm
from .models import Tag


# Create your tests here.
class TagArticleListView(BaseFilteredArticleListView):
    filter_model = Tag
    filter_field = "tags"
    context_object_name_filter = "current_tag"
    filter_type = "tag"


class TagListView(ListView):
    model = Tag
    template_name = "tags/tag-list.html"
    context_object_name = "tags"
    queryset = Tag.objects.order_by("name")


class TagSlugMixin:
    model = Tag
    slug_field = "slug"
    slug_url_kwarg = "slug"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagCreateForm
    template_name = "tags/tag-create.html"
    success_url = reverse_lazy("tags:list")


class TagEditView(TagSlugMixin, UpdateView):
    form_class = TagEditForm
    template_name = "tags/tag-edit.html"
    success_url = reverse_lazy("tags:list")


class TagDeleteView(TagSlugMixin, DeleteView):
    form_class = TagDeleteForm
    template_name = "tags/tag-delete.html"
    success_url = reverse_lazy("tags:list")
