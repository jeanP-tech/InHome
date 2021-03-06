from django.shortcuts import render, get_object_or_404, redirect

def main(request):
    return render(request, 'home/main.html', {})

def login(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'home/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'home/login.html')

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"]
            )
            auth.login(request, user)
            return redirect('index')
        return render(request, "home/signup.html")
    return render(request, 'home/signup.html')
