from os import system

myList = ["canela"]


def Menu():
    
    system('clear')
    print("+-------------------------------+")
    print("+            Mi Lista           +")
    print("+-------------------------------+")
    print("+-------------------------------+")
    print("+-----      1.- Agregar    -----+")
    print("+-----      2.- Borrar     -----+")
    print("+-----      3.- Editar     -----+")
    print("+-----      4.- Ver Lista  -----+")
    print("+-----      5.- Salir      -----+")
    print("+-------------------------------+")


def printList():
    for x in myList:
            index = myList.index(x)
            print("+", end=" ")
            print(index + 1 , x , sep=" -> ")




k = 1
myList = [ 'canela', 'pimienta' , 'tomillo']

while k > 0:
    Menu()
    
    
    numberToch = int(input())       
    system('clear')


    if numberToch == 1:
        print("+-------------------------------+")
        print("+           Agregar             +")
        print("+-------------------------------+")
        print("+          Tu lista             +")
        printList()
        print("+-------------------------------+")
        
        Item = input("| nombre del Item : ")
        myList.append(Item)
        print("+-------------------------------+")
        
        
        system('clear')

        print("+-------------------------------+")
        print("+     Tu Lista Actualizada      +")
        print("+-------------------------------+")
        printList()
        print("+-------------------------------+")

        print()
        input("Presiona 'Enter' volver al Menu")


    if numberToch == 2:
        print("+-------------------------------+")
        print("+           Borrar              +")
        print("+-------------------------------+")
        print("+          Tu lista             +")
        print("+-------------------------------+")
        printList()
        print("+-------------------------------+")

        Item = int(input("+ Numero del Item a Borrar : "))

        print("+-------------------------------+")
        myList.pop(Item - 1)
        system('clear')
        print("+-------------------------------+")
        print("+        Cambio Realizado       +")
        print("+-------------------------------+")
        print("+            Tu lista           +")
        print("+-------------------------------+")
        printList()
        print("+-------------------------------+")
        print()
        input("Presiona 'Enter' volver al Menu")


    if numberToch == 3:

        print("+-------------------------------+")
        print("+           Editar              +")
        print("+-------------------------------+")
        print("+          Tu lista             +")
        print("+-------------------------------+")
        printList()
        print("+-------------------------------+")
        
        Item  = int(input("+ Numero del Item a Editar : "))
        myList.pop(Item - 1)

        ItemEdit = input("Nombre Cambiado : ")
        myList.insert(Item - 1,ItemEdit )
        system('clear')
        print("+-------------------------------+")
        print("+        Cambio Realizado       +")
        print("+-------------------------------+")
        print("+            Tu lista           +")
        print("+-------------------------------+")

        printList()
        
        input("Presiona 'Enter' volver al Menu")

    if numberToch == 4:
        system('clear')
        print("+-------------------------------+")
        print("+            Tu lista           +")
        print("+-------------------------------+")
        printList()
        print("+-------------------------------+")
        input("Presiona 'Enter' volver al Menu")
        
    if numberToch == 5:
        
        system('clear')
        k= -10
        
