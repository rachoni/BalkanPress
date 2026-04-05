from django.contrib.auth import get_user_model
from django.test import TestCase

from BalkanPress.articles.models import Article
from BalkanPress.categories.models import Category
from BalkanPress.tags.models import Tag

from .forms import CommentCreateForm

# Create your tests here.
User = get_user_model()


class CommentFormTests(TestCase):
    def setUp(self):
        # Create user (author)
        self.author = User.objects.create_user(
            username="author", password="testpass123"
        )

        # Create category
        self.category = Category.objects.create(name="Technology3", author=self.author)

        # Create tag
        self.tag = Tag.objects.create(name="Python", author=self.author)

        # Create published article
        self.article = Article.objects.create(
            title="Test Article",
            author=self.author,
            summary="This is a test article summary",
            content="This is the full content of the test article",
            is_published=True,
        )
        self.article.categories.add(self.category)
        self.article.tags.add(self.tag)

    # TEST 1: Comment validation
    def test_comment_form_body_validation(self):
        """Test that comment form validates body minimum length"""

        # Test with body shorter than 5 characters
        invalid_form_data = {
            "author_name": "John Doe",
            "body": "abc",  # Less than 5 characters
        }
        invalid_form = CommentCreateForm(data=invalid_form_data)

        # Assert form is invalid
        self.assertFalse(invalid_form.is_valid())

        # Assert there is an error for the "body" field
        self.assertIn("body", invalid_form.errors)
        self.assertIn(
            "Comment must be at least 5 characters long.",
            invalid_form.errors["body"][0],
        )

        # Test with valid body (5 or more characters)
        valid_form_data = {
            "author_name": "John Doe",
            "body": "This is a valid comment with more than 5 characters.",
        }
        valid_form = CommentCreateForm(data=valid_form_data)

        # Assert form is valid
        self.assertTrue(valid_form.is_valid())
