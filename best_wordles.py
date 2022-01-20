with open('allowed-words.txt') as file:
    words = file.readlines()

letter_count = dict()
for word in words:
    for character in word:
        if not character.isalnum():
            continue
        try:
            letter_count[character] = letter_count[character] + 1
        except KeyError:
            letter_count[character] = 1

word_scores = dict()
for word in words:
    score = 0
    for character in word:
        if not character.isalnum():
            continue
        score = score + letter_count[character]
    word_scores[word] = score

sorted_words = dict(
    sorted(word_scores.items(),
           key=lambda item: item[1],
           reverse=True)
)

number_to_show = 25
print("word\tscore")
print("-----\t-----")
for word in sorted_words.items():
    if number_to_show <= 0:
        break
    print("{}\t{}".format(word[0].strip(), word[1]))
    number_to_show -= 1
