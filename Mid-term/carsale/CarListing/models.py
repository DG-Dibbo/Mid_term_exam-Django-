from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BrandModel(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=100,unique=True,null=True,blank=True)
    def __str__(self):
        return self.name
    
class CarModel(models.Model):
    image = models.ImageField(upload_to='cars/')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, related_name="cars")
    description = models.TextField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name 
    
class CarPurchase(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    carModel = models.ForeignKey(CarModel,on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.carModel.name}'
    
class Comments(models.Model):
    car_model =models.ForeignKey(CarModel, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name}"