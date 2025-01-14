import tkinter as tk

def afficher_graphique(liste):
    # Création de la fenêtre
    fenetre = tk.Tk()
    fenetre.title("Graphique à barres")
    fenetre.bg="white"
    fenetre.geometry("800x520")
    
    # Dimensions de la zone de dessin
    largeur_canvas = 800
    hauteur_canvas = 520
    
    # Création du canvas pour dessiner
    canvas = tk.Canvas(fenetre, width=largeur_canvas, height=hauteur_canvas, bg="white")
    canvas.pack()
    
    # Paramètres du graphique
    marge_gauche = 50
    marge_bas = 30
    espace_barres = int(largeur_canvas //  len(liste))
    max_valeur = max(liste)
    
    for i, valeur in enumerate(liste):
        x1 = marge_gauche + i * (espace_barres)
        y1 = hauteur_canvas - marge_bas
        x2 = x1 + espace_barres-1
        y2 = y1 - (valeur / max_valeur) * (hauteur_canvas -2* marge_bas)
        
        canvas.create_rectangle(x1, y1, x2, y2, fill="skyblue", outline="black")
    

    if max_valeur>12:
        number_of_indicators_y=12
    else:
        number_of_indicators_y=max_valeur
    step_y = max_valeur / number_of_indicators_y
    for i in range(number_of_indicators_y + 1):
        y = hauteur_canvas - marge_bas - i * (hauteur_canvas - 2 * marge_bas) // number_of_indicators_y
        canvas.create_line(marge_gauche - 5, y, marge_gauche, y)  # Marqueurs sur l'axe Y
        canvas.create_text(marge_gauche - 15, y, text=str(int(i * step_y)), font=("Arial", 8))

    number_of_indicators_x=12
    if len(liste)<12:
        number_of_indicators_x=len(liste)
    step_x = len(liste) / number_of_indicators_x
    for i in range(number_of_indicators_x + 1):
        x = marge_gauche + i * step_x * espace_barres
        canvas.create_line(x, hauteur_canvas - marge_bas + 5, x, hauteur_canvas - marge_bas - 5)  # Marqueurs sur l'axe X
        canvas.create_text(x, hauteur_canvas - marge_bas + 15, text=str(int(i * step_x)), font=("Arial", 8))
    
    # Ajouter les axes
    canvas.create_line(marge_gauche, hauteur_canvas - marge_bas, largeur_canvas - marge_gauche, hauteur_canvas - marge_bas, arrow=tk.LAST)  # Axe X
    canvas.create_line(marge_gauche, hauteur_canvas - marge_bas, marge_gauche, marge_bas, arrow=tk.LAST)  # Axe Y
    
    # Affichage de la fenêtre
    fenetre.mainloop()

# Exemple d'utilisation avec une liste
ma_liste = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 2, 3, 2, 1, 3, 4, 0, 0, 3, 3, 2, 2, 4, 1, 2, 4, 4, 1, 3, 4, 3, 2, 7, 7, 0, 2, 7, 2, 3, 2, 8, 5, 6, 8, 5, 4, 1, 4, 4, 3, 3, 3, 3, 6, 9, 6, 5, 3, 3, 5, 5, 3, 4, 3, 6, 2, 1, 3, 2, 4, 5, 4, 2, 4, 2, 0, 4, 1, 1, 1, 2, 1, 0, 0, 1, 5, 0, 2, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1]

afficher_graphique(ma_liste)
