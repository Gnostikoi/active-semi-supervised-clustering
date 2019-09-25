class MaximumQueriesExceeded(Exception):
    pass


class Oracle:
    def __init__(self, text, max_queries_cnt=20):
        self.text = text
        self.queries_cnt = 0
        self.max_queries_cnt = max_queries_cnt

    def query(self, i, j):
        "Query the oracle to find out whether i and j should be must-linked"
        if self.queries_cnt < self.max_queries_cnt:
            self.queries_cnt += 1
            feedback = raw_input(f"Sentence 1: {text[i]}\nSentence 2: {text[j]}\nEnter: a) must-link\tb)cannot-link")
            return feedback.strip() == "a"
        else:
            raise MaximumQueriesExceeded
