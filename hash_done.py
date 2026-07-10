class HashMap:

    INITIAL_CAPACITY = 8
    MAX_LOAD_FACTOR = 0.75

    def __init__(self):
        self.capacity = self.INITIAL_CAPACITY
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        self.word_count = 0



    def _hash(self, key):

        hash_value = 0
        prime = 31
        for char in key:
            hash_value = hash_value * prime + ord(char)
        return hash_value

    def _reduce(self, hash_value):

        return hash_value % self.capacity

    def _bucket_index(self, key):
        return self._reduce(self._hash(key))

    @property
    def load_factor(self):
        return self.size / self.capacity

    def _find_entry(self, bucket, key):

        for entry in bucket:
            if entry[0] == key:
                return entry
        return None

    def _resize(self):

        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]

        for bucket in old_buckets:
            for key, words in bucket:
                index = self._bucket_index(key)
                self.buckets[index].append([key, words])

    def _put(self, key, clean_word, original_word):

        index = self._bucket_index(key)
        bucket = self.buckets[index]
        entry = self._find_entry(bucket, key)

        if entry is None:
            bucket.append([key, [(clean_word, original_word)]])
            self.size += 1
            if self.load_factor > self.MAX_LOAD_FACTOR:
                self._resize()
        else:
            if not any(existing_clean == clean_word for existing_clean, _ in entry[1]):
                entry[1].append((clean_word, original_word))

    def _get(self, key):
        index = self._bucket_index(key)
        entry = self._find_entry(self.buckets[index], key)
        return entry[1] if entry is not None else None

    def _contains(self, key):
        return self._get(key) is not None



    @staticmethod
    def _clean(word):

        cleaned_chars = []
        for char in word:

            if not char.isalpha():
                continue
            cleaned_chars.append(char)
        return "".join(cleaned_chars)

    @staticmethod
    def _validate_word(word):

        if not isinstance(word, str):
            raise TypeError(f"Expected a string, got {type(word).__name__}")



    def insert(self, word):
        self._validate_word(word)
        lower_word = word.lower()
        clean_word = self._clean(lower_word)
        if not clean_word:
            return
        for i in range(1, len(clean_word) + 1):
            suffix = clean_word[-i:]
            self._put(suffix, clean_word, lower_word)
        self.word_count += 1

    def find_longest_shared_suffix(self, word):
        self._validate_word(word)
        clean_word = self._clean(word.lower())
        for i in range(len(clean_word), 0, -1):
            suffix = clean_word[-i:]
            entries = self._get(suffix)
            if entries is None:
                continue

            if any(existing_clean != clean_word for existing_clean, _ in entries):
                return suffix
        return None

    def get_words(self, suffix, exclude_clean=None):
        if suffix is None:
            return []
        entries = self._get(suffix)
        if entries is None:
            return []
        results = []
        for clean_word, original_word in entries:
            if clean_word != exclude_clean:
                results.append(original_word)
        return results

    def get_rhymes(self, word):
        self._validate_word(word)
        clean_word = self._clean(word.lower())
        best_suffix = self.find_longest_shared_suffix(clean_word)
        if best_suffix is None:
            return []
        return self.get_words(best_suffix, exclude_clean=clean_word)



    def stats(self):

        longest_chain = max((len(bucket) for bucket in self.buckets), default=0)
        return {
            "capacity": self.capacity,
            "distinct_keys": self.size,
            "words_inserted": self.word_count,
            "load_factor": round(self.load_factor, 4),
            "longest_chain": longest_chain,
        }

    def __len__(self):

        return self.size

    def __contains__(self, suffix):
        return self._contains(suffix)

    def __repr__(self):
        return (
            f"HashMap(capacity={self.capacity}, size={self.size}, "
            f"load_factor={self.load_factor:.2f})"
        )


if __name__ == "__main__":
    demo = HashMap()

    demo_words = ["cat", "hat", "bat", "matter", "batter", "Don't", "dont", "flat"]
    for w in demo_words:
        demo.insert(w)

    print("Demo dictionary:", demo_words)
    print(repr(demo))
    print("stats():", demo.stats())

    for test_word in ["cat", "batter", "dont"]:
        print(f"\nget_rhymes('{test_word}') ->", sorted(demo.get_rhymes(test_word)))
