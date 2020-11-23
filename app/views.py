from django.shortcuts import get_object_or_404, render, redirect
from .models import Category, Product, Info, Slider, TextProduct
# from .filter import ProductFilter
from django.views.generic import View, TemplateView




def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    slider = Slider.objects.all()
    info = Info.objects.all()
    produkt = TextProduct.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        produkt = produkt.filter(category=category)
    return render(request, 'app/index.html',
                  {
                      "category": category,
                      "categories": categories,
                      "products": products,
                      "info": info,
                      "produkt": produkt,
                      "slider": slider
                  })




model = Category
context_object_name = 'categorys'


class Index(TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context



