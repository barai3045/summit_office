from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls", namespace='home')),
    path('payment/', include("management.payment.urls", namespace="payment")),
    path('order/', include("management.order.urls", namespace="order")),
    path('approval/', include("management.approval.urls", namespace="approval")),
    path('base/', include("management.base.urls", namespace="management_base")),
    path('', include("hr.employee.urls", namespace="employee")),
    path('api/management/', include("management.urls", namespace="management")),
    path('api/hr/', include("hr.urls", namespace="hr")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

