from django.shortcuts import render
from django.http import HttpResponse


def staff_index(request):
    return HttpResponse(
        """
        <div>
            <h1>Chef</h1>
        </div>
        <div>
            <h1>Super staff</h1>
        </div>
        """
    )
