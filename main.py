# Importieren des necessary Moduls
import random

# Definieren der Klassendefinition für den Kichatbot
class KichatBot:
    def __init__(self):
        # Initialisieren der Wörterbuch mit Antworten
        self.worterbuch = {
            "hallo": ["Hallo!", "Hi there!"],
            "welt": ["Hello world!", "The world is big!"],
            "aufgabe": ["Was kannst du mir tun?", "I can help you with tasks."],
            "bye": ["Goodbye!", "See you later!"]
        }

    def antworten(self,frage):
        # Überprüfen, ob die Frage im Wörterbuch enthalten ist
        iffrage.lower() in self.worterbuch:
            return random.choice(self.worterbuch[frage.lower()])
        else:
            return "Sorry, I don't know how to answer that."

# Hauptprogramm
if __name__ == "__main__":
    # Erstellen eines neuen Kichatbots
    bot = KichatBot()

    print("Welcome to the Kichatbot!")
    while True:
        # Hinzufügen einer Frage zum Chat
       frage = input("You: ")
        
        # Verarbeiten der Frage und geben der Antwort zurück
        antwort = bot.antworten(frage)
        print("Bot:", antwort)

        # Beenden des Programms, wenn der Benutzer "exit" eingibt
        iffrage.lower() == "exit":
            break