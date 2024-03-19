from django.contrib import admin

# Register your models here.
from .models import Feedback, Product

# Register your models here.
admin.site.register(Feedback)
admin.site.register(Product)
