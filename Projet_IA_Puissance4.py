from tkinter import *
from tkinter.messagebox import *
from random import *
from PIL import Image
from PIL import ImageTk as itk
import time
import pygame
from copy import copy, deepcopy



humain = 1
ia = 2
Quicommence = humain
Joueur = Quicommence
Fenetre = Tk()
Largeur = 600
Hauteur = 600
Nombre_ligne = 12
Nombre_colonne = 12
largeur_case = Largeur//Nombre_ligne
hauteur_case = Hauteur//Nombre_colonne

tab = ([0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0])



def grille(zone, epaisseur, couleur):
    for i in range (Nombre_ligne):
        zone.create_line(0, hauteur_case * (i+1), Largeur, hauteur_case * (i+1), fill = couleur, width = epaisseur)
    for j in range(Nombre_colonne):
        zone.create_line(largeur_case * (j+1), 0, largeur_case * (j+1), Hauteur, fill = couleur, width = epaisseur)
    zone.pack()


def attribut_valeur(tab1,coord_x):
    global Joueur
    [x,y] = tomber_pion(tab1,coord_x)
    tab1[y][x] = Joueur
    #print("joueur : ", Joueur)
    #print("tab(",x,",",y,") :", tab1[y][x])
    #affichage_console(tab1)
    if(Joueur == humain):
        Zone.create_oval((x)*largeur_case + 2, (y)*largeur_case + 2, (x)*largeur_case +  largeur_case - 2 , (y)*largeur_case +  largeur_case - 2, fill = "green")
        if(Terminal_Test(tab1)[0]):
            showinfo("Partie terminée","Gagné! Le joueur " + str(Terminal_Test(tab1)[1]) + " remporte la partie.")
        #Joueur = ia #Switch de joueur à chaque tour

    else:
        Zone.create_oval((x)*largeur_case + 2, (y)*largeur_case + 2, (x)*largeur_case +  largeur_case - 2 , (y)*largeur_case +  largeur_case - 2, fill = "yellow")
        if(Terminal_Test(tab1)[0]):
            showinfo("Partie terminée","Gagné! Le joueur " + str(Terminal_Test(tab1)[1]) + " remporte la partie.")
        #Joueur = humain
            
    return [tab1,x,y]

def Utility(tab1,x,y): # A modifier un peu pour la complexité si nécéssaire sinon pas grave
    resultat = 0
    if(Terminal_half_test(tab1,x,y)[0]):
        if(Terminal_half_test(tab1,x,y)[1] == humain):
            resultat -= 20
        else:
            resultat += 25
            
    if(Terminal_Test(tab1,x,y)[0]):
        if(Terminal_Test(tab1,x,y)[1] == humain):
            resultat -= 50;
        else:
            resultat += 55;
        
    return resultat


def Minmax_decision(): #On va fixer la profondeur à 4
    global Joueur, tab
    #Normalement Joueur = ia (ici).
    
    
    listeia=Nombre_colonne*[0]
    
    for i in range(0,Nombre_colonne) :
        tableau=deepcopy(tab)
        tab_res =poser_pion_test(tableau,2,i)
        tableau = tab_res[0]
        w=tab_res[2]
        carotte=Terminal_Test(tableau)
        #carotte = Terminal_full_test(tableau,i,w)
        if carotte[0] :
            if carotte[1]==2:
                listeia[i]+=50
                #break
            if(carotte[1] == 1) :
                listeia[i]-=50
                #break
        """else :
            banane = Terminal_half_test(tableau,i,w)
            if(banane[0]):
                listeia[i] += 25
            else:
                listeia[i] -= 25"""
        
        for i2 in range(0,Nombre_colonne) :
            tableau2=deepcopy(tableau)
            tab_res2 =poser_pion_test(tableau2,1,i2)
            tableau2 = tab_res2[0]
            w2=tab_res2[2]
            carotte2=Terminal_Test(tableau2)
            #carotte2 = Terminal_full_test(tableau2,i2,w2)
            if carotte2[0] :
                if carotte2[1]==2:
                    listeia[i]+=40
                    #break
                if(carotte2[1] == 1) :
                    listeia[i]-=40
                    #break
            """else :
                banane2 = Terminal_half_test(tableau2,i2,w2)
                if(banane2[0]):
                    listeia[i] += 18
                else:
                    listeia[i] -= 18"""
                    
            for i3 in range(0,Nombre_colonne) :
                tableau3=deepcopy(tableau2)
                tab_res3 =poser_pion_test(tableau3,2,i3)
                tableau3 = tab_res3[0]
                w3=tab_res3[2]
                carotte3=Terminal_Test(tableau3)
                #carotte3 = Terminal_full_test(tableau3,i3,w3)
                if carotte3[0] :
                    if carotte3[1]==2:
                        listeia[i]+=30
                        #break
                    if(carotte3[1] == 1) :
                        listeia[i]-=30
                        #break
                
                """else :
                    banane3 = Terminal_half_test(tableau3,i3,w3)
                    if(banane3[0]):
                        listeia[i] += 15
                    else:
                        listeia[i] -= 15"""
                     
                for i4 in range(0,Nombre_colonne) :
                    tableau4=deepcopy(tableau3)
                    tab_res4 =poser_pion_test(tableau4,1,i4)
                    tableau4 = tab_res4[0]
                    w4=tab_res4[2]
                    carotte4=Terminal_Test(tableau4)
                    #carotte4 = Terminal_full_test(tableau4,i4,w4)
                    #print(carotte4)
                    if carotte4[0] :
                        if carotte4[1]==2:
                            listeia[i]+=20
                            #break
                        if(carotte4[1] == 1) :
                            listeia[i]-=20
                            #break
                    #affichage_console(tableau4)
                    """else :
                        banane4 = Terminal_half_test(tableau4,i4,w4)
                        if(banane4[0]):
                            listeia[i] += 10
                        else:
                            listeia[i] -= 10"""
    print(listeia)
    
    
    compteur = True
    
    for i in range(len(listeia)- 1 ):
        compteur = (listeia[i] == listeia[i +1]) and compteur

    #print(compteur)
    if(compteur == True):
        nbr = randint(0,Nombre_colonne-1)
        print("Aléatoire : ", nbr)
        return (nbr)

    
    for i in range(len(listeia)):
        listeia[i] = abs(listeia[i])

    maxi=min(listeia)
    
    for i in range(len(listeia)) :
        if maxi==listeia[i] :
            print(i)
            return i
    
    return -1
    
        
def poser_pion_test(tab1,n,x):
    
    [x1,y1] = [0,0]
    
    if(n%2 == 0): #ie si c'est l'ia qui joue
        [x1,y1] = tomber_pion(tab1,x)
        #print(x1,y1)
        tab1[y1][x1] = ia
    else :
        [x1,y1] = tomber_pion(tab1,x)
        tab1[y1][x1] = humain
        
    return [tab1,x1,y1]


    
def tomber_pion(tab1,coord_x):
    j = 0
    while(j<11):
        if(tab1[j+1][coord_x]!=0):
            return([coord_x,j])
        j += 1
    return [coord_x,11]
    

def clique(event):
    global Joueur, tab
    #affichage_console(tab)#1
    profondeur = 0
    #JOUEUR HUMAIN
    
    #print(Joueur)
    coord_x = event.x//largeur_case
    coord_y = event.y//hauteur_case
    
    if(tab[0][coord_x] == 0):
        res = attribut_valeur(tab,coord_x)[:]
        tab = res[0]
        
        #affichage_console(tab)#2
    else:
        showinfo("Impossible","Cette colonne est pleine.")

    
    

    #JOUEUR IA
    
    Joueur = ia  # Switch
    copie = deepcopy(tab)
    res2 = deepcopy(attribut_valeur(copie,Minmax_decision()))
    tab = res2[0]
    Joueur = humain#Switch
    
    #affichage_console(tab)#3
    #affichage_console(tab)



    

def Terminal_full_test(tab1,x,y):
    # Calcul sur la verticale
    if y <= Nombre_ligne - 2 - 3 :
        # On ne peut gagner verticalement que si la ligne jouée est au dessus des 3 premières
        if tab1[y][x] == tab1[y+1][x] == tab1[y + 2][x] == tab1[y +3][x] and  (tab1[y][x] != 0) :
            return [True,tab1[y][x]]

    # Calcul sur l'horizontale
    x_gauche = x
    x_droite = x
    while (x_gauche >= 0) and (tab1[y][x_gauche] != 0) :
        x_gauche -= 1
    while (x_droite <= len(tab1[y]) - 1) and (tab1[y][x_droite] != 0) :
        x_droite += 1
    if x_droite - x_gauche >= 2 + 3 :
        return [True,tab1[y][x]]


    # Calcul sur la diagonale Nord-Est
    x_gauche = x
    x_droite = x
    y_gauche = y
    y_droite = y
    while (x_gauche <= len(tab1) - 1 and x_gauche >= 0) and (tab1[y_gauche][x_gauche] != 0) :
        y_gauche -= 1
        x_gauche += 1
    while (x_droite >= 0  and y_droite <= len(tab1[x]) - 1) and (tab1[y_droite][x_droite] != 0) :
        y_droite += 1
        x_droite -= 1
    if x_gauche - x_droite >= 2 + 3 :
        return [True,tab1[y][x]]
    
    # Calcul sur la diagonale Sud-Est
    x_gauche = x
    x_droite = x
    y_gauche = y
    y_droite = y
    while (x_gauche >= 0 and y_gauche >= 0) and (tab1[y_gauche][x_gauche] != 0) :
        y_gauche -= 1
        x_gauche -= 1
    while (x_droite <= len(tab1) - 1 and y_droite <= len(tab1[x]) - 1) and (tab1[y_droite][x_droite] != 0) :
        y_droite += 1
        x_droite += 1
    if x_droite - x_gauche >= 2 + 3 :
        return [True,tab1[y][x]]
    
    # Calcul si le plateau est complet ou il ne reste plus de pions
    
    return [False,0]





def Terminal_half_test(tab1,x,y): # Pour savoir quand 3 pions sont alignés
    # Calcul sur la verticale
    if y <= Nombre_ligne - 2 - 3 :
        # On ne peut gagner verticalement que si la ligne jouée est au dessus des 3 premières
        if tab1[y][x] == tab1[y+1][x] == tab1[y + 2][x] == tab1[y+3][x] and (tab1[y][x] == Joueur) :
            return [True,Joueur]

    # Calcul sur l'horizontale
    x_gauche = x
    x_droite = x
    while (x_gauche >= 0) and (tab1[y][x_gauche] == Joueur) :
        x_gauche -= 1
    while (x_droite <= len(tab1[y]) - 1) and (tab1[y][x_droite] == Joueur) :
        x_droite += 1
    if x_droite - x_gauche >= 2 + 2 :
        return [True,Joueur]


    # Calcul sur la diagonale Nord-Est
    x_gauche = x
    x_droite = x
    y_gauche = y
    y_droite = y
    while (x_gauche <= len(tab1) - 1 and x_gauche >= 0) and (tab1[y_gauche][x_gauche] == Joueur) :
        y_gauche -= 1
        x_gauche += 1
    while (x_droite >= 0  and y_droite <= len(tab1[x]) - 1) and (tab1[y_droite][x_droite] == Joueur) :
        y_droite += 1
        x_droite -= 1
    if x_gauche - x_droite >= 2 + 2 :
        return [True,Joueur]
    
    # Calcul sur la diagonale Sud-Est
    x_gauche = x
    x_droite = x
    y_gauche = y
    y_droite = y
    while (x_gauche >= 0 and y_gauche >= 0) and tab1[y_gauche][x_gauche] == Joueur :
        y_gauche -= 1
        x_gauche -= 1
    while (x_droite <= len(tab1) - 1 and y_droite <= len(tab1[x]) - 1) and (tab1[y_droite][x_droite] == Joueur) :
        y_droite += 1
        x_droite += 1
    if x_droite - x_gauche >= 2 + 2 :
        return [True,Joueur]
    
    # Calcul si le plateau est complet ou il ne reste plus de pions
    
    return [False,Joueur]

def Terminal_Test(self,colonnes = Nombre_colonne, lignes   = Nombre_ligne):

     for k in range(0,colonnes) :
         for i in range(0,lignes - 4) :
             if (self[k][i]==self[k][(i+1)]==self[k][(i+2)]==self[k][(i+3)]) and (self[k][i] == 1 or self[k][i] ==2):
                 return True,self[k][i]
     for i in range(0,lignes) :
         for k in range(0,colonnes - 4) :
             if (self[k][i]==self[(k+1)][i]==self[(k+2)][i]==self[(k+3)][i]) and (self[k][i] == 1 or self[k][i] ==2):
                 return True,self[k][i]
                
     for i in range(0,lignes - 4) :
         for k in range(0,colonnes - 4) :
             if (self[k][i]==self[(k+1)][(i+1)]==self[(k+2)][(i+2)]==self[(k+3)][(i+3)]) and (self[k][i] == 1 or self[k][i] ==2):
                 return True,self[k][i]
             if (self[(colonnes - 1-k)][(lignes - 1-i)]==self[(colonnes - 1 -1 -k)][(lignes - 1 - 1-i)]==self[(colonnes - 1 - 2 -k)][(lignes - 1 - 2-i)]==self[(colonnes - 1 - 3-k)][(lignes - 1 -3-i)]) and (self[colonnes - 1 - k][lignes - 1 -i] == 1 or self[colonnes - 1 - k][lignes - 1 -i] ==2):
                 return True,self[(colonnes - 1-k)][(lignes - 1-i)]
            
     return False,0
    
def Terminal_Test2(tab1,x,y) :
    
    # Calcul sur la verticale
    if y <= Nombre_ligne - 1 - 3 :
        # On ne peut gagner verticalement que si la ligne jouée est au dessus des 3 premières
        if tab1[y][x] == tab1[y+1][x] == tab1[y + 2][x] == tab1[y + 3][x] and (tab1[y][x] == Joueur) :
            return [True,Joueur]
    
    # Calcul sur l'horizontale
    x_gauche = x
    x_droite = x
    while (x_gauche >= 0) and (tab1[y][x_gauche] == Joueur) :
        x_gauche -= 1
    while (x_droite <= len(tab1[y]) - 1) and (tab1[y][x_droite] == Joueur) :
        x_droite += 1
    if x_droite - x_gauche >= 3 + 2 :
        #print(x_gauche,x_droite)
        return [True,Joueur]
    
    # Calcul sur la diagonale Nord-Est
    x_gauche = x
    x_droite = x
    y_gauche = y
    y_droite = y
    while (x_gauche <= len(tab1) - 1 and x_gauche >= 0) and (tab1[y_gauche][x_gauche] == Joueur) :
        y_gauche -= 1
        x_gauche += 1
    while (x_droite >= 0  and y_droite <= len(tab1[x]) - 1) and (tab1[y_droite][x_droite] == Joueur) :
        y_droite += 1
        x_droite -= 1
    if x_gauche - x_droite >= 3 + 2 :
        return [True,Joueur]
    
    # Calcul sur la diagonale Sud-Est
    x_gauche = x
    x_droite = x
    y_gauche = y
    y_droite = y
    while (x_gauche >= 0 and y_gauche >= 0) and tab1[y_gauche][x_gauche] == Joueur :
        y_gauche -= 1
        x_gauche -= 1
    while (x_droite <= len(tab1) - 1 and y_droite <= len(tab1[x]) - 1) and (tab1[y_droite][x_droite] == Joueur) :
        y_droite += 1
        x_droite += 1
    if x_droite - x_gauche >= 3 + 2 :
        return [True,Joueur]
    
    # Calcul si le plateau est complet ou il ne reste plus de pions
    
    return [False,Joueur]

def affichage_console(tab):
    for i in range (len(tab)):
        for j in range (len(tab[0])):
            print("",tab[i][j], " ",end = '')
        print('')
    print("----------------------------------")
        
if __name__ == "__main__":
    
    Couleur = '#E0E0E0'
    Zone =  Canvas(Fenetre, width = Largeur, height = Hauteur, background = Couleur)
    grille(Zone,1,"black")
    #Zone.create_oval((5)*largeur_case + 2, (5)*largeur_case + 2, (5)*largeur_case +  largeur_case - 2 , (5)*largeur_case +  largeur_case - 2, fill = "yellow")
    Fenetre.bind("<Button-1>",clique)
    Fenetre.mainloop()

