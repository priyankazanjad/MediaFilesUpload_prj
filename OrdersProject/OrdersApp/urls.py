from django.urls import path
from . import views

urlpatterns = [
    path('addord/',views.AddOrdersView.as_view(),name='add_ord'),
    path('showord/',views.ShowOrdersView.as_view(),name='show_ord'),
    path('delete/<int:i>/',views.DeleteOrdersView.as_view(),name='delete'),
    path('update/<int:i>/',views.UpdateOrdersView.as_view(),name='update'),
]