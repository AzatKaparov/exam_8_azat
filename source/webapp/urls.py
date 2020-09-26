from django.urls import path
from webapp.views import ProductIndexView, ProductView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ReviewCreateView, UpdateReviewView, DeleteReviewView


app_name = 'webapp'

urlpatterns = [
    path('', ProductIndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/add', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/add_review', ReviewCreateView.as_view(), name='add_review'),
    path('review/<int:pk>/update', UpdateReviewView.as_view(), name='update_review'),
    path('review/<int:pk>/delete', DeleteReviewView.as_view(), name='delete_review')
]

