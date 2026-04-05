from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from BalkanPress.categories.models import Category
from BalkanPress.tags.models import Tag

from .models import Article

# Create your tests here.
User = get_user_model()


class ArticleTests(TestCase):
    def setUp(self):
        # Create users
        self.author = User.objects.create_user(
            username="author", password="testpass123"
        )
        self.other_user = User.objects.create_user(
            username="other", password="testpass123"
        )

        # Create category
        self.category = Category.objects.create(
            name="Technology1", slug="technology1", author=self.author
        )

        # Create tag
        self.tag = Tag.objects.create(name="Python", slug="python", author=self.author)

        # Create published article
        self.published_article = Article.objects.create(
            title="Publshed Article",
            author=self.author,
            summary="This is a published article summary",
            content="This is the full content of the published article",
            is_published=True,
        )
        self.published_article.categories.add(self.category)
        self.published_article.tags.add(self.tag)

        # Create unpublished article
        self.unpublished_article = Article.objects.create(
            title="Unpublshed Article",
            author=self.author,
            summary="This is a unpublished article summary",
            content="This is the full content of the unpublished article",
            is_published=False,
        )
        self.unpublished_article.categories.add(self.category)
        self.unpublished_article.tags.add(self.tag)

    # TEST 1: slug creation
    def test_slug_creation_on_article_save(self):
        """Test that slug is automatically created when saving an article without slug"""
        article = Article.objects.create(
            title="Test Article Without Slug",
            author=self.author,
            summary="Test summary",
            content="Test content for slug creation",
            is_published=True,
        )

        # Assert slug is not empty
        self.assertIsNotNone(article.slug)
        self.assertNotEqual(article.slug, "")

        # Assert slug length is <= 50 characters
        self.assertLessEqual(len(article.slug), 50)

    # TEST 2: list view - only published articles
    def test_article_list_view_shows_only_published_articles(self):
        """Test that the article list view only displays published articles"""
        url = reverse("articles:list")
        response = self.client.get(url)

        # Assert response is successful
        self.assertEqual(response.status_code, 200)

        # Get articles from context
        articles = response.context["articles"]

        # Assert published article is in the result
        self.assertIn(self.published_article, articles)

        # Assert unpublished article is NOT in the result
        self.assertNotIn(self.unpublished_article, articles)

    # TESt 3: detail view - unpublished article
    def test_unpublished_article_detail_view_return_404(self):
        """Test that accessing detail view of unpublished article returns 404"""
        url = reverse("articles:detail", kwargs={"slug": self.unpublished_article.slug})
        response = self.client.get(url)

        # Assert response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

    # TEST 4: create view - login required
    def test_article_create_view_redirects_anonymous_user(self):
        """Test that anonymous users are redirected to login when accessing create view"""
        # GET request
        get_url = reverse("articles:create")
        get_response = self.client.get(get_url)

        # Assert redirect to login page
        self.assertEqual(get_response.status_code, 302)
        self.assertIn("/accounts/login/", get_response.url)

        # POST request with valid data
        post_data = {
            "title": "New Article",
            "summary": "This is a summary",
            "content": "This is the full content of the new article",
            "categories": [self.category.id],
            "tags": [self.tag.id],
            "is_published": True,
        }
        post_response = self.client.post(get_url, post_data)

        # Assert redirect to login page
        self.assertEqual(post_response.status_code, 302)
        self.assertIn("/accounts/login/", post_response.url)

    # TEST 5: create view - author is set automatically
    def test_article_create_view_sets_author_automatically(self):
        """Test that the logged-in user is automatically set as the article author"""
        # Login as author
        self.client.login(username="author", password="testpass123")

        url = reverse("articles:create")
        post_data = {
            "title": "Author Test Article",
            "summary": "Testing author assignment",
            "content": "This article tests automatic author assignment",
            "categories": [self.category.id],
            "tags": [self.tag.id],
            "is_published": True,
        }

        response = self.client.post(url, post_data)

        # Assert redirect after successful creation
        self.assertEqual(response.status_code, 302)

        # Get the created article
        created_article = Article.objects.get(title="Author Test Article")

        # Assert article author is the logged-in user
        self.assertEqual(created_article.author, self.author)

    # TEST 6: edit/delete - owner only
    def test_edit_delete_views_restrict_non_owners(self):
        """Test that only article owners can edit or delete their articles"""

        # Test as other_user (non-owner)
        self.client.login(username="other", password="testpass123")

        # Try to edit author's article
        edit_url = reverse(
            "articles:edit", kwargs={"slug": self.published_article.slug}
        )
        edit_response = self.client.get(edit_url)
        # Assert 403 Forbidden or redirect
        self.assertEqual(edit_response.status_code, 403)

        # Try to delete author's article
        delete_url = reverse(
            "articles:delete", kwargs={"slug": self.published_article.slug}
        )
        delete_response = self.client.get(delete_url)
        # Assert 403 Forbidden or redirect
        self.assertEqual(delete_response.status_code, 403)

        # Test as author (owner)
        self.client.login(username="author", password="testpass123")

        # Try to edit own article
        edit_response_owner = self.client.get(edit_url)
        # Assert 200 OK (successfull access)
        self.assertEqual(edit_response_owner.status_code, 200)

        # Try to delete own article
        delete_response_owner = self.client.get(delete_url)
        # Assert 200 OK (successful access to confirmation page)
        self.assertEqual(delete_response_owner.status_code, 200)
