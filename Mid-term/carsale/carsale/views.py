from django.shortcuts import render
from CarListing.models import CarModel,BrandModel

def car_sale(request, category_slug=None):
    data = CarModel.objects.all()
    
    if category_slug is not None:
        brand = BrandModel.objects.get(slug=category_slug)  
        data = CarModel.objects.filter(brand=brand)
    brand = BrandModel.objects.all()
    return render(request, 'home.html', {'data': data, 'brand': brand})
