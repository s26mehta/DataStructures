
TEST_INPUT = """
3
cat
hog
vault
crypt
oxy
ivy
30
aat
ace
ait
ane
cog
cot
her
hog
hot
ice
ick
icy
ink
ins
ire
ivy
joy
lag
mom
ohm
oms
one
ono
ons
ore
oxo
sen
sir
win
yan
"""


"""

dictonary = [cot, hog, cet, her,ice, cog]


start: cat

cat -> aat
cat -> cet
cet -> cog
cat -> caa cab cac

path = cat -> aat
path = 

q = [[cat, ], cet, ...]

cot
aat
cet
cog
hog

cat, hog


cat -> cot -> cog
cat -> hog [x]
cat -> cet
cat -> her [x]



1) process the input -> store dictionary in a set and create a dictionary to store pre-computed valid transformations for a word
        -> dictionary = set(), valid_tranformation = {}
        -> shortest_paths = []
2) Process pairs to find transformation sequence
      2a. For first word in pair:
                check if pre-computed transformations exists:
                    follow path of pre-comupted transformation
                else compute transformations for each letter and check if it exists in dictionary
                    follow that path with recursive call or BFS approach
                    add valid_transformations for future calls
3) return shortest_paths
      
output format:
2
cat,cot,cog,hog
cat,cot,hot,hog
0s


"""

from collections import deque 
import string
def find_shortest_paths():
    pairs, dicitonary = process_input()

    valid_tranformations = {}
    shortest_paths = []

    q = deque()

    for pair in pairs:
        shortest_path = []
        word_1, word_2 = pair

        q.append([word_1, [word_1]])

        while q:
            set_of_words = set(wordList)
        set_of_words.add(beginWord)
        all_letters = string.ascii_lowercase
        dict_words = {}

        if endWord not in set_of_words:
            return 0

        for word in set_of_words:
            if word not in dict_words:
                dict_words[word] = []
            idx = 0
            while idx < len(word):
                for letter in all_letters:
                    if word[idx] == letter:
                        continue
                    new_word = word[:idx] + letter + word[idx+1:]
                    if new_word in set_of_words:
                        dict_words[word].append(new_word)
                idx += 1

        q = deque()
        q.append([beginWord, [beginWord], set(beginWord)])
        while q:
            cur_word, cur_path, visited = q.pop()
            if cur_word in dict_words:
                for new_word in dict_words[cur_word]:
                    if new_word == endWord:
                        return cur_path + [new_word]
                    if new_word not in visited:
                        new_path = cur_path.copy()
                        new_path.append(new_word)
                        new_visited = visited.copy()
                        new_visited.add(new_word)
                        q.appendleft([new_word, new_path, new_visited])
        return []


    
'''
2 (number of pairs)
cat
hog
vault
crypt
30 (len of dictionary)
aat
ace
'''


def process_input():
    global TEST_INPUT
    # Sanitize TEST_INPUT for errant whitespace
    TEST_INPUT = [line.strip() for line in TEST_INPUT.split('\n') if line]
    
    number_of_pairs = int(TEST_INPUT[0])
    pairs = []
    
    idx = 1
    while idx < number_of_pairs*2:
        pair = [TEST_INPUT[idx], TEST_INPUT[idx+1]]
        pairs.append(pair)

        idx = idx + 2

    dictionary = set(TEST_INPUT[number_of_pairs*2+1:])
    return pairs, dictionary

        
find_shortest_paths()