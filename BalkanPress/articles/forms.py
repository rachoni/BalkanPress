from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Count, Q
from django.utils.safestring import mark_safe

from BalkanPress.categories.models import Category
from BalkanPress.common.forms import BootStrapModelForm, ReadOnlyModelForm
from BalkanPress.tags.models import Tag

from .models import Article


class ArticleSearchForm(forms.Form):
    SORT_CHOICES = (
        ("newest", "Newest"),
        ("oldest", "Oldest"),
        ("title_asc", "Title A-Z"),
        ("title_desc", "Title Z-A"),
        ("most_commented", "Most Commented"),
    )

    q = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search articles...", "class": "form-control"}
        ),
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.order_by("name"),
        required=False,
        empty_label="All categories",
        label="",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    tag = forms.ModelChoiceField(
        queryset=Tag.objects.order_by("name"),
        required=False,
        empty_label="All tags",
        label="",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    sort = forms.ChoiceField(
        choices=SORT_CHOICES,
        required=False,
        initial="newest",
        label="",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    def filter_queryset(self, queryset):
        query = self.cleaned_data.get("q")
        category = self.cleaned_data.get("category")
        tag = self.cleaned_data.get("tag")
        sort = self.cleaned_data.get("sort", "newest")

        # Start with published articles only
        queryset = queryset.filter(is_published=True)

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
                | Q(summary__icontains=query)
                | Q(content__icontains=query)
                | Q(categories__name__icontains=query)
                | Q(tags__name__icontains=query)
            )

            if category:
                queryset = queryset.filter(categories=category)

            if tag:
                queryset = queryset.filter(tags=tag)

            if sort == "oldest":
                queryset = queryset.order_by("created_at")
            elif sort == "title_asc":
                queryset = queryset.order_by("title")
            elif sort == "title_desc":
                queryset = queryset.order_by("-title")
            elif sort == "most_commented":
                queryset = queryset.annotate(comment_count=Count("comments")).order_by(
                    "-comment_count", "-created_at"
                )
            else:  # 'newest' or default
                queryset = queryset.order_by("-created_at")

        return queryset.distinct()


class ArticleBaseForm(BootStrapModelForm):
    class Meta:
        model = Article
        fields = [
            "title",
            "featured_image",
            "summary",
            "content",
            "categories",
            "tags",
            "is_published",
        ]
        widgets = {
            "featured_image": forms.FileInput(attrs={"class": "form-control-file"}),
            "summary": forms.Textarea(attrs={"rows": 3}),
            "content": forms.Textarea(attrs={"rows": 10}),
        }


class ArticleCreateForm(ArticleBaseForm):
    pass


class ArticleEditForm(ArticleBaseForm):
    pass


class ArticleDeleteForm(ReadOnlyModelForm):
    confirmation = forms.BooleanField(
        required=True,
        label=mark_safe(
            '<strong class="text-danger">'
            "I understand that this action cannot be undone."
            "</strong>"
        ),
        help_text="Check this box to confirm deletion.",
    )

    readonly_exclude = ["confirmation"]

    class Meta:
        model = Article
        fields = [
            "title",
            "featured_image",
            "summary",
            "content",
            "categories",
            "tags",
            "is_published",
        ]

    def clean_confirmation(self):
        if not self.cleaned_data.get("confirmation"):
            raise ValidationError("You must confirm that this action cannot be undone.")
        return True
