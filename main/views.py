from django.shortcuts import render

# views disini
def show_main(request):
    context = {
        'npm' : '2406411824',
        'name': 'Marco Imanuel',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
