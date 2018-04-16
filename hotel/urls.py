from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.users, name='users'),
    url(r'^orders/$', views.orders, name='orders'),
    url(r'^admin/menu/$', views.adminmenu, name='adminmenu'),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^foods/$', views.foods, name='foods'),
    url(r'^landing/$', views.landing, name='landing'),
    url(r'^sales/$', views.sales, name='sales'),
    url(r'^foodDetails/(?P<foodID>\d+)/$', views.food_details, name='food_details'),
    
    url(r'^add_user/(?P<ID>\d+)/$', views.add_user, name='add_user'),
    url(r'^delete_item/(?P<ID>\d+)/$', views.delete_item, name='delete_item'),
    url(r'^addTocart/(?P<foodID>\d+)/(?P<userID>\d+)/$', views.addTocart, name='addTocart'),
    url(r'^add_food/$', views.add_food, name='add_food'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^add_sales/$', views.add_sales, name='add_sales'),
    url(r'^confirm_order/(?P<orderID>\d+)/$', views.confirm_order, name='confirm_order'),
    url(r'^confirm_delivery/(?P<orderID>\d+)/$', views.confirm_delivery, name='confirm_delivery'),
    url(r'^editFood/(?P<foodID>\d+)/$', views.edit_food, name='edit_food'),
    url(r'^editSale/(?P<saleID>\d+)/$', views.edit_sales, name='edit_sales'),
]
