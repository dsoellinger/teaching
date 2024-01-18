# Assignment 2: Crowd Counting

In diesem Assignment soll ein CNN zur Personenzählung (d.h. eine Regressionsaufgabe) implementiert werden.

Grundlage hierfür bildet das [UCSD-Dataset](http://www.svcl.ucsd.edu/projects/peoplecnt/) welches Bilder von Überwachungsvideos von Bürgersteigen enthält. Pro Bild wird die Anzahl der gehenden Personen mitgeliefert. Weitere Einzelheiten finden sich in der Beschreibung des Datasets.

Ich werde Ihnen die Implementierung des `torch.utils.data.Dataset` zur Verfügung stellen, so dass Sie den vanilla `torch.utils.data.DataLoader` verwenden können. Ihre Aufgabe ist es, eine CNN-Architektur zu implementieren, mit der Sie die Zählaufgabe durchführen können. Zur Inspiration können Sie sich z.B. an der AlexNet-Implementierung orientieren.

Das Netz soll zunächst auf einem zufällig gewählten Teil der Daten trainiert und auf dem verbleibenden Teil getestet werden. Um die geschätzte Personenzahl mit der tatsächlichen Personenzahl zu vergleichen soll der mittlere quadratische Fehler (MSE) sowie der mittlere absolute Fehler bestimmt werden.


## Infos zur Abgabe
- Abgabe wieder wie zuletzt über Google Classroom als Jupyter Notebook


**Deadline:** 25. Februar 2024 (23:59)
 

