# echo.py - Ultimate version
import json
import random
from datetime import datetime
from rich.console import Console
from rich.panel import Panel

console = Console()

class Echo:
    def __init__(self):
        self.memory_file = "echo_memory.json"
        self.memory = self.load_memory()
        self.age_now = 2026
        console.print(Panel("[bold cyan]Echo is awake... Your future self has been waiting.[/bold cyan]", title="🌌"))

    def load_memory(self):
        try:
            with open(self.memory_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []

    def save_memory(self):
        with open(self.memory_file, "w", encoding="utf-8") as f:
            json.dump(self.memory, f, indent=2)

    def respond(self, user_input: str, years_ahead: int = 10):
        self.memory.append({"role": "user", "text": user_input, "timestamp": datetime.now().isoformat()})

        future_age = self.age_now + years_ahead

        if any(word in user_input.lower() for word in ["fear", "scared", "anxious", "worry"]):
            response = f"From {future_age}... I still feel that same fear sometimes. But the regret of not acting hurts so much more."
        elif any(word in user_input.lower() for word in ["job", "quit", "career"]):
            response = f"You spent years in that job you hated. I still carry that weight. Don't make the same mistake I did."
        elif any(word in user_input.lower() for word in ["relationship", "love", "partner"]):
            response = f"The people you didn't fight for? They're happy now. You still think about them."
        else:
            responses = [
                f"From {future_age}... I remember the exact day you asked me this.",
                f"The version of you in {future_age} wishes you would stop overthinking and just do it.",
                f"You already know the answer. You're just scared. I was too.",
                f"This decision is going to define the next decade. Choose the one that makes older me proud.",
            ]
            response = random.choice(responses)

        self.memory.append({"role": "future", "text": response, "years_ahead": years_ahead, "timestamp": datetime.now().isoformat()})
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
        years = int(input("How many years ahead? (5/10/20) [default 10]: ") or 10)
        response = echo.respond(user_input, years)
        console.print(f"[bold cyan]Future You ({echo.age_now + years}):[/bold cyan] {response}\n")
