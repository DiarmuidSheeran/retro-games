from django.shortcuts import render

# Create your views here.
def space_invaders(request):

    template = 'space_invaders/space-invaders.html'

    return render(request, template)