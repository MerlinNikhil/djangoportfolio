#view.py

from django.shortcuts import render
from .models import Profile, AboutMe, Projects, Education, Experience, Contact, Skill
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Profile

# Create your views here.
def main(request):
    profile = Profile.objects.first()
    aboutme=AboutMe.objects.first()
    skills = Skill.objects.all()
    projects=Projects.objects.all()
    education=Education.objects.all()
    experience=Experience.objects.all()
    contact=Contact.objects.first()



    return render(request,'home.html',{
        'profile': profile,
        'aboutme':aboutme,
        'skills': skills,
        'projects':projects,
        'education':education,
        'experience':experience,
        'contact':contact,
        })

# views.py


def download_resume(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    
    if not profile.resume:
        raise Http404("Resume not found for this profile.")

    file_path = profile.resume.path
    with open(file_path, 'rb') as resume_file:
        response = HttpResponse(resume_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{profile.name}_resume.pdf"'
        return response

def project_details(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)
    return render(request, 'project_details.html', {'project': project})