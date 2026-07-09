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

    def _put(self, key, word):

        index = self._bucket_index(key)
        bucket = self.buckets[index]
        entry = self._find_entry(bucket, key)

        if entry is None:
            bucket.append([key, [word]])
            self.size += 1
            if self.load_factor > self.MAX_LOAD_FACTOR:
                self._resize()
        else:
            entry[1].append(word)

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
        original_word = self._clean(word.lower())
        if not original_word:
            return
        for i in range(1, len(original_word) + 1):
            suffix = original_word[-i:]
            self._put(suffix, original_word)
        self.word_count += 1

    def find_longest_shared_suffix(self, word):
        self._validate_word(word)
        lower_word = self._clean(word.lower())
        for i in range(len(lower_word), 0, -1):
            suffix = lower_word[-i:]
            words = self._get(suffix)
            if words is None:
                continue





            if any(candidate != lower_word for candidate in words):
                return suffix
        return None

    def get_words(self, suffix, exclude_word=None):
        if suffix is None:
            return []
        words = self._get(suffix)
        if words is None:
            return []
        results = []
        for candidate in words:
            if candidate != exclude_word:
                results.append(candidate)
        return results

    def get_rhymes(self, word):
        self._validate_word(word)
        lower_word = self._clean(word.lower())
        best_suffix = self.find_longest_shared_suffix(lower_word)
        if best_suffix is None:
            return []
        return self.get_words(best_suffix, exclude_word=lower_word)



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
    import time

    print("=" * 70)
    print("Demo 1: basic insert + rhyme lookup")
    print("=" * 70)
    hm = HashMap()
    test_words = ["cat", "hat", "bat", "flat", "dog", "log", "frog", "through", "cough"]

    start = time.perf_counter()
    for w in test_words:
        hm.insert(w)
    end = time.perf_counter()
    print(f"Inserted {len(test_words)} words in {end - start:.8f} seconds")
    print(f"stats(): {hm.stats()}")
    print(f"repr(): {hm!r}")
    print(f"len(): {len(hm)} distinct suffix keys")

    for query in ["cat", "dog", "through"]:
        start = time.perf_counter()
        rhymes = hm.get_rhymes(query)
        end = time.perf_counter()
        print(f"Rhymes for '{query}': {rhymes}  ({end - start:.8f} sec)")

    print("\n" + "=" * 70)
    print("Demo 2: messy/edge-case input (mirrors what a user might type)")
    print("=" * 70)
    edge_cases = ["Cat!", "h@t", "  Bat  ", "123", "", "flat-out", "FROG"]
    for w in edge_cases:
        try:
            hm.insert(w)
            print(f"insert({w!r}) -> ok")
        except TypeError as e:
            print(f"insert({w!r}) -> TypeError: {e}")
    print(f"Rhymes for 'cat' after messy inserts: {hm.get_rhymes('cat')}")

    try:
        hm.insert(42)
    except TypeError as e:
        print(f"insert(42) correctly rejected -> TypeError: {e}")

    print("\n" + "=" * 70)
    print("Demo 3: forcing a resize with a larger batch")
    print("=" * 70)
    hm2 = HashMap()
    import random
    import string

    random.seed(0)
    bulk_words = [
        "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 8)))
        for _ in range(500)
    ]
    before_capacity = hm2.capacity
    start = time.perf_counter()
    for w in bulk_words:
        hm2.insert(w)
    end = time.perf_counter()
    print(f"Inserted {len(bulk_words)} random words in {end - start:.6f} sec")
    print(f"Capacity grew from {before_capacity} to {hm2.capacity} via automatic rehashing")
    print(f"stats(): {hm2.stats()}")
