import socket

g = 3
p = 353

b = 233
B = pow(g, b, p)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('127.0.0.1', 8000))

A = int(clientSocket.recv(2048).decode())

clientSocket.send(str(B).encode())

M = True
while M:
    K = pow(A, b, p)
    print(f"Clé secrète calculée (Client) : {K}")

    # Envoi d'un message au serveur
    Message = input("Saisissez un message à envoyer au serveur: ")
    clientSocket.send(Message.encode())

    if Message.strip().lower() == "exit":
        M = False
    else:
        # Réception de la réponse du serveur
        Donnees = clientSocket.recv(2048).decode()
        print(f"Le serveur a envoyé : {Donnees}")

clientSocket.close()
