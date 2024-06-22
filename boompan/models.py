from django.db import models

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length = 120)
	descriptions = models.TextField(blank = True, null = True)
	price = models.DecimalField(max_digits = 10, decimal_places = 2 )
	active = models.TextField(blank = False, null = False )
	featured = models.BooleanField()
