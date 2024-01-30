# NAI Projekt - Porównanie Efektywności Modeli Podsumowywania Tekstu

## Początkowe Informacje
Projekt korzysta z biblioteki transformers do pracy z modelami podsumowującymi tekst.
Wykorzystuje metryki ROUGE (Recall-Oriented Understudy for Gisting Evaluation) do oceny efektywności generowanych podsumowań.
W pliku all_data.txt znajdują się zestawy testowe do oceny modeli.

Autor
Nikodem Kunach
s25030@pjwstk.edu.pl

## Opis Projektu
Projekt skupia się na porównaniu efektywności trzech różnych modeli podsumowywania tekstu: "facebook/bart-large-cnn", "sshleifer/distilbart-cnn-12-6", i "philschmid/bart-large-cnn-samsum". Celem jest zrozumienie, który z tych modeli generuje najbardziej sensowne podsumowania tekstu na podstawie różnorodnych przypadków testowych.

## Opis Modeli

facebook/bart-large-cnn:
BART (Bidirectional and Auto-Regressive Transformers): To model bazujący na architekturze transformer, opracowany przez Facebook AI. BART łączy w sobie mechanizmy auto-regresyjne (umożliwiające generowanie tekstu w kierunku od lewej do prawej) oraz bidirekcyjne (zdolność rozumienia kontekstu zarówno przed, jak i po danym punkcie w tekście). Działa na zasadzie dekodera, czyli generuje tekst na podstawie danego kontekstu.

sshleifer/distilbart-cnn-12-6:
DistilBART (Distilled BART): To zoptymalizowana i mniejsza wersja modelu BART, stworzona do wydajniejszego przetwarzania. DistilBART jest bardziej "przepuszczalny" od pełnowymiarowego BART, co oznacza, że zajmuje mniej zasobów, ale zachowuje przyzwoitą zdolność do generowania tekstu. Wersja "cnn-12-6" sugeruje, że model ten był trenowany z użyciem danych związanych z nagłówkami i artykułami z serwisu CNN, co może wpłynąć na jego zdolność do podsumowywania tekstu z tego źródła.

philschmid/bart-large-cnn-samsum:
BART-Large-CNN-Samsum: To kolejna wersja BART, jednak dostosowana specjalnie do generowania podsumowań w kontekście zadań związanych z treściami internetowymi. Samsum odnosi się do zastosowania modelu do zbioru danych zawierającego podsumowania samouczące się ze stron internetowych. Model ten jest szkolony na dużym zbiorze danych tekstowych, co może wpłynąć na jego zdolność do generowania podsumowań zróżnicowanych treści.

Wszystkie te modele są przykłady tzw. modeli językowych opartych na transformerach. Transformer to nowoczesna architektura sieci neuronowej, która wykazuje doskonałą skuteczność w zadaniach przetwarzania języka naturalnego. Modele bazujące na transformerach są zdolne do rozumienia kontekstu w dużych ilościach tekstu i generowania odpowiedzi lub podsumowań. Szkolenie tych modeli wymaga ogromnych zbiorów danych oraz dużych zasobów obliczeniowych, ale rezultaty są imponujące, umożliwiając generowanie wysokiej jakości podsumowań tekstowych.

## Struktura Projektu
- `models_evaluation.py`: Skrypt Pythona zawierający kod do oceny modeli oraz generowania porównawczych wykresów metryk.
- `all_data.txt`: Plik zawierający zestawy testowe, gdzie każdy zestaw składa się z tekstu do podsumowania i oczekiwanego podsumowania.
- `README.md`: Ten plik, zawierający opis projektu, jego struktury i sposób użycia.

## Instrukcja Użycia
1. Uruchom skrypt `models_evaluation.py` w środowisku Pythona 3.x, które obsługuje wymagane biblioteki.
2. Poczekaj na zakończenie oceny modeli oraz generowanie wykresów metryk.
3. Zweryfikuj wyniki oceny modeli oraz przeanalizuj porównawcze wykresy metryk.

## Wymagania
- Python 3.x
- Biblioteki: transformers, rouge-score, scikit-learn, matplotlib, numpy

Aby zainstalować wymagane biblioteki, użyj poniższej komendy w terminalu:
pip install transformers rouge-score scikit-learn matplotlib numpy

## Wyniki Oceny Modeli
Wyniki porównania trzech modeli na podstawie 44 opowiadań i ich streszczeń (opowiadania od 100-500 słów około, streszczenia od 30-130 słów) przy użyciu metryk ROUGE (Recall-Oriented Understudy for Gisting Evaluation) dają ciekawy obraz efektywności tych modeli w zadaniu podsumowywania tekstu.

Model 1: facebook/bart-large-cnn
ROUGE-1: Precision: 0.82, Recall: 0.43, F-measure: 0.57
ROUGE-2: Precision: 0.40, Recall: 0.21, F-measure: 0.27
ROUGE-L: Precision: 0.45, Recall: 0.24, F-measure: 0.31
Model 2: sshleifer/distilbart-cnn-12-6
ROUGE-1: Precision: 0.80, Recall: 0.47, F-measure: 0.59
ROUGE-2: Precision: 0.36, Recall: 0.21, F-measure: 0.27
ROUGE-L: Precision: 0.42, Recall: 0.24, F-measure: 0.31
Model 3: philschmid/bart-large-cnn-samsum
ROUGE-1: Precision: 0.80, Recall: 0.56, F-measure: 0.66
ROUGE-2: Precision: 0.38, Recall: 0.26, F-measure: 0.31
ROUGE-L: Precision: 0.43, Recall: 0.30, F-measure: 0.35


## Analiza Wyników

Rouge (Recall-Oriented Understudy for Gisting Evaluation) to zestaw metryk oceny jakości podsumowań tekstu, często stosowany w zadaniach przetwarzania języka naturalnego. Składa się z trzech głównych miar: Rouge-1, Rouge-2 i Rouge-L, z których każda mierzy różne aspekty podobieństwa pomiędzy referencyjnym (oczekiwanym) podsumowaniem a generowanym podsumowaniem.

Rouge-1:

Mierzy podobieństwo jednoelementowych n-gramów (pojedynczych słów) pomiędzy referencyjnym a generowanym tekstem. Zawiera metryki precyzji, recall i F1-score.

Rouge-2:

Mierzy podobieństwo dwuelementowych n-gramów (dwóch kolejnych słów) pomiędzy referencyjnym a generowanym tekstem. Podobnie jak Rouge-1, zawiera precyzję, recall i F1-score.

Rouge-L:

Mierzy długość wspólnego najdłuższego podciągu (LCS - Longest Common Subsequence) pomiędzy referencyjnym a generowanym tekstem. Skupia się na zachowaniu sekwencji słów. Zawiera precyzję, recall i F1-score.

Wyniki porównania trzech modeli na podstawie 44 opowiadań i ich streszczeń (opowiadania od 100-500 słów około, streszczenia od 30-130 słów) przy użyciu metryk ROUGE (Recall-Oriented Understudy for Gisting Evaluation) dają ciekawy obraz efektywności tych modeli w zadaniu podsumowywania tekstu. Poniżej przedstawiam analizę wyników.


## Opis Modeli

facebook/bart-large-cnn
Najwyższa precyzja, skupiony na wydobywaniu istotnych informacji, mniejszy zakres ogólnego kontekstu. Wyższa precyzja i recall niż Model 2.

sshleifer/distilbart-cnn-12-6
Mniejsza precyzja i recall niż Model 1, sugeruje mniejszą skuteczność w generowaniu sensownych podsumowań tekstu. Potencjalnie bardziej zbalansowany, ale niższe wartości ROUGE. Niższy f-measure.

philschmid/bart-large-cnn-samsum
Najwyższe wartości recall i f-measure, efektywny w wydobywaniu informacji i utrzymaniu ogólnego kontekstu. Precyzja nieco niższa niż w Modelu 1, ale ogólna jakość podsumowań wyższa.

## Metryki Oceny Jakości Podsumowań
Precyzja (Precision): Stosunek TP do TP+FP. Mierzy, ile spośród przewidzianych podsumowań jest rzeczywiście poprawnych.
Recall (Czułość): Stosunek TP do TP+FN. Określa, ile z rzeczywiście istniejących podsumowań zostało poprawnie przewidziane.
F1 Score: Średnia harmoniczna precyzji i recall. Zrównoważona ocena między precyzją a czułością.

## Interpretacja Wyników
Model 1 ma najwyższą precyzję, niższy recall i f-measure niż Model 3. Bardziej skupiony na wydobywaniu istotnych informacji.
Model 2 jest mniej skuteczny niż Model 1, z niższymi wartościami wszystkich trzech metryk.
Model 3 osiąga najwyższe wartości recall i f-measure, co sugeruje efektywność w generowaniu sensownych podsumowań.

## Wnioski
Model 3 zdaje się osiągać najlepsze wyniki na podstawie metryk ROUGE, co sugeruje, że może być bardziej efektywny w generowaniu sensownych podsumowań tekstu.
Wyniki stabilizują się przy większej ilości danych testowych, co może pomóc w uzyskaniu bardziej wiarygodnych wyników.
Wybór najlepszego modelu zależy od konkretnej aplikacji i preferencji między precyzją a recall.
Uwagi końcowe
Analiza wyników pozwala lepiej zrozumieć mocne i słabe strony poszczególnych modeli, co może pomóc w dalszym doskonaleniu aplikacji podsumowującej tekst. Warto również uwzględnić indywidualne potrzeby i kontekst zastosowania w wyborze optymalnego modelu do konkretnego zadania.

## Upewnij się, że ścieżki do plików i wszelkie inne parametry są dostosowane do Twojej struktury katalogów i danych.
