from django.urls import path
from .import views
urlpatterns = [
    path('signup/',views.register,name='register'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('pass-change/',views.pass_change,name='pass_change'),
    path('profile/', views.profile, name='profile'),
    path('datachange/', views.user_change_data, name='change_data'),
    path('add/',views.AddCarCreateView.as_view(),name='add_car'),
    path('details/<int:id>',views.ReadCarDetailView.as_view(),name='read_car'),
    path('buy/<int:id>/', views.buy_car, name='buy_car'),
    path('comment/<int:id>/', views.commentPeople, name='comment_car'),

]
