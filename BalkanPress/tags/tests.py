from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify

from .models import Tag

# Create your tests here.
User = get_user_model()


class TagTests(TestCase):
    def setUp(self):
        # Create users
        self.owner = User.objects.create_user(username="owner", password="testpass123")
        self.other_user = User.objects.create_user(
            username="other", password="testpass123"
        )

        # Create tag with author=owner
        self.tag = Tag.objects.create(name="Python", author=self.owner)

    # TEST 1: create view - login required
    def test_tag_create_view_redirects_anonymous_user(self):
        """Test that anonymous users are redirected to login when accessing create view"""
        url = reverse("tags:create")

        # GET request
        get_response = self.client.get(url)
        self.assertEqual(get_response.status_code, 302)
        self.assertIn("/accounts/login/", get_response.url)

        # POST request with valid data
        post_data = {"name": "Django"}
        post_response = self.client.post(url, post_data)
        self.assertEqual(post_response.status_code, 302)
        self.assertIn("/accounts/login", post_response.url)

    # TEST 2: create view - author is set automatically
    def test_tag_create_view_sete_author_automatically(self):
        """Test that the logged-in user is automatically set as the tag author"""
        # Login as owner
        self.client.login(username="owner", password="testpass123")

        url = reverse("tags:create")
        post_data = {"name": "JavaScript"}

        response = self.client.post(url, post_data)

        # Assert redirect after successful creation
        self.assertEqual(response.status_code, 302)

        # Get the created tag
        created_tag = Tag.objects.get(name="JavaScript")

        # Assert tag author is the logged-in user
        self.assertEqual(created_tag.author, self.owner)

    # TEST 3: edit/delete - owner only
    def test_edit_delete_view_restrict_non_owners(self):
        """Test that only tag owners can edit or delete their tags"""

        # Test as other_user (non-owner)
        self.client.login(username="other", password="testpass123")

        # Try to edint owner's tag
        edit_url = reverse("tags:edit", kwargs={"slug": self.tag.slug})
        edit_response = self.client.get(edit_url)
        # Assert 403 Forbidden
        self.assertEqual(edit_response.status_code, 403)

        # Try to delete owner's tag
        delete_url = reverse("tags:delete", kwargs={"slug": self.tag.slug})
        delete_response = self.client.get(delete_url)
        # Assert 403 Forbidden
        self.assertEqual(delete_response.status_code, 403)

        # Test as owner
        self.client.login(username="owner", password="testpass123")

        # Try to edit own tag
        edit_response_owner = self.client.get(edit_url)
        # Assert 200 OK (successful access)
        self.assertEqual(edit_response_owner.status_code, 200)

        # Try to delete own tag
        delete_response_owner = self.client.get(delete_url)
        # Assert 200 OK (successful access to confirmation page)
        self.assertEqual(delete_response_owner.status_code, 200)

    # TEST 4: slug generation
    def test_slug_generation_on_tag_save(self):
        """Test that slug is automatically generated from the tag name"""
        # Create a new tag
        new_tag = Tag.objects.create(name="Web Development", author=self.owner)

        # Assert slug is generated from name
        expected_slug = slugify("Web Development")
        self.assertEqual(new_tag.slug, expected_slug)

        # Test with existing tag
        expected_existing_slug = slugify("Python")
        self.assertEqual(self.tag.slug, expected_existing_slug)
