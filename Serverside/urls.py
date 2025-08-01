"""
URL configuration for Serverside project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path,include
from Apps.CustomUsers_app.urls import url_patterns
from rest_framework import permissions
from Apps.Communication_app.urls import url_patterns as com_urls
from drf_yasg.views import get_schema_view

from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Dev API",
        default_version='v1',
        description="APIs for Users, Attendance, Results, Fees, Communication, etc.",
        
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
from Apps.Fee_app.urls import url_patterns as fee_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/',include(url_patterns)),
    path('api/',include(fee_urls)),
    path('api/',include(com_urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
]
