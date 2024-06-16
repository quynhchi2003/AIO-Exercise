#Exercise 1
num_list = [3,4,5,1,-44,5,10,12,33,1]
k = 3
max_list = []
def sliding_window(elements, window_size):
    if window_size < 1:
        print('Window size must be >= 1')
        return
    if len(elements) <= window_size:
        return max_list.append(max(elements))
    for i in range(len(elements) - window_size + 1):
        window = elements[i:i+window_size]
        max_list.append(max(window))
    print(f'Output: {max_list}')

sliding_window(elements = num_list, window_size = k)    

#Exercise 2
string = input('Choose a word:')
def count_chars(word):
    char_count_dict = {}
    for i in word:
        if i in char_count_dict:
            char_count_dict[i] += 1
        else:
            char_count_dict[i] = 1
    print(char_count_dict)
count_chars(string)

#Exercise 3
#!gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
file_path = '/content/P1_data.txt'
with open (file_path, 'r') as f:
  documents = f.readlines()
def word_count(sentences):
  for sentence in sentences:
    sentence = sentence.lower().strip()
    words = sentence.split(' ')
    set_words = set(words)
    wcount = {}
    for word in set_words:
      if word in wcount:
        wcount[word] += 1
      else:
        wcount[word] = 1
    print(wcount)
  
#Exercise 4
def levenshtein_calc(source, target):
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