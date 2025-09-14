from django.forms import ModelForm
from main.models import Cleats

class CleatsForm(ModelForm):
    class Meta:
        model = Cleats
        fields = [
            "name", "brand", "size", "price", "stock", "description", "thumbnail", 
            "category", "is_featured"
        ]