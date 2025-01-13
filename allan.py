import random
import json
from datetime import datetime
import timeit
#import matplotlib.pyplot as plt

class Graphe:
    
    def generer_un_graphe_random(self):
        self.taille_graphe = int(input("Taille du graphe : "))
        self.probabilite_branche = random.random()  # Probabilité aléatoire entre 0 et 1
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
        answer=input("Voulez-vous sauvegarder ce graphe aléatoire dans un fichier? (o/O si oui): ")
        if(answer=="o" or answer=="O"):
            answer=input("Souhaitez-vous choisir le nom du fichier où sauvegarder le graphe? (o/O si oui, n/N sinon): ")
            if(answer=="o" or answer=="O"):
                file_name="Graphes/"+input("Entrez le nom du fichier: ")+".json"
            elif(answer=="n" or answer=="N"):
                current_time = datetime.now()
                file_name = "Graphes/random_graphe-"+current_time.strftime("%Y-%m-%d_%H-%M-%S") + ".json"
            else:
                return
            graphe = {str(i): self.matrice_adjacence_ordonne[i] for i in range(self.taille_graphe)}
            data= {
                "n": self.taille_graphe,
                "graphe": graphe
            }
            with open(file_name, "w") as file:
                json.dump(data, file)

    def ordonner_matrice(self):
        #print("Liste non ordonnée: ",self.matrice_adjacence_non_ordonne)
        #print("Liste de correspondance: ",self.list_correspondance)
        if self.ordonne ==False:
            self.matrice_adjacence_ordonne = []
            for i in range(self.taille_graphe):
                self.matrice_adjacence_ordonne.append([])

            for sommet,indice in self.list_correspondance:
                for i in range (self.taille_graphe):
                    for j in range (len(self.matrice_adjacence_non_ordonne[i])):
                        if self.matrice_adjacence_non_ordonne[i][j]==sommet:
                            self.matrice_adjacence_ordonne[i].append(indice)
        #print("Liste ordonnée: ",self.matrice_adjacence_ordonne)

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
        nb_sommet = [0] * (self.deg_max + 1)
        for i in range(self.taille_graphe):
            nb_sommet[len(self.matrice_adjacence_ordonne[i])] += 1
        
        '''print("Nombre de noeud par degré: [ ",end="")
        for i in range(self.deg_max-1):
            if nb_sommet[i]!=0:
                print(i,":",nb_sommet[i],", ",end="")
        if nb_sommet[self.deg_max]!=0:
            print(self.deg_max,":",nb_sommet[self.deg_max],"]")
        '''
        '''
        # Filtrer les indices où les valeurs sont différentes de 0
        indices = [i for i, val in enumerate(nb_sommet) if val != 0]
        valeurs = [nb_sommet[i] for i in indices]

        # Afficher le graphe à bâtons
        plt.bar(indices, valeurs)
        plt.xlabel('Degré des sommets')
        plt.ylabel('Nombre de sommets')
        plt.title('Nombre de sommets par degré')
        plt.xticks(indices)  # S'assurer que seuls les indices pertinents sont affichés
        plt.show()'''




    def nb_chemins_induits_longueur_2(self):
        compteur=0
        for i in range(self.taille_graphe):
            for k in self.matrice_adjacence_ordonne[i]:
                for j in self.matrice_adjacence_ordonne[k]:
                    if j>i:
                        if i not in self.matrice_adjacence_ordonne[j]:              
                            compteur+=1
        
        #print("nombre de chemin induit longueur 2 = " ,compteur)

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
                clique = sorted(R)  # Trie la clique pour une meilleure lisibilité
                #print("Clique maximale trouvée:", clique)
            else:
                clique = [self.list_correspondance[i][0] for i in R]
                #print("Clique maximale trouvée:", " ".join(map(str, clique)))

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




    def import_graphe(self,file):
            # Lecture du fichier JSON
            with open(file, "r") as file:
                self.data = json.load(file)

            self.taille_graphe = self.data["n"]
            self.import_matrice()
            self.ordonner_matrice()
            print("Liste ordonnée")
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


graphe = Graphe()
#graphe.generer_un_graphe_random()
graphe.import_graphe("Graphes/random_graphe-2025-01-12_16-39-47.json")

#execution_time_ms = timeit.timeit("graphe.degre_maximum()", globals={"graphe": graphe}, number=1000) * 1000 / 1000
#print(f"Temps moyen d'exécution : {execution_time_ms:.3f} ms")
#execution_time_ms = timeit.timeit("graphe.nb_sommets_par_degre()", globals={"graphe": graphe}, number=100) * 1000 / 100
#print(f"Temps moyen d'exécution : {execution_time_ms:.3f} ms")
#execution_time_ms = timeit.timeit("graphe.nb_chemins_induits_longueur_2()", globals={"graphe": graphe}, number=20) * 1000 / 20
#print(f"Temps moyen d'exécution : {execution_time_ms:.3f} ms")

execution_time_ms = timeit.timeit("graphe.algo_Bron_et_Kerbosch_avec_pivot(set(), set(range(graphe.taille_graphe)), set())", globals={"graphe": graphe}, number=1000) *1000 / 1000
print(f"Temps moyen d'exécution : {execution_time_ms:.3f} ms")

#graphe.afficher()
#graphe.afficher_degre_max()
#graphe.nb_sommets_par_degre()
#graphe.nb_chemins_induits_longueur_2()
#graphe.algo_Bron_et_Kerbosch_sans_pivot(set(), set(range(graphe.taille_graphe)), set())
#graphe.algo_Bron_et_Kerbosch_avec_pivot(set(), set(range(graphe.taille_graphe)), set(),"random_clique")