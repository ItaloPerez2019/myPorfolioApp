"""todo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views
from expense.models import User, Expense
from rest_framework import routers, serializers, viewsets

from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as vi

# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#
#
# # Serializers define the API representation.
# class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Expense
#         fields = ('user', 'description', 'amount', 'types')
#
#
# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# # ViewSets define the view behavior.
# class ExpenseViewSet(viewsets.ModelViewSet):
#     queryset = Expense.objects.all()
#     serializer_class = ExpenseSerializer
#
# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'user', UserViewSet)
# # router.register(r'expense', ExpenseViewSet)



urlpatterns = [
    path('', views.api_root),
    path('user/', views.UserList.as_view(), name='user-list'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('expense/', views.ExpenseList.as_view(), name='expense-list'),
    path('expense/<int:pk>/', views.ExpenseDetail.as_view()),
    path('api-token-auth/', vi.obtain_auth_token),
    # url(r'^user/$', views.user_list, name='user_list'),
    # url(r'^user/(?P<pk>[0-9]+)$', views.user_detail, name='user_detail'),
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^expense/$', views.expense_list, name='expense_list'),
    # # url(r'^tasks/(?P<pk>[0-9]+)$', views.task_detail, name='task_detail'),
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)