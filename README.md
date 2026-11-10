# Analiza comparativa a metodelor de detectare si clasificare a elementelor structurale din documente
## Descriere
Proiectul urmareste dezvoltarea unei aplicatii pentru analiza automata a structurii vizuale a documentelor (Document Layout Analysis), utilizand metode de procesare a imaginilor si computer vision.

Scopul principal este identificarea si clasificarea elementelor structurale ale documentelor, precum titluri, paragrafe, coloane, tabele si imagini. Vor fi comparate doua abordari principale:

- Metode clasice: segmentarea documentului prin tehnici de procesare a imaginilor, analiza componentelor conexe si reguli geometrice pentru gruparea si clasificarea regiunilor.

- Metode moderne: utilizarea unor modele pretrained de computer vision pentru detectarea si clasificarea automata a elementelor structurale.

Rezultatele vor fi reprezentate printr-un [format JSON structurat](output_example.json), care va contine numele imaginii, dimensiunile acesteia, iar, pentru fiecare sectiune identificata, identificatorul regiunii, clasa acesteia si pozitia bounding box-ului regiunii care va fi afisat pe imagine.

Proiectul va fi orientat in principal catre documente tiparite, precum articole, rapoarte si pagini de carte, cu layout-uri simple sau moderate ca nivel de complexitate.

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
### Set de date
#### Alegerea datasetului: Datasetul PubLayNet
[Datasetul PubLayNet](https://huggingface.co/datasets/jordanparker6/publaynet) contine imagini reprezentand documente anotate pentru analiza layout-ului documentelor.

### Preprocesarea imaginilor
Preprocesarea va avea rolul de a imbunatati calitatea imaginilor si de a facilita identificarea regiunilor structurale.

Vor fi utilizate urmatoarele tehnici, in aceasta ordine:
- Conversia imaginilor in grayscale.
- Filtrarea zgomotului cu filtre mediane sau gaussiene.
- Binarizarea globala folosind algoritmul [Otsu](https://learnopencv.com/otsu-thresholding-with-opencv/).
- [Operatii morfologice](https://docs.opencv.org/4.13.0/d9/d61/tutorial_py_morphological_ops.html), precum dilatarea, eroziunea, deschiderea sau inchiderea morfologica, pentru eliminarea zgomotului.

### Abordarea clasica
Prima abordare va utiliza algoritmi traditionali de procesare a imaginilor pentru identificarea regiunilor documentului. Aceasta metoda va permite studierea modului in care algoritmii clasici pot reconstrui structura documentelor fara utilizarea unor modele neuronale, si care metoda este cea mai performanta pentru diferite tipuri de documente.

Metodele propuse:
- operatii morfologice, cu scopul de a grupa pixelii in blocuri (dilatare/inchidere): [Run-length Smoothing Algorithm](https://mirrors.meulie.net/bitsavers.org/pdf/ibm/IBM_Journal_of_Research_and_Development/266/ibmrd2606B.pdf)
- [Connected Component Analysis (CCA)](https://datacarpentry.github.io/image-processing/08-connected-components.html): bottom-up
- Projection Profiles: top-down
- Analiza geometrica si reguli euristice pentru identificarea claselor.

### Abordarea moderna
A doua abordare va utiliza un model pretrained de Document Layout Analysis, capabil sa identifice si sa clasifice direct regiunile structurale ale documentelor. Pot fi utilizate modele bazate pe arhitecturi de object detection, precum [YOLO](https://github.com/opendatalab/DocLayout-YOLO), antrenate pentru analiza documentelor. Nu se urmareste antrenarea unei retele neuronale de la zero, ci utilizarea si evaluarea unui model existent.

Pentru compararea corecta a celor doua abordari, va fi definit un set comun de categorii, precum cele folosite in datasetul PubLayNet:
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

Va fi analizata capacitatea metodelor de a diferentia tipurile de regiuni, precum titluri, paragrafe, imagini si tabele. Se vor utiliza matrici de confuzie si scoruri F1 calculate separat pentru fiecare clasa.

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

## Dependente
- datasets
- pillow
- opencv-python
- pyyaml

## Posibile imbunatatiri proprii

- Imbunatatirea pipeline-ului pentru date cu o calitate mai joasa
- Dezvoltarea unor reguli adaptive pentru gruparea componentelor conexe in blocuri de text.
- Optimizarea parametrilor operatiilor morfologice in functie de dimensiunea si densitatea elementelor.
- Implementarea unui algoritm de detectare a coloanelor si reconstruire a ordinii de citire.
- Combinarea rezultatelor metodei clasice cu cele ale modelului pretrained, pentru reducerea detectarilor eronate.
- Analiza si adaptarea metodelor pentru anumite categorii de documente.

## Bibliografie:
- BinMakhashen, G. M., & Mahmoud, S. A. (2019). Document layout analysis: A comprehensive survey. *ACM Computing Surveys*, *52*(6), Article 109. [https://dl.acm.org/doi/fullHtml/10.1145/3355610](https://dl.acm.org/doi/fullHtml/10.1145/3355610)
- Data Carpentry. (n.d.). *Connected component analysis*. In *Image processing with Python*. [https://datacarpentry.github.io/image-processing/08-connected-components.html](https://datacarpentry.github.io/image-processing/08-connected-components.html)
- Fisher, J. L., Hinds, S. C., & D'Amato, D. P. (1990). A rule-based system for document image segmentation. In *Proceedings of the 10th International Conference on Pattern Recognition* (pp. 567–572). IEEE. [https://www.scribd.com/document/725795681/a-rulebased-system-for-document-image-segmentation](https://www.scribd.com/document/725795681/a-rulebased-system-for-document-image-segmentation)
- Ha, J., Haralick, R. M., & Phillips, I. T. (1995). Recursive X-Y cut using bounding boxes of connected components. In *Proceedings of the Third International Conference on Document Analysis and Recognition* (pp. 952–955). IEEE. [https://www.haralick.org/conferences/71280952.pdf](https://www.haralick.org/conferences/71280952.pdf)
- jordanparker6. (n.d.). *PubLayNet* [Data set]. Hugging Face. [https://huggingface.co/datasets/jordanparker6/publaynet](https://huggingface.co/datasets/jordanparker6/publaynet)
- LearnOpenCV. (n.d.). *Otsu's thresholding with OpenCV*. [https://learnopencv.com/otsu-thresholding-with-opencv/](https://learnopencv.com/otsu-thresholding-with-opencv/)
- OpenCV. (n.d.). *Morphological transformations* (Version 4.13.0) [Documentation]. [https://docs.opencv.org/4.13.0/d9/d61/tutorial_py_morphological_ops.html](https://docs.opencv.org/4.13.0/d9/d61/tutorial_py_morphological_ops.html)
- OpenDataLab. (n.d.). *DocLayout-YOLO* [Computer software]. GitHub. [https://github.com/opendatalab/DocLayout-YOLO](https://github.com/opendatalab/DocLayout-YOLO)
- Rosenfeld, A., & Pfaltz, J. L. (1966). Sequential operations in digital picture processing. *Journal of the ACM*, *13*(4), 471–494. [https://www.cs.virginia.edu/~jlp/66.sequential.op.pdf](https://www.cs.virginia.edu/~jlp/66.sequential.op.pdf)
- Wong, K. Y., Casey, R. G., & Wahl, F. M. (1982). Document analysis system. *IBM Journal of Research and Development*, *26*(6), 647–656. [https://mirrors.meulie.net/bitsavers.org/pdf/ibm/IBM_Journal_of_Research_and_Development/266/ibmrd2606B.pdf](https://mirrors.meulie.net/bitsavers.org/pdf/ibm/IBM_Journal_of_Research_and_Development/266/ibmrd2606B.pdf)
- Zhong, X., Tang, J., & Jimeno Yepes, A. (2019). PubLayNet: Largest dataset ever for document layout analysis. In *2019 International Conference on Document Analysis and Recognition (ICDAR)* (pp. 1015–1022). IEEE. [https://doi.org/10.1109/ICDAR.2019.00166](https://doi.org/10.1109/ICDAR.2019.00166)


## Sprint 1 note
### Preprocesare
- optiuni de noise filtering: median, gaussian, none.
- optiuni de noise filtering prin operatii morfologice: opening, line_opening, none. Metoda de line opening aplica doua operatii de opening separate pe aceeasi imagine binara, una cu un kernel orizontal si una cu un kernel vertical, apoi combina rezultatele prin bitwise-or. Aceasta metoda a fost introdusa deoarece metoda de opening cu un kernel patrat s-a dovedit a fi prea agresiva.
- va fi evaluata acuratetea cu vs fara noise filtering
- asteptarile sunt ca noise filtering nu va imbunatati acuratetea pentru acest dataset, deoarece imaginile au deja o calitate inalta.
- valorile parametrilor folositi in noise filtering depind de marimea textului
