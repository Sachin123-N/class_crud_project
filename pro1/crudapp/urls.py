from django.urls import path
from .views import *

urlpatterns = [
    path('create/', Create_view.as_view(), name="create_url"),
    path('show/', Show.as_view(), name="show_url"),
    path('update/<int:pk>', Update.as_view(), name='update_url'),
    path('cancel/<int:pk>', Cancel_order.as_view(), name='cancel_url')
]