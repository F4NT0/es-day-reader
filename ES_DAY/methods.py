# imports
import keyboard


class Methods:
    def __init__(self);

    def reading(self):
        p = True
        while p:
            matricula = input('MATRICULA: ')
            matricula = matricula[0:7]
            print('MATRICULA DO ALUNO: ',matricula)
            check = input('CONFIRMAR MATRICULA \n [ENTER]Confirmar  [t/T]Tentar novamente : ')
            if(check == 't' or check == 'T'):
                continue
            else if keyboard.is_pressed('enter'):
                print('MATRICULA CONFIRMADA!')
                writeOnFile(matricula)
                