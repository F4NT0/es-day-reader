def writeOnFile(matricula):
    file = open("matriculas.csv","w")
    matricula = matricula + "\n"
    file.write(matricula)
    file.close()
    
def readOfFile(arquivo):
    file = open(arquivo,"r")
    content = file.read()
    print(cont)
    file.close()

                