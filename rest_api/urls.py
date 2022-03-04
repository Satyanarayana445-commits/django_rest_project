"""rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from api_rest.views import article_list,article_update,ArticleAPIView,ArticleDetails,GenericView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('article/', article_list,name = "article_list"),
    path('article_class/', ArticleAPIView.as_view() ,name = "article_list"),
    path('generic_view/<int:id>', GenericView.as_view() ,name = "generic_view"),
    path('update/<int:pk>/', ArticleDetails.as_view(),name = "article_update"),
    # path('article_update/<int:pk>/', article_update,name = "article_update"),
]
