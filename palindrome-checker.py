from colorama import *
init()
frase = input('Digite uma frase: ').strip().upper()
frase_sem_esp = (frase.replace(" ", ""))
inverso = (frase_sem_esp[::-1])
print('O inverso de {} é {}'.format(frase_sem_esp, inverso))
if frase_sem_esp == inverso:
    print(Fore.GREEN+'A frase digitada é um palíndromo')
else:
    print(Fore.RED+'A frase digitada não é um palíndromo')
