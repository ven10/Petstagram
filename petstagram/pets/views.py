from django.shortcuts import render


# Create your views here.

def pet_add_page(request):
    context = {}
    return render(request, 'pets/pet-add-page.html', context)


def pet_delete_page(request, username: str, pet_slug: str):
    context = {}
    return render(request, 'pets/pet-delete-page.html', context)


def pet_edit_page(request, username: str, pet_slug: str):
    context = {}
    return render(request, 'pets/pet-edit-page.html', context)


def pet_details_page(request,  username: str, pet_slug: str):
    context = {}
    return render(request, 'pets/pet-details-page.html', context)
