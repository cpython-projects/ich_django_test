from django.urls import path
from .views import staff_index

app_name = 'staff'

urlpatterns = [
    path('', staff_index, name='index'),
]