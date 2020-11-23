from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product, Info, Slider, TextProduct

from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)



@admin.register(TextProduct)
class TextProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'title', 'price', 'slug', 'available']
    list_filter = ['name', 'available']

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='70' />".format(obj.image.url))
        return "None"

    image_show.__name__="Картинка"




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'title', 'price', 'image', 'slug', 'available']
    list_filter = ['name', 'available']

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='70' />".format(obj.image.url))
        return "None"

    image_show.__name__="Картинка"




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'slug', 'menu']
    prepopulated_fields = {'slug': ('title',)}






@admin.register(Info)
class Info(admin.ModelAdmin):
    list_display = ['insta','insta2','insta3', 'image1', 'image', 'slug', 'slug2', 'slug3']

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(Slider)
class Slider(admin.ModelAdmin):
    list_display = ['name', 'title', 'image', 'sale', 'slug', 'available']

