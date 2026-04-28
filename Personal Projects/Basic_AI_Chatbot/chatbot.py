import re
import random
import urllib.request
import json
import difflib
import tkinter as tk
from tkinter import scrolledtext
from typing import Dict, Any, List

def fetch_weather():
    """
    Fetches real live weather data from wttr.in.
    """
    url = "https://wttr.in/?format=3"
    req = urllib.request.Request(url, headers={'User-Agent': 'curl/7.81.0'})
    response = urllib.request.urlopen(req, timeout=5)
    weather_data = response.read().decode('utf-8').strip()
    
    prefixes = [
        "I checked the internet! Here is the latest:",
        "According to the web, the weather is:",
        "Just pulled this from the forecast online:",
        "Here's what the internet says about the weather:"
    ]
    one_line_weather = weather_data.replace('\n', ' ').replace('\r', '')
    return f"{random.choice(prefixes)} {one_line_weather}"

def fetch_joke():
    """
    Fetches a random joke from the official-joke-api.
    """
    url = "https://official-joke-api.appspot.com/random_joke"
    req = urllib.request.Request(url, headers={'User-Agent': 'curl/7.81.0'})
    response = urllib.request.urlopen(req, timeout=5)
    data = json.loads(response.read().decode('utf-8'))
    
    prefixes = [
        "I found a joke online for you!",
        "Here's a funny one I grabbed from the internet:",
        "I connected to the web and found this joke:",
        "Get ready to laugh! From the web:"
    ]
    setup = data['setup'].replace('\n', ' ')
    punchline = data['punchline'].replace('\n', ' ')
    return f"{random.choice(prefixes)} {setup} ... {punchline}"

# Dictionary storing different "intents" (topics), recognizing patterns, and how to reply
INTENTS: Dict[str, Dict[str, Any]] = {
    'greeting': {
        'patterns': [r'\bhello\b', r'\bhi\b', r'\bhey\b', r'\bgreetings\b', r'\bhallo\b'],
        'responses': ["Hello there! 👋 Let's make today awesome. What can I do for you?", 
                      "Hey bestie! ✨ What's on your mind?", 
                      "Greetings! 🤖 I'm powered up and ready to help!"]
    },
    'goodbye': {
        'patterns': [r'\bbye\b', r'\bgoodbye\b', r'\bsee ya\b', r'\bexit\b', r'\bquit\b'],
        'responses': ["Catch you later! 👋 Have a phenomenal day!", 
                      "Goodbye! Stay awesome out there. ✨", 
                      "Closing my circuits for now! See ya! 🤖"]
    },
    'weather': {
        'patterns': [r'\bweather\b', r'\bforecast\b', r'\brain\b', r'\bsun\b'],
        'action': fetch_weather
    },
    'joke': {
        'patterns': [r'\bjoke\b', r'\bmake me laugh\b', r'\bfunny\b'],
        'action': fetch_joke
    },
    'help': {
        'patterns': [r'\bhelp\b', r'\bassist\b', r'\bwhat can you do\b'],
        'responses': ["I'm a personal digital assistant with internet access! 🌐\nTry asking me for the 'weather' or a 'joke'!", 
                      "I can chat, spell-check, and search the web for jokes and weather! 🧠 What do you need?"]
    },
    'how_are_you': {
        'patterns': [r'\bhow are you\b', r'\bhow are u\b', r'\bhow do you do\b'],
        'responses': ["I'm doing fantastic, thanks for asking! 🌟 Just floating in the data streams. How are you?", 
                      "My CPU is happy and my code is running perfectly! ⚡ How's your day going?"]
    },
    'name': {
        'patterns': [r'\byour name\b', r'\bwho are you\b'],
        'responses': ["I'm PyBot, your personal digital sidekick! 🦸‍♂️", 
                      "You can call me PyBot! Nice to meet you. ✨"]
    }
}

# Fallback responses when no intents match the user input
DEFAULT_RESPONSES = [
    "Hmm, I'm not totally sure what you mean by that. 🤔 Want to ask me about the weather or a joke?",
    "That went right over my digital head! 🛸 Could you rephrase it?",
    "Interesting! 📝 I don't know the answer to that yet, but I'm always learning.",
    "I'm a bit lost there. 😅 Maybe try asking for a joke?"
]

BOT_VOCABULARY = [
    'hello', 'hi', 'hey', 'greetings', 'bye', 'goodbye', 'exit', 'quit',
    'weather', 'forecast', 'rain', 'sun', 'joke', 'laugh', 'funny',
    'help', 'assist', 'name'
]

def correct_spelling(user_input):
    words = user_input.split()
    corrected_words: List[str] = []
    corrections_made = False
    
    for word in words:
        clean_word = re.sub(r'[^\w]', '', word.lower())
        if not clean_word:
            corrected_words.append(word)
            continue
            
        matches = difflib.get_close_matches(clean_word, BOT_VOCABULARY, n=1, cutoff=0.75)
        if matches and matches[0] != clean_word:
            corrected_words.append(matches[0])
            corrections_made = True
        else:
            corrected_words.append(word)
            
    return " ".join(corrected_words), corrections_made

def clean_input(user_input):
    return user_input.strip().lower()

def identify_intent(user_input):
    for intent, data in INTENTS.items():
        for pattern in data['patterns']:
            if re.search(pattern, user_input):
                return intent
    return None

def generate_response(intent):
    if intent and intent in INTENTS:
        intent_data = INTENTS[intent]
        if 'action' in intent_data:
            return intent_data['action']()
        return random.choice(intent_data['responses'])
    return random.choice(DEFAULT_RESPONSES)

class ChatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PyBot Virtual Assistant")
        self.root.geometry("550x700")
        self.root.configure(bg="#1E1E2E")
        
        # Header
        header = tk.Label(
            self.root, text="🤖 PyBot Assistant", bg="#89B4FA", fg="#11111B", 
            font=("Segoe UI", 16, "bold"), pady=15
        )
        header.pack(fill=tk.X)

        # Input Frame
        input_frame = tk.Frame(self.root, bg="#1E1E2E")
        input_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=15, pady=(0, 15))
        
        # Entry Widget
        self.entry = tk.Entry(
            input_frame, font=("Segoe UI", 14), bg="#313244", fg="#CDD6F4", 
            insertbackground="#CDD6F4", borderwidth=0, relief=tk.FLAT
        )
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 15), ipady=10)
        self.entry.bind("<Return>", self.send_message)
        
        # Send Button
        self.send_btn = tk.Button(
            input_frame, text="Send 🚀", font=("Segoe UI", 12, "bold"), 
            bg="#89B4FA", fg="#11111B", activebackground="#B4BEFE", 
            activeforeground="#11111B", command=self.send_message, 
            relief=tk.FLAT, cursor="hand2"
        )
        self.send_btn.pack(side=tk.RIGHT, ipadx=20, ipady=5)

        # Chat Display
        self.chat_display = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, bg="#11111B", fg="#CDD6F4", 
            font=("Segoe UI", 12), state=tk.DISABLED, padx=15, pady=15,
            borderwidth=0, highlightthickness=0
        )
        self.chat_display.pack(side=tk.TOP, padx=15, pady=15, fill=tk.BOTH, expand=True)
        
        # Tags for formatting messages
        self.chat_display.tag_configure("user_name", foreground="#A6E3A1", font=("Segoe UI", 12, "bold"), justify="right", spacing1=10)
        self.chat_display.tag_configure("user_msg", foreground="#CDD6F4", font=("Segoe UI", 12), justify="right", rmargin=10)
        self.chat_display.tag_configure("bot_name", foreground="#F38BA8", font=("Segoe UI", 12, "bold"), justify="left", spacing1=10)
        self.chat_display.tag_configure("bot_msg", foreground="#BAC2DE", font=("Segoe UI", 12), justify="left", lmargin1=10)
        
        # Initial greeting
        self.display_message("PyBot", "Hello! I'm online and ready to chat. ⚡\nType 'bye', 'exit', or 'quit' to close the app.")
        self.entry.focus()

    def send_message(self, event=None):
        user_input = self.entry.get()
        if not user_input.strip():
            return
            
        self.entry.delete(0, tk.END)
        self.display_message("You", user_input)
        
        sanitized_input = clean_input(user_input)
        corrected_input, was_corrected = correct_spelling(sanitized_input)
        
        if was_corrected:
            self.display_message("PyBot", f"(I corrected your typo to: '{corrected_input}') 🪄")
        
        sanitized_input = corrected_input
        
        if sanitized_input in ['quit', 'exit', 'bye']:
            goodbye = random.choice(INTENTS['goodbye']['responses'])
            self.display_message("PyBot", goodbye)
            self.root.after(1500, self.root.destroy)
            return
            
        matched_intent = identify_intent(sanitized_input)
        response = generate_response(matched_intent)
        
        self.display_message("PyBot", response)

    def display_message(self, sender, message):
        self.chat_display.configure(state=tk.NORMAL)
        
        if sender == "You":
            self.chat_display.insert(tk.END, f"{sender}\n", "user_name")
            self.chat_display.insert(tk.END, f"{message}\n", "user_msg")
        else:
            self.chat_display.insert(tk.END, f"{sender}\n", "bot_name")
            self.chat_display.insert(tk.END, f"{message}\n", "bot_msg")
            
        self.chat_display.see(tk.END)
        self.chat_display.configure(state=tk.DISABLED)

def start_chat():
    root = tk.Tk()
    app = ChatGUI(root)
    root.mainloop()

if __name__ == "__main__":
    start_chat()