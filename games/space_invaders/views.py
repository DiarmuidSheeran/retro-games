from django.shortcuts import render, redirect
from .forms import GameScoreForm
from .models import GameScore

# Create your views here.

def space_invaders(request):
    game_scores = GameScore.objects.all()[:10]
    game_won = False

    if request.method == 'POST':
        form = GameScoreForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to create a new GameScore object
            return redirect('space_invaders')  # Redirect to prevent form resubmission
    else:
        form = GameScoreForm()
    
    context = {
        'form': form,
        'game_scores': game_scores,
        'game_won': game_won,
    }

    template = 'space_invaders/space-invaders.html'

    return render(request, template, context)

