from django.contrib import admin
from django.urls import path, include

from chat.views import TestView

urlpatterns = [
    path('', TestView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include('chat.urls')),

]
