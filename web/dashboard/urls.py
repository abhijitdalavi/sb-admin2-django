from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    #path('editar_contrato/<int:id>', v.editar_contrato, name='editar_contrato'),
    path('', views.IndexView, name="index"),
    path('blank/', views.BlankView, name="blank"),
    path('buttons/', views.ButtonsView, name="buttons"),
    path('login/', views.LoginView, name="login"),
    path('404/', views.Page404View, name="404"),
    path('cards/', views.CardsView, name="cards"),
    path('charts/', views.ChartsView, name="chats"),
    path('forgot-password/', views.ForgotPassView, name="forgot-password"),
    path('register/', views.RegisterView, name="register"),
    path('utilities-animation/', views.UtilAnimationView, name="utilities-animation"),
    path('utilities-border/', views.UtilBorderView, name="utilities-border"),
    path('utilities-color/', views.UtilColorView, name="utilities-color"),
    path('utilities-other/', views.UtilOtherView, name="utilities-other"),
]