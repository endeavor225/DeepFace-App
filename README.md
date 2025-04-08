# 🔍 DeepFace Face Verification App

Cette application permet de comparer une image cible avec une série d'images pour détecter s'il y a une correspondance faciale (reconnaissance de visage) à l'aide de la bibliothèque **DeepFace**.

Construite avec **Python**, **Streamlit** pour l'interface web, et **Pipenv** pour la gestion de l'environnement.

---

## 📸 Fonctionnalités

- ✅ Upload d'une image cible
- 📁 Upload de plusieurs images à comparer
- 🧠 Détection faciale avec DeepFace
- 🖥️ Interface web intuitive avec Streamlit

---

## 🚀 Démarrage rapide

### 1. Cloner le projet

```bash
git clone https://github.com/ton-utilisateur/deepface-app.git
cd deepface-app
```

### 2. Installer les dépendances avec pipenv

#### a. Installer pipenv (si nécessaire)

```bash
pip install pipenv
# ou sous Ubuntu
sudo apt install pipenv
```

#### b. Créer l'environnement virtuel et l'activer

```bash
pipenv --python 3.10
pipenv shell
```

#### c. Installer les dépendances

```bash
pipenv install deepface opencv-python streamlit

```

### 3. Lancer l'application

```bash
streamlit run app.py
```

🗂️ Arborescence du projet

```bash
deepface-app/
├── Pipfile
├── Pipfile.lock
├── app.py
└── README.md
```

🛠️ Technologies utilisées

- Python 3.10+
- DeepFace
- OpenCV
- Streamlit
- Pipenv

📌 Remarques

- L'application utilise le modèle par défaut de DeepFace pour la vérification.
- Pour des performances optimales, tu peux utiliser un GPU avec TensorFlow.
- Tu peux modifier le modèle (Facenet, VGG-Face, etc.) et le détecteur (retinaface, mtcnn, etc.) dans le code si besoin.
