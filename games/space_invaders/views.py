from django.shortcuts import render

# Create your views here.
def space_invaders(request):

    template = 'space_invaders/game.html'

    return render(request, template)