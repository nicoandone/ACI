# Analiza comparativa a metodelor de detectare si clasificare a elementelor structurale din documente
## Descriere
Proiectul urmareste dezvoltarea unei aplicatii pentru analiza automata a structurii vizuale a documentelor (Document Layout Analysis), utilizand metode de procesare a imaginilor si computer vision.

Scopul principal este identificarea si clasificarea elementelor structurale ale documentelor, precum titluri, paragrafe, coloane, tabele si imagini. Vor fi comparate doua abordari principale:

- Metode clasice: segmentarea documentului prin tehnici de procesare a imaginilor, analiza componentelor conexe si reguli geometrice pentru gruparea si clasificarea regiunilor.

- Metode moderne: utilizarea unor modele pretrained de computer vision pentru detectarea si clasificarea automata a elementelor structurale.

Rezultatele vor fi reprezentate printr-un format JSON structurat. Proiectul va fi orientat in principal catre documente tiparite, precum articole, rapoarte si pagini de carte, cu layout-uri simple sau moderate ca nivel de complexitate.

## Obiective
- Studierea tehnicilor clasice si moderne de Document Layout Analysis.
- Implementarea unei abordari clasice de segmentare a documentelor, utilizand procesarea imaginilor si reguli geometrice.
- Integrarea unui model pretrained pentru detectarea si clasificarea regiunilor structurale.
- Identificarea principalelor elemente vizuale ale documentelor si a pozitiilor acestora.
- Implementarea unei reprezentari JSON a structurii documentului.
- Compararea performantelor metodelor in functie de acuratete, timp de procesare si complexitatea layout-ului.
- Analiza situatiilor in care metodele produc rezultate incorecte, precum documentele cu mai multe coloane sau elemente grafice intercalate.
- Optional, dezvoltarea unei imbunatatiri a metodei clasice prin adaptarea regulilor de segmentare si grupare a regiunilor.

## Algoritmi si metode
### Preprocesarea imaginilor
Preprocesarea va avea rolul de a imbunatati calitatea imaginilor si de a facilita identificarea regiunilor structurale.

Pot fi utilizate urmatoarele tehnici:
- Conversia imaginilor in grayscale.
- Binarizarea globala folosind algoritmul Otsu.
- Binarizarea adaptiva pentru documente cu iluminare neuniforma.
- Filtrarea zgomotului cu filtre mediane sau gaussiene.
- Operatii morfologice, precum dilatarea, eroziunea si inchiderea morfologica.

### Abordarea clasica
Prima abordare va utiliza algoritmi traditionali de procesare a imaginilor pentru identificarea regiunilor documentului. Aceasta metoda va permite studierea modului in care algoritmii clasici pot reconstrui structura documentelor fara utilizarea unor modele neuronale.

Metodele propuse:
- Connected Component Analysis (CCA)
- Operatii morfologice
- Projection Profiles
- Analiza geometrica si reguli euristice

### Abordarea moderna
A doua abordare va utiliza un model pretrained de Document Layout Analysis, capabil sa identifice si sa clasifice direct regiunile structurale ale documentelor. Pot fi utilizate modele bazate pe arhitecturi de object detection, precum YOLO sau Faster R-CNN, antrenate pentru analiza documentelor. Nu se urmareste antrenarea unei retele neuronale de la zero, ci utilizarea si evaluarea unui model existent.

Pentru compararea corecta a celor doua abordari, va fi definit un set comun de categorii, precum:
- Titlu
- Bloc de text
- Imagine
- Tabel

### Analiza structurii spatiale si a coloanelor

Dupa detectarea regiunilor, vor fi analizate pozitiile relative ale acestora pentru identificarea organizarii generale a documentului. Vor putea fi utilizate:

- Sortarea regiunilor dupa coordonatele spatiale.
- Gruparea blocurilor pe baza alinierii si proximitatii.
- Identificarea spatiilor verticale dintre coloane
- Reguli geometrice pentru determinarea apartenentei blocurilor la o anumita coloana.

Aceste informatii vor fi folosite pentru reconstruirea ordinii de citire a regiunilor, pornind de la organizarea documentului in coloane si sectiuni.

## Metode de evaluare
Evaluarea va urmari atat performanta cantitativa a metodelor, cat si comportamentul acestora in situatii diferite.

### Acuratetea detectarii regiunilor

Vor fi utilizate metrici precum:
- Intersection over Union (IoU)
- Precision
- Recall
- F1-score

### Acuratetea clasificarii elementelor

Va fi analizata capacitatea metodelor de a diferentia tipurile de regiuni, precum titluri, paragrafe, imagini si tabele. Se pot utiliza matrici de confuzie si scoruri F1 calculate separat pentru fiecare clasa.

### Robustetea la structuri diferite

Metodele vor fi comparate pe categorii de documente:

- Documente cu o singura coloana.
- Documente cu doua coloane.
- Documente cu imagini si tabele intercalate.
- Documente cu structuri neuniforme.

### Timpul de procesare

Se va masura durata medie necesara procesarii unei imagini pentru fiecare abordare, utilizand aceleasi conditii hardware.

### Evaluarea ordinii de citire

Ordinea estimata a regiunilor va fi comparata cu o ordine de referinta. Se va putea utiliza proportia perechilor de regiuni ordonate corect pentru a evalua rezultatele.

### Analiza calitativa

Vor fi prezentate exemple reprezentative in care metodele functioneaza corect sau produc erori, insotite de explicatii privind posibilele cauze.

## Tehnologii propuse

- Python
- OpenCV
- NumPy
- PyTorch
- JSON
- Matplotlib / Pandas

## Posibile imbunatatiri proprii

- Dezvoltarea unor reguli adaptive pentru gruparea componentelor conexe in blocuri de text.
- Optimizarea parametrilor operatiilor morfologice in functie de dimensiunea si densitatea elementelor.
- Implementarea unui algoritm de detectare a coloanelor si reconstruire a ordinii de citire.
- Combinarea rezultatelor metodei clasice cu cele ale modelului pretrained, pentru reducerea detectarilor eronate.
- Analiza si adaptarea metodelor pentru anumite categorii de documente.
