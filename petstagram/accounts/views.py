from django.shortcuts import render


def signup_user(request):
    context = {}
    return render(request, "accounts/signup_user.html", context)


def signin_user(request):
    context = {}
    return render(request, 'accounts/signin_user.html', context)


def signout_user(request):
    context = {}
    return None


def details_profile(request, pk):
    context = {}
    return render(request, 'accounts/details_profile.html', context)


def edit_profile(request, pk):
    context = {}
    return render(request, 'accounts/edit_profile.html', context)


def delete_profile(request, pk):
    context = {}
    return render(request, 'accounts/delete_profile.html', context)

