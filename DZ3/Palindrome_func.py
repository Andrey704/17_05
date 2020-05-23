def palindrome_check():
  word = input ('Введите слово ')
  reverse_word = word[::-1]
  if word == reverse_word:
    print("It is palindrome")
  else:
   print("It is not palindrome")

palindrome_check()
