# MigChat 💬

Une application de chat en temps réel construite avec Django et Django Channels.

## Fonctionnalités

- 🔐 Authentification des utilisateurs (inscription, connexion, déconnexion)
- 💬 Messagerie en temps réel via WebSockets
- 👤 Profils utilisateurs avec avatars
- 🔔 Notifications en temps réel

## Technologies utilisées

- **Backend** : Django 6.0, Django Channels 4.3, Daphne
- **Base de données** : SQLite (développement)
- **WebSockets** : Django Channels + Twisted
- **Frontend** : HTML, CSS, JavaScript

## Installation

### Prérequis

- Python 3.10+
- pip

### Étapes

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/VOTRE_USERNAME/migchat.git
   cd migchat
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Appliquer les migrations**
   ```bash
   python manage.py migrate
   ```

5. **Lancer le serveur**
   ```bash
   python manage.py runserver
   ```

6. Ouvrir [http://localhost:8000](http://localhost:8000) dans votre navigateur.

## Structure du projet

```
migchat/
├── accounts/        # Gestion des utilisateurs
├── chat/            # Application de chat
├── core/            # Configuration Django (settings, urls, asgi)
├── static/          # Fichiers statiques (CSS, JS)
├── templates/       # Templates HTML
├── manage.py
└── requirements.txt
```

## Licence

MIT
