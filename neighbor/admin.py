from django.contrib import admin
from .models import Neighbourhood ,Business,User,Post

# Register your models here.

admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(User)
admin.site.register(Post)