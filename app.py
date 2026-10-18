from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Liste des tâches
taches = []

# Page principale
@app.route("/")
def accueil():
    page = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>TaskFlow</title>
        <style>
            body {
                font-family: Arial;
                max-width: 700px;
                margin: 50px auto;
                background: #f2f5f9;
            }
            h1 { color: #2457a7; }
            form, li {
                background: white;
                padding: 15px;
                margin: 10px 0;
                border-radius: 8px;
            }
            input, button {
                padding: 10px;
            }
            button {
                background: #2457a7;
                color: white;
                border: none;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h1>TaskFlow — Gestion des tâches</h1>

        <form action="/ajouter" method="POST">
            <input name="tache" placeholder="Nouvelle tâche" required>
            <button type="submit">Ajouter</button>
        </form>

        <h2>Mes tâches</h2>
        <ul>
            {% for tache in taches %}
                <li>{{ tache }}</li>
            {% else %}
                <li>Aucune tâche pour le moment.</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """
    return render_template_string(page, taches=taches)


# Ajouter une tâche
@app.route("/ajouter", methods=["POST"])
def ajouter():
    tache = request.form.get("tache", "").strip()

    if tache:
        taches.append(tache)

    return redirect(url_for("accueil"))


# Démarrer le serveur
if __name__ == "__main__":
    app.run(debug=True)