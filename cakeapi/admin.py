from django.contrib import admin

# Register your models here.
from .models import User, Cake, Review 

admin.site.register(User)
admin.site.register(Cake)
admin.site.register(Review)
