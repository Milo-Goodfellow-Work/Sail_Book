from django import forms
from django.forms import ModelForm
# from django.utils.safestring import mark_safe
# rom django.core.exceptions import ValidationError


from listings.models import listing


class ListingForm(ModelForm):
    class Meta():
        model = listing
        fields = ['title',
                  'description',
                  'price',
                  'email',
                  'image_one',
                  'image_two',
                  'image_three']
        widgets = {
            'description': forms.Textarea(
                                attrs={'class': 'materialize-textarea'}),

        }

    def clean(self):
        cd = self.cleaned_data

        image_one = self.cleaned_data.get('image_one', False)
        image_two = self.cleaned_data.get('image_two', False)
        image_three = self.cleaned_data.get('image_three', False)

        if image_one:
            if image_one.size > 4*1024*1024:
                self.add_error("image_one", "The first image exceeds 4mb.")

        if image_two:
            if image_two.size > 4*1024*1024:
                self.add_error("image_two", "The second image exceeds 4mb.")

        if image_three:
            if image_three.size > 4*1024*1024:
                self.add_error("image_three", "The third image exceeds 4mb.")

        return cd
