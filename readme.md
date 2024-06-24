# Join Backend
Dieses Projekt stellt den Backend-Service für die Join-Anwendung dar. Es nutzt das Django REST Framework und bietet eine API zur Verwaltung und Bereitstellung von User, Tasks und Subtasks für die Join-Frontend-Anwendung.

## Inhaltsverzeichnis
- [Installation](#installation)
  - [Voraussetzungen](#voraussetzungen)
  - [Schritte zur Installation](#schritte-zur-installation)
- [Nutzungsanweisungen](#nutzungsanweisungen)
  - [API-Dokumentation](#api-dokumentation)
  - [API-Dokumentation](#api-dokumentation)
  - [API-endpunkte](#api-endpunkte)
  - [Tests](#tests)



## Installation
### Voraussetzungen
- Python 3.10.1+
- Django 5.0.4+
- Pip (Python Paket-Manager)
- Virtualenv (empfohlen)

### Schritte zur Installation
1. Repository klonen:
```
git clone https://github.com/coder-91/Join_Backend.git
cd Join_Backend
```

2. Virtuelle Umgebung erstellen und aktivieren:
```
python -m venv venv
venv\Scripts\activate
```

3. Abhängigkeiten installieren:
```
pip install -r requirements.txt
```

4. Datenbankmigrationen durchführen:
```
manage.py migrate --run-syncdb
```

5. Entwicklungsserver starten:
```
python manage.py runserver
```

Die API sollte jetzt unter http://127.0.0.1:8000/ erreichbar sein.


## Nutzungsanweisungen

### API-Dokumentation
Die API-Dokumentation kann unter http://127.0.0.1:8000/api/docs/ aufgerufen werden, nachdem der Entwicklungsserver gestartet wurde.

### API-Endpunkte
Die wichtigsten API-Endpunkte sind:
- `GET /api/users/`: Liste aller Benutzer
- `POST /api/users/register`: Neuen Benutzer erstellen
- `POST /api/users/token`: Benutzer-Token erstellen
- `GET /api/users/me`: Eigenes Benutzerprofil anzeigen

Weitere Endpunkte und deren Dokumentation sind unter http://127.0.0.1:8000/api/docs/ zu finden.

### Tests
Um die Testsuite auszuführen, verwenden Sie den folgenden Befehl:
```
python manage.py test
```
