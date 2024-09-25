from django.shortcuts import render


def photo_add_page(request):
    context = {}
    return render(request, 'photos/photo-add-page.html', context)


def photo_edit_page(request, pk: int):
    context = {}
    return render(request, 'photos/photo-edit-page.html', context)


def photo_details_page(request, pk: int):
    context = {}
    return render(request, 'photos/photo-details-page.html', context)
