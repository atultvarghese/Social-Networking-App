from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def home(request):
    user_list = User.objects.all()
    # for user in user_list:
    #     print(vars(user))
    return render(request, 'registration/home.html', {'user_list': user_list})


def register(request):

    if request.method == "POST":
        # Create user and save to the database
        print(request.POST.get("email"))
        user = User.objects.create_user(request.POST.get("email").split('@')[0], email=request.POST.get("email"),
                                        password=request.POST.get("psw"))

        # # Update fields and then save again
        # user.first_name = 'Tyrone'
        # user.last_name = 'Citizen'
        user.save()
        return HttpResponse("Hello register successfully completed!")

    if request.user.is_authenticated:
        # Do something for authenticated users.
        print("Authenticated")
        return render(request, 'registration/home.html')

    else:
        # Do something for anonymous users.
        print("Not Authenticated")
        return render(request, 'registration/register.html')

