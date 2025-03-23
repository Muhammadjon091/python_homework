import threading

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    """Find prime numbers in a given range."""
    primes = [num for num in range(start, end) if is_prime(num)]
    result.extend(primes)

def threaded_prime_checker(start, end, num_threads=4):
    """Use multiple threads to check for prime numbers."""
    threads = []
    results = []
    chunk_size = (end - start) // num_threads

    for i in range(num_threads):
        chunk_start = start + i * chunk_size
        chunk_end = start + (i + 1) * chunk_size if i != num_threads - 1 else end
        thread_result = []
        thread = threading.Thread(target=check_primes, args=(chunk_start, chunk_end, thread_result))
        threads.append(thread)
        results.append(thread_result)
        thread.start()

    for thread in threads:
        thread.join()

    primes = [p for sublist in results for p in sublist]
    print("Prime numbers found:", primes)

# Example usage
threaded_prime_checker(10, 100, num_threads=4)





import threading
from collections import Counter

def count_words(lines, result):
    """Count word occurrences in a list of lines."""
    word_count = Counter()
    for line in lines:
        words = line.strip().lower().split()
        word_count.update(words)
    result.append(word_count)

def threaded_word_count(file_path, num_threads=4):
    """Use multiple threads to count word occurrences in a large text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_threads
    threads = []
    results = []

    for i in range(num_threads):
        chunk_start = i * chunk_size
        chunk_end = (i + 1) * chunk_size if i != num_threads - 1 else len(lines)
        thread_result = []
        thread = threading.Thread(target=count_words, args=(lines[chunk_start:chunk_end], thread_result))
        threads.append(thread)
        results.append(thread_result)
        thread.start()

    for thread in threads:
        thread.join()

    final_word_count = Counter()
    for result in results:
        final_word_count.update(result[0])

    print("Word occurrences:", final_word_count.most_common(10))  # Display top 10 words

# Example usage
threaded_word_count("large_text.txt", num_threads=4)
