from django.shortcuts import render, redirect
from .forms import GameScoreForm
from .models import GameScore

# Create your views here.

def space_invaders(request):
    game_scores = GameScore.objects.all()[:5]
    all_game_scores = GameScore.objects.all()
    game_won = False

    if request.method == 'POST':
        form = GameScoreForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('space_invaders')
    else:
        form = GameScoreForm()
    
    context = {
        'form': form,
        'game_scores': game_scores,
        'all_game_scores': all_game_scores,
        'game_won': game_won,
    }

    template = 'space_invaders/space-invaders.html'

    return render(request, template, context)

def space_invaders_leaderboard(request):

    all_game_scores = GameScore.objects.all()

    context = {
        'all_game_scores': all_game_scores,
    }

    template = 'space_invaders/space-invaders-leaderboard.html'

    return render(request, template, context)

