n1=1
n2=2
n3=3
n4=4
n5=5
n6=6
n7=7
n8=8
n9=9

complet=False
# 1
print ("1","|","2","|","3")
print ("-"," ","-"," ","-")
print ("4","|","5","|","6")
print ("-"," ","-"," ","-")
print ("7","|","8","|","9")

# 2
x= tour =0


while tour<89:
    joue = int(input("ecrit la ou tu veux jouer"))

    # 2
    if (tour==0):
        x="X" 
    if (tour==10):
        x="O"
    if (tour==20):
        x="X" 
    if (tour==30):
        x="O"        
    if (tour==40):
        x="X" 
    if (tour==50):
        x="O" 
    if (tour==60):
        x="X" 
    if (tour==70):
        x="O"
    if (tour==80):
        x="X" 
    if (tour==90):
        x="O"



    if (joue==1):
        n1=x
    if (joue ==2):
        n2=x   
    if (joue ==3):
        n3=x 
    if (joue ==4):
        n4=x 
    if (joue ==5):
        n5=x                          
    if (joue ==6):
        n6=x 
    if (joue ==7):
        n7=x 
    if (joue ==8):
        n8=x 
    if (joue ==9):
        n9=x 
    
    print (n1,"|",n2,"|",n3)
    print ("-"," ","-"," ","-")
    print (n4,"|",n5,"|",n6)
    print ("-"," ","-"," ","-")
    print (n7,"|",n8,"|",n9)        
    
    tour=tour+10
    
    # 3
    if(n1==n2==n3):
        tour=90
    if(n4==n5==n6):
        tour=90   
    if(n7==n8==n9):
        tour=90
    if(n1==n4==n7):
        tour=90 
    if(n2==n5==n8):
        tour=90 
    if(n3==n6==n9):
        tour=90
    if(n1==n5==n9):
        tour=90          
    if(n3==n5==n7):
        tour=90 
    
    # 4
    if(n1!=1):
        if(n2!=2):
            if(n3!=3):
                if(n4!=4):
                    if(n5!=5):
                        if(n6!=6):
                            if(n7!=7):
                                if(n8!=8):
                                    if(n9!=9):
                                        complet==True


if (complet==True):
    tour=90

if (tour==90):
    print("fin")


# 6
# Pour passer d'un tic tac toe a un puissance 4 la condition de victoire doit passer de 3 pions coller a 4 
# Il faut aussi y inserer de la "graviter" pour pas que les joueurs puissent poser leurs pions partout
# Il faudras aussi augmenter la taille de la grille
# Il faudras aussi augmenter le nombre de tour a jouer et de pions a jouer 













