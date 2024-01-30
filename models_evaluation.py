# Upewnij się, że zainstalowane są wymagane biblioteki
#pip install transformers
#pip install rouge-score
#pip insatll sciki-learn
#pip install matplotlib
#pip install numpy

from transformers import pipeline
from sklearn.metrics import precision_recall_fscore_support
from rouge_score import rouge_scorer
import matplotlib.pyplot as plt
import numpy as np

# Inicjalizacja modeli
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
summarizer3 = pipeline("summarization", model="philschmid/bart-large-cnn-samsum")

# Funkcja do wczytywania tekstu z pliku
def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text
def evaluate_model_with_metrics(model, test_data):
    # Generowanie podsumowań dla danych testowych
    predictions = [model(item["text"], max_length=125, min_length=30, do_sample=False)[0]['summary_text'] for item in test_data]
    expected_summaries = [item["expected_summary"] for item in test_data]

    # Ocena modelu przy użyciu metryk precyzji, recall i F1
    y_true = [1 if len(summary) > 0 else 0 for summary in expected_summaries]
    y_pred = [1 if len(summary) > 0 else 0 for summary in predictions]

    precision, recall, f1, _ = precision_recall_fscore_support(y_true, y_pred, average='binary')

    # Obliczenie ROUGE Scores
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    rouge_scores = scorer.score(" ".join(expected_summaries), " ".join(predictions))

    # Wydruk wyników oceny modelu
    print("Model Evaluation Results:")
    for i, (pred, expected) in enumerate(zip(predictions, expected_summaries)):
        print(f"Example {i + 1}:")
        print(f"Predicted Summary: {pred}")
        print(f"Expected Summary: {expected}")
        print()

    # Wydruk ROUGE Scores
    print("ROUGE Scores:")
    for metric, score in rouge_scores.items():
        print(f"{metric}: {score}")

    return precision, recall, f1

def plot_metrics(model_names, precision_scores, recall_scores, f1_scores):
    width = 0.25
    ind = np.arange(len(model_names))

    # Wykres dla precyzji
    plt.bar(ind - width, precision_scores, width, label='Precision', alpha=0.7)

    # Wykres dla recall
    plt.bar(ind, recall_scores, width, label='Recall', alpha=0.7)

    # Wykres dla F1
    plt.bar(ind + width, f1_scores, width, label='F1', alpha=0.7)

    plt.xlabel('Models')
    plt.ylabel('Scores')
    plt.title('Metrics Comparison')
    plt.xticks(ind, model_names)
    plt.legend()

    plt.show()
# listy z wynikami metryk
model_names = ["Model 1", "Model 2", "Model 3"]
precision_scores = []
recall_scores = []
f1_scores = []

# Wczytanie danych testowych z pliku
all_data_text = read_text_from_file('all_data.txt')
article_summary_pairs = [pair.split('\n') for pair in all_data_text.split('\n\n') if pair]
test_data = [{"text": pair[0], "expected_summary": pair[1]} for pair in article_summary_pairs]

# Ocena Modelu 1
precision, recall, f1 = evaluate_model_with_metrics(summarizer, test_data)
precision_scores.append(precision)
recall_scores.append(recall)
f1_scores.append(f1)

# Ocena Modelu 2
precision, recall, f1 = evaluate_model_with_metrics(pipe, test_data)
precision_scores.append(precision)
recall_scores.append(recall)
f1_scores.append(f1)

# Ocena Modelu 3
precision, recall, f1 = evaluate_model_with_metrics(summarizer3, test_data)
precision_scores.append(precision)
recall_scores.append(recall)
f1_scores.append(f1)

# wykres
plot_metrics(model_names, precision_scores, recall_scores, f1_scores)