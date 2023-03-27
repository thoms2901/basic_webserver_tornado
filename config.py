#################################################################################################################
#   Inserire i file html nella cartella templates con i nomi NAME_HOME, NAME_LOGIN e root                       #
#   Nei file html, importare i file statici da static Es. "static/styles/login.css"                             #
#   Dipendenze:     - Tornado Web, base64, uuid                                                                 #                                     
#   Per il login usare input con id="username" e id="password"                                                  #
#################################################################################################################

# Porta di connessione
PORT = 80

# Scegliere quale pagina mettere e il nome da far comparire
HOME = True
NAME_HOME = r"/home"

LOGIN = True
NAME_LOGIN = r"/login"

ROOT = True
NAME_ROOT = r"/"

# Modificare il nome del servizio
HEADER_NAME = "Mongoose/6.18"

# Cookie di sessione per il login: disabilitare se disabilitato login
COOKIE = True

# Username e password per login
USERNAME = "admin"
PASSWORD = "admin"