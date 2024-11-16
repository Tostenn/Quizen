from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from time import sleep


class Output:
    """
    Classe Output : Gestion de l'affichage pour le jeu de quiz.
    """

    def __init__(self) -> None:
        self.logo_name = "Quiz Game"
        self.console = Console()

    def info(self, player: str, score: int, life: int):
        """Affiche les informations générales sur le joueur."""
        table = Table(show_header=False, box=None)
        table.add_row("Gamer:", f"[bold green]{player}[/bold green]")
        table.add_row("Score:", f"[bold yellow]{score}[/bold yellow]")
        table.add_row("Vie:", f"[red]{':heart:' * life}[/red]")

        panel = Panel(table, border_style="bold blue")
        self.console.print(panel, justify="center")

    def show_quiz(self, question, reponses):
        """Affiche la question et les réponses du quiz."""
        self.console.print(Panel(f"{question} ?", border_style="bold blue"), justify="center")

        table = Table(show_header=False, box=None)
        line = []

        for i, reponse in enumerate(reponses, 1):
            line.append(Panel(f"{i} - {reponse}", border_style="bold blue"))
            if i % 2 == 0 or i == len(reponses):
                table.add_row(*line)
                line = []

        self.console.print(table, justify="center")

    def prompt(self, start: int = 1, end: int = 4) -> int:
        """Demande la réponse du joueur."""
        while True:
            value = self.console.input(f"Quelle est la [bold green]bonne réponse[/bold green] (ou entrez 'end' pour quitter) : ")

            if value.lower() in ["end", "."]:
                return 0

            if not value.isdigit():
                self.console.print(f"[bold red]Entrez un nombre entre {start} et {end} ![/bold red]")
                continue

            value = int(value)
            if start <= value <= end:
                return value

            self.console.print(f"[bold red]Entrez une valeur valide entre {start} et {end} ![/bold red]")

    def read_event_touch(self):
        """Pause jusqu'à ce que l'utilisateur appuie sur Entrée."""
        self.console.input("\n[bold green]Appuyez sur Entrée pour continuer...[/bold green]")

    def good_reponse_animation(self, text: str = "Bonne réponse !"):
        """Animation pour une bonne réponse."""
        self.console.clear()

        message = Text(text, justify="center", style="bold green")
        with Live(message, refresh_per_second=4, console=self.console) as live:
            for i in range(5):
                if i % 2 == 0:
                    message.stylize("on green")
                else:
                    message.stylize("on yellow")
                live.update(message)
                sleep(0.3)

    def bad_reponse_animation(self, reponse):
        """Animation pour une mauvaise réponse."""
        self.console.clear()
        self.console.print("Mauvaise réponse !", justify="center", style="bold red on red")
        self.console.print(
            Panel(f"La bonne réponse était [bold green]{reponse}[/bold green]", border_style="cyan"),
            justify="center"
        )
        self.read_event_touch()

    def show_stat(self, data: dict):
        """Affiche les statistiques finales du joueur."""
        self.logo()
        print("\n")

        panel = Panel(f"[bold black]{data['name']}[/bold black]", style="on white", border_style="")
        self.console.print(panel, justify="center")
        self.console.print("Mes performances lors de cette partie :", justify="center")

        table = Table(show_header=False, box=None)

        # Ajout des données au tableau
        self.table_add_row(table, "Questions répondues", data['answered'])
        self.table_add_row(table, "Questions trouvées", data['correct'], highlight=data['correct'] < data['incorrect'])
        self.table_add_row(table, "Questions perdues", data['incorrect'], highlight=data['correct'] > data['incorrect'])
        self.table_add_row(table, "Score", data['score'])
        self.table_add_row(table, "Bonnes réponses successives", data['max_successive_correct'])
        self.table_add_row(table, "Vies restantes", data['remaining_life'])

        self.console.print(Panel(table, border_style="bold blue"), justify="center")

    def table_add_row(self, table: Table, key: str, value: int, highlight: bool = False):
        """Ajoute une ligne au tableau avec style conditionnel."""
        style = "red" if value == 0 or highlight else "green"
        table.add_row(
            Panel(key, border_style="bold blue"),
            Panel(str(value), style=f"bold {style}", border_style=f"bold {style}")
        )

    def logo(self):
        """Affiche le logo du jeu."""
        panel = Panel(self.logo_name, style="green bold", border_style="bold blue")
        self.console.print(panel, justify="center")
