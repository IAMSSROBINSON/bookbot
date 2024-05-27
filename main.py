file_name = "books/frankenstein.txt"

def print_report(sorted_list, file_name, words_in_doc_count):
  report_template_start = f"--- Begin report of {file_name} ---"
  report_template_word_count = f"{words_in_doc_count} found in the document\n"
  report_template_end = f"--- End report ---"
  
  print(report_template_start)
  print(report_template_word_count)
  for dict in sorted_list:
    letter = dict["name"]
    count = dict["num"]
    if letter.isalpha():
      print(f"The '{letter}' character was found {count} times")
  print(report_template_end)

def sort_on(dict):
  return dict["num"]
  
def sort_for_report(letters_dict):
  list = []
  
  for letter in letters_dict:
    dict = {
      "name" : letter,
      "num" : letters_dict[letter]
    }
    
    list.append(dict)
  
  list.sort(reverse=True, key=sort_on)
  return list
  
def count_letters(content_string):
  letters = {}
  words = content_string.split()
  
  for word in words:
    for char in word:
      char_lower = char.lower()
      letters[char_lower] = 0
    
  for word in words:
    for char in word:
      char_lower = char.lower()
      letters[char_lower] += 1
  return letters

def word_count(file_content):
  words_split = file_content.split()
  words = len(words_split)
  words_in_doc = len(words_split)
  return words_in_doc

  
def main():
  with open(file_name) as f:
      file_content = f.read()
    
  return file_content
  
file_content = main()
words_in_document = word_count(file_content)
letters_count_in_document = count_letters(file_content)
sorted_letters = sort_for_report(letters_count_in_document)
print_report(sorted_letters, file_name, words_in_document)
