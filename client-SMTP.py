import socket
import ssl
import base64

serverName = "smtp.gmail.com"
serverPort = 465
mail = ""
password = ""
alici_mail = ""


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl.create_default_context()
ssl_socket = context.wrap_socket(clientSocket, server_hostname=serverName)
ssl_socket.connect((serverName, serverPort))


def istek_gonder(komut = ""):
    ssl_socket.send(f"{komut}\n".encode("utf-8"))
    cevap_al(komut + " isteği:")


def cevap_al(deger = "Sunucudan gelen cevap:"):
    print(deger + "\n  ", ssl_socket.recv(1024).decode("utf-8"))

def mail_icerigi(baslik, icerik):
    ssl_socket.send(f"SUBJECT: {baslik}\r\n\r\n".encode("utf-8"))
    ssl_socket.send(f"{icerik}\r\n".encode("utf-8"))


base64sifreleme = lambda deger: base64.b64encode(deger.encode()).decode()


# print("Sunucudan gelen mesaj: ", clientSocket.recv(1024).decode())
cevap_al("Bağlantı başlangıç cevabı:")

# clientSocket.send(
#     "EHLO gmail.com\n".encode()
# )  # alt satıra geç(\n) girilmeli yoksa çalıştığında bu kısma gelince bekliyor.
istek_gonder("EHLO gmail.com")

# print("Sunucudan gelen mesaj: ", clientSocket.recv(1024).decode())

# clientSocket.send("AUTH LOGIN\n".encode())
istek_gonder("AUTH LOGIN")

# print("Sunucudan gelen mesaj: ", clientSocket.recv(1024).decode())

# istek_gonder((base64.b64encode(mail.encode())).decode())
istek_gonder(base64sifreleme(mail))

istek_gonder(base64sifreleme(password))

istek_gonder(f"MAIL FROM: <{mail}>")

istek_gonder(f"RCPT TO: <{alici_mail}>")

istek_gonder("DATA")

# istek_gonder("SUBJECT: Burası başlık yazısı")

# istek_gonder("Mail içeriğinde ne olsun karar veremedim.")

mail_icerigi("Burası başlık", "Mail içeriği")

istek_gonder(".\r")

istek_gonder("QUIT")

ssl_socket.close()
