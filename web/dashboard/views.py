from django.shortcuts import render

# Create your views here.

def IndexView(request):
    return render(request, 'components/index.html')

def BlankView(request):
    return render(request, 'components/blank.html')

def ButtonsView(request):
    return render(request, 'components/buttons.html')

def LoginView(request):
    return render(request, 'components/login.html')

def Page404View(request):
    return render(request, 'components/404.html')

def CardsView(request):
    return render(request, 'components/cards.html')

def ChartsView(request):
    return render(request, 'components/chats.html')

def ForgotPassView(request):
    return render(request, 'components/forgot-password.html')

def RegisterView(request):
    return render(request, 'components/register.html')

def UtilAnimationView(request):
    return render(request, 'components/utilities-animation.html')

def UtilBorderView(request):
    return render(request, 'components/utilities-border.html')

def UtilColorView(request):
    return render(request, 'components/utilities-color.html')

def UtilOtherView(request):
    return render(request, 'components/utilities-other.html')