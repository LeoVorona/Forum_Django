from django.urls import path, include
from rest_framework import routers
from api.views import CheckBoxViewSet
from api import views


router = routers.DefaultRouter()
router.register('CheckBox', CheckBoxViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('CheckBox_list', views.CheckBox_list, name='CheckBox_list'),
    #path('CheckBox_list/<int:pk>', views.CheckBox_detail, name='CheckBox_detail'),
    #path('CheckBox_create', views.CheckBox_create, name = 'CheckBox_create'),
    #path('CheckBox_update/<int:pk>', views.CheckBox_update, name = 'CheckBox_update'),
    #path('CheckBox_delete/<int:pk>', views.CheckBox_delete, name = 'CheckBox_delete'),
    #path('CheckBox_list', views.CheckBoxList.as_view(), name='user_list'),
    path('data', views.DataView.as_view()),
]