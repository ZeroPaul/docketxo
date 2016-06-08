from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter


from .views import CategoriaDocenteViewSet


# from .api_views import load_menu

# router = ExtendedSimpleRouter()
router = routers.DefaultRouter()

router.register(r'docentes',CategoriaDocenteViewSet)

urlpatterns = [

    url(r'^docente/$', CategoriaDocenteViewSet),

    url(r'^', include(router.urls)),
]
