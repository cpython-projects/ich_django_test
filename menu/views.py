from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', context={})

def menu_index(request):
    return HttpResponse(
        """
        <div>
            <h1>Завтраки</h1>
        </div>
        <div>
            <h1>Обеды</h1>
        </div>
        """
    )