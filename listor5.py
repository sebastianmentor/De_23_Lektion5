lista_med_djur:list[str] = []
# MAX_ANTAL_DJUR:int = 10

while True:
    djur_eller_avsluta = input(
        'Skriv in ett djur eller q för att avsluta: '
        ).lower()
    
    if djur_eller_avsluta == 'q':
        break
    elif djur_eller_avsluta in lista_med_djur:
        print('Djuret finns redan i listan!')
    else:
        lista_med_djur.append(djur_eller_avsluta)

lista_med_djur.sort()



for djur in lista_med_djur:
    print(f"{djur.capitalize()}")



