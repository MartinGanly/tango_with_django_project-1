from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

#this is the index view, it takes a necessary HttpRequest obj 'request'
#returns a necessary HttpResponse(string:contentOfPage)
#template response is a python dictionary that maps template variable names with python variables
def index(request):
    #Construct a dictionary to pass the template engine as it's context
    #note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    #Return a rendered response to send to client
    #We make use of the shortcut function to make our lives easier
    #Note that the first parameter is the template we wish to use
    return render(request, 'rango/index.html', context=context_dict)
