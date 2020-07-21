from unittest.mock import MagicMock

from django import forms
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from single_page.forms import ListingForm

class SinglePageFormTests(TestCase):
    def test_listing_creation_form_success(self):
        test_image_one = open('test_images/forms/test_image_one.jpg', 'rb')
        test_image_two = open('test_images/forms/test_image_two.jpg', 'rb')
        test_image_three = open('test_images/forms/test_image_three.jpg', 'rb')
        form = ListingForm(data={'title':'the_title', 'description':'the_description', 'price':35, 'email':'test_email@example.com'}, files={'image_one':SimpleUploadedFile(test_image_one.name, test_image_one.read()), 'image_two':SimpleUploadedFile(test_image_two.name, test_image_two.read()), 'image_three':SimpleUploadedFile(test_image_three.name, test_image_three.read())})

        self.assertTrue(form.is_valid())
