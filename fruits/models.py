from django.db import models
from users.models import User 

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Fruits(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(default="1.00", decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to="images/")
    description = models.TextField()
    rating = models.IntegerField(default=1)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    name = models.CharField(max_length=1000)
    profession = models.CharField(max_length=1000)
    profile_pic = models.ImageField(upload_to="testimony/")
    testimony = models.TextField()

    def __str__(self):
        return self.name