from django.test import TestCase
from unittest.mock import MagicMock

from single_page.email_tools import send_controls
from listings.models import listing

# Create your tests here.
class SinglePageEmailToolsTests(TestCase):
    def setUp(self):
        test_image = MagicMock(spec="File", name="FileMock")
        listing.objects.create(title="Placeholder", description="This is a description", price=35, email="milogoodfellowworkemail@gmail.com", image_one = test_image, image_two = test_image, image_three = test_image, secret_token="test_public_token")

    def test_attempt_to_send_email(self):
        new_listing = listing.objects.get(title="Placeholder")
        self.assertTrue(send_controls(new_listing))
