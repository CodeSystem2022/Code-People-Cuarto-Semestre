from django.shortcuts import render
from django.views.generic import View

class Indexx(View):
    
    def get(self, request):
        return render(request, 'index.html')