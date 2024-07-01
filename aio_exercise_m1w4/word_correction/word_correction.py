import streamlit as st

def levenshtein_distance(source, target):
  distances = [[0] * (len(target) + 1) for _ in range(len(source) + 1)]

  for i in range(len(target) + 1):
    distances[0][i] = i

  for j in range(len(source) + 1):
    distances[j][0] = j

  del_cost = 1
  ins_cost = 1
  for r in range(1, len(source) + 1):
    for c in range (1, len(target) + 1):
      if source[r - 1] == target[c - 1]:
        sub_cost = 0
      else:
        sub_cost = 1
      distances[r][c] = min(distances[r-1][c] + del_cost
                           , distances[r][c-1] + ins_cost
                           , distances[r-1][c-1] + sub_cost)
  return distances[len(source)][len(target)]

def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words
vocabs = load_vocab(file_path='word_correction./vocab.txt')

def main():
  st.title('Word Correction using Levenshtein Distance')
  word = st.text_input('Your Word:')

  if st.button('Compute'):
      distances = dict()
      for vocab in vocabs:
          distance = levenshtein_distance(word, vocab)
          distances[vocab] = distance
      sorted_distances = dict(sorted(distances.items(), key=lambda item: item[1]))
      correct_word = list(sorted_distances.keys())[0]
      st.write('Correct: ', correct_word)
      col1, col2 = st.columns(2)
      col1.write('Vocabulary:')
      col1.write(vocabs)

      col2.write('Distances:')
      col2.write(sorted_distances)

if __name__ == '__main__':
  main()

