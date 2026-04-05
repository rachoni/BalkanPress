from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify

from .models import Category

# Create your tests here.
User = get_user_model()


class CategoryTests(TestCase):
    def setUp(self):
        # Create users
        self.owner = User.objects.create_user(username="owner", password="testpass123")
        self.other_user = User.objects.create_user(
            username="other", password="testpass123"
        )

        # Create category with author=owner
        self.category = Category.objects.create(name="Technology2", author=self.owner)

    # TEST 1: create view - login required
    def test_category_create_view_redirects_anonymous_user(self):
        """Test that anonymous users are redirected to login when accessing create view"""
        url = reverse("categories:create")

        # GET request
        get_response = self.client.get(url)
        self.assertEqual(get_response.status_code, 302)
        self.assertIn("/accounts/login/", get_response.url)

        # POST request with valid data
        post_data = {"name": "New Category"}
        post_response = self.client.post(url, post_data)
        self.assertEqual(post_response.status_code, 302)
        self.assertIn("/accounts/login", post_response.url)

    # TEST 2: create view - author is set automatically
    def test_category_create_view_sete_author_automatically(self):
        """Test that the logged-in user is automatically set as the category author"""
        # Login as owner
        self.client.login(username="owner", password="testpass123")

        url = reverse("categories:create")
        post_data = {"name": "Programming"}

        response = self.client.post(url, post_data)

        # Assert redirect after successful creation
        self.assertEqual(response.status_code, 302)

        # Get the created category
        created_category = Category.objects.get(name="Programming")

        # Assert category author is the logged-in user
        self.assertEqual(created_category.author, self.owner)

    # TEST 3: edit/delete - owner only
    def test_edit_delete_view_restrict_non_owners(self):
        """Test that only category owners can edit or delete their categories"""

        # Test as other_user (non-owner)
        self.client.login(username="other", password="testpass123")

        # Try to edint owner's category
        edit_url = reverse("categories:edit", kwargs={"slug": self.category.slug})
        edit_response = self.client.get(edit_url)
        # Assert 403 Forbidden
        self.assertEqual(edit_response.status_code, 403)

        # Try to delete owner's category
        delete_url = reverse("categories:delete", kwargs={"slug": self.category.slug})
        delete_response = self.client.get(delete_url)
        # Assert 403 Forbidden
        self.assertEqual(delete_response.status_code, 403)

        # Test as owner
        self.client.login(username="owner", password="testpass123")

        # Try to edit own category
        edit_response_owner = self.client.get(edit_url)
        # Assert 200 OK (successful access)
        self.assertEqual(edit_response_owner.status_code, 200)

        # Try to delete own category
        delete_response_owner = self.client.get(delete_url)
        # Assert 200 OK (successful access to confirmation page)
        self.assertEqual(delete_response_owner.status_code, 200)

    # TEST 4: slug generation
    def test_slug_generation_on_category_save(self):
        """Test that slug is automatically generated from the category name"""
        # Create a new category
        new_category = Category.objects.create(
            name="Web Development", author=self.owner
        )

        # Assert slug is generated from name
        expected_slug = slugify("Web Development")
        self.assertEqual(new_category.slug, expected_slug)

        # Test with existing category
        expected_existing_slug = slugify("Technology2")
        self.assertEqual(self.category.slug, expected_existing_slug)
