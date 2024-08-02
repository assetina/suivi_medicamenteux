import network
import usocket as socket
from machine import Pin
from neopixel import NeoPixel
import ujson
from config import wifi_config
from fonctions import *
import gc

class WebServer:
    def __init__(self):
        # Activer le mode Station (STA)
        sta = network.WLAN(network.STA_IF)
        sta.active(True)

        # Se connecter à un réseau Wi-Fi existant
        sta.connect(wifi_config['ssid'], wifi_config['password'])
        self.ap_if = network.WLAN(network.AP_IF)
        self.ap_if.active(True)
        self.ap_if.config(essid='SMART TRASH', password='bright', authmode=network.AUTH_OPEN)
        
        self.led = Pin(13)
        allumerled(self.led)
        self.buzzer = Pin(5, Pin.OUT)
        self.ruban_led = NeoPixel(Pin(23), 95)
        self.micro_variable = "Poubelle fermée"
        self.port = 80



    def serve_file(self, client_sock, filename):
        try:
            with open("/site" + filename, "r") as file:
                file_content = file.read()
                response_headers = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
                client_sock.send(response_headers.encode("utf-8"))
                client_sock.send(file_content.encode("utf-8"))
        except OSError as e:
            response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\nFile not found."
            client_sock.send(response.encode("utf-8"))
        finally:
            client_sock.close()
            
            
    def lire_et_effacer_fichier_json(self,nom_fichier):
        try:
            # Ouvrir le fichier JSON en mode lecture
            with open(nom_fichier, 'r') as fichier:
                # Charger le contenu JSON depuis le fichier
                data = ujson.load(fichier)
            
            # Récupérer la valeur souhaitée (par exemple, 'micro_variable')
            valeur = data
            
            if valeur is not None:
                # Effacer le contenu du fichier (écrire un JSON vide)
                with open(nom_fichier, 'w') as fichier:
                    fichier.write('{}')
            
            return valeur
        
        except Exception as e:
            print("Erreur lors de la lecture et de la suppression du fichier JSON :", str(e))
            return ""


    def lire_fichier_json(self,nom_fichier):
            try:
                # Ouvrir le fichier JSON en mode lecture
                with open(nom_fichier, 'r') as fichier:
                    # Charger le contenu JSON depuis le fichier
                    data = ujson.load(fichier)
                
                # Récupérer la valeur souhaitée (par exemple, 'micro_variable')
                valeur = data
                return valeur
            
            except Exception as e:
                print("Erreur lors de la lecture et de la suppression du fichier JSON :", str(e))
                return ""



    def handle_request(self, client_sock):
        request = client_sock.recv(1024).decode("utf-8")
        parts = request.split(" ")
        if len(parts) > 1:
            method = parts[0]
            filename = parts[1]
            if method == "GET" and filename == "/":
                self.serve_file(client_sock, "/index.html")
            elif method == "POST" and filename == "/login":
                # Trouver la dernière ligne contenant les données POST
                data = request.split('\n')[-1].strip()
                # Diviser la ligne pour obtenir la valeur du champ "code_secret"
                entered_code = data.split('=')[1]
                if entered_code == secret_code:
                    self.serve_file(client_sock, "/control.html")
                    gc.collect()
                    client_sock.close()
                    return
                else:
                    # En cas d'erreur de code secret, afficher la page de connexion
                    self.serve_file(client_sock, "/index.html")

            elif 'GET /?micro_variable' in request:
                self.micro_variable= self.lire_et_effacer_fichier_json('notifs.json')
                response_data = {"micro_variable": self.micro_variable}
                response="HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n" + ujson.dumps(response_data)
                client_sock.send(response.encode('utf-8'))
                client_sock.close()
            elif 'GET /?log' in request:
                log= self.lire_fichier_json('log.json')
                response_data = {"log": log}
                response="HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n" + ujson.dumps(response_data)
                client_sock.send(response.encode('utf-8'))
                print(response)
                #client_sock.close()

            elif 'GET /?led=on' in request:
                 allumerled(self.led)
                 client_sock.close()
            elif 'GET /?led=off' in request:
                 eteindreled(self.led)
                 client_sock.close()
            elif 'GET /?buzzer=on' in request:
                 self.buzzer.on()
                 client_sock.close()
            elif 'GET /?buzzer=off' in request:
                 self.buzzer.off()
                 client_sock.close()
            elif 'GET /?ruban=on' in request:
                jeuleds(self.ruban_led)
                client_sock.close()
            elif 'GET /?ruban=off' in request:
                eteindreruban(self.ruban_led)
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
            gc.collect()

# Définir le code secret
secret_code = "1234"

# Utilisation de la classe WebServer
if __name__ == "__main__":
    web_server = WebServer()
    web_server.run_server()
