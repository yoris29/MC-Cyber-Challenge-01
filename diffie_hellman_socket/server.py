import socket

g = 3
p = 353

a = 97
A = pow(g, a, p) 

serveurSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveurSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serveurSocket.bind(('127.0.0.1', 8000))
serveurSocket.listen(1)
(socketClient, adIPClient) = serveurSocket.accept()

socketClient.send(str(A).encode())

M = True
while M:
    B = socketClient.recv(2048).decode()
    
    if B.strip().lower() == "exit": 
        print("Le client a quitté la session.")
        M = False
    else:
        B = int(B)
        K = pow(B, a, p)
        print(f"Clé secrète calculée (Serveur) : {K}")

    # Réception du message du client
    Donnees = socketClient.recv(2048).decode()
    if Donnees.strip().lower() == "exit":
        print("Le client a quitté la session.")
        M = False
    else:
        print(f"Le client a envoyé : {Donnees}")

    # Envoi d'un message au client
    if M:
        Message = input("Saisissez un message à envoyer au client: ")
        socketClient.send(Message.encode())

socketClient.close()
serveurSocket.close()
