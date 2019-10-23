'''
from django.shortcuts import render

# Create your views here.
def showtemplate(request):
    # 今天先不探討什麼是 render，先記得它會去撈 test.html
    return render(request, 'test.html')
'''

from django.shortcuts import render
from .models import Vendor
from .forms import VendorForm # 要記得 import 相對應的 Model Form 唷!
from .forms import RawVendorForm # 新增 RawVendorForm

# Create your views here.
def showtemplate(request):
    vendor_list = Vendor.objects.all() # 把所有 Vendor 的資料取出來
    context = {'vendor_list': vendor_list} # 建立 Dict對應到Vendor的資料，
    return render(request, 'test.html', context)

def showdetail(request):
    return render(request, 'vendor\detail.html')

''' # --> 舊的，作者也沒說要刪…
# 針對 vendor_create.html
def vendor_create_view(request):
    form = VendorForm(request.POST or None)
    if form.is_valid():
        form.save()
        #form = VerdorForm() # 清空 form -->作者說可清空，我試會出錯!

    context = {
        'form' : form
    }
    return render(request, "vendor/vendor_create.html", context)
'''

# 新增
def vendor_create_view(request):
    form = RawVendorForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = VendorForm()
    context = {
        'form' : form
    }
    return render(request, "vendors/vendor_create.html", context)