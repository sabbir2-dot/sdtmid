from django.shortcuts import render
from car.models import CarModel, Brand
# def home(request):
#     data = CarModel.objects.all()
#     brand = Brand.objects.all()
#     print(data)
#     return render(request, 'home.html', {'data': data, 'brand' : brand})
def home(request):
    brand_filter = request.GET.get('brand')  # Get the brand filter from query parameters
    if brand_filter:
        data = CarModel.objects.filter(brand__name=brand_filter)  # Filter by brand name
    else:
        data = CarModel.objects.all()  # Show all cars if no filter is applied
    
    brand = Brand.objects.all()
    return render(request, 'home.html', {'data': data, 'brand': brand})