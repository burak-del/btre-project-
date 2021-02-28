from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from listings.choices import price_choices, bedroom_choices, state_choices
from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors=Realtor.objects.order_by('-hire_date')

    mvp_realtor= Realtor.objects.order_by('-hire_date').filter(is_mvp=True)

    context={
        'realtors': realtors,
        'mvp_realtor':mvp_realtor,
    }

    return render(request, 'pages/about.html', context)