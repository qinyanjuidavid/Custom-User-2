from django.contrib import admin
from accounts.models import User,Supplier,Customer,Products,Agreement
from accounts.forms import UserChangeForm,UserCreationForm


class useradmin(admin.ModelAdmin):
    search_fields=['email','username']
    list_display=('username','email','is_admin','is_staff','is_active','is_customer','is_supplier')
    list_filter=('is_admin','is_staff','is_active','is_customer','is_supplier')
    form=UserChangeForm
    add_form=UserCreationForm
admin.site.register(User,useradmin)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Agreement)
