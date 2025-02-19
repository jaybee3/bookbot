def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    lowercase_text = text.lower()
    dict = {}
    for c in lowercase_text:
        try: 
            dict[c] += 1
        except:
            dict[c] = 1
    return dict

def create_report(book_path):
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_counts = get_character_count(text)

    report = f"--- Begin report of {book_path} ---\n"
    report += f"{word_count} words found in the document\n\n"

    for k,v in character_counts.items():
        if k.isalpha():
            report += f"The '{k}' character was found {v} times\n"
    
    report += f"--- End report ---"

    return report

def main():
    book_path = "books/frankenstein.txt"
    report = create_report(book_path)

    #print(f"{word_count} in {book_path}")
    print(f"{report}")

main()