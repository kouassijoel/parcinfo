import socket

adresseIP = "127.0.0.1"
port = 50000
while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((adresseIP, port))
    print("Bienvenue dans votre Banque Python")
    noCompte = input("Entrez votre numero de Compte : ")
    pin = input("Entrez votre CodePIN : ")
    client.send(("TESTPIN" + noCompte + " " + pin).encode("utf-8"))
    reponse = client.recv(255)
    if reponse == "TESTPIN OK":
        print("Bienvenue ! ")
        print("  Operations : ")
        print("1 - Depot")
        print("2 - Retrait")
        print("3 - Transfert")
        print("4 - Historique des operations")
        print("5 - Solde du compte")
        operation = input("Entrez l'operation que vous souhaitez : ")

        if operation =="1":
            montant = input("Entrez le montant  deposer: ")
            client.send("DEPOT" + noCompte + " " + montant).encode("utf-8")
            reponse = client.recv(255).decode("utf-8")
            print("Depot effectué.")
        elif operation == "2":
            montant = input("Entrez le montant à retirer : ")
            montant = str(- float(montant))
            client.send(("RETRAIT" + noCompte + " " + montant).encode("utf-8"))
            reponse = client.recv(255).decode("utf-8")
            if reponse =="RETRAIT OK":
                print("Retrait effectué")
            else:
                print("Retrait refusé")
        elif operation == "3":
            montant = input("Entrez le montant à transferé: ")
            noCompteDestination = input("Entrez le numero de compte de benificiare: ")
            client.send("TRANSFERT", + noCompte + " " + noCompteDestination + " " + montant)
            reponse = client.recv(255).decode("utf-8")
            if reponse == " TRANSFERT OK ":
                print("Transfert effectué")
            else:
                print("Transfert refusé")
        elif operation == "4":
            client.send(("HISTORIQUE" + noCompte).encode("utf-8"))
            historique = client.recv(4096).decode("utf-8").replace("HISTORIQUE ", "")
            print(historique)
        elif operation == "5":
            client.send(("SOLDE" + noCompte).encode("utf-8"))
            solde = client.recv(4096).decode("utf-8").replace("SOLDE ", "")
            print("Le solde du compte est de " + solde)
        else:
            print("Vos identifiants sont incorrects.")
        print("Au revoir ! ")
        client.close()
