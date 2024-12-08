import dictionnaire 
print("1.voulez voous chifrez")
print("2.voulez vous dichifrez")
choix=input()
def numcount():
    count= dictionnaire.list_characters()
    num=int(input("enter number= "))
    text=input("text here: ")
    resultat=""
    for i in text:
        position = count.index(i)
        nouvelle_position = (position +num) %26
        resultat=resultat+count[nouvelle_position]
        
    print(resultat)
def dichifrer():
    count= dictionnaire.list_characters()
    num=int(input("enter number= "))
    text=input("text here: ")
    resultat=""
    for i in text:
        position = count.index(i)
        nouvelle_position = (position -num) %26
        resultat=resultat+count[nouvelle_position]
    print(resultat)

match choix:
    case "1":
        numcount()
    case "2":
        dichifrer()
    case _:
        print("error input")



#ghilessiamer
    

