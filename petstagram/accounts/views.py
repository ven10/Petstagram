from django.shortcuts import render


def login(request):
    context = {}
    return render(request, 'accounts/login-page.html', context)


def register(request):
    context = {}
    return render(request, "accounts/register-page.html", context)


def profile_delete(request, pk: int):
    context = {}
    return render(request, 'accounts/profile-delete-page.html', context)


def profile_details(request, pk: int):
    context = {}
    return render(request, 'accounts/profile-details-page.html', context)


def profile_edit(request, pk: int):
    context = {}
    return render(request, 'accounts/profile-edit-page.html', context)


def signout_user(request):
    context = {}
    return None
