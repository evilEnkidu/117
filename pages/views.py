from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
# function based view
def test_view(request):
      return render(request, "pages/test.html")

def about_view(request):
      return render(request, 'pages/about.html')

def contact_view(request):
      if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                  print("Email sent")
                  name = form.sanitized_data['name']
                  email = form.sanitized_data['email']
                  message = form.sanitized_data['message']
                  send_mail(
                        "email from " + name, 
                        message,
                        email,
                        ['websmithmxl@gmail.com']
                  )
            else: 
                  print("Invalid data on the form")
      else:
            #display page
            form = ContactForm()      

      form = ContactForm()
      return render(request, "pages/contact.html", {"form": form})
