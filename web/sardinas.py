import statistics
import math
import pandas as pd # type: ignore
import joblib # type: ignore
import os

def get_cols():
  cols = ['num_zeros','avg_word_length', 'num_words','std_dev_word_length','max_word_length', 'entropy', 'min_word_length', 'num_state_changes']
  return cols

def compute_num_zeros(language):
  num_zeros = 0
  for word in language:
    num_zeros += word.count("0")
  return num_zeros

def compute_num_ones(language):
  num_ones = 0
  for word in language:
    num_ones += word.count("1")
  return num_ones

def compute_avg_word_length(language):
  total_word_length = 0
  for word in language:
    total_word_length += len(word)
  return total_word_length / len(language)

def compute_num_words(language):
  return len(language)

def compute_std_dev_word_length(language):
  word_lengths = [len(word) for word in language]
  if len(word_lengths) < 2:
    return 0
  else:
    return statistics.stdev(word_lengths)

def compute_max_word_length(language):
  word_lengths = [len(word) for word in language]
  return max(word_lengths)

def compute_entropy(language):
  probabilities = [len(word) / sum(len(word) for word in language) for word in language]
  entropy = 0
  for p in probabilities:
    if p > 0:
      entropy -= p * math.log2(p)
  return entropy

def compute_min_word_length(language):
  word_lengths = [len(word) for word in language]
  return min(word_lengths)

def compute_num_state_changes(language):
  current_state = 0
  num_state_changes = 0
  for word in language:
    for char in word:
      if char == "0":
        if current_state == 1:
          num_state_changes += 1
          current_state = 0
      else:
        if current_state == 0:
          num_state_changes += 1
          current_state = 1
  return num_state_changes

def compute_language_stats(language):
  return {
      "num_zeros": compute_num_zeros(language),
      # "num_ones": compute_num_ones(language),
      "avg_word_length": compute_avg_word_length(language),
      "num_words": compute_num_words(language),
      "std_dev_word_length": compute_std_dev_word_length(language),
      "max_word_length": compute_max_word_length(language),
      "entropy": compute_entropy(language),
      "min_word_length": compute_min_word_length(language),
      "num_state_changes": compute_num_state_changes(language),
  }

def predict_code(language, model = None, cols = get_cols()):
  if model == None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, 'sardinas_model.joblib')
    model = joblib.load(model_path)
  stats = compute_language_stats(language)
  X_new = pd.DataFrame([stats], columns=cols)
  prediction = model.predict(X_new)
  if prediction == 1:
    return True
  else:
    return False