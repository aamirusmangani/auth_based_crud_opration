from django.urls import path
from . import views
urlpatterns = [
    path('',views.GetAndPostData.as_view()),
    path('update/<int:id>/', views.UpdateData.as_view()),
    path('delete/<int:id>/', views.DeleteData.as_view()),
    path('signup/', views.signup),
    path('login/', views.login_user),
    path('logout/', views.logout_user),
]
