#3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)

def season (month):
    
    if month == 1 or month == 2 or month == 12 :
       season_1 = 'winter'
    elif month == 3 or month == 4 or month == 5:
        season_1 = 'spring'
    elif month == 6 or month == 7 or month == 8:
        season_1 = 'summer'
    elif month == 9 or month == 10 or month == 11:
        season_1 = 'autumn'
    else:
        season_1 = 'FORMAT for Month not Correct.'
    
    return season_1



print (season(7))