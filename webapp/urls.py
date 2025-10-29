from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.urls import reverse_lazy
from django.shortcuts import redirect


urlpatterns = [

    path('admin/', admin.site.urls),
    path('cuentas/', include('cuentas.urls')),
    path('', RedirectView.as_view(url=reverse_lazy('cuentas:login'), permanent=False)),

]



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/', include(('cuentas.urls', 'cuentas'), namespace='cuentas')),  # ← clave
]