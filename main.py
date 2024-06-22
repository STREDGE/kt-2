from pathlib import Path
    

def main() -> None:
    list(map(lambda word: print(guess_word(word)), read_words()))


def guess_word(word: str, guessed: str = "", attempt_num: int = 1) -> str:
    if not guessed:
        guessed = "_" * len(word)

    print(guessed)
    if guessed == word:
        return "Ты победил."

    input_char = input("Какая буква?")
    if input_char not in word:
        print(read_stage(attempt_num))
        if attempt_num == 7:
            return "Ты проиграл"
        return guess_word(word, guessed, attempt_num + 1)

    guessed = [
        guessed := guessed[:idx] + char + guessed[idx + 1:]
        for idx, char in enumerate(word)
        if char == input_char
    ][-1]
    return guess_word(word, guessed, attempt_num)


def read_words() -> list[str]:
    return (Path(__file__).parent / "words.txt").read_text().split()


def read_stage(stage: int) -> str:
    return (Path(__file__).parent / f"stages/{stage}.txt").read_text()


if __name__ == "__main__":
    main()
