from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# def home(request):
#     return HttpResponse("""<h1>hey , i am django server.</h1>
#                         <p>hey people</p>
#                         <hr>
#                         <h3 style="color:red">loving it</h3>
#                         """)

def home(request):
    peoples=[
        {'name':'a','age':71},
        {'name':'b','age':9},
        {'name':'c','age':19},
        {'name':'d','age':7},
        {'name':'e','age':35}
    ]
    #if we want to send data from view to template we can do it by the help of context.

    return render(request, "index.html",context= {'peoples':peoples})


def success_page(request):
    return HttpResponse("hey,this is success page.")