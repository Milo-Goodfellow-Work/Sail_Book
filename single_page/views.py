# import secrets

from django.shortcuts import render, redirect
# from django.core.mail import send_mail
from django.contrib.postgres.search import SearchVector

from .forms import ListingForm
from listings.models import listing
# from sail_book.settings import hidden_settings
from .email_tools import send_controls


# Create your views here.
def single_page_view(request):
    if request.GET.get('search') is None:
        if request.method == "POST":
            form = ListingForm(request.POST, request.FILES)
            if form.is_valid():
                new_listing = form.save()
                send_controls(new_listing)

                return redirect('single_page:single_page')
        listings = listing.objects.all()

    else:
        listings = listing.objects.annotate(search=SearchVector('title',
                                                                'description',
                                                                'price',
                                                                'email',
                                                                'public'
                                                                '_token'))
        listings = listings.filter(search=request.GET.get('search'))

    form = ListingForm()
    return render(request,
                  'single_page/single_page.html',
                  {'form': form, 'listings': listings})


def delete_listing_view(request, secret_token):
    listing.objects.get(secret_token=secret_token).delete()
    return redirect('single_page:single_page')
