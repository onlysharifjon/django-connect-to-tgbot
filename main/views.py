from django.shortcuts import render

from main.management.commands.bot import bot

from main.forms import TaskForm


def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save()
            bot.send_document(5172746353, task.file, caption=task.title)
    return render(request, 'index.html', {})
