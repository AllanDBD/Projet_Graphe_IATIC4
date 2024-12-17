import random

class Graphe:
    def __init__(self, n):
        self.n = n
        self.p = random.random()  # Probabilité aléatoire entre 0 et 1
        self.graphe = self.generer_lists()
        self.degre_maximum()

    def generer_lists(self):
        graphe = []
        for i in range(self.n):
            ligne = []
            graphe.append(ligne)
        for j in range(self.n):
            for k in range(j+1,self.n):
                if random.random() < self.p:
                    graphe[j].append(k)
                    graphe[k].append(j)
        return graphe

    def afficher(self):
        print(f"Probabilité p = {self.p:.2f}")
        for ligne in self.graphe:
            print(ligne)

    def degre_maximum(self):
        self.deg_max=0
        self.indice_degre_max=[]
        for i in range(self.n):
            if len(self.graphe[i]) > self.deg_max:
                self.deg_max=len(self.graphe[i])
                self.indice_degre_max=[]
                self.indice_degre_max.append(i)
            elif len(self.graphe[i])==self.deg_max:
                self.indice_degre_max.append(i)

    def afficher_degre_max(self):
        print("Degré max:",self.deg_max,"Sommet(s):",self.indice_degre_max)

    def nb_sommets_par_degre(self):
        nb_sommet=[0]*(self.deg_max+1)
        for i in range(self.n):
            nb_sommet[len(self.graphe[i])]=nb_sommet[len(self.graphe[i])]+1
        print(nb_sommet)
            
    def nb_chemins_induits_longueur_2(self):
        compteur=0
        for i in range(self.n):
            for k in self.graphe[i]:
                for j in self.graphe[k]:
                    if j>i:
                        if i not in self.graphe[j]:              
                            compteur+=1
        
        print(compteur)

n = int(input("Taille du graphe : "))
graphe = Graphe(n)
graphe.afficher()
graphe.degre_maximum()
graphe.afficher_degre_max()
graphe.nb_sommets_par_degre()
graphe.nb_chemins_induits_longueur_2()