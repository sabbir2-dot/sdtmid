from django.shortcuts import render
from .models import CarModel, Purchase
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
# Create your views here.

class DetailCarView(DetailView):
    model = CarModel
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'
    context_object_name = 'car'

@login_required
def buy_now(request, car_id):
    car = get_object_or_404(CarModel, id=car_id)
    
    if car.quantity > 0:
        # Reduce the quantity
        car.quantity -= 1
        car.save()

        # Create a purchase record
        Purchase.objects.create(user=request.user, car=car)

        messages.success(request, f"You have successfully purchased {car.name}.")
    else:
        messages.error(request, f"Sorry, {car.name} is out of stock.")

    return redirect('detail_car', id=car_id)

@login_required
def profile(request):
    purchases = Purchase.objects.filter(user=request.user)
    return render(request, 'profile.html', {'purchases': purchases})