from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('car_listing/',include('CarListing.urls')),
    path('',views.car_sale,name='carsale'),
    path('brand/<slug:category_slug>/', views.car_sale, name='brand_wise_slug'),
]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)