from django.urls import path
from .views import \
    dynamic_product_lookup, all_product_detail_view, product_deletion, product_create_view, product_detail_view

urlpatterns = [
    path('<int:my_id>/', dynamic_product_lookup, name='product_details'),
    path('<int:my_id>/delete', product_deletion, name='product_delete'),
    path('all', all_product_detail_view, name='all_products'),
    path('', product_detail_view),
]
