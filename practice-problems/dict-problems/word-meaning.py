# meaning of words

word_meaning = {
    "area": "a region or part of a town, a country, or the world",
    "book": "a written or printed work consisting of pages glued or sewn together along one side and bound in covers",
    "computer": "an electronic device for storing and processing data, typically in binary form, according to instructions given to it in a variable program",
    "language": "the method of human communication, either spoken or written, consisting of the use of words in a structured and conventional way",
    "music": "vocal or instrumental sounds (or both) combined in such a way as to produce beauty of form, harmony, and expression of emotion",
    "phone": "a telephone",
    "television": "a system for converting visual images (with sound) into electrical signals, transmitting them by radio or other means, and displaying them electronically on a screen",
    "watch": "a small timepiece worn typically on a strap on one's wrist",
    "internet": "a global computer network providing a variety of information and communication facilities, consisting of interconnected networks using standardized communication protocols"
}

word = input("Enter a word: ").lower()
# word = word.lower()
meaning = word_meaning.get(word , 'Word not found')
print(f"Meaning of {word} is {meaning}")