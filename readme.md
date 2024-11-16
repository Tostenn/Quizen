

# Quizen  

🎉 **Quizen** is an interactive console application designed to simplify the creation of **Quiz Games**. With a well-structured dictionary, you can set up a quiz in just **3 lines of code**!  

🚀 Aimed at both beginners and advanced developers, Quizen offers an intuitive way to integrate educational and entertaining quizzes into your Python projects.  

![PyPI](https://img.shields.io/pypi/v/quizen)
![Python](https://img.shields.io/pypi/pyversions/quizen)
![License](https://img.shields.io/pypi/l/quizen)
![PyPI - Downloads](https://img.shields.io/pypi/dm/quizen)

---

## ⚙️ **Features**  

- 🧩 **Customizable**: Easily create questions and answers using dictionaries.  
- 🎯 **Engaging Gameplay**: Automatic handling of scores, lives, and consecutive correct answers.  
- 💾 **Data Persistence**: Player statistics are saved to a file for review.  
- 🔀 **Shuffling**: Randomize questions and answers to keep things fresh.  

---

## 📦 **Installation**  

Install the latest version of **Quizen** from PyPI:  
```bash  
pip install quizen  
```  

---

## 🛠 **How to Use**  

Using **Quizen** is as simple as this:  

### Step 1: Create your questions  

Prepare your questions in a JSON file or Python dictionary. For example:  
```json  
{
    "What is the capital of France?": ["Paris", "London", "Berlin", "Madrid"],
    "Who developed Python?": ["Guido van Rossum", "Dennis Ritchie", "James Gosling", "Bjarne Stroustrup"]
}
```  

### Step 2: Launch your quiz  

Here's a complete example to start a quiz:  
```python  
from quizen import Quiz  
from json import load  

path = "data/questions.json"  

with open(path, "r", encoding="utf-8") as file:  
    questions = load(file)  

Quiz(questions, player="John").play()  
```  

---

## 📊 **Statistics**  

At the end of each game, Quizen displays and saves player statistics, including:  
- **Questions answered**  
- **Correct answers**  
- **Wrong answers**  
- **Score**  
- **Longest streak of correct answers**  
- **Remaining lives**  

---

## 🛡 **Dependencies**  

Quizen depends on the following libraries:  
- [**rich**](https://github.com/Textualize/rich): For beautiful console output.  

Install all dependencies automatically with:  
```bash  
pip install quizen  
```  

---

## 🏆 **Contributing**  

We welcome contributions! Here's how you can help:  
1. **Report bugs**: Found a bug? Let us know by opening an issue.  
2. **Suggest improvements**: Have ideas for new features? Share them on GitHub.  
3. **Submit pull requests**: Fix a bug or implement a feature and submit your PR.  

Start by cloning the repository:  
```bash  
git clone https://github.com/Tostenn/Quizen.git  
cd quizen  
```  

---

## 📣 **Get in Touch**  

Your feedback is invaluable! If you encounter issues, have suggestions, or want to contribute, feel free to:  
- **Open an issue** on GitHub.  
- **Contact me directly** through my [GitHub profile](https://github.com/Tostenn).  

Let’s make **Quizen** the ultimate tool for interactive quizzes!  


---

Enjoy using **Quizen** and happy coding! 😊
