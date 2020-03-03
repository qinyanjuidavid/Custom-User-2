from django.urls import path
from accounts import views
from accounts.views import SupplierSignupView,CustomerSignupView
from django.contrib.auth import views as auth_views
app_name='accounts'


urlpatterns=[
path('home/',views.Home,name='home'),
path('',SupplierSignupView.as_view(),name='supplier'),
path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
path('logout/',auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
path('customer',CustomerSignupView.as_view(),name='customer')
]
