import email
import random
import string
import time
import os
output = []
randomLeghnt = 5




def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def prefixgen(exportAmount, Email):
    for i in range(exportAmount):
        ranID = get_random_string(5)
        Emailcore = Email.replace("@gmail.com", "")
        final = "{}+{}@gmail.com".format(Emailcore, ranID)
        output.append(final)
    print(output)
    input("Presione Enter para continuar...")
    mainmenu()

def exportprefix(exportdir):
    try:
        Directory = r'{}\Output.txt'.format(exportdir)
        print("Ubicación del archivo: " + Directory)
        with open(Directory, 'w') as fp:
            for item in output:
                fp.write("%s\n" % item)
            
            print('\033[32m' + "Los sufijos se exportan en el directorio seleccionado" + '\033[0m')
            input("Presione Enter para continuar...")
            mainmenu()
    except:
        print('\033[31m' + "Directory not found or no generated suffix found" + '\033[0m')
        input("Presione Enter para continuar...")
        mainmenu()




def mainmenu():
    os.system('cls')
    print('\033[35m' + """  



  ____  ___ ___   ____  ____  _           _____ __ __  _____  _____  ____  __ __       ____    ___  ____  
 /    ||   |   | /    ||    || |         / ___/|  |  ||     ||     ||    ||  |  |     /    |  /  _]|    \ 
|   __|| _   _ ||  o  | |  | | |        (   \_ |  |  ||   __||   __| |  | |  |  |    |   __| /  [_ |  _  |
|  |  ||  \_/  ||     | |  | | |___      \__  ||  |  ||  |_  |  |_   |  | |_   _|    |  |  ||    _]|  |  |
|  |_ ||   |   ||  _  | |  | |     |     /  \ ||  :  ||   _] |   _]  |  | |     |    |  |_ ||   [_ |  |  |
|     ||   |   ||  |  | |  | |     |     \    ||     ||  |   |  |    |  | |  |  |    |     ||     ||  |  |
|___,_||___|___||__|__||____||_____|      \___| \__,_||__|   |__|   |____||__|__|    |___,_||_____||__|__|
                                                                                                          

                                                                                                                     

made by: freedarwuin

""" + '\033[0m')
    print('\033[35m' + """ 

    [1] generar sufijo
    [2] sufijo de exportación
    [3] cerrar programa

""" + '\033[0m')
    answer = input()
    if answer == "1" :
        email
        genAmount = int(input("¿Cuántos sufijos quieres generar?         "))
        emailinput = input("Proporciona la cuenta de Gmail que deseas utilizar                        ")
        prefixgen(genAmount, emailinput)
        

    elif answer == "2":
        exportpath = input("¿Donde quieres guardar el archivo? ")
        exportprefix(exportpath)


    elif answer == "3":
        print("")
    else:
        print('\033[31m' + "Esta no es una respuesta válida" + '\033[0m')

mainmenu()



            

