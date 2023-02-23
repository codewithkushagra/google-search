import nltk
from nltk.corpus import stopwords
from collections import Counter


class Indexer:

    def __init__(self, documents):
        self.documents = documents

    def get_anchor(self):
        return [ document['links'] for document in self.documents ]

    def run_indexer(self):
        forward_index = dict()
        for index, data in enumerate(self.documents):
            # Define the input string
            input_string = data['text']

            # Convert the input string to lowercase and tokenize it
            words = nltk.word_tokenize(input_string.lower())

            # Remove stop words from the list of tokens
            stop_words = set(stopwords.words('english'))

            # Remove the stop words from the list of words using a list comprehension
            filtered_words = [(i, word) for i, word in enumerate(words) if word.lower() not in stop_words]

            # Count the occurrences of each word in the filtered list using the Counter class
            word_counts = Counter([word for _, word in filtered_words])

            index_data = []

            # Print the filtered list of words and their counts
            for word, count in word_counts.items():
                indices = [i for i, w in filtered_words if w == word]
                print(f"{word}: {count} (indices: {indices})")
                index_data.append({'word': word,'count': count,'indices': indices})
            
            title = data['title']
            
            forward_index[f'doc{title}{index}'] = index_data
        
        return forward_index