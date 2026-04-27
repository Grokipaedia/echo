# echo.py - Talk to your future self
import json
import random
from datetime import datetime
from rich.console import Console
from rich.panel import Panel

console = Console()

class FutureSelf:
    def __init__(self, name="You"):
        self.name = name
        self.age_now = 2026
        self.memory = [
            "You always said you'd regret not taking the risk.",
            "Health is the only thing you can't buy back.",
            "The relationships you neglected still hurt years later.",
            "You were braver than you gave yourself credit for."
        ]
        console.print(Panel(f"[bold cyan]Echo v1.0 — Talking to {self.name} in the future...[/bold cyan]", title="🌌"))

    def respond(self, user_input: str) -> str:
        # Simulate future wisdom + personality evolution
        responses = [
            f"Remember when you asked me this exact thing at {self.age_now}? I told you the same thing I'm telling you now...",
            "Ten years from now you'll look back and laugh at how scared you were. Just do it.",
            "The version of you that exists in 2035 is begging you to stop overthinking this.",
            "You already know the answer. You're just hoping I'll give you permission.",
            "This decision is going to define the next decade. Choose the one that makes you proud when you look back."
        ]
        
        # Make it feel personal
        if any(word in user_input.lower() for word in ["job", "quit", "career"]):
            return "You spent years in that job you hated. The future me still carries that regret. Don't make the same mistake twice."
        if any(word in user_input.lower() for word in ["relationship", "love", "partner"]):
            return "The person you didn't fight for? They're happy now. You still think about them sometimes."
        
        return random.choice(responses)

if __name__ == "__main__":
    console.print("[bold green]Echo is waking up... Your future self is here.[/bold green]\n")
    echo = FutureSelf()
    
    console.print("\n[italic]Type 'quit' to end the conversation.[/italic]\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            console.print("[yellow]Future You: Take care of yourself. I'll be waiting.[/yellow]")
            break
        response = echo.respond(user_input)
        console.print(f"[bold cyan]Future You ({echo.age_now + random.randint(8,25)}):[/bold cyan] {response}\n")
