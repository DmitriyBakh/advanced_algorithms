""" You want to turn one word to another using a chain of intermediate words that differ in 1 letter. E.g. kick - mick - mice - dice - dive - five - fine. Sometimes it's impossible so you want the changes to be as little as possible. So you invent a simple scoring function for you chain. Its a sum of scores of individual pairs of words, which are squares of numbers of differing letters. E.g. the chain kick - mick - vice - nice has a score or 1^2 + 2^2 + 1^2 = 1 + 4 + 1 = 6 as mick and vice have 2 positions where letters differ.

Note: this chain is not the best answer. Also the best answer depends on the vocabulary you can use.

Implement function

def solve(

    all_words: List[str],
    begin_word: str,
    end_word: str,

) -> int:

that will calculate the lowest possible score for chains from begin_word to end_word. All words have the same length.

Example:

all_words = ['vice', 'noon', 'mick', 'hear'],
begin_word = 'kick'
end_word = 'nice'
the answer is 4.  'kick' - 'nice' = 2^2 = 4 """

from typing import List, Tuple
import heapq

# Check if two words are adjacent (differ by only one letter)
def is_adjacent(word1: str, word2: str) -> bool:
    diff_count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_count += 1
    return diff_count == 1

# Dijkstra's algorithm for finding the shortest path in a weighted graph
def dijkstra(graph: List[Tuple[int, int]], start: int, end: int) -> int:
    pq = [(0, start)]  # (score, node)
    visited = set()
    while pq:
        score, node = heapq.heappop(pq)
        if node not in visited:
            visited.add(node)
            if node == end:
                return score
            for neighbor, weight in graph[node]:
                heapq.heappush(pq, (score + weight, neighbor))
    return -1

# Build the graph from the list of words
def build_graph(all_words: List[str], begin_word: str, end_word: str) -> List[List[Tuple[int, int]]]:
    graph = [[] for _ in range(len(all_words) + 2)]
    all_words.insert(0, begin_word)
    all_words.append(end_word)
    for i, word1 in enumerate(all_words):
        for j, word2 in enumerate(all_words):
            if i != j and is_adjacent(word1, word2):
                weight = (sum([word1[k] != word2[k] for k in range(len(word1))]))**2
                graph[i].append((j, weight))
    return graph

# Main function to solve the problem
def solve(all_words: List[str], begin_word: str, end_word: str) -> int:
    graph = build_graph(all_words, begin_word, end_word)
    min_score = dijkstra(graph, 0, len(graph) - 1)
    
    # If no valid chain found, start swapping letters in begin_word to achieve end_word
    if min_score == -1:
        min_score = sum([begin_word[i] != end_word[i] for i in range(len(begin_word))]) ** 2
        
    return min_score

# Test cases
all_words = ['vice', 'noon', 'mick', 'hear']
begin_word = 'kick'
end_word = 'nice'

print(solve(all_words, begin_word, end_word))
