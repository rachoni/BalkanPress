from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Category
from .forms import CategoryCreateForm, CategoryEditForm, CategoryDeleteForm

# Create your views here.
class CategoryBaseView:
    model = Category

class CategoryListView(CategoryBaseView, ListView):
    template_name = 'categories/category-list.html'
    context_object_name = 'categories'

class CategoryCreateView(CategoryBaseView, CreateView):
    form_class = CategoryCreateForm
    template_name = 'categories/category-create.html'
    success_url = reverse_lazy('categories:list')

class CategoryEditView(CategoryBaseView, UpdateView):
    form_class = CategoryEditForm
    template_name = 'categories/category-edit.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('categories:list')

class CategoryDeleteView(CategoryBaseView, DeleteView):
    form_class = CategoryDeleteForm
    template_name = 'categories/category-delete.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('categories:list')