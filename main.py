def count_letter(text):
    letter = "аэеуоиы"
    count = 0

    for i in text.lower():
        if i in letter:
            count += 1
    return count

word= input("Соз жаз: ")
print(count_letter(word))
