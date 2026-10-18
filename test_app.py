import app as taskflow


def test_page_accueil():
    taskflow.taches.clear()

    client = taskflow.app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"TaskFlow" in response.data


def test_ajouter_tache():
    taskflow.taches.clear()

    client = taskflow.app.test_client()
    response = client.post(
        "/ajouter",
        data={"tache": "Reviser DevOps"},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Reviser DevOps" in response.data
    assert "Reviser DevOps" in taskflow.taches


def test_tache_vide():
    taskflow.taches.clear()

    client = taskflow.app.test_client()
    client.post(
        "/ajouter",
        data={"tache": "   "}
    )

    assert len(taskflow.taches) == 0