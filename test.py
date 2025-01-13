import random
import json
from datetime import datetime




class Graphe:
    
    def generer_un_graphe_random(self):
        self.taille_graphe = int(input("Taille du graphe : "))
        self.probabilite_branche = random.random()  # Probabilité aléatoire entre 0 et 1
        self.ordonne=True
        self.generer_matrice_random()
        self.degre_maximum()
        
        
        #self.save_graphe()


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



    def nb_sommets_par_degre(self):
        nb_sommet=[0]*(self.deg_max+1)
        for i in range(self.taille_graphe):
            nb_sommet[len(self.matrice_adjacence_ordonne[i])]=nb_sommet[len(self.matrice_adjacence_ordonne[i])]+1
        print(nb_sommet)




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




    def algo_Bron_et_Kerbosch_avec_pivot(self, R, P, X):
        if len(P) == 0 and len(X) == 0:  
            self.cliques.append(R)
            return

        else :
            pivot = P.union(X).pop()
            for sommet in list(P.difference(self.matrice_adjacence_ordonne[pivot])): # Convert P to a list to safely iterate
                self.algo_Bron_et_Kerbosch_avec_pivot(
                    R.union({sommet}),  # Add the current vertex to R
                    P.intersection(self.matrice_adjacence_ordonne[sommet]),  # Neighbors in P
                    X.intersection(self.matrice_adjacence_ordonne[sommet])   # Neighbors in X
                )
                P.remove(sommet)
                X.add(sommet)


    def afficher_cliques(self):
        if self.ordonne:
            for i in self.cliques:
                print("Clique maximale trouvée:", i)
        else:
            for i in (self.cliques):
                print("Clique maximale trouvée:")
                for j in (i):
                    print(self.list_correspondance[j][0],end=" ")
                print("")

############################# source wikipedia ########################################




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
            

        
    def afficher_degre_max(self):
        if(self.ordonne):
            print("Degré max:",self.deg_max,"         Sommet(s):",self.indice_degre_max)

        else:
            list_indice=[]
            for i in range(len(self.indice_degre_max)):
                list_indice.append(self.list_correspondance[self.indice_degre_max[i]][0])
            print("Degré max:",self.deg_max,"         Sommet(s):",list_indice)



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


            return graphe





graphe = Graphe()
graphe.generer_un_graphe_random()
#graphe.import_graphe("test3.json")
graphe.afficher()
graphe.afficher_degre_max()
graphe.cliques=[]
graphe.algo_Bron_et_Kerbosch_avec_pivot(set(), set(range(graphe.taille_graphe)), set())
graphe.afficher_cliques()
#graphe.give_ordering()
#i=input("give_position in ordering : ")
#g=graphe.Gi_construct(int(i))
#g.afficher()


#graphe.generer_un_graphe_random()
#graphe.afficher()
#graphe.afficher_degre_max()
#graphe.nb_sommets_par_degre()
#graphe.nb_chemins_induits_longueur_2()






