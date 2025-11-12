from django.shortcuts import render
from .models import UserName
from .forms import NameForm

def index(request):
    """Главная страница с формой ввода имени"""
    form = NameForm()
    return render(request, 'greeting_app/index.html', {'form': form})

def greeting(request):
    """Обрабатываем имя и показываем приветствие"""
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            # Сохраняем имя в базе данных
            UserName.objects.create(name=name)
            # Отображаем приветствие
            return render(request, 'greeting_app/greeting.html', {'name': name})
        else:
            # если форма не валидна, показываем ошибки
            return render(request, 'greeting_app/index.html', {'form': form})
    else:
        # Если GET запрос, перенаправляем на главную
        form = NameForm()
        return render(request, 'greeting_app/index.html', {'form': form})

def name_list(request):
    """Страница со списком всех введенных имен"""
    names = UserName.objects.all().order_by('-created_at')
    return render(request, 'greeting_app/name_list.html', {'names': names})