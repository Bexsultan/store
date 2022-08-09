from django.contrib import admin

# Register your models here.
from app.models import Category, Product, Review, UserProduct

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(UserProduct)


