from django.db import models
from user.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    image = models.ImageField(null=True,blank=True,upload_to='')


    def get_absolute_url(self):
        return reverse("ecom:categorycreate")
    


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    image = models.ImageField()
    is_active = models.BooleanField(default=False)
    quantity = models.IntegerField()
    description = models.TextField()

COMPLETED = "COMPLETED"
PENDING = "PENDING"
CANCELLED= "CANCELLED"

OrderChoices = (
    ("COMP", COMPLETED),
    ("PEND", PENDING),
    ("CANCEL", CANCELLED),
)

class Order(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.DecimalField(decimal_places=2, max_digits=6)
    createdOn = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=OrderChoices, max_length=10)
    updatedOn = models.DateTimeField(auto_now=True)