import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-file', default="sample_input.txt")

args = parser.parse_args()

class Solution:
  def __init__(self):
    self.dictionary = []

  def read_file(self, filePath):
    with open(str(filePath)) as f:
      lines = f.readlines()
    lines = [x.strip() for x in lines]

    return lines


  def validate_constraints(self, num_dict_words, num_process_words, num_lines):
    if num_dict_words <= 0 or num_dict_words >= 20000:
      raise Exception('Number of words for input dictionary is not within constraints of 0 < N < 20000, its %s' % num_dict_words)

    if num_process_words <= 0 or num_process_words >= 1000:
      raise Exception('Number of words for processing is not within constraints of 0 < M < 1000, its %s' % num_process_words)

    if num_lines != num_dict_words+num_process_words+2:
      raise Exception('Invalid input')


  def process_input(self, filePath):
    # Get lines of input
    lines = self.read_file(filePath)

    # Classify inputs
    num_dict_words = int(lines[0])
    num_process_words = int(lines[1])
    dict_words_start = 2
    process_words_start = dict_words_start + num_dict_words

    # Validate constraints
    self.validate_constraints(num_dict_words, num_process_words, len(lines))

    # Add words to dictionary
    self.dictionary = lines[dict_words_start:process_words_start]

    self.process_words(lines[process_words_start:])


  def process_words(self, words):
    for word in words:
      max_print = 5
      for idx in range(len(self.dictionary)):
        suggest = False
        for char in range(len(word)):
          if char < len(self.dictionary[idx]) and word[char] !=  self.dictionary[idx][char]:
            break
          suggest = True
        if suggest and max_print > 0:
          max_print -= 1
      print("\n")


if __name__ == "__main__":
  test = Solution()
  test.process_input(args.file)



# Ran out time but to optimize:
## Instead of using a list I would use a trie for finding the words to suggest words
