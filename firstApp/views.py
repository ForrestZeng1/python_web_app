from django.shortcuts import render
from django.http import HttpResponse
from .models import user, loginCredential

# Create your views here.
data = {}
data['functions'] = [['Cost', '0.00yeedollars ', '0.00yeedollars '],
                     ['Access to the archive? ', 'Yes ', 'Yes '],
                     ['Color picker? ', 'No ', 'Yes '],
                     ['Date picker? ', 'No ', 'Yes '],
                     ['Image Picker? ', 'No ', 'Yes '],
                     ['Number picker? ', 'No ', 'Yes '],
                     ['Pick from range?', 'No', 'Yes']]
users = user.objects.all()
loginCredentials = loginCredential.objects.all()
data['users'] = users
data['loginCredentials'] = loginCredentials


def index(request):
    return render(request, 'firstApp/index.html')
    # return HttpResponse('Here is my response!')


def archive(request):
    return render(request, 'firstApp/archive.html')


def about(request):
    return render(request, 'firstApp/about.html')


def premium(request):
    return render(request, 'firstApp/premium.html', data)


def contact(request):
    return render(request, 'firstApp/contact.html')


def coolWebsites(request):
    websites = [['Taobao', 'http://taobao.com'], [
                'Ymatou', 'http://ymatou.com'], ['Google', 'http://google.com']]
    return render(request, 'firstApp/coolWebsites.html', websites)


def getpremium(request):
    return render(request, 'firstApp/getpremium.html', data)


def premiumLogin(request):
    return render(request, 'firstApp/premiumLogin.html', data)


def premiumtab(request):
    authorized = False
    data_dict = dict()
    loginCredentials = loginCredential.objects.all()
    signupfirstname = request.POST.get('firstname')
    signuplastname = request.POST.get('lastname')
    signupyeename = request.POST.get('yeename')
    signupyeepassword = request.POST.get('yeepassword')
    signupyeepassword2 = request.POST.get('yeepasswordconf')
    logyeename = request.POST.get('logyeename')
    logyeepassword = request.POST.get('logyeepassword')
    if signupyeepassword == signupyeepassword2 and len(signupfirstname) <= 20 and len(signuplastname) <= 20 and len(signupyeename) <= 10 and len(signupyeename) > 5 and len(signupyeepassword) <= 10 and len(signupyeepassword) > 5:
        credentials = loginCredential(
            firstname=signupfirstname, lastname=signuplastname, username=signupyeename, password=signupyeepassword)
        credentials.save(
        )
        credentials.id()
        authorized = True

    for each in loginCredentials:
        if signupyeename == each.username:
            authorized = False
        if each.username == logyeename and each.password == logyeepassword:
            authorized = True
    data_dict['authorized'] = authorized
    return render(request, 'firstApp/premiumtab.html', data_dict)
