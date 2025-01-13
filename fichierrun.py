import json
from collections import defaultdict

def create_json_from_graph(file_path, output_path):
    """
    Lit un fichier texte contenant les transitions d'un graphe et crée un fichier JSON.
    
    :param file_path: Chemin vers le fichier texte d'entrée contenant les transitions.
    :param output_path: Chemin vers le fichier JSON de sortie.
    """
    # Dictionnaire pour stocker les listes de voisins
    adjacency_list = defaultdict(list)

    # Lecture du fichier texte
    with open(file_path, "r") as file:
        for line in file:
            if line.strip():  # Ignorer les lignes vides
                # Séparer les deux nœuds dans chaque ligne
                node1, node2 = map(int, line.strip().split())
                
                # Ajouter le voisin seulement s'il n'est pas déjà dans la liste
                if node2 not in adjacency_list[str(node1)]:
                    adjacency_list[str(node1)].append(node2)
                if node1 not in adjacency_list[str(node2)]:
                    adjacency_list[str(node2)].append(node1)

    # Structure finale
    data = {
        "graphe": adjacency_list
    }

    # Écriture dans le fichier JSON
    with open(output_path, "w") as json_file:
        json.dump(data, json_file)

    print(f"Fichier JSON créé : {output_path}")

# Exemple d'utilisation
create_json_from_graph("email-Eu-core.txt", "Graphes/email-Eu-core.json")