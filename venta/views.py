from django.shortcuts import render

# Create your views here.
 def menu_view(request):
    return render(request, 'main/menu.html')




    def menu_view(request):
    return render(request, 'venta/menu.html')