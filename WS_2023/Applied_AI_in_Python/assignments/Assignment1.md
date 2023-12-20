# Assignment 1: Titanic - Machine Learning from Disaster

Folgende Aufgabenstellung soll einzeln oder in 2er-Gruppe bearbeitet werden: https://www.kaggle.com/competitions/titanic

Das bereitgestellte Datenset (siehe Link) liefert eine Passagierliste mit div. Zusatzinformationen (Geschlecht, Alter, sozioökonomoscher Status, etc.) von Personen, welche am 15. April 1912 im Zuge der Kollision der Titanic mit einem Eisberg ums Leben kamen. Es soll durch eine explorative Datenanalyse (EDA) und Training eines ML-Modells festgestellt werden, ob bestimmte Personengruppen eine höhere Überlebenschance besitzen bzw. deren Überlebenschance vorhergesagt werden.

## Teil 1 - Explorative Datenanalyse

Analysieren sie das Datenset mit Hilfe von Pandas, Matplotlib, Seaborn wie wir es in der VO gemacht haben.
Ziel der Analyse ist die Beantwortung der Frage welche Faktoren maßgeblich für ein Überleben des Titanic Unglücks waren.

Um diese Frage zu beantworten könnten bspw. folgende Aspekte interessant sein?

- Wie viele Passagiere waren an Board? Wie groß ist der Anteil der Personen welche überlebt haben?
- Gibt es eine Korrelation (und ggf. kausalen Zusammenhang) zwischen der Überlebenschance und Eigenschaften wie Alter, Geschlecht, etc.?
- Welchen Einfluss hatten Faktoren wie die Reiseklasse, Familiengröße, der Einschiffungszeitpunkt, usw.?
- Welche Kombination von Eigenschaften besaß die höchste Überlebenschance?


## Teil 2 - Training und Evaluation 

Trainieren sie mind. 3 ML-Modellen (bspw. jene aus der VO). Die optimalen Hyperparameter sollen mittels k-Fold Cross-Validation und einer "Grid Search" bestimmt werden.
- Welches Modell erzielt die beste Vorhersagegenauigkeit? 
- Was sind die aus der Sicht des Modells relevanten Features und deckt sich dies mit der zuvor durchgeführten Analyse? (*) 

(*) Diese Frage ist für alle tree-basierten Verfahren (Decision Trees, Random Forests, usw.) leicht zu beantworten. 


## Infos zur Abgabe
Abgabeformat ist ein Jupyter-Notebook. Bitte das Jupyter-Notebook unbedingt im **ausgeführten Zustand**, so dass die Ergebnisse und Plots unmittelbar sichtbar sind und das Notebook nicht
erst ausgeführt werden muss! Die Abgabe erfolgt über Gitlab Classroom (Details folgen).

**Deadline:** 10. Jänner 2024 (23:59)
 

