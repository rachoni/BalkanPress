from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

# Create your tests here.
User = get_user_model()


class AccountsTests(TestCase):
    def setUp(self):
        # Create staff user
        self.staff_user = User.objects.create_user(
            username="staffuser", password="staffpass123", is_staff=True
        )

        # Create regular user
        self.regular_user = User.objects.create_user(
            username="regularuser", password="regularpass123", is_staff=False
        )

    # TEST 1: Register view - creates user
    def test_register_view_creates_new_user(self):
        """Test that POST request to register view creates a new user and redirects to login"""
        url = reverse("accounts:register")

        # Valid registration data
        register_data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "display_name": "New User",
            "password1": "testpass123",
            "password2": "testpass123",
        }

        response = self.client.post(url, register_data)

        # Assert a new user is created in the database
        self.assertTrue(User.objects.filter(username="newuser").exists())

        # Assert response redirects to login page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("accounts:login"))

    # TEST 2: User list - staff only
    def test_user_list_view_restricted_to_staff(self):
        """Test that only staff users can access the user list view"""
        url = reverse("accounts:user-list")

        # Test as regular_user (non-staff)
        self.client.login(username="regularuser", password="regularpass123")
        regular_response = self.client.get(url)
        # Assert access to denied (403 Forbidden)
        self.assertEqual(regular_response.status_code, 403)

        # Test as staff_user
        self.client.login(username="staffuser", password="staffpass123")
        staff_response = self.client.get(url)
        # Assert response status is 200 OK
        self.assertEqual(staff_response.status_code, 200)
