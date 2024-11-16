from output import Output
from random import shuffle
from json import dump, load
from pathlib import Path



output = Output()


class Quiz:
    def __init__(self, questions: dict, player: str, life: int = 3, score: int = 0, path_save: str = "data.json") -> None:
        """
        # Quiz
        est une application console interactive, 
        conçue pour faciler la mise en place de **Game Quiz** amusant.

        Parameters
        ----------
        questions : dict
            Dictionnaire des questions et réponses.
        player : str
            Nom du joueur.
        life : int, optional
            Nombre initial de vies (par défaut : 3).
        score : int, optional
            Score initial (par défaut : 0).
        path_save : str, optional
            Chemin pour sauvegarder les statistiques (par défaut : 'data.json').
        """
        
        if not isinstance(questions, dict):
            raise ValueError("Le paramètre 'questions' doit être un dictionnaire.")

        self.output = output
        self.questions = questions
        self.player = player
        self.life = life if life > 0 else 3
        self.init_life = self.life
        self.score = score

        self.count_success = 0
        self.count_responses = 0
        self.count_correct_responses = 0
        self.max_successive_correct = 0

        self.path_save = Path(path_save)
        
    def shuffle_questions(self):
        """Mélange les questions et réponses."""
        data = list(self.questions.items())
        shuffle(data)
        self.questions = dict(data)

    def play(self):
        """Lancer le quiz."""
        self.shuffle_questions()

        for question, answers in self.questions.items():
            self.output.console.clear()

            # Mise à jour des statistiques
            self.increment_count_responses()

            # Affichage des informations
            self.output.info(self.player, self.score, self.life)

            # Préparation de la question et des réponses
            correct_answer = answers[0]
            shuffle(answers)

            # Affichage de la question
            self.output.show_quiz(question, answers)

            # Saisie du joueur
            player_response = self.output.prompt(end=len(answers))

            # Arrêt du jeu si le joueur choisit 0
            if player_response == 0:
                break

            # Vérification de la réponse
            if answers[player_response - 1] == correct_answer:
                self.handle_correct_answer()
            else:
                self.handle_wrong_answer(correct_answer)

            # Fin du jeu si les vies sont épuisées
            if self.life == 0:
                break

        # Affichage des statistiques finales
        self.end_game()

    def handle_correct_answer(self):
        """Gérer une réponse correcte."""
        self.output.good_reponse_animation()
        self.increment_score()
        self.increment_count_success()
        self.increment_count_correct_responses()
        self.check_bonus_life()

    def handle_wrong_answer(self, correct_answer):
        """Gérer une réponse incorrecte."""
        self.output.bad_reponse_animation(correct_answer)
        self.decrement_score()
        self.decrement_life()
        self.update_max_successive_correct()
        self.reset_count_success()

    def check_bonus_life(self):
        """Accorder un bonus de vie toutes les 5 réponses correctes consécutives."""
        if self.count_success % 5 == 0 and self.life < self.init_life:
            self.increment_life()
            self.output.good_reponse_animation(text="Vous gagnez une vie supplémentaire (+1) !")

    def end_game(self):
        """Afficher les statistiques et sauvegarder les données."""
        self.output.console.clear()
        player_data = self.save()
        self.output.show_stat(player_data)

    def increment_score(self):
        self.score += 1

    def decrement_score(self):
        if self.score > 0:
            self.score -= 1

    def increment_life(self):
        self.life += 1

    def decrement_life(self):
        self.life -= 1

    def increment_count_responses(self):
        self.count_responses += 1

    def increment_count_correct_responses(self):
        self.count_correct_responses += 1

    def increment_count_success(self):
        self.count_success += 1

    def reset_count_success(self):
        self.count_success = 0

    def update_max_successive_correct(self):
        if self.count_success > self.max_successive_correct:
            self.max_successive_correct = self.count_success

    def save(self):
        """Sauvegarder les données du joueur dans un fichier JSON."""
        try:
            with open(self.path_save, 'r', encoding='utf-8') as file:
                data = load(file)
        except (FileNotFoundError, ValueError):
            data = []

        # Ajout des données du joueur
        player_data = self.get_player_data()
        data.append(player_data)

        # Sauvegarde dans le fichier
        with open(self.path_save, 'w', encoding='utf-8') as file:
            dump(data, file, indent=4)

        return player_data

    def get_player_data(self):
        """Créer un dictionnaire contenant les données du joueur."""
        return {
            'name': self.player,
            'answered': self.count_responses,
            'correct': self.count_correct_responses,
            'incorrect': self.count_responses - self.count_correct_responses,
            'score': self.score,
            'max_successive_correct': self.max_successive_correct,
            'remaining_life': self.life,
        }
