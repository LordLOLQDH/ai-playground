# Importieren der ChatBoz C Bibliothek
from chatboz import ChatBot

# Erstellen eines neuen ChatBoz C-Objekts
chatbot = ChatBot()

# Definieren des Kichatbots' Namens und Beschreibung
chatbot.name = "Kitty"
chatbot.description = "Ein einfacher Kichatbot"

# Definieren des Kichatbots' Antworten
chatbot.responses = {
    "hallo": "Hallo! Wie kann ich Ihnen heute helfen?",
    "welt": "Hallo Welt!",
    "aufgabe": "Ich kann Ihnen Aufgaben erledigen.",
    "bye": "Auf Wiedersehen!"
}

# Starten des Kichatbots
chatbot.start()