# imports
import methods
import keyboard

p = True
while p:
    matricula = input('MATRICULA: ')
    matricula = matricula[0:8]
    print("\n")
    print("-------------------------------------------------------------------------")
    print("\n")
    print('MATRICULA DO ALUNO: ',matricula)
    print("\n")
    check = input('CONFIRMAR MATRICULA \n [ENTER]Confirmar  [t/T]Tentar novamente : ')
    print("\n")
    print("-------------------------------------------------------------------------")
    if(check == 't' or check == 'T'):
        continue
    elif(keyboard.is_pressed('enter')):
        print('MATRICULA CONFIRMADA!')
        methods.writeOnFile(matricula)
    else:
        print('Comando Não confirmado, tente novamente!')
        check

# methods.writeOnFile(matricula)
methods.readOfFile("matriculas.csv")




