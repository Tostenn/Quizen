# Quizen 🎮

**Quizen** est une bibliothèque Python qui permet de créer et de jouer à des quiz interactifs en ligne de commande. Grâce à un simple dictionnaire structuré, vous pouvez créer des quiz facilement. Ce paquet est conçu pour faciliter la mise en place de jeux de quiz amusants pour tester vos connaissances !

Vous pouvez installer cette bibliothèque via `pip` et l'utiliser pour démarrer un quiz en quelques lignes de code.

![Version](https://img.shields.io/pypi/v/quizen?color=blue) 
![Python Version](https://img.shields.io/pypi/pyversions/quizen?color=green)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Installation 🛠️

### Installation via `pip` (depuis PyPI) 📦

Vous pouvez installer `quizen` en utilisant `pip` :

```bash
pip install quizen
```

### Installation en mode développement 🧑‍💻

Si vous souhaitez contribuer ou tester le code localement, vous pouvez installer `quizen` en mode développement :

```bash
git clone https://github.com/username/quizen.git
cd quizen
pip install -e .
```

---

## 🏃‍♂️ **Créer un quiz en 3 lignes**
Grâce au futur package `quiz` (disponible bientôt sur PyPI), voici comment créer et exécuter un quiz en seulement 3 lignes :

```python
from quizen.quiz import Quiz

questions = {"Quelle est la capitale de la France ?": ["Paris", "Londres", "Berlin", "Madrid"]}

Quiz(questions, player="Joueur").play()
```


## Utilisation 🚀

Une fois que vous avez installé `quizen`, vous pouvez commencer à l'utiliser pour créer et jouer à des quiz interactifs.

1. **Créer un fichier `questions.json`** avec vos questions et réponses. Exemple de fichier `questions.json` :

```json
{
  "Quelle est la capitale de la France ?": ["Paris", "Lyon", "Marseille", "Toulouse"],
  "Qui a écrit 'Les Misérables' ?": ["Victor Hugo", "Émile Zola", "Marcel Proust", "Molière"]
}
```

2. **Exécuter le quiz** dans votre script Python :
```python
from quizen.quiz import Quiz
from json import load

# Charger les questions depuis un fichier JSON
with open('data/questions.json', 'r', encoding='utf-8') as file:
    questions = load(file)

# Lancer le quiz
quiz = Quiz(questions, player="VotreNom")
quiz.play()
```

3. **Lancer le quiz depuis la ligne de commande** :

Vous pouvez également démarrer un quiz directement depuis votre terminal en utilisant la commande suivante (après avoir installé la bibliothèque) :

```bash
quizen
```

Cela exécutera le quiz en utilisant les questions définies dans le fichier `data/questions.json`.

---

## Fonctionnalités ✨

- **Création de quiz** : Utilisez un simple dictionnaire structuré pour créer vos questions et réponses.
- **Interface CLI** : Une interface en ligne de commande pour jouer au quiz.
- **Sauvegarde des résultats** : Les statistiques du joueur sont sauvegardées dans un fichier JSON.
- **Vie et score** : Gérez les vies et le score des joueurs au fur et à mesure du quiz.
- **Bonus de vie** : Un bonus de vie est accordé toutes les 5 réponses correctes consécutives.

---

## Exemple de code 📝

Voici un exemple complet pour démarrer un quiz avec `quizen` :

```python
from quizen.quiz import Quiz
from json import load

path = 'data/questions.json'

# Charger les questions depuis un fichier JSON
with open(path, 'r', encoding='utf-8') as file:
    questions = load(file)

# Lancer le quiz
quiz = Quiz(questions, player="CR7")
quiz.play()
```

---

## Contribuer 🤝

Si vous souhaitez contribuer à ce projet, vous pouvez faire un fork du repository, apporter vos modifications et soumettre une pull request. Pour installer le projet en mode développement, suivez les instructions ci-dessus.

---

## License 📝

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

### Notes supplémentaires 📝

- Vous devez avoir Python 3.7+ installé pour utiliser cette bibliothèque.
- Assurez-vous que le fichier `questions.json` se trouve à la racine du répertoire courant

