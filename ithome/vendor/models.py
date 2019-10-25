from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse # day22, 新增

# Create your models here.
class Vendor(models.Model):
    vendor_name = models.CharField(max_length=20) #vendor name
    store_name = models.CharField(max_length=10) #vendor店名
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    # 覆寫 __str__
    def __str__(self):
        return self.vendor_name

    # 將 get_absolute_url 修改如下
        def get_absolute_url(self):
            return reverse("vendors:vendor_id", kwargs={"id": self.id})    


class Food(models.Model):
    food_name = models.CharField(max_length=30)
    price_name = models.DecimalField(max_digits=3, decimal_places=0) #food price
    food_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE) #food belong which vendor

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    #list_display = ('id', 'vendor_name')
    list_display = [field.name for field in Vendor._meta.fields]

# 自行宣告 類別
class Morethanfifty(admin.SimpleListFilter):

	title = _('price')
	parameter_name = 'compareprice' # url最先要接的參數

	def lookups(self, request, model_admin):
		return (
			('>50',_('>50')), # 前方對應下方'>50'(也就是url的request)，第二個對應到admin顯示的文字
			('<=50',_('<=50')),
		)
    # 定義查詢時的過濾條件
	def queryset(self, request, queryset):
		if self.value() == '>50':
			return queryset.filter(price_name__gt=50)
		if self.value() == '<=50':
			return queryset.filter(price_name__lte=50)
                
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Food._meta.fields]
    #list_filter = ('price_name',)
    list_filter = (Morethanfifty,)
    fields = ['price_name'] # 顯示欄位
    search_fields = ('food_name','price_name') # 搜尋欄位
    ordering = ('price_name',) # 價格 由小到大 排序
