import random # Ajout de la bibliothèque pour le choix aléatoire de quel joueur commence

# Fonction qui affiche l'état actuel du plateau de jeu
def display_board(board): 
    print("╔══════╦══════╦══════╗") # Délimite la partie supérieure du plateau
    for i in range(0, 9, 3): # Boucle for qui parcourt les indices 0, 3, et 6 (pas de 3) pour afficher 3 lignes
        print(f"║ {board[i]} ║ {board[i+1]} ║ {board[i+2]} ║") # Chaque ligne affiche 3 éléments consécutifs du paramètre board
        if i == 0 or i == 3:
            print("╠══════╬══════╬══════╣") # Condition qui imprime une ligne de séparation après la ligne 0 et la ligne 3
    print("╚══════╩══════╩══════╝") # Délimite la partie inférieure du plateau

# Fonction qui gère le tour du joueur (choisit 1 case et met à jour le plateau) et qui prend 2 paramètres
def player_turn(board, player): 
    valid_choice = True # Variable qui sert à savoir si le choix du joueur est valide
    while valid_choice: # Boucle qui continue de s'exécuter tant que le choix n'est pas valide
        try: # Teste un bloc de code
            choice = int(input(f"Player {player}, choose a square between 1 and 9 : ")) - 1 # Demande une entrée (convertie en nombre entier) au joueur et soustrait 1 pour que ce soit ludique (car les indices des listes commencent à 0)
            if choice < 0 or choice > 8 or board[choice] != "    ": # Vérifie si le choix est < à 0, > à 8, ou que la case n'est pas vide
                print("Invalid choice, try again : ") # Affiche un message
            else: # Si aucune des conditions précédentes n'est vraie, ce bloc est exécuté
                board[choice] = player # Met à jour le plateau en écrivant le symbole du joueur à la case choisie
                valid_choice = False # Met fin à la boucle en rendant la condition while valid_choice fausse
        except ValueError: # Intercepte une erreur si l'utilisateur entre quelque chose qui n'est pas un nombre, pour éviter un bug
            print("Enter a valid number : ") # Affiche un message


def ai_turn(board, player): # Fonction pour le tour de l’intelligence artificielle


    for i in range(9): # La boucle parcourt les 9 cases du plateau
        if board[i] == "    ":
            board[i] = player # Si une case est vide, elle est temporairement jouée par le joueur
            if check_victory(board, player):
                return # Si cette action mène à une victoire, la fonction s’arrête immédiatement
            board[i] = "    " # Sinon, le coup est annulé, et le programme continue à tester d'autres options
    # 1°) Vérifie si l'IA peut gagner immédiatement et si oui l'IA joue cette case
    
    if board[4] == "    ":
        board[4] = player
        return
    # 2°) Si la case centrale est libre, l'IA la prend


    for i in [0, 2, 6, 8]:
        if board[i] == "    ":
            board[i] = player
            return
    # 3°) Si un coin est libre, l'IA le choisit
    
    for i in range(9):
        if board[i] == "    ":
            board[i] = player
            return
    # 4°) Si aucune des options n'est possible, l'IA choisit une case libre

  # Parcourt chaque combinaison gagnante et vérifie si toutes les cases de cette combinaison contient le symbole du joueur (si oui, retourne True)
def check_victory(board, player): # Fonction qui vérifie si un joueur a gagné et qui prend 2 paramètres
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    # liste contenant toutes les combinaisons gagnantes possibles (3 lignes, 3 colonnes, 2 diagonales)
    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False # Si aucune combinaison gagnante n'est trouvée, retourne False


def play(): # Fonction gère toute la logique du jeu
    board = ["    " for i in range(9)] # Crée un plateau de jeu représenté par une liste de 9 espaces vides
    mode = input('Choose mode : "1" for Player vs Player or "2" for Player vs AI : ')
    # Demande au joueur de choisir le mode de jeu
    
    current_player = random.choice([" 🦊 ", " 🐸 "]) # Détermination aléatoire du premier joueur
    print(f"The first player is randomly chosen to be Player {current_player}.")
    
    for turn in range(9):  # Boucle qui itère un maximum de 9 tours
        display_board(board) # Affiche le plateau de jeu à l'état actuel
        
        if mode == "1":
            player_turn(board, current_player)
        # Si le mode est Joueur contre Joueur, appelle le joueur à jouer
        
        elif mode == "2" and current_player == " 🦊 ":
            player_turn(board, current_player)
        # Si c'est le tour de " 🦊 " dans le mode 2, appelle le joueur à jouer


        else:
            ai_turn(board, current_player)
        # Sinon, appelle l'IA à jouer


        if check_victory(board, current_player):
            display_board(board)
            print(f"Congratulations ! Player {current_player} has won !")
            return
        # Après chaque tour, vérifie si le joueur actuel a gagné. Si oui, affiche un message et termine la partie
        
        if current_player == " 🦊 ":
            current_player = " 🐸 "
        else:
            current_player = " 🦊 "
        # Change de joueur pour le prochain tour (" 🦊 " devient " 🐸 ", et vice-versa)
    
    display_board(board)
    print("It's a draw !")
    # Si aucun joueur ne gagne après 9 tours, affiche le plateau final et un message


play() # Appelle la fonction play() pour démarrer le jeu
