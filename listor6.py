secret = list("hemligt")


while True:
    print('Skriv in det hemliga lösenordet:')
    for letter in secret:
        letter_input =  input('Skriv bokstav')
        if letter == letter_input:
            print('Korrekt!')
            continue
        break
    
