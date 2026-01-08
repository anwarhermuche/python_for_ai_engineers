

class TokenStats:

    def __init__(self, avg_chars_per_word: float = 6.11, min_chars: int = 15):
        self.avg_chars_per_word = avg_chars_per_word
        self.min_chars = min_chars

    def estimate_tokens(self, text: str) -> int:
        return len(text) // self.avg_chars_per_word

    def build_lengths(self, texts: list[str]) -> list[int]:
        return [self.estimate_tokens(text) for text in texts]

    def classify_topic(self, text: str, topic_rules: dict[str, list[str]]) -> list[str | None]:
        topics = []
        for topic, rules in topic_rules.items():
            if any(rule in text.lower() for rule in rules):
                topics.append(topic)
            
        return topics

    def count_topics(self, texts: list[str], topic_rules: dict[str, list[str]]) -> dict[str, int]:
        topics_count = {topic: 0 for topic in topic_rules.keys()}
        for text in texts:
            topics = self.classify_topic(text, topic_rules)
            for topic in topics:
                topics_count[topic] += 1
        return topics_count