from django.contrib.auth import login as auth_login
from django.shortcuts import redirect, render, HttpResponse
from . forms import *
from django.contrib.auth import authenticate, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# MAIN PAGE


def index(request):
    return render(request, 'indexpage.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def contactus(request):
    return render(request, 'contact.html')


def popularbooks(request):
    return render(request, 'books.html')


def contactus(request):
    if request.method == "POST":
        usname = request.POST.get('usname')
        print(usname)
        email = request.POST.get('email')
        print(email)
        message = request.POST.get('message')
        contact_list = Contact.objects.create(
            name=usname, email=email, message=message)
        contact_list.save()
        messages.success(request, f"sended")
        return redirect('index')
        print('form saved')
    return render(request, 'contact.html')

# librarian


def li_register(request):
    form = li_registerForm()
    if request.method == 'POST':
        form = li_registerForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            print("form saved")
            messages.success(request, f"New account created")
            return redirect('li_login')
        else:
            print('not saved')
            messages.success(request, f"check the details")
            form = li_registerForm()
    context = {"form": form}
    return render(request, "librarian/lr_register.html", context)


def li_login(request):
    form = li_LoginForm()
    if request.method == 'POST':
        form = li_LoginForm(data=request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if form.is_valid():
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"loginned suceesfully")
                return redirect('li_index')

            else:
                print("user not found")
                messages.success(request, f"please try again")
        else:
            form = li_LoginForm()
    context = {'form': form}
    return render(request, 'librarian/lr_login.html', context)

@login_required
def li_index(request):
    return render(request, "librarian/lr_index.html")

@login_required
def book_add(request):
    form = lr_addbookForm()
    if request.method == 'POST':
        form = lr_addbookForm(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            form.save()
            print("book added")
            messages.success(request, f"BOOK ADDED")
            return redirect("li_bookview")
        else:
            form = lr_addbookForm()
            print("not added")
            messages.success(request, f"please try again")
    context = {
        'form': form}
    return render(request, 'librarian/lr_addbook.html', context)

@login_required
def book_view(request):
    show_books = lr_addbook.objects.all()
    print(show_books)
    context = {
        'show_books': show_books}
    return render(request, "librarian/li_viewbooks.html", context)

@login_required
def booktaken(request):
    takedbooks = book_rent.objects.all()
    context = {
        'takedbooks': takedbooks}
    return render(request, "librarian/cu_booktaken.html", context)

@login_required
def lr_bookedit(request, id):
    bookform = lr_addbook.objects.get(id=id)
    form = lr_addbookForm(instance=bookform)
    if request.method == 'POST':
        form = lr_addbookForm(request.POST, request.FILES, instance=bookform)
        if form.is_valid():
            form.save()
            messages.success(request, f"edited")
            return redirect('li_bookview')

    context = {'form': form, 'id': id}
    return render(request, 'librarian/lr_editbook.html', context)

@login_required
def lr_bookdelete(request, id):
    book = lr_addbook .objects.get(id=id)
    book.delete()
    messages.success(request, f"deleted suceesfully")
    return redirect('li_bookview')

@login_required
def lr_delete_cu(request, id):
    buyer = book_rent .objects.get(id=id)
    buyer.delete()
    messages.success(request, f"deleted suceesfully")
    return redirect('li_booktaken')

@login_required
def lr_password_change(request):
    form = lr_StPasswordForm(request.user)
    if request.method == 'POST':
        form = lr_StPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            print("password changed")
            messages.success(request, f"password changed")
            return redirect("li_login")
        else:
            messages.success(request, f"please try again")
            form = lr_StPasswordForm(request.user)

    context = {'form': form}
    return render(request, "librarian/lr_changepass.html", context)

# READER


def cu_register(request):
    form = cu_registerForm()
    if request.method == 'POST':
        form = cu_registerForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            print("form saved")
            messages.success(request, f"Registerd succesfully")
            return redirect('cu_login')
        else:
            print('not saved')
            messages.success(request, f"please try again")
            form = cu_registerForm()
    context = {"form": form}
    return render(request, "customer/cu_register.html", context)


def cu_login(request):
    form = cu_LoginForm()
    if request.method == 'POST':
        form = cu_LoginForm(data=request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if form.is_valid():
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"Logined succesfully")
                return redirect('cu_index')
            else:
                messages.success(request, f"please try again")
                print("user not found")
        else:
            form = cu_LoginForm()

    context = {'form': form}
    return render(request, 'customer/cu_login.html', context)

@login_required
def cu_index(request):
    return render(request, "customer/cu_index.html")

@login_required
def cu_changepass(request):
    form = cu_StPasswordForm(request.user)
    if request.method == 'POST':
        form = cu_StPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            print("password changed")
            messages.success(request, f"changed")
            return redirect("cu_login")
        else:
            form = cu_StPasswordForm(request.user)
            messages.success(request, f"not changed")

    context = {'form': form}
    return render(request, "customer/cu_changepass.html", context)

@login_required
def cubook_view(request):
    show_books = lr_addbook.objects.all()
    print(show_books)
    context = {
        'show_books': show_books}
    return render(request, "customer/cu_viewbook.html", context)

@login_required
def cu_rent_book(request):
    form = Cu_Rentbookform()
    if request.method == 'POST':
        form = Cu_Rentbookform(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            messages.success(request, f"book taked")
            return redirect("cu_bookview")
        else:
            form = Cu_Rentbookform()
    context = { 
        'form': form}
    return render(request, 'customer/rentbook.html', context)


# ADMIN


def ad_login(request):
    form = ad_LoginForm()
    if request.method == 'POST':
        form = ad_LoginForm(data=request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if form.is_valid():
            if user.is_superuser:
                auth_login(request, user)
                messages.success(request, f"Loginned")
                return redirect('ad_index')
            else:
                print("user not found")
                messages.success(request, f"please try again")
        else:
            form = ad_LoginForm()
    context = {'form': form}
    return render(request, 'Admin/ad_login.html', context)

@login_required
def ad_index(request):
    return render(request, "Admin/ad_index.html")

@login_required
def ad_changepass(request):
    form = ad_StPasswordForm(request.user)
    if request.method == 'POST':
        form = ad_StPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            print("password changed")
            messages.success(request, f"changed")
            return redirect("ad_login")
        else:
            form = ad_StPasswordForm(request.user)
            messages.success(request, f"notchanged")
    context = {'form': form}
    return render(request, "admin/ad_changepass.html", context)

@login_required
def con_peoples(request):
    show_peoples = Contact.objects.all()
    print(show_peoples)
    context = {
        'show_peoples': show_peoples}
    return render(request, "admin/ad_contactedP.html", context)

@login_required
def ad_delCon(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('con_peoples')

@login_required
def ad_readers(request):
    reader = cu_profile.objects.all()
    print(reader)
    context = {
        'readers': reader}
    return render(request, "admin/ad_readers.html", context)

@login_required
def ad_delreaders(request, id):
    readers = cu_profile.objects.get(id=id)
    readers.delete()
    return redirect('readers')

@login_required
def ad_bookview(request):
    show_books = lr_addbook.objects.all()
    print(show_books)
    context = {
        'show_books': show_books}
    return render(request, "admin/ad_bookview.html", context)

@login_required
def ad_bookedit(request, id):
    bookform = lr_addbook.objects.get(id=id)
    form = lr_addbookForm(instance=bookform)
    if request.method == 'POST':
        form = lr_addbookForm(request.POST, request.FILES, instance=bookform)
        if form.is_valid():
            form.save()
            messages.success(request, f"edited")
            return redirect('ad_bookview')
    context = {'form': form, 'id': id}
    return render(request, 'admin/ad_editbook.html', context)

@login_required
def ad_bookdelete(request, id):
    readers = lr_addbook.objects.get(id=id)
    readers.delete()
    return redirect('ad_bookview')

@login_required
def ad_show_li(request):
    adminshow_li = lr_profile.objects.all()
    context = {
        'adminshow_li': adminshow_li}
    return render(request, "admin/adminshow_li.html", context)

@login_required
def ad_del_li(request, id):
    libr = lr_profile.objects.get(id=id)
    libr.delete()
    return redirect('ad_show_li')

@login_required
def ad_booktaken(request):
    takedbooks = book_rent.objects.all()
    context = {
        'takedbooks': takedbooks}
    return render(request, "admin/ad_booktaken.html", context)

@login_required
def ad_booktakendel(request, id):
    booktaken = book_rent .objects.get(id=id)
    booktaken.delete()
    return redirect('ad_booktaken')

@login_required
def lr_send_messages(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            your_object = form.save(commit=False)
            your_object.sender = request.user.username
            your_object.save()
            messages.success(request, f"sended")
            return redirect("li_index")
        else:
            print("check the data")
            messages.success(request, f"check the data")
    context = {'form': form}
    return render(request, 'librarian/lr_sendmessage.html', context)

@login_required
def show_messages(request):
    my_msgs = li_message.objects.filter(reciever=request.user.username)
    context = {'my_msgs': my_msgs}
    return render(request, 'customer/showmessages.html', context)

@login_required
def adshow_messages(request):
    my_msgs = li_message.objects.filter(reciever=request.user.username)
    context = {'my_msgs': my_msgs}
    return render(request, 'admin/adshowmessages.html', context)

@login_required
def lrshow_messages(request):
    my_msgs = li_message.objects.filter(reciever=request.user.username)
    context = {'my_msgs': my_msgs}
    return render(request, 'librarian/showmessages.html', context)

@login_required
def sendmessages(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            your_object = form.save(commit=False)
            your_object.sender = request.user.username
            your_object.save()
            messages.success(request, f"sended")

        else:
            print("check the data")
            messages.success(request, f"chec the data")
    context = {'form': form}
    return render(request, 'messages.html', context)
