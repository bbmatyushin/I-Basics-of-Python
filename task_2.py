# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите
# в формате чч:мм:сс. Используйте форматирование строк.

user_time = int(input('Укажиет время в секундах: '))

hours = user_time // 3600
if hours < 10:
    hours = '0' + str(hours)  # переводим в формат чч

minutes = user_time % 3600 // 60
if minutes < 10:
    minutes = '0' + str(minutes)  # переводим в формат мм

seconds = user_time % 3600 % 60
if seconds < 10:
    seconds = '0' + str(seconds)  # переводим в формат сс

print(f'{hours}:{minutes}:{seconds}')
