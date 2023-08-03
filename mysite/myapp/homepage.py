from django.shortcuts import redirect, render

def homepage(request):
            # Render the homepage.html template and pass the image data as a variable to the template context
    return render(request,'homepage.html')