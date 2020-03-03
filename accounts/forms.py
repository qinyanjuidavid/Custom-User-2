from django import forms
from django.forms import ModelForm
from accounts.models import User,Supplier,Customer,Products,Agreement
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.db import transaction
from django.contrib.auth.decorators import login_required



class UserCreationForm(ModelForm):
    class Meta:
        model=User
        fields=('username','first_name','last_name','email')
    password1=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Password Confirmation',widget=forms.PasswordInput)
    def clean_password2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("Password don\'t match")

        return password2

    def save(self,commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
class UserChangeForm(ModelForm):
    password=ReadOnlyPasswordHashField()
    class Meta:
        model=User
        fields=('username','first_name','last_name','password','is_admin','is_staff','is_active','is_supplier','is_customer')
    def clean_password(self):
        return self.initial['password']
class SupplierSignupForm(ModelForm):
    agreement=forms.ModelMultipleChoiceField(
    queryset=Agreement.objects.all(),
    widget=forms.CheckboxSelectMultiple,
    required=True
    )
    class Meta(ModelForm):
        model=User
        fields=('username','first_name','last_name','email')
    password1=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Password Confirmation',widget=forms.PasswordInput)
    def clean_password2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("Password don\'t match")

        return password2
    @transaction.atomic
    def save(self,commit=True):
        user=super().save(commit=False)
        user.is_supplier=True
        user.is_admin=False
        user.is_staff=False
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        supplier=Supplier.objects.create(user=user)
        supplier.agreement.add(*self.cleaned_data.get('agreement'))
        return user
class CustomerSignupForm(ModelForm):
        interest=forms.ModelMultipleChoiceField(
        queryset=Products.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
        )
        class Meta(ModelForm):
            model=User
            fields=('username','first_name','last_name','email')
        password1=forms.CharField(label='Password',widget=forms.PasswordInput)
        password2=forms.CharField(label='Password Confirmation',widget=forms.PasswordInput)
        def clean_password2(self):
            password1=self.cleaned_data.get('password1')
            password2=self.cleaned_data.get('password2')
            if password1 and password2 and password1!=password2:
                raise forms.ValidationError("Password don\'t match")

            return password2
        @transaction.atomic
        def save(self,commit=True):
            user=super().save(commit=False)
            user.is_customer=True
            user.is_admin=False
            user.is_staff=False
            user.set_password(self.cleaned_data['password1'])
            if commit:
                user.save()
            customer=Customer.objects.create(user=user)
            customer.interest.add(*self.cleaned_data.get('interest'))
            return user
