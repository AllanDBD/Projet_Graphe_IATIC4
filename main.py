import random
import json
from datetime import datetime

class Graphe:
    def afficher(self):
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

class Random_graphe(Graphe):
    def __init__(self):
        self.n = int(input("Taille du graphe : "))
        self.p = random.random()  # Probabilité aléatoire entre 0 et 1
        self.graphe = self.generer_lists()
        self.degre_maximum()
        self.save_graphe()

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
    
    def save_graphe(self):
        answer=input("Voulez-vous sauvegarder ce graphe aléatoire dans un fichier? (o/O si oui): ")
        if(answer=="o" or answer=="O"):
            answer=input("Souhaitez-vous choisir le nom du fichier où sauvegarder le graphe? (o/O si oui, n/N sinon): ")
            if(answer=="o" or answer=="O"):
                file_name=input("Entrez le nom du fichier: ")
            elif(answer=="n" or answer=="N"):
                current_time = datetime.now()
                file_name = "random_graphe-"+current_time.strftime("%Y-%m-%d_%H-%M-%S") + ".json"
            else:
                return
            graphe = {str(i): self.graphe[i] for i in range(self.n)}
            data= {
                "n": self.n,
                "graphe": graphe
            }
            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)

class Import_graphe(Graphe):
    def __init__(self,file):
        #self.file= str(input("Entrer le nom du fichier dont vous souhaitez importer le graphe: "))
        # Lecture du fichier JSON
        with open(file, "r") as file:
            self.data = json.load(file)

        self.n = self.data["n"]
        self.graphe = self.import_listes()
        self.degre_maximum()

    def import_listes(self):    
        lists = self.data["graphe"]
        graphe=[]
        for node in lists:
            graphe.append(lists[node])
        return graphe

#graphe = Random_graphe()
graphe = Import_graphe("test2.json")
graphe.afficher()
graphe.afficher_degre_max()
graphe.nb_sommets_par_degre()
graphe.nb_chemins_induits_longueur_2()