from django.shortcuts import render
from .models import Project, Experience

# Create your views here.
def projects(request):
      projects = Project.objects.all()
      return render(request, 'content/projects.html', {
            'projects':projects
      })

def experience(request):
      #get info from Admin panel
      experiences = Experience.objects.all()
      return render(request, 'content/experience.html', {"experiences":experiences})