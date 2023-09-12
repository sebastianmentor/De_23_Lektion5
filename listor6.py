secret = list("hemligt")

LEN_OF_SECRET = len(secret)

index = 0
reset = True

while True:
    if reset:
        print('Skriv in det hemliga lösenordet:')
    letter_input =  input('Skriv bokstav')
    if index == LEN_OF_SECRET-1:
        print('Grattis!! Du kunde lösenordet!')
        break
    
    if secret[index]== letter_input:
        print('Korrekt! Vi fortsätter!')
        index+=1
        reset = False
        continue

    index = 0
    reset = True
    


    # for letter in secret:
    #     letter_input =  input('Skriv bokstav')
    #     if letter == letter_input:
    #         print('Korrekt!')
    #         continue
    #     break
    
