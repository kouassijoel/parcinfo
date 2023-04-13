import socket

adresseIp = "127.0.0.1"
port = 50000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((adresseIp, port))
print("Connecté au serveur.")
client.send("Bonjour, je suis le client ".encode(" utf-8 "))
reponse = client.recv(255)
print(reponse.decode("utf-8"))
print("Connexio fermée")
client.close()
