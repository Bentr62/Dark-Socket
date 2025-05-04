import threading

def dire_bonjour(nom):
    print(f"Bonjour {nom} !")

# Créer un thread
mon_thread = threading.Thread(target=dire_bonjour, args=("Benoit",))

# Lancer le thread
mon_thread.start()

# Attendre que le thread finisse
mon_thread.join()
