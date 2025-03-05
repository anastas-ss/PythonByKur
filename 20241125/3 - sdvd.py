import sys

encodings = ['KOI8-R', 'CP1251', 'MACCYRILLIC', 'CP866', 'ISO-8859-5', 'CP855']

def find_original_text(encoded_text):
    for first_encoding in encodings:
        for second_encoding in encodings:
            for third_encoding in encodings:
                try:
                    temp_text = encoded_text.decode(first_encoding, errors='ignore')
                    restored_text = temp_text.encode(second_encoding, errors='ignore')
                    final_text = restored_text.decode(third_encoding, errors='ignore')
                    if "Зимбабве" in final_text:
                        return final_text
                except (UnicodeDecodeError, TypeError):
                    continue
    return 0

encoded_text = sys.stdin.buffer.read()

recovered_text = find_original_text(encoded_text)
print(recovered_text)
