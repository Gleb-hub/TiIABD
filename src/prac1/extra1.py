def task(text: str):
    morze = {
        "a": ".-",
        "b": "-…",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "….",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "…",
        "t": "-",
        "u": "..-",
        "v": "…-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
    }

    words = text.lower().split()
    morze_words = []
    for word in words:
        morze_words.append(" ".join(morze[letter] for letter in word))

    return "\n".join(morze_words)


if __name__ == "__main__":
    text = "Ignition sequence start"
    print(task(text))
