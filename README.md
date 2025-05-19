SmartAlgorithms/
├─ main.py
├─ algorithms/
│  ├─ __init__.py
│  ├─ kruskal.py
│  ├─ prim.py
│  ├─ dijkstra.py
│  ├─ bfs.py
│  └─ dfs.py
├─ assets/
│  └─ logo.png          # facultatif : votre illustration de thème
├─ requirements.txt
└─ README.md

-------------------------------------------------
## Installation locale

```bash
git clone https://github.com/<votre-utilisateur>/SmartAlgorithms.git
cd SmartAlgorithms
python -m venv venv && source venv/Scripts/activate
pip install -r requirements.txt
python main.py         # lance l’interface

-------------------------------------------------

pyinstaller --onefile --noconsole --icon=assets/logo.ico main.py


-------------------

**Résumé clair du projet “SmartAlgorithms” (application Python + Tkinter)**

* **But principal**

  * Application de bureau éducative permettant d’apprendre et de tester cinq algorithmes classiques de graphes : Kruskal, Prim, Dijkstra, BFS, DFS.
  * Interface graphique simple ; chaque algorithme présente : rappel théorique, code source, zone d’exécution avec saisie interactive.

* **Pile technologique**

  * **Python 3.12+** (langage unique).
  * **Tkinter / ttk** pour la GUI (inclus dans la distribution CPython).
  * **PyInstaller** (optionnel) pour générer un exécutable Windows “one-file”.
  * Aucune dépendance externe : pas de bases de données, pas de bibliothèques tierces.

* **Architecture & arborescence**

  * Dossier racine `SmartAlgorithms/`.
  * `main.py` : point d’entrée – crée la fenêtre principale, boutons et navigation.
  * Dossier `algorithms/` : un module Python par algorithme (`kruskal.py`, `prim.py`, etc.).

    * Chaque module contient :

      * Docstring explicative (théorie + étapes).
      * Fonctions utilitaires (find/union, etc.) et une fonction `main()` qui :

        1. Demande les paramètres utilisateur (nœuds, densité…).
        2. Exécute l’algorithme.
        3. Retourne un texte résumé (poids total, liste d’arêtes, chemin, etc.).
  * Dossier `assets/` (facultatif) : icône ou logo.
  * `requirements.txt` : uniquement `pyinstaller==6.5.0`.
  * `README.md` : instructions d’installation, exécution, build `.exe` et description pédagogique.

* **Fonctionnement de l’interface**

  * Fenêtre principale :

    * Titre : “Smart Algorithms”.
    * Label d’en-tête, puis cinq boutons (`ttk.Button`) – un par algorithme.
  * Clic sur un bouton → `open_algo()` :

    * Ouvre un `Toplevel` dédié.
    * Affiche la docstring dans un `ScrolledText` (lecture seule).
    * Bouton “Exécuter” appelle `run_algo()` :

      * Lance `module.main()` (interaction console via `input()` ou version plus GUI à terme).
      * Affiche le résultat dans un `messagebox`.

* **Style & thème**

  * Couleurs stockées dans dict `THEME` : arrière-plan sombre, texte clair, accent orange.
  * Widgets ttk : cohérence et compatibilité multi-OS (Windows, macOS, Linux).

* **Flux de développement typique**

  1. Cloner le repo, créer un venv ; **aucune installation** sauf PyInstaller si packaging.
  2. `python main.py` pour tester en développement.
  3. Modifier / enrichir algorithmes : changer la `docstring`, optimiser code, ajouter visualisation.
  4. (Optionnel) `pyinstaller --onefile --noconsole --icon=assets/logo.ico main.py` pour générer `dist/main.exe`.

* **Améliorations faciles**

  * Remplacer les `input()` dans chaque `main()` par des champs Tkinter (Entry, Spinbox) → exécution 100 % GUI.
  * Ajouter des visualisations pas à pas (Canvas, couleurs dynamiques).
  * Internationalisation, plus d’algorithmes ou de structures de données.
  * Thème clair/sombre commutable via `ttk.Style`.

* **Objectif pédagogique**

  * Projet semestriel à livrer : code propre, commentaires français, rapport PDF décrivant choix techniques et capture d’écran.
  * Noté sur : modularité, interface soignée, exécutable fonctionnel, explications théoriques.

> Ces points résument l’essentiel pour qu’un·e autre développeur·e ou modèle puisse reprendre, compléter ou refactoriser rapidement le projet.
