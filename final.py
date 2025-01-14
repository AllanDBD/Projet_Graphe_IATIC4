import random
import json
from datetime import datetime
import timeit
import tkinter as tk


class Graphe:
    
    def generer_un_graphe_random(self):
        self.taille_graphe = int(input("Taille du graphe : "))
        p=input("voulez-vous donner la probanilité d'apparition de branche tapez o si oui sinon n'importe quel autre touche ")
        if p=="o" or p=="O":
            while True:
                self.probabilite_branche = float(input("Probabilité de branche au format 0.XX : "))
                if 1>self.probabilite_branche > 0 :
                    break
        else:
            self.probabilite_branche = random.random()  # Probabilité aléatoire entre 0 et 1
            print(f"Probabilité de branche : {self.probabilite_branche:.2f}")
        self.ordonne=True
        self.generer_matrice_random()
        self.degre_maximum()
        self.save_graphe()


    def generer_matrice_random(self):
        self.matrice_adjacence_ordonne = []
        self.ordonne=True
        for i in range(self.taille_graphe):
            ligne = []
            self.matrice_adjacence_ordonne.append(ligne)
        for j in range(self.taille_graphe):
            for k in range(j+1,self.taille_graphe):
                if random.random() < self.probabilite_branche:
                    self.matrice_adjacence_ordonne[j].append(k)
                    self.matrice_adjacence_ordonne[k].append(j)



    def save_graphe(self):
        answer=input("Voulez-vous sauvegarder ce graphe dans un fichier? (o/O si oui): ")
        if(answer=="o" or answer=="O"):
            answer=input("Souhaitez-vous choisir le nom du fichier où sauvegarder le graphe? (o/O si oui, n/N sinon): ")
            if(answer=="o" or answer=="O"):
                file_name="Graphes/"+input("Entrez le nom du fichier: ")+".json"
            elif(answer=="n" or answer=="N"):
                current_time = datetime.now()
                file_name = "Graphes/random_graphe-"+current_time.strftime("%Y-%m-%d_%H-%M-%S") + ".json"
            else:
                return
            if self.ordonne:
                graphe = {str(i): self.matrice_adjacence_ordonne[i] for i in range(self.taille_graphe)}
                data= {
                    "n": self.taille_graphe,
                    "graphe": graphe
                }
                with open(file_name, "w") as file:
                    json.dump(data, file)
            else:
                graphe = {str(self.list_correspondance[i][0]): [self.list_correspondance[val][0] for val in self.matrice_adjacence_ordonne[i]]
        for i in range(self.taille_graphe)
    }
                data= {
                    "n": self.taille_graphe,
                    "graphe": graphe
                }
                with open(file_name, "w") as file:
                    json.dump(data, file)




    def import_graphe(self,file):
            # Lecture du fichier JSON
            with open(file, "r") as file:
                self.data = json.load(file)

            self.taille_graphe = self.data["n"]
            self.import_matrice()
            self.ordonner_matrice()
            self.degre_maximum()



    def import_matrice(self):    
            lists = self.data["graphe"]
            self.matrice_adjacence_non_ordonne=[]
            self.list_correspondance=[]
            i=0
            self.ordonne=False
            for node in lists:
                int_node = int(node)  # Convertir la clé en entier
                self.matrice_adjacence_non_ordonne.append([int(neighbor) for neighbor in lists[node]])  # Convertir les voisins en entiers
                self.list_correspondance.append((int_node, i))
                i += 1



    def afficher(self):
        if self.ordonne:
            for i in range (len(self.matrice_adjacence_ordonne)):
                print(i, ":", self.matrice_adjacence_ordonne[i])
        else:
            for sommet,indice in self.list_correspondance:
                list_afficher=[]
                print(sommet, ":",end=" ")
                for i in range (len(self.matrice_adjacence_ordonne[indice])):
                    valeur=self.matrice_adjacence_ordonne[indice][i]
                    list_afficher.append(self.list_correspondance[valeur][0])
                list_afficher.sort()
                print(list_afficher)





    def ordonner_matrice(self):

        if self.ordonne ==False:
            self.matrice_adjacence_ordonne = []
            for i in range(self.taille_graphe):
                self.matrice_adjacence_ordonne.append([])

            for sommet,indice in self.list_correspondance:
                for i in range (self.taille_graphe):
                    for j in range (len(self.matrice_adjacence_non_ordonne[i])):
                        if self.matrice_adjacence_non_ordonne[i][j]==sommet:
                            self.matrice_adjacence_ordonne[i].append(indice)


                        
    def degre_maximum(self):
        self.deg_max=0
        self.indice_degre_max=[]
        for i in range(self.taille_graphe):
            if len(self.matrice_adjacence_ordonne[i]) > self.deg_max:
                self.deg_max=len(self.matrice_adjacence_ordonne[i])
                self.indice_degre_max=[]
                self.indice_degre_max.append(i)
            elif len(self.matrice_adjacence_ordonne[i])==self.deg_max:
                self.indice_degre_max.append(i)



    def afficher_degre_max(self):
        if(self.ordonne):
            print("Degré max:",self.deg_max,"         Sommet(s):",self.indice_degre_max)
        else:
            list_indice=[]
            for i in range(len(self.indice_degre_max)):
                list_indice.append(self.list_correspondance[self.indice_degre_max[i]][0])
            print("Degré max:",self.deg_max,"         Sommet(s):",list_indice)



    def nb_sommets_par_degre(self):
        nb_sommet = [0] * (self.deg_max + 1)
        for i in range(self.taille_graphe):
            nb_sommet[len(self.matrice_adjacence_ordonne[i])] += 1
        
        print("Nombre de noeud par degré: [ ",end="")
        for i in range(self.deg_max-1):
            if nb_sommet[i]!=0:
                print(i,":",nb_sommet[i],", ",end="")
        if nb_sommet[self.deg_max]!=0:
            print(self.deg_max,":",nb_sommet[self.deg_max],"]")
            self.afficher_graphique(nb_sommet)
        



    def afficher_graphique(self,liste):
        # Création de la fenêtre
        fenetre = tk.Tk()
        fenetre.title("Graphique à barres")
        fenetre.bg="white"
        fenetre.geometry("1080x600")
        
        # Dimensions de la zone de dessin
        largeur_canvas = 1080
        hauteur_canvas = 600
        
        # Création du canvas pour dessiner
        canvas = tk.Canvas(fenetre, width=largeur_canvas, height=hauteur_canvas, bg="white")
        canvas.pack()
        
        # Paramètres du graphique
        marge_gauche = 50
        marge_bas = 30
        max_valeur = max(liste)
        begin=False
        for i, valeur in enumerate(liste):
            if begin:
                x1 = marge_gauche + (i-debut) * (espace_barres)
                y1 = hauteur_canvas - marge_bas
                x2 = x1 + espace_barres-1
                y2 = y1 - (valeur / max_valeur) * (hauteur_canvas -2* marge_bas)
                canvas.create_rectangle(x1, y1, x2, y2, fill="skyblue", outline="black")
            elif valeur>0:
                begin=True
                debut=i
                espace_barres = int((largeur_canvas-2*marge_gauche) //  (len(liste)-debut))
                x1 = marge_gauche + (i-debut) * (espace_barres)
                y1 = hauteur_canvas - marge_bas
                x2 = x1 + espace_barres-1
                y2 = y1 - (valeur / max_valeur) * (hauteur_canvas -2* marge_bas)
                canvas.create_rectangle(x1, y1, x2, y2, fill="skyblue", outline="black")

           
            
        
        

        if max_valeur>12:
            number_of_indicators_y=12
        else:
            number_of_indicators_y=max_valeur
        step_y = max_valeur /number_of_indicators_y
        for i in range(number_of_indicators_y + 1):
            y = hauteur_canvas - marge_bas - i * (hauteur_canvas - 2 * marge_bas) // number_of_indicators_y
            canvas.create_line(marge_gauche - 5, y, marge_gauche, y)  # Marqueurs sur l'axe Y
            canvas.create_text(marge_gauche - 15, y, text=str(int(i * step_y)), font=("Arial", 8))

        number_of_indicators_x=35
        if len(liste)-debut<35:
            number_of_indicators_x=len(liste)-debut
        step_x = (len(liste)-debut) / number_of_indicators_x
        for i in range(number_of_indicators_x):
            x = marge_gauche + i * step_x * espace_barres+0.5*espace_barres
            canvas.create_line(x, hauteur_canvas - marge_bas + 5, x, hauteur_canvas - marge_bas - 5)  # Marqueurs sur l'axe X
            canvas.create_text(x, hauteur_canvas - marge_bas + 15, text=str(int((i * step_x)+debut)), font=("Arial", 8))
        
        # Ajouter les axes
        canvas.create_line(marge_gauche, hauteur_canvas - marge_bas, largeur_canvas - marge_gauche, hauteur_canvas - marge_bas, arrow=tk.LAST)  # Axe X
        canvas.create_line(marge_gauche, hauteur_canvas - marge_bas, marge_gauche, marge_bas, arrow=tk.LAST)  # Axe Y
        
        # Affichage de la fenêtre
        fenetre.mainloop()


    def nb_chemins_induits_longueur_2(self):
        compteur=0
        for i in range(self.taille_graphe):
            for k in self.matrice_adjacence_ordonne[i]:
                for j in self.matrice_adjacence_ordonne[k]:
                    if j>i:
                        if i not in self.matrice_adjacence_ordonne[j]:              
                            compteur+=1
        
        print("nombre de chemin induit longueur 2 = " ,compteur)





    def algo_Bron_et_Kerbosch_sans_pivot(self, R, P, X):
        if len(P) == 0 and len(X) == 0:  
            if self.ordonne:
                print("Clique maximale trouvée:", R)
            else:
                print("Clique maximale trouvée:")
                for i in (R):
                    print(self.list_correspondance[i][0],end=" ")
                print("")

            return

        for sommet in list(P):  # Convert P to a list to safely iterate
            self.algo_Bron_et_Kerbosch_sans_pivot(
                R.union({sommet}),  # Add the current vertex to R
                P.intersection(self.matrice_adjacence_ordonne[sommet]),  # Neighbors in P
                X.intersection(self.matrice_adjacence_ordonne[sommet])   # Neighbors in X
            )
            P.remove(sommet)  # Modify P after iteration
            X.add(sommet)     # Add to X after iteration




    def algo_Bron_et_Kerbosch_avec_pivot(self, R, P, X, output_file=None):
        """
        Implémente l'algorithme de Bron-Kerbosch avec pivot pour trouver les cliques maximales.

        :param R: Ensemble de sommets actuellement dans la clique.
        :param P: Ensemble de sommets candidats pour agrandir la clique.
        :param X: Ensemble de sommets déjà explorés.
        :param output_file: Chemin vers un fichier texte où les cliques maximales seront ajoutées.
        """
        if len(P) == 0 and len(X) == 0:
            # Une clique maximale a été trouvée
            if self.ordonne:  
                print("Clique maximale trouvée:", R)
            else:
                clique = [self.list_correspondance[i][0] for i in R]
                print("Clique maximale trouvée:", " ".join(map(str, clique)))

            # Ajouter la clique au fichier si un chemin est fourni
            '''if output_file:
                with open(output_file, "a") as file:
                    if self.ordonne:
                        file.write(f"{clique}\n")
                    else:
                        file.write(f"{' '.join(map(str, clique))}\n")'''

            return
        else:
            # Choisir un pivot
            pivot = P.union(X).pop()
            for sommet in list(P.difference(self.matrice_adjacence_ordonne[pivot])):  # Convertir P en liste pour itérer en toute sécurité
                self.algo_Bron_et_Kerbosch_avec_pivot(
                    R.union({sommet}),  # Ajouter le sommet courant à R
                    P.intersection(self.matrice_adjacence_ordonne[sommet]),  # Voisins de P
                    X.intersection(self.matrice_adjacence_ordonne[sommet]),  # Voisins de X
                    output_file  # Passer le chemin du fichier de sortie
                )
                P.remove(sommet)
                X.add(sommet)




############################# source wikipedia ########################################





#ordre necessaire pour la fonction Gi_construct
    def give_ordering(self):

        self.ordering = list(range(self.taille_graphe))
        random.shuffle(self.ordering)
        if self.ordonne:
            print("Ordre aleatoire:",self.ordering)
        else :
            print("ordre aleatoire",end=" ")
            for i in self.ordering:
                print(self.list_correspondance[i][0],end=",")
            print(" ")




    def Gi_construct(self, position_in_ordering):
        if self.ordonne:
            graphe = Graphe()
            graphe.ordonne = False
            graphe.list_correspondance = []
            graphe.matrice_adjacence_ordonne = []

            sommet_i = self.ordering[position_in_ordering]
            liste_voisin_premier_degre = []
            liste_voisin_second_degre = []

            for voisin in self.matrice_adjacence_ordonne[sommet_i]:
                liste_voisin_premier_degre.append(voisin)
                for voisin2 in self.matrice_adjacence_ordonne[voisin]:
                    if voisin2 not in liste_voisin_second_degre:
                        liste_voisin_second_degre.append(voisin2)

            sommet_considere = set(self.ordering[position_in_ordering:])
            liste_voisin_premier_degre = list(set(liste_voisin_premier_degre).intersection(sommet_considere))
            liste_voisin_second_degre = list(set(liste_voisin_second_degre).intersection(sommet_considere))
            liste_voisin_second_degre = list(
                (set(liste_voisin_second_degre) - set(liste_voisin_premier_degre)) - {sommet_i}
            )

            graphe.matrice_adjacence_ordonne.append([])
            graphe.list_correspondance.append((sommet_i, 0))

            for i, voisin in enumerate(liste_voisin_premier_degre):
                graphe.matrice_adjacence_ordonne.append([])
                graphe.list_correspondance.append((voisin, i + 1))

            for i, voisin in enumerate(liste_voisin_second_degre):
                graphe.matrice_adjacence_ordonne.append([])
                graphe.list_correspondance.append(
                    (voisin, i + len(liste_voisin_premier_degre) + 1)
                )

            for i in range(len(liste_voisin_premier_degre) - 1):
                for j in range(i + 1, len(liste_voisin_premier_degre)):
                    sommet1 = liste_voisin_premier_degre[i]
                    sommet2 = liste_voisin_premier_degre[j]
                    if sommet2 in self.matrice_adjacence_ordonne[sommet1]:
                        graphe.matrice_adjacence_ordonne[i + 1].append(j + 1)
                        graphe.matrice_adjacence_ordonne[j + 1].append(i + 1)

            offset = len(liste_voisin_premier_degre) + 1
            for i in range(len(liste_voisin_second_degre) - 1):
                for j in range(i + 1, len(liste_voisin_second_degre)):
                    sommet1 = liste_voisin_second_degre[i]
                    sommet2 = liste_voisin_second_degre[j]
                    if sommet2 in self.matrice_adjacence_ordonne[sommet1]:
                        graphe.matrice_adjacence_ordonne[i + offset].append(j + offset)
                        graphe.matrice_adjacence_ordonne[j + offset].append(i + offset)


            for i in range(len(liste_voisin_premier_degre)):
                for j in range(len(liste_voisin_second_degre)):
                    sommet1 = liste_voisin_premier_degre[i]
                    sommet2 = liste_voisin_second_degre[j]
                    if sommet2 not in self.matrice_adjacence_ordonne[sommet1]:
                        graphe.matrice_adjacence_ordonne[i + 1].append(j + offset)
                        graphe.matrice_adjacence_ordonne[j + offset].append(i + 1)
            
            graphe.taille_graphe = len(graphe.matrice_adjacence_ordonne)

            return graphe
        
        
        else:
            graphe = Graphe()
            graphe.ordonne = False
            graphe.list_correspondance = []
            graphe.matrice_adjacence_ordonne = []

            sommet_i = self.ordering[position_in_ordering]
            liste_voisin_premier_degre = []
            liste_voisin_second_degre = []

            for voisin in self.matrice_adjacence_ordonne[sommet_i]:
                liste_voisin_premier_degre.append(voisin)
                for voisin2 in self.matrice_adjacence_ordonne[voisin]:
                    if voisin2 not in liste_voisin_second_degre:
                        liste_voisin_second_degre.append(voisin2)

            sommet_considere = set(self.ordering[position_in_ordering:])
            liste_voisin_premier_degre = list(set(liste_voisin_premier_degre).intersection(sommet_considere))
            liste_voisin_second_degre = list(set(liste_voisin_second_degre).intersection(sommet_considere))
            liste_voisin_second_degre = list(
                (set(liste_voisin_second_degre) - set(liste_voisin_premier_degre)) - {sommet_i}
            )

            graphe.matrice_adjacence_ordonne.append([])
            graphe.list_correspondance.append((self.list_correspondance[sommet_i][0], 0))

            for i, voisin in enumerate(liste_voisin_premier_degre):
                graphe.matrice_adjacence_ordonne.append([])
                graphe.list_correspondance.append((self.list_correspondance[voisin][0], i + 1))

            for i, voisin in enumerate(liste_voisin_second_degre):
                graphe.matrice_adjacence_ordonne.append([])
                graphe.list_correspondance.append(
                    (self.list_correspondance[voisin][0], i + len(liste_voisin_premier_degre) + 1)
                )

            for i in range(len(liste_voisin_premier_degre) - 1):
                for j in range(i + 1, len(liste_voisin_premier_degre)):
                    sommet1 = liste_voisin_premier_degre[i]
                    sommet2 = liste_voisin_premier_degre[j]
                    if sommet2 in self.matrice_adjacence_ordonne[sommet1]:
                        graphe.matrice_adjacence_ordonne[i + 1].append(j + 1)
                        graphe.matrice_adjacence_ordonne[j + 1].append(i + 1)

            offset = len(liste_voisin_premier_degre) + 1
            for i in range(len(liste_voisin_second_degre) - 1):
                for j in range(i + 1, len(liste_voisin_second_degre)):
                    sommet1 = liste_voisin_second_degre[i]
                    sommet2 = liste_voisin_second_degre[j]
                    if sommet2 in self.matrice_adjacence_ordonne[sommet1]:
                        graphe.matrice_adjacence_ordonne[i + offset].append(j + offset)
                        graphe.matrice_adjacence_ordonne[j + offset].append(i + offset)


            for i in range(len(liste_voisin_premier_degre)):
                for j in range(len(liste_voisin_second_degre)):
                    sommet1 = liste_voisin_premier_degre[i]
                    sommet2 = liste_voisin_second_degre[j]
                    if sommet2 not in self.matrice_adjacence_ordonne[sommet1]:
                        graphe.matrice_adjacence_ordonne[i + 1].append(j + offset)
                        graphe.matrice_adjacence_ordonne[j + offset].append(i + 1)

            graphe.taille_graphe = len(graphe.matrice_adjacence_ordonne)
            return graphe






graphe = Graphe()

nom_fichier= input("Veuillez donner le nom du fichier que vous voulez importer sous le format 'nom_fichier.json', si vous voulez générer un graphe aléatoirement tapez 'n' : ").strip()
if nom_fichier.lower() == 'n':
    print("Vous avez choisi de générer un graphe aléatoire.")
    graphe.generer_un_graphe_random()
else:
    print(f"Vous avez choisi d'importer un graphe depuis le fichier : {nom_fichier}")
    nom_fichier="Graphes/"+nom_fichier + ".json"
    graphe.import_graphe(nom_fichier)

graphe.afficher()
graphe.degre_maximum()
graphe.afficher_degre_max()
graphe.nb_sommets_par_degre()
graphe.nb_chemins_induits_longueur_2()
clique=input("Voulez-vous trouver les cliques maximales? (o/O si oui): ")
if clique=="o" :
    graphe.algo_Bron_et_Kerbosch_avec_pivot(set(), set(range(graphe.taille_graphe)), set())
    


gi_construction = input("Voulez-vous avoir le graphe Gi? (o/O si oui): ")
if gi_construction == "o":
    graphe.give_ordering()
    position_in_ordering = int(input("Veuillez donner la position dans l'ordre: "))
    gi=graphe.Gi_construct(position_in_ordering)
    gi.afficher()
    gi.save_graphe()

    










#graphe.generer_un_graphe_random()
#graphe.import_graphe("Graphes/random_graphe-2025-01-12_16-39-47.json")

#execution_time_ms = timeit.timeit("graphe.degre_maximum()", globals={"graphe": graphe}, number=1000) * 1000 / 1000
#print(f"Temps moyen d'exécution : {execution_time_ms:.3f} ms")
#execution_time_ms = timeit.timeit("graphe.nb_sommets_par_degre()", globals={"graphe": graphe}, number=100) * 1000 / 100
#print(f"Temps moyen d'exécution : {execution_time_ms:.3f} ms")
#execution_time_ms = timeit.timeit("graphe.nb_chemins_induits_longueur_2()", globals={"graphe": graphe}, number=20) * 1000 / 20
#print(f"Temps moyen d'exécution : {execution_time_ms:.3f} ms")

#execution_time_ms = timeit.timeit("graphe.algo_Bron_et_Kerbosch_avec_pivot(set(), set(range(graphe.taille_graphe)), set())", globals={"graphe": graphe}, number=1000) *1000 / 1000
#print(f"Temps moyen d'exécution : {execution_time_ms:.3f} ms")

#graphe.afficher()
#graphe.afficher_degre_max()
#graphe.nb_sommets_par_degre()
#graphe.nb_chemins_induits_longueur_2()
#graphe.algo_Bron_et_Kerbosch_sans_pivot(set(), set(range(graphe.taille_graphe)), set())
#graphe.algo_Bron_et_Kerbosch_avec_pivot(set(), set(range(graphe.taille_graphe)), set(),"random_clique")