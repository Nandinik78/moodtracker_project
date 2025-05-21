from django.shortcuts import render, redirect
from .forms import MoodEntryForm
from .models import MoodEntry

def index(request):
    if request.method == 'POST':
        form = MoodEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the same page after saving
    else:
        form = MoodEntryForm()

    entries = MoodEntry.objects.all().order_by('-date')
    return render(request, 'tracker/index.html', {'form': form, 'entries': entries})
