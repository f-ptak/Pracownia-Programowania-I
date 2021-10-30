def check_letters(funtion_sentence, function_letter):
    sentence_list = list(funtion_sentence)
    number = sentence_list.count(function_letter)
    return number

sentence = input('Enter a sentence: ')
letter = input('Enter a letter: ')
print(f'The number of {letter} in the sentence is', check_letters(sentence, letter))