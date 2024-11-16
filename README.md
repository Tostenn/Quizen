# Quiz Game

**Quiz Game** est une application console interactive conçue pour tester vos connaissances tout en vous amusant. Grâce à un simple dictionnaire structuré, vous pouvez créer des quiz de manière rapide et efficace. Une version de ce projet sera bientôt disponible en tant que package Python sur PyPI !

---

## 🎯 **Caractéristiques**
- Interface console interactive et colorée grâce à la bibliothèque **Rich**.
- Gestion des scores, des vies, et des bonnes réponses consécutives.
- Sauvegarde des statistiques du joueur dans un fichier JSON.
- Fonctionnalité d'affichage des statistiques à la fin du jeu.
- Possibilité de personnaliser les questions et réponses via un dictionnaire structuré.

---

## 📦 **Technologies utilisées**
- **Python 3.9+** : Langage principal du projet.
- **Rich** : Pour les affichages stylés dans la console.
- **JSON** : Pour la sauvegarde des données des joueurs.
- **random.shuffle** : Pour mélanger les questions et réponses.

---

## 🚀 **Installation**
1. Clonez le dépôt ou téléchargez les fichiers :
   ```bash
   git clone https://github.com/Tostenn/Quiz.git
   cd Quiz
   ```

2. Installez les dépendances :
   ```bash
   pip install rich
   ```

3. Lancez le jeu :
   ```bash
   python main.py
   ```

---

## ⚙️ **Structure des questions**
Les questions sont définies sous forme d'un dictionnaire Python, où :
- La clé est la question.
- La valeur est une liste contenant :
  1. La bonne réponse (en première position).
  2. Les mauvaises réponses.

### Exemple de dictionnaire structuré :
```python
questions = {
    "Quelle est la capitale de la France ?": ["Paris", "Londres", "Berlin", "Madrid"],
    "Combien de continents y a-t-il ?": ["7", "5", "6", "8"],
    "Quelle est la langue officielle du Brésil ?": ["Portugais", "Espagnol", "Français", "Anglais"],
}
```

---

## 🏃‍♂️ **Créer un quiz en 3 lignes**
Grâce au futur package `quiz` (disponible bientôt sur PyPI), voici comment créer et exécuter un quiz en seulement 3 lignes :

```python
from quiz import Quiz
questions = {"Quelle est la capitale de la France ?": ["Paris", "Londres", "Berlin", "Madrid"]}
Quiz(questions, player="Joueur").play()
```

---

## 📈 **Améliorations prévues**
- Ajout de fonctionnalités audio (sons pour bonnes et mauvaises réponses).
- Création du package **`quiz`** pour une utilisation facile via PyPI.
- Ajout d'une interface graphique (GUI) simple.

---

## 📝 **Contribuer**
Les contributions sont les bienvenues ! Veuillez :
1. Forker le projet.
2. Créer une branche pour votre fonctionnalité :  
   ```bash
   git checkout -b feature/ma-fonctionnalite
   ```
3. Soumettre une *pull request*.

---

## 📜 **Licence**
Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.

---

Avec ce projet, la création d'un jeu de quiz devient intuitive, éducative et amusante. Préparez-vous à apprendre et à vous divertir avec vos propres questions personnalisées ! 🎉