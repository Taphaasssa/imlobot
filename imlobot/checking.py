from uzwords import words
from difflib import get_close_matches
from transliterate import to_cyrillic, to_latin


def forwork(word, words=words):
    word = word.lower()

    if word in words:
        return f"Ushbu so'z to'g'ri: {word.title()} ✅"

    word_cyrillic = to_cyrillic(word)
    if word_cyrillic in words:
        return f"Ushbu so'z to'g'ri: {to_latin(word_cyrillic).title()} ✅"

    matches_latin = get_close_matches(word, words)
    matches_cyrillic = get_close_matches(word_cyrillic, words)
    matches = matches_latin + [to_latin(match) for match in matches_cyrillic if match not in matches_latin]

    if matches:
        response = f"Bunday so'z mavjud emas❌. Yaqin so'zlar👇\n\n"
        response += '\n\n'.join(matches)
        return response
    else:
        return "Yaqin so'z topilmadi ❌"


if __name__ == '__main__':
    test_word = "salom"
    print(forwork(test_word))
