from stats import count_words, count_letters, sort_counts
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
    return content

def main():
    try:
        file_path = sys.argv[1]
        text = get_book_text(file_path)
        word_count = count_words(text)
        letter_count = count_letters(text)
        sorted = sort_counts(letter_count)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for item in sorted:
            letter = item["letter"]
            count = item["count"]
            if letter.isalpha():
                print(f"{letter}: {count}")
        print("============= END ===============")
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()