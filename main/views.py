from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Muhammad Fadhlan Karimuddin',
        'class': 'PBP F'
    }
    return render(request, "main.html", context)