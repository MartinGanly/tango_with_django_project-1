from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category
from rango.models import Page
# Create your views here.

#this is the index view, it takes a necessary HttpRequest obj 'request'
#returns a necessary HttpResponse(string:contentOfPage)
#template response is a python dictionary that maps template variable names with python variables
def index(request):
    #Construct a dictionary to pass the template engine as it's context
    #note the key boldmessage is the same as {{ boldmessage }} in the template!

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    #Return a rendered response to send to client
    #We make use of the shortcut function to make our lives easier
    #Note that the first parameter is the template we wish to use
    return render(request, 'rango/index.html', context=context_dict)

def show_category(request, category_name_slug):
    #create a context dictionary which we can pass
    # to the template rendering engine
    context_dict = {}

    try:
        # can we find a category name sug with the given name?
        #if we can't the .get() method raises a DoesNotExist exception
        # so the .get() method returns one model instance or raises an exception
        category = Category.objects.get(slug=category_name_slug)

        #retreive all of hte associated pages
        #note that filter() will return a list of page objects or an empty list
        pages = Page.objects.filter(category=category)

        #adds our results list to the template context under name pages
        context_dict['pages'] = pages
        #we also add the category object from
        #the database to the context dict
        #we'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        #do nothing
        #the template will display the no category message for us
        context_dict['category'] = None
        context_dict['pages'] = None

    #go render the respones and return it to the client
    return render(request, 'rango/category.html', context_dict)
