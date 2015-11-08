from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Profile, Charity


# Create your views here.
def index(request):
    profiles = Profile.objects.all()[:4]
    vets = []
    for profile in profiles:
        vet = {}
        vet["name"] = profile.name
        vet["years_of_service"] = profile.years_of_service
        vet["story"] = profile.story
        vet["goal"] = profile.goal
        vet["id"] = profile.id
        vets.append(vet)
    context = dict()
    context["vets"] = vets
    return render(request, 'home-page.html', context)
    
def allProfiles(request):
    profiles = Profile.objects.all()
    vets = []
    for profile in profiles:
        vet = {}
        vet["name"] = profile.name
        vet["years_of_service"] = profile.years_of_service
        vet["story"] = profile.story
        vet["goal"] = profile.goal
        vet["id"] = profile.id
        vets.append(vet)
    context = dict()
    context["vets"] = vets
    return render(request, 'all-projects.html', context)
    
def detail(request, profile_id):
    vet = get_object_or_404(Profile, pk=profile_id)
    context = {'vet': vet}
    return render(request, 'detail.html', context)
    
def checkout(request, profile_id):
    donation_amount = int(request.POST.get("donate"))
    profile = get_object_or_404(Profile, pk=profile_id)
    profile.current += donation_amount
    profile.save()
    context = {'number': profile.current}
    return render(request, 'checkout.html', context)
    
def new_project(request):
    if request.user.is_authenticated():

        if request.method == 'POST':
            name = request.POST.get("first_name") + request.POST.get("last_name")
            description = request.POST.get("description")
            email = request.POST.get("email")
            duration = request.POST.get("duration")
            goal = request.POST.get("goal")
            
            profile = Profile(name=name, years_of_service=duration, story=description, goal=goal, current=0)
            
            profile.save()
            return HttpResponseRedirect('/profiles')
        else:
            return render(request, 'new-project.html')
            
    else:
        return HttpResponseRedirect('/users/register')
    
def charitiesIndex(request):
    charities = Charity.objects.all()
    chars = []
    for charity in charities:
        char = {}
        char['charity_name'] = charity.charity_name
        char['description'] = charity.description
        char['goal'] = charity.goal
        char['id'] = charity.id
        chars.append(char)
    context = dict()
    context['chars'] = chars
    return render(request, 'charities-home-page.html', context)

def charitiesDetail(request, charity_id):
    print "charitiesDetail"
    char = get_object_or_404(Charity, pk=charity_id)
    context = {'char': char}
    return render(request, 'charities-detail.html', context)
    
def charitiesCheckout(request, charity_id):
    donation_amount = int(request.POST.get("donate"))
    char = get_object_or_404(Charity, pk=charity_id)
    char.current += donation_amount
    char.save()
    context = {'number': char.current}
    return render(request, 'charities-checkout.html', context)