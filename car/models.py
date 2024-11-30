from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"brand {self.name}"
       

class CarModel(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car/media/uploads/', blank=True, null=True)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} purchased {self.car.name}"