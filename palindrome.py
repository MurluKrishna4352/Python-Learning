#palindrome

word_for_palindrome = input("provide_a_word_to_check_whether_in_palindrome_or_not: ")
palindrome_checker = word_for_palindrome[::-1]

if word_for_palindrome == palindrome_checker:
    print(word_for_palindrome,"is in palindrome")

else:
    print(word_for_palindrome,"is not in palindrome")
