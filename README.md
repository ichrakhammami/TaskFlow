
# TaskFlow

TaskFlow est une application web simple de gestion des tâches développée avec Flask. Ce projet a pour objectif de mettre en pratique les concepts DevOps, notamment les tests automatisés, l'intégration continue et la vérification de sécurité des dépendances.

## Objectifs du projet

- Développer une application web avec Flask.
- Automatiser les tests avec pytest.
- Mettre en place un pipeline CI avec GitHub Actions.
- Vérifier les vulnérabilités connues des dépendances avec pip-audit.

## Technologies utilisées

- Python 3.13
- Flask
- pytest
- Git et GitHub
- GitHub Actions
- pip-audit

## Fonctionnalités

- Afficher la page d'accueil.
- Ajouter une tâche.
- Vérifier le comportement de l'application avec des tests automatisés.

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/ichrakhammami/TaskFlow.git
cd TaskFlow
```

### 2. Créer un environnement virtuel

Sous Windows avec PowerShell :

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Installer les dépendances

```bash
python -m pip install -r requirements.txt
```

## Lancer l'application

```bash
python app.py
```

Ouvre ensuite l'adresse locale affichée dans le terminal, généralement http://127.0.0.1:5000.

## Tests automatisés

Pour exécuter les tests :

```bash
python -m pytest -v
```

Les tests vérifient la page d'accueil, l'ajout d'une tâche et le comportement en cas de tâche vide.

## Vérification de sécurité

Pour lancer l'audit des dépendances :

```bash
python -m pip_audit
```

## Intégration continue

Le workflow GitHub Actions est défini dans `.github/workflows/ci.yml`.

Il s'exécute lors d'un `push` ou d'une `pull request` vers la branche `main`. Il installe les dépendances, exécute les tests automatisés et vérifie les vulnérabilités connues des dépendances.

