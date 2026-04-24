# 📘 Guide de déploiement sur GitHub — MigChat

Ce document explique étape par étape comment le projet MigChat a été déployé sur GitHub,
et pourquoi certaines commandes trouvées sur GitHub ne fonctionnent pas toujours directement.

---

## 🧩 Pourquoi les commandes GitHub ne marchent pas toujours ?

Quand vous créez un dépôt sur GitHub, il vous propose ces commandes :

```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/username/repo.git
git push -u origin main
```

Ces commandes sont correctes **mais** elles échouent souvent pour ces raisons :

| Problème rencontré | Cause | Solution |
|--------------------|-------|----------|
| `fatal: not a git repository` | `git init` pas encore fait | Faire `git init` en premier |
| `error: remote origin already exists` | `git remote add` déjà exécuté une fois | Utiliser `git remote set-url origin URL` |
| Push bloqué / timeout | Authentification GitHub manquante | Utiliser un token d'accès personnel |
| `src refspec main does not match` | Pas de commit avant le push | Faire `git add .` puis `git commit` avant |
| Fichiers sensibles envoyés sur GitHub | Pas de `.gitignore` | Créer `.gitignore` AVANT `git add .` |

---

## ✅ Le processus complet qui a fonctionné

### Étape 1 — Vérifier l'état du projet

```bash
git status
```

**Résultat obtenu :**
```
fatal: not a git repository (or any of the parent directories): .git
```
➡️ Aucun dépôt Git n'existait. Il fallait tout initialiser depuis le début.

---

### Étape 2 — Créer le fichier `.gitignore` EN PREMIER

**Avant** de faire `git add .`, il est crucial de créer un `.gitignore` pour éviter
d'envoyer des fichiers sensibles ou inutiles sur GitHub.

Voici le `.gitignore` créé pour ce projet Django :

```
# Python
__pycache__/
*.py[cod]

# Virtual environments
venv/
env/
.venv/

# Django
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal
media/

# Secrets
.env
.env.*

# IDE
.vscode/
.idea/
```

> ⚠️ **Erreur fréquente** : faire `git add .` AVANT de créer `.gitignore` envoie
> la base de données (`db.sqlite3`), les mots de passe, et des fichiers inutiles sur GitHub.

---

### Étape 3 — Initialiser le dépôt Git

```bash
git init
```

**Résultat :**
```
Initialized empty Git repository in C:/Users/COMP2TECH/OneDrive/migchat/.git/
```

---

### Étape 4 — Configurer l'identité Git

```bash
git config user.email "votre@email.com"
git config user.name "VotreNom"
```

> Sans cette configuration, Git peut refuser de faire un commit.

---

### Étape 5 — Ajouter tous les fichiers

```bash
git add .
```

Vérifier ce qui sera commité :
```bash
git status
```

---

### Étape 6 — Faire le premier commit

```bash
git commit -m "Initial commit - MigChat Django application"
```

**Résultat obtenu :**
```
[master (root-commit) e9fa27c] Initial commit - MigChat Django application
 40 files changed, 1418 insertions(+)
```

> ⚠️ **Erreur fréquente** : essayer de faire `git push` SANS avoir fait de commit.
> Git n'a rien à envoyer si aucun commit n'existe → erreur `src refspec main does not match`.

---

### Étape 7 — Connecter le dépôt GitHub distant

```bash
git remote add origin https://github.com/yavski45/chat.git
```

Vérifier la connexion :
```bash
git remote -v
```

**Résultat :**
```
origin  https://github.com/yavski45/chat.git (fetch)
origin  https://github.com/yavski45/chat.git (push)
```

> ⚠️ **Erreur fréquente** : si vous avez déjà exécuté `git remote add origin` une fois,
> la deuxième fois donne l'erreur `error: remote origin already exists`.
> Dans ce cas, utilisez plutôt :
> ```bash
> git remote set-url origin https://github.com/yavski45/chat.git
> ```

---

### Étape 8 — Renommer la branche en `main` et pousser

```bash
git branch -M main
git push -u origin main
```

**Résultat obtenu :**
```
To https://github.com/yavski45/chat.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

> ℹ️ `git branch -M main` renomme la branche de `master` (ancien nom par défaut) à `main`
> (nouveau standard GitHub depuis 2020).
>
> ℹ️ `-u origin main` configure le tracking automatique : les prochains `git push`
> n'auront plus besoin de préciser `origin main`.

---

## 🔐 Authentification GitHub

GitHub n'accepte plus les mots de passe depuis août 2021.
Il faut utiliser un **token d'accès personnel (PAT)** :

1. Aller sur : https://github.com/settings/tokens
2. Cliquer **"Generate new token (classic)"**
3. Cocher la permission **`repo`**
4. Copier le token généré
5. Lors du `git push`, entrer votre **username** GitHub et coller le **token** comme mot de passe

Ou configurer l'URL avec le token directement (plus pratique) :
```bash
git remote set-url origin https://yavski45:VOTRE_TOKEN@github.com/yavski45/chat.git
git push -u origin main
```

---

## 🔄 Commandes pour les prochaines mises à jour

Après avoir modifié des fichiers, pour mettre à jour GitHub :

```bash
git add .
git commit -m "Description de vos modifications"
git push
```

---

## 📋 Résumé — Toutes les commandes dans l'ordre

```bash
# 1. Créer .gitignore (avec un éditeur de texte)

# 2. Initialiser Git
git init

# 3. Configurer l'identité
git config user.email "votre@email.com"
git config user.name "VotreNom"

# 4. Ajouter les fichiers
git add .

# 5. Vérifier ce qui sera envoyé
git status

# 6. Premier commit
git commit -m "Initial commit"

# 7. Connecter GitHub (créer le dépôt sur github.com d'abord !)
git remote add origin https://github.com/USERNAME/REPO.git

# 8. Pousser vers GitHub
git branch -M main
git push -u origin main
```

---

*Documentation générée lors du déploiement de MigChat — Avril 2026*
