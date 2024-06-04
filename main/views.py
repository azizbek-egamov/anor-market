from django.shortcuts import render, redirect
from django.http import *
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


people = [
    {
        "ism": "Akmal",
        "familiya": "Karimov",
        "yoshi": 28,
        "jinsi": "Erkak",
        "telefon": "+998901234567",
    },
    {
        "ism": "Dilnoza",
        "familiya": "Tursunova",
        "yoshi": 24,
        "jinsi": "Ayol",
        "telefon": "+998901234568",
    },
    {
        "ism": "Sardor",
        "familiya": "Rasulov",
        "yoshi": 30,
        "jinsi": "Erkak",
        "telefon": "+998901234569",
    },
    {
        "ism": "Feruza",
        "familiya": "Ismoilova",
        "yoshi": 26,
        "jinsi": "Ayol",
        "telefon": "+998901234570",
    },
    {
        "ism": "Jasur",
        "familiya": "Norboev",
        "yoshi": 32,
        "jinsi": "Erkak",
        "telefon": "+998901234571",
    },
]

from django.http import JsonResponse

def check_value(request):
    a = 99
    if request.method == 'GET':
        user_value = int(request.GET.get('number_input', 0))
        if user_value > a:
            new_value = user_value - a
            return JsonResponse({'message': f"Qiymat {a} ga kamaytirildi. Chegarasiga yetdi: {new_value}"})
        else:
            return JsonResponse({'message': "Qiymat 99 dan kichik."})
    return JsonResponse({'message': 'Noto\'g\'i so\'rov.'})

def homePage(request):
    u = request.user
    print(u)
    r = Category.objects.all()
    return render(request, "index.html", {"user": 'Nomalum foydalanuvchi', 'categ': r if r.exists() else 'False'})
    # if str(u) == "AnonymousUser":
    # elif str(u) == "admin":
    #     return redirect("/admin")
    # else:
    #     return render(request, "index.html", {"user": u})


def aboutPage(request):
    return render(request, "about.html", {"book": Book.objects.all()})

def CategoryPage(request, some_value):
    r = Category.objects.all()
    all = Products.objects.filter(category=some_value)
    context = {'cont': some_value, 'categ': r if r.exists() else 'False', 'prodct': all if all.exists() else 'False',}
    return render(request, 'category.html', context)

def ProductPage(request, some_value, id):
    r = Category.objects.all()
    all = Products.objects.filter(id=id)
    a1 = Products.objects.get(id=id)
    
    print(all)
    print(request.method)
    if request.method == "POST":
        soni = request.POST.get("soni")
        for i in all:
            m = i.info.split("\n")
            d = int(i.soni) - int(soni)
            a1.soni = d
            a1.save()   
            # us = Products.objects.get(id=id)
            # us.delete()
            # Products.objects.create(category=i.category, product_id=i.product_id, name=i.name, info=i.info, narx=i.narx, soni=d, rasm=i.rasm)
            Orders.objects.create(category=some_value, product_id=id, username=request.user, name=i.name, info = i.info, narx=i.narx, soni=soni, rasm=i.rasm, viloyat='xorazm', holat='tayorlanmoqda')
        context = {'cont': some_value, 'id':id, 'categ': r if r.exists() else 'False', 'prodct': all if all.exists() else 'False', 'mr': m}
        return render(request, 'product.html', context)
    else:
        for i in all:
            m = i.info.split("\n")
            print(str(m))
        context = {'cont': some_value, 'id':id, 'categ': r if r.exists() else 'False', 'prodct': all if all.exists() else 'False', 'mr': m}
        return render(request, 'product.html', context)


def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(
                request,
                "login.html",
                {
                    "error": "Login yoki parol noto'g'ri",
                    "clas": "error",
                    "us": username,
                    "ps": password,
                },
            )

    return render(request, "login.html")


def LogoutPage(request):
    logout(request)
    return redirect("home")


def SignupPage(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                return render(
                    request,
                    "signup.html",
                    {
                        "error": "Ushbu user band, boshqa o'ylab toping",
                        "clas": "error",
                        'fn': first_name,
                        'ln': last_name,
                        "em": email,
                        "us": username,
                        "p1": pass1,
                        "p2": pass2,
                    },
                )
            elif User.objects.filter(email=email).exists():
                return render(
                    request,
                    "signup.html",
                    {
                        "error": "Ushbu email band, boshqa email kiriting",
                        "clas": "error",
                        'fn': first_name,
                        'ln': last_name,
                        "em": email,
                        "us": username,
                        "p1": pass1,
                        "p2": pass2,
                    },
                )
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=pass1, first_name=first_name, last_name=last_name
                )
                user.save()
                login(request, user)
                return redirect("home")
        else:
            return render(
                request,
                "signup.html",
                {
                    "error": "Parollar mos kelmayabdi",
                    "clas": "error",
                    "em": email,
                    "us": username,
                    "p1": pass1,
                    "p2": pass2,
                },
            )
    return render(request, "signup.html")


def contactPage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        lname = request.POST.get("lname")
        age = request.POST.get("age")
        Users.objects.create(name=name, fname=lname, age=age)
        return redirect("about")
    else:
        return render(request, "contact.html")


def UpdatePage(request, id):
    try:
        user = Users.objects.get(id=id)
        if request.method == "POST":
            user.name = request.POST.get("name")
            user.fname = request.POST.get("lname")
            user.age = request.POST.get("age")
            Users.save()
            return redirect("about")

        return render(request, "update.html", {"cls": Users.objects.get(id=id)})
    except:
        return redirect("about")


def DeletePage(request, id):
    try:
        user = Users.objects.get(id=id)
        user.delete()
        return redirect("about")
    except:
        return redirect("about")


# Create your views here.
