class Sorter:

    def __init__(self, documents):
        self.documents = documents

    def generate_inverted_index(self):
        inverted_index = {}
        for docid, word_counts in self.documents.items():
            for word_count in word_counts:
                word_id = word_count['wordID']
                if word_id not in inverted_index:
                    inverted_index[word_id] = set()
                inverted_index[word_id].add(docid)

        return inverted_index
