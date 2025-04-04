from django.contrib import admin
from . import models
# Register your models here.
# admin.site.register(models.CarModel)
@admin.register(models.CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'brand','description','quantity') 
    
class BrandModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']

admin.site.register(models.BrandModel, BrandModelAdmin)
