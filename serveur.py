import network
import usocket as socket
import ujson
from machine import Pin
from fonctions import *

class WebServer:
    def __init__(self):
        self.ap_if = network.WLAN(network.AP_IF)
        self.ap_if.active(True)
        self.ap_if.config(essid='ALARME MEDICALE', password='rappel', authmode=network.AUTH_OPEN)
        self.port = 80
        self.json_file = 'heures.json'  # Nom du fichier JSON

    def serve_file(self, client_sock, filename):
        try:
            with open("/pages" + filename, "r") as file:
                file_content = file.read()
                response_headers = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
                client_sock.send(response_headers.encode("utf-8"))
                client_sock.send(file_content.encode("utf-8"))
        except OSError as e:
            response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\nFile not found."
            client_sock.send(response.encode("utf-8"))
        finally:
            client_sock.close()

    def write_json_data(self, data):
        try:
            with open(self.json_file, 'w') as file:
                ujson.dump(data, file)
        except Exception as e:
            print("Erreur lors de l'écriture du fichier JSON :", str(e))

    def read_and_clear_json(self):
        try:
            with open(self.json_file, 'r') as file:
                data = ujson.load(file)

            # Effacer le contenu du fichier (écrire un JSON vide)
            with open(self.json_file, 'w') as file:
                file.write('{}')

            return data

        except Exception as e:
            print("Erreur lors de la lecture et de la suppression du fichier JSON :", str(e))
            return {}

    def handle_request(self, client_sock):
        request = client_sock.recv(1024).decode("utf-8")
        parts = request.split(" ")
        if len(parts) > 1:
            method = parts[0]
            filename = parts[1]
            if method == "GET" and filename == "/":
                self.serve_file(client_sock, "/index.html")
         
            elif 'GET /?select=1' in request:
                data = ["06:00", "18:00"]
                print("fait")
                self.write_json_data(data)
                client_sock.close()
            elif 'GET /?select=1' in request:
                data = ["06:00", "12:00", "18:00"]
                print("fait")
                self.write_json_data(data)
                client_sock.close()
            elif 'GET /?select=3' in request:
                data = ["06:00", "10:00", "14:00", "18:00", "22:00", "02:00"]
                print("fait")
                self.write_json_data(data)
                client_sock.close()
            elif 'GET /?select=4' in request:
                data = ["06:00", "11:00", "16:00", "21:00", "02:00"]
                print("fait")
                self.write_json_data(data)
                client_sock.close()
            elif 'GET /?select=5' in request:
                data = ["06:00", "09:00", "12:00", "15:00", "18:00", "21:00", "00:00", "03:00"]
                print("fait")
                self.write_json_data(data)
                client_sock.close()
                
            else:
                self.serve_file(client_sock, "/index.html")
                client_sock.close()

    def run_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', self.port))
        server_socket.listen(5)

        print("Serveur en cours d'exécution sur http://192.168.4.1")

        while True:
            client_sock, client_addr = server_socket.accept()
            print("Nouvelle connexion depuis {}".format(client_addr))
            self.handle_request(client_sock)

# Utilisation de la classe WebServer
if __name__ == "__main__":
    web_server = WebServer()
    web_server.run_server()

