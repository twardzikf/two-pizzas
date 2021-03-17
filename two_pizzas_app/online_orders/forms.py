from django.forms import ModelForm, HiddenInput
from .models import Order, Size

class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = [
            'product_id',
            'product_size',
            'product_size',
            'name',
            'email',
            'phone'
        ]
        widgets = {
            'product_id': HiddenInput(),
            'product_name': HiddenInput(),
        }
    
    def __init__(self, *args, **kwargs):
        product = kwargs.pop('product')
        super(OrderForm, self).__init__(*args, **kwargs)
        if product != None:
            self.fields['product_size'].choices = map(lambda s: (s, s), product.sizes)
