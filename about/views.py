from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.


def about_me(request):
    """
    Render the about me page. the most recent information on the website Author and allows user callaborattion requests.

    Displays and individual instance of :model:`about.About`.

    **Context**
    ``about``
        The most recent instance of :model:`about.About`.
        ``collaborate_form``
        An instance of :form:`about.CollaborateForm` for user collaboration requests.
    **Template:**
    :template:`about/about.html`
    """
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            collaborate_form = CollaborateForm()
            messages.add_message(request, messages.SUCCESS, "Collaboration request receieved! I endeavor to respond within 2 working days.")

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
         },
    )
