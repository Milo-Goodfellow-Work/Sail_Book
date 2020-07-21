from unittest.mock import MagicMock

from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.
from listings.models import listing

class SinglePageViewTests(TestCase):
    def test_page_exists_at_view_url(self):
        checker = self.client.get('')

        self.assertEqual(checker.status_code, 200)

    def test_page_accessible_by_name(self):
        checker = self.client.get(reverse('single_page:single_page'))

        self.assertEqual(checker.status_code, 200)

    def test_page_template_accurate(self):
        checker = self.client.get(reverse('single_page:single_page'))

        self.assertEqual(checker.status_code, 200)
        self.assertTemplateUsed(checker, 'single_page/single_page.html')


class SinglePageSearchTests(TestCase):
    def test_page_exists_at_view_url(self):
        checker = self.client.get('/test_search/')

        self.assertEqual(checker.status_code, 200)

    def test_page_accessible_by_name(self):
        checker = self.client.get(reverse('single_page:single_page_search', args=['test_search']))

        self.assertEqual(checker.status_code, 200)

    def test_page_template_accurate(self):
        checker = self.client.get(reverse('single_page:single_page_search', args=['test_search']))

        self.assertEqual(checker.status_code, 200)
        self.assertTemplateUsed(checker, 'single_page/single_page.html')

class SinglePageDeleteTests(TestCase):
    def setUp(self):
        test_image = MagicMock(spec="File", name="FileMock")
        listing.objects.create(title="Placeholder", description="This is a description", price=35, email="testemail@example.com", image_one = test_image, image_two = test_image, image_three = test_image, secret_token="test_public_token")

    def test_page_exists_at_view_url(self):
        checker = self.client.get('/delete/test_public_token/')

        self.assertEqual(checker.status_code, 302)

    def test_page_accessible_by_name(self):
        checker = self.client.get(reverse('single_page:delete_listing_page', args=['test_public_token']))

        self.assertEqual(checker.status_code, 302)
