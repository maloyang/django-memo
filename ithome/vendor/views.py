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
from django.http import Http404 # day21, 額外 import Http404
from django.shortcuts import get_object_or_404 # day21, 新增

# Create your views here.
def showtemplate(request):
    vendor_list = Vendor.objects.all() # 把所有 Vendor 的資料取出來
    context = {'vendor_list': vendor_list} # 建立 Dict對應到Vendor的資料，
    return render(request, 'test.html', context)

def showdetail(request):
    return render(request, 'vendor\detail.html')

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

def singleVendor(request, id):
    vendor_list = get_object_or_404(Vendor, id=id)
    '''
    try:
        vendor_list = Vendor.objects.get(id=id)
    except Vendor.DoesNotExist:
        raise Http404
    '''

    context = {
        'vendor_list': vendor_list
    }
    return render(request, 'vendor/vendor_detail.html', context)

