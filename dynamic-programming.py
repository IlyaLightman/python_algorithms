def longest_substring(first_word, second_word):
    # Вторая строка должна быть длинее (или равна),
    # чтобы ответ являлся максимальным числом в нижней строке:
    if len(first_word) > len(second_word):
        first_word, second_word = second_word, first_word
    print(first_word, second_word)
    # Создание таблицы
    table = [[0] * len(second_word) for i in range(len(first_word))]
    for i in range(len(table)):
        for j in range(len(table[i])):
            if first_word[i] == second_word[j]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = 0
    print(table)
    return max(table[len(first_word) - 1])


print(longest_substring('fosh', 'fisher'), '\n')


def longest_subsequence(first_word, second_word):
    if len(first_word) > len(second_word):
        first_word, second_word = second_word, first_word
    table = [[0] * len(second_word) for i in range(len(first_word))]
    for i in range(len(table)):
        for j in range(len(table[i])):
            if first_word[i] == second_word[j]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    print(table)
    return max(table[len(first_word) - 1])


print(longest_subsequence('fosh', 'fisher'))
