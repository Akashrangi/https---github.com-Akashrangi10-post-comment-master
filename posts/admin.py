from django.contrib import admin
from .models import AllUsers, Like,Post,Comments
# Register your models here.
admin.site.register(AllUsers)
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Like)

