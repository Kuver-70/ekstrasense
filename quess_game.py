from random import randint

def game():
    ekstrasense_levels = [0, 0, 0]
    ekstrasense_guess_numbers = [0, 0, 0]
    ekstrasense_guess_numbers[0] = randint(0, 10)
    ekstrasense_guess_numbers[1] = randint(0, 10)
    ekstrasense_guess_numbers[2] = randint(0, 10)


    print("Загадайте число от 0 до 10: ")
    print("Догадка экстрасенса № 1 - ", ekstrasense_guess_numbers[0])
    print("Догадка экстрасенса № 2 - ", ekstrasense_guess_numbers[1])
    print("Догадка экстрасенса № 3 - ", ekstrasense_guess_numbers[2])

    print("Теперь впишите ваше число: ", end='')
    user_number = int(input())
    print("Ваше число - ", user_number)

    if user_number in ekstrasense_guess_numbers:
        for i in range(len(ekstrasense_guess_numbers)):
            if user_number == ekstrasense_guess_numbers[i]:
                ekstrasense_levels[i] += 1
                print("Ух ты! Экстрасенс под № %s угадал ваше число! Ведь это " %(i+1), ekstrasense_guess_numbers[i], ", верно?")
                print("Этот экстрасенс получает плюс 1 к своему уровню достверности! И теперь его уровень достверности составляет ",
                ekstrasense_levels[i])
    else:
        print(
            "Ни один из экстрасенсов не угадал вашего числа. И поэтому у них у всех уровень достоверности уменьшается на 1.")
        if ekstrasense_levels[0] > 0:
            ekstrasense_levels[0] -= 1
        elif ekstrasense_levels[1] > 0:
            ekstrasense_levels[1] -= 1
        elif ekstrasense_levels[2] > 0:
            ekstrasense_levels[2] -= 1

    print("Уровни достоверности экстрасенсов:", ekstrasense_levels[0], ekstrasense_levels[1], ekstrasense_levels[2])

game()