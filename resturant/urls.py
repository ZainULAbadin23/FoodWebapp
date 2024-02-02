from django.urls import path
from . import views as v


urlpatterns = [
    path('dashboard/', v.dashboard, name='resturant-dashboard'),

    path("products/", v.ProductList.as_view(), name="products_list"),
    path("products/<int:pk>/", v.ProductDetailView.as_view(), name="product_detail"),
    path("products/add/", v.AddProductView.as_view(), name="products_add"),
    path("products/edit/<int:pk>", v.ProductUpdateView.as_view(), name="product_edit"),
    path("products/delete/<int:pk>", v.inactive_product, name="inactive-product"),
    path("products/c/", v.ProductCategoryList.as_view(), name="products_category_list"),
    path(
        "products/c/<int:pk>/",
        v.ProductCategoryDetailView.as_view(),
        name="product_category_detail",
    ),
    path("products/c/add/", v.AddProductCategoryView.as_view(),
         name="products_category_add"),
    path("products/c/delete/<int:pk>", v.ProductCategoryDeleteView.as_view(), name="products_category_delete"),
    path("products/c/edit/<int:pk>", v.ProductCategoryUpdateView.as_view(), name="products_category_edit"),
]
