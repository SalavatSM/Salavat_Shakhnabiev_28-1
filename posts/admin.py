from django.contrib import admin
from posts.models import Post
from posts.models import Product, Comment


# Register your models here.


admin.site.register(Post)
admin.site.register(Product)
admin.site.register(Comment)

