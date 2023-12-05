from django.views.generic import View
from django.shortcuts import render

#Dos tipos de vistas(De clases y de funciones)

class HomeView (View):
    def get(self, request, *args, **kwargs):
        context =  {
            
        }
        return render(request, 'index.html', context)