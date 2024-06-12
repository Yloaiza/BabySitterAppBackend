from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from BabySitter import views

router = routers.DefaultRouter()
router.register(r'users',views.UserView,'users')
router.register(r'nannys',views.NannyView,'nannys')
router.register(r'reservations',views.ReservationView,'reservations')

# api versioning
urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title="Tasks API"))
]
