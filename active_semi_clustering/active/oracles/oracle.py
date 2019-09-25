from ...exceptions import MaximumQueriesExceeded

class Oracle:
    def __init__(self, text, max_queries_cnt=20):
        self.text = text
        self.queries_cnt = 0
        self.max_queries_cnt = max_queries_cnt

    def query(self, i, j):
        "Query the oracle to find out whether i and j should be must-linked"
        if self.queries_cnt < self.max_queries_cnt:
            self.queries_cnt += 1
            feedback = input(f"Sentence 1: {self.text[i]}\nSentence 2: {self.text[j]}\nEnter: a) must-link\tb)cannot-link\n")
            return feedback.strip() == "a"
        else:
            raise MaximumQueriesExceeded
