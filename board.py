# placera ut bönder (lilla ‘b’)  på rad 2 och rad 7 skriv ut schackbrädet 
# googla på  python termcolor module och se om du kan 
# skriva ut svarta bönder och vita bönder!
from termcolor import colored

tom_lista = 8*[' ']
board = [tom_lista[:] for i in range(8)]

for i in range(8):
    for j in range(8):
        if (j+i) % 2 == 0:
            färg = 'on_white'
        else:
            färg = 'on_black'
        
        if i == 1:
            ruta = colored(' b ',color='light_grey', on_color=färg)
        elif i == 6:
            ruta = colored(' b ',color='dark_grey', on_color=färg)
        else:
            ruta = colored('   ', on_color=färg)
        board[i][j] = ruta


for row in board:
    for item in row:
        print(f'{item}', end='')
    print()