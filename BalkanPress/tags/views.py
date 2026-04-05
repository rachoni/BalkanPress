from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
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


class AuthorOrStaffMixin(UserPassesTestMixin):
    def test_func(self):
        tag = self.get_object()
        user = self.request.user
        return user.is_authenticated and (
            tag.author == user or user.is_staff or user.is_superuser
        )


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    form_class = TagCreateForm
    template_name = "tags/tag-create.html"
    success_url = reverse_lazy("tags:list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TagEditView(AuthorOrStaffMixin, LoginRequiredMixin, TagSlugMixin, UpdateView):
    form_class = TagEditForm
    template_name = "tags/tag-edit.html"
    success_url = reverse_lazy("tags:list")


class TagDeleteView(AuthorOrStaffMixin, LoginRequiredMixin, TagSlugMixin, DeleteView):
    form_class = TagDeleteForm
    template_name = "tags/tag-delete.html"
    success_url = reverse_lazy("tags:list")

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
