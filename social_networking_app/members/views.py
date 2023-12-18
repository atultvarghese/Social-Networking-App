from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required()
def home(request):
    # if request.user.is_authenticated:
    #     user_list = User.objects.all()
    #     return render(request, 'registration/home.html', {'user_list': user_list})
    #
    # else:
    #     # Do something for anonymous users.
    #     print("Not Authenticated home")
    #     return render(request, 'registration/register.html')

    user_list = User.objects.all()
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
        user_list = User.objects.all()
        return render(request, 'registration/home.html', {'user_list': user_list})

    else:
        # Do something for anonymous users.
        print("Not Authenticated reg")
        return render(request, 'registration/register.html')
