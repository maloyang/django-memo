from django import forms

from .models import Vendor, Food

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        # 新增 labels 對應
        labels = {
            'vendor_name': ('攤販名稱'),
            'store_name' : ('店名'),
            'phone_number' : ('電話'),
            'address' : ('地址'),
        }
