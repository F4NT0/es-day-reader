def writeOnFile(matricula):
    file = open("matriculas.csv","a+")
    matricula = f"{matricula}\n"
    file.write(matricula)
    file.close()
    
def readOfFile(arquivo):
    file = open(arquivo,"r")
    content = file.read()
    print(content)
    file.close()

def welcomeScreen():
    print('--------------------------------------------------------------------')
    print('________ _____          ______    __ __     __ ____   ___  ___ ___  ')
    print('|  ____|/ ____|         |  __ \   /\ \ \   / / |__ \ / _ \/_ |/ _ \ ')
    print('| |__  | (___   ______  | |  | | /  \ \ \_/ /     ) | | | || | (_) |')
    print('|  __|  \___ \  ______  | |  | |/ /\ \ \   /     / /| | | || |\__, |')
    print('| |____ ____) |         | |__| / ____ \ | |     / /_| |_| || |  / / ')
    print('|______|_____/          |_____/_/    \_ \_|    |____|\___/ |_| /_/  ')
    print('--------------------------------------------------------------------')
    print('\n')
    print('\n')           