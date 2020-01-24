
print("\n Insira qualquer palavra:")
word_1 = input()

print("\n Insira a palavra que você queira verificar se é o inverso da anterior:")
word_2 = input()

reverse_word = word_1[::-1]

if reverse_word == word_2:
    print("\n As palavras são o inverso uma da outra!")
else:
    print("\n As palavras não são o inverso uma da outra.")

