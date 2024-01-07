from django.urls import path
from Restocafe.views import SignInView,SignUpView,CategoryCreateView,SubCategoryCreateView,ItemAddCategoryCreateView,remove_category,remove_subcategory,remove_item,CategoryListView,CategoryDetailView,SubcategoryListView,SubcategoryDetailView,ItemListView,ItemDetailView,ItemUpdateView,remove_itemview,OfferCreateView,offer_delete_view,IndexView


urlpatterns=[
    path("signup/",SignUpView.as_view(),name="signup"),
    path("",SignInView.as_view(),name="signin"),
    path("index/",IndexView.as_view(),name='index'),
    path("category",CategoryCreateView.as_view(),name='category-add'),
    path("subcategory",SubCategoryCreateView.as_view(),name="subcategory-add"),
    path("items",ItemAddCategoryCreateView.as_view(),name="items-add"),
    path("categories/<int:pk>/remove",remove_category,name="remove-category"),
    path("subcategories/<int:pk>/remove",remove_subcategory,name="remove-subcategory"),
    path("items/<int:pk>/remove",remove_item,name="remove-item"),
    path("category/all",CategoryListView.as_view(),name="category-list"),
    path("category/<int:pk>",CategoryDetailView.as_view(),name="category-detail"),
    path("subcategory/all",SubcategoryListView.as_view(),name="subcategory-list"),
    path("subcategory/<int:pk>",SubcategoryDetailView.as_view(),name="subcategory-detail"),
    path("items/all",ItemListView.as_view(),name="items-list"),
    path("items/<int:pk>/edit",ItemUpdateView.as_view(),name="items-edit"),
    path("items/<int:pk>/remove",remove_itemview,name="remove-items"),
    path("items/<int:pk>",ItemDetailView.as_view(),name="items-detail"),
    path("items/<int:pk>/offer/add",OfferCreateView.as_view(),name="offer-add"),
    path("offers/<int:pk>/remove",offer_delete_view,name="offer-delete"),






]       