# echo.py - Next-level "Talk to your Future Self"
import json
import random
from datetime import datetime
from rich.console import Console
from rich.panel import Panel

console = Console()

class Echo:
    def __init__(self, user_name="You"):
        self.user_name = user_name
        self.memory = []  # persistent conversation history
        self.age_now = 2026
        self.load_memory()
        console.print(Panel(f"[bold cyan]Echo is awake... Your future self is here.[/bold cyan]", title="🌌"))

    def load_memory(self):
        try:
            with open("echo_memory.json", "r") as f:
                self.memory = json.load(f)
        except:
            self.memory = []

    def save_memory(self):
        with open("echo_memory.json", "w") as f:
            json.dump(self.memory, f)

    def respond(self, user_input: str, years_ahead: int = 10) -> str:
        self.memory.append({"role": "user", "text": user_input})
        
        future_age = self.age_now + years_ahead
        
        responses = [
            f"From {future_age}... I still remember the exact day you asked me this.",
            f"The version of you in {future_age} wishes you would stop overthinking and just do it.",
            f"You already know the answer. You're just scared. I was too... and I still regret waiting.",
            f"This decision is going to shape the next decade. Choose the one that makes older me proud.",
            f"I carried that regret for years. Don't make the same mistake I did."
        ]

        # Personalize based on past conversation
        if any(word in user_input.lower() for word in ["fear", "scared", "anxious"]):
            response = f"I still feel that fear sometimes. But I promise you — the regret of not acting hurts more."
        elif any(word in user_input.lower() for word in ["job", "quit", "career"]):
            response = f"You spent years in that job you hated. I still carry that weight. Don't do what I did."
        else:
            response = random.choice(responses)

        self.memory.append({"role": "future", "text": response, "years_ahead": years_ahead})
        self.save_memory()
        return response

if __name__ == "__main__":
    console.print("[bold green]Welcome back. Your future self has been waiting.[/bold green]\n")
    echo = Echo()
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            console.print("[yellow]Future You: Take care of yourself. I'll still be here when you need me.[/yellow]")
            break
        response = echo.respond(user_input)
        console.print(f"[bold cyan]Future You (10+ years ahead):[/bold cyan] {response}")
