from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Tag
from .forms import TagCreateForm, TagEditForm, TagDeleteForm

# Create your tests here.
class TagBaseView:
    model = Tag

class TagListView(TagBaseView, ListView):
    template_name = 'tags/tag-list.html'
    context_object_name = 'tags'

class TagCreateView(TagBaseView, CreateView):
    form_class = TagCreateForm
    template_name = 'tags/tag-create.html'
    success_url = reverse_lazy('tags:list')

class TagEditView(TagBaseView, UpdateView):
    form_class = TagEditForm
    template_name = 'tags/tag-edit.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('tags:list')

class TagDeleteView(TagBaseView, DeleteView):
    form_class = TagDeleteForm
    template_name = 'tags/tag-delete.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('tags:list')