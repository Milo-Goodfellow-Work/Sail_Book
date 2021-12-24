# from unittest.mock import MagicMock

# from django import forms
from django.test import TestCase
# from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from single_page.forms import ListingForm


class SinglePageFormTests(TestCase):
    def test_listing_creation_form_success(self):
        i_o = open('test_images/forms/test_image_one.jpg', 'rb')
        i_t = open('test_images/forms/test_image_two.jpg', 'rb')
        i_th = open('test_images/forms/test_image_three.jpg', 'rb')
        form = ListingForm(data={'title': 'the_title',
                                 'description': 'the_description',
                                 'price': 35,
                                 'email': 'test_email@example.com'},
                           files={
                                 'image_one': SimpleUploadedFile(i_o.name,
                                                                 i_o.read()),
                                 'image_two': SimpleUploadedFile(i_t.name,
                                                                 i_t.read()),
                                 'image_three': SimpleUploadedFile(i_th.name,
                                                                   i_th.read())
                           })
        self.assertTrue(form.is_valid())
