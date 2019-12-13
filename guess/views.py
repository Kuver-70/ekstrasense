from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from random import randint


ekstrasense_levels = [0, 0, 0] # уровни доверенности экстрасенсов
ekstrasense_guess_numbers = [0, 0, 0] # догадки экстрасенсов
user_quess_history = [] # история догадок пользователя
begining = True
user_number = None # Загаданное пользователем число
ekstrasense_1_guess_hystory = []
ekstrasense_2_guess_hystory = []
ekstrasense_3_guess_hystory = []

@csrf_exempt
def game(request):
    global ekstrasense_levels, ekstrasense_guess_numbers, begining, user_number
    if request.method == 'POST' and request.POST.get('user_number'):
        ekstrasense_guess_numbers[0] = randint(0, 10)
        ekstrasense_1_guess_hystory.append(ekstrasense_guess_numbers[0])
        ekstrasense_guess_numbers[1] = randint(0, 10)
        ekstrasense_2_guess_hystory.append(ekstrasense_guess_numbers[1])
        ekstrasense_guess_numbers[2] = randint(0, 10)
        ekstrasense_3_guess_hystory.append(ekstrasense_guess_numbers[2])
        user_number = int(request.POST['user_number'])
        user_quess_history.append(user_number)

        for i in range(len(ekstrasense_guess_numbers)): # Ищем, какая догадка экстрасенса совпала с пользовательским числом
            if user_number == ekstrasense_guess_numbers[i]:
                ekstrasense_levels[i] += 1 # Увеличиваем уровень доверия отгадавшего экстрасенса
            else:
                if ekstrasense_levels[i] > 0:  # Условие, чтобы уровень доверенности экстрасенсов не уходил в минус
                    ekstrasense_levels[i] -= 1 # Уменьшаем уровень доверия неотгадавшего экстрасенса

    return render(request, 'index.html', {
        'ekstrasense_guess_numbers': ekstrasense_guess_numbers,
        'user_number': user_number,
        'user_quess_history': user_quess_history,
        'ekstrasense_1_guess_hystory': ekstrasense_1_guess_hystory,
        'ekstrasense_2_guess_hystory': ekstrasense_2_guess_hystory,
        'ekstrasense_3_guess_hystory': ekstrasense_3_guess_hystory,
        'ekstrasense_levels': ekstrasense_levels
        })

# Create your views here.