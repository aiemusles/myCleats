from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            "name", "brand", "size", "price", "stock", "description", "thumbnail", 
            "category", "is_featured"
        ]