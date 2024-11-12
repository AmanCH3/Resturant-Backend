from django.urls import path
from . import views

urlpatterns = [
    path('menus/', views.MenuListCreate.as_view(), name='menus-list-create'),
    path('menus/<int:pk>/', views.MenuRetrieveUpdateDestroy.as_view(), name='menu-retrieve-update-destroy'),
    path('menuitems/', views.MenuItemListCreate.as_view(), name='menuitems-list-create'),
    path('menuitems/<int:pk>/', views.MenuItemRetrieveUpdateDestroy.as_view(), name='menuitem-retrieve-update-destroy'),
    path('menucategories/', views.MenuCategoryListCreate.as_view(), name='menucategories-list-create'),
    path('menucategories/<int:pk>/', views.MenuCategoryRetrieveUpdateDestroy.as_view(), name='menucategory-retrieve-update-destroy'),
    path('menuitemcategories/', views.MenuItemCategoryListCreate.as_view(), name='menuitemcategories-list-create'),
    path('menuitemcategories/<int:pk>/', views.MenuItemCategoryRetrieveUpdateDestroy.as_view(), name='menuitemcategory-retrieve-update-destroy'),
    path('menuitemoptions/', views.MenuItemOptionListCreate.as_view(), name='menuitemoptions-list-create'),
    path('menuitemoptions/<int:pk>/', views.MenuItemOptionRetrieveUpdateDestroy.as_view(), name='menuitemoption-retrieve-update-destroy'),
    path('menuitemoptioncategories/', views.MenuItemOptionCategoryListCreate.as_view(), name='menuitemoptioncategories-list-create'),
    path('menuitemoptioncategories/<int:pk>/', views.MenuItemOptionCategoryRetrieveUpdateDestroy.as_view(), name='menuitemoptioncategory-retrieve-update-destroy'),
    path('menuitemoptionchoices/', views.MenuItemOptionChoiceListCreate.as_view(), name='menuitemoptionchoices-list-create'),
    path('menuitemoptionchoices/<int:pk>/', views.MenuItemOptionChoiceRetrieveUpdateDestroy.as_view(), name='menuitemoptionchoice-retrieve-update-destroy'),
    path('menuitemoptionchoicecategories/', views.MenuItemOptionChoiceCategoryListCreate.as_view(), name='menuitemoptionchoicecategories-list-create'),
    path('menuitemoptionchoicecategories/<int:pk>/', views.MenuItemOptionChoiceCategoryRetrieveUpdateDestroy.as_view(), name='menuitemoptionchoicecategory-retrieve-update-destroy'),
    path('menuitemoptionchoicecategoryoptions/', views.MenuItemOptionChoiceCategoryOptionListCreate.as_view(), name='menuitemoptionchoicecategoryoptions-list-create'),
    path('menuitemoptionchoicecategoryoptions/<int:pk>/', views.MenuItemOptionChoiceCategoryOptionRetrieveUpdateDestroy.as_view(), name='menuitemoptionchoicecategoryoption-retrieve-update-destroy'),
]