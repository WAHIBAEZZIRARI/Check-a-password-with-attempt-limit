mot_de_passe_correct = "DEV@2023"
tentatives = 3

while tentatives > 0:
    mot_de_passe = input("Entrez le mot de passe : ")
    if mot_de_passe == mot_de_passe_correct:
        print("Bonjour")
        break
    else:
        tentatives -= 1
        if tentatives > 0:
            print(f"Mauvais mot de passe. Il vous reste {tentatives} tentatives.")
        else:
            question_secrete = input("Répondez à la question secrète : ")
            # Ici, vous pouvez vérifier la réponse à la question secrète.
