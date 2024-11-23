
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers
from staffs import views



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
#  swagger

schema_view = get_swagger_view(title='Pastebin API')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('staffs/', include("staffs.urls")),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)





