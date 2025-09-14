from collections import Counter
from pathlib import Path

path = Path('file.txt')
content = path.read_text()

words_dict = Counter(content.split())
print(words_dict)