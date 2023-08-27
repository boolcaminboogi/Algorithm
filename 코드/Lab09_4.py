from heapq import heappush, heappop
from collections import defaultdict


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_frequency_table(data):
    frequency_table = defaultdict(int)
    for char in data:
        frequency_table[char] += 1
    return frequency_table


def build_huffman_tree(frequency_table):
    priority_queue = []
    for char, freq in frequency_table.items():
        node = HuffmanNode(char, freq)
        heappush(priority_queue, node)

    while len(priority_queue) > 1:
        left_node = heappop(priority_queue)
        right_node = heappop(priority_queue)
        new_freq = left_node.freq + right_node.freq
        new_node = HuffmanNode(None, new_freq)
        new_node.left = left_node
        new_node.right = right_node
        heappush(priority_queue, new_node)

    return priority_queue[0]


def build_codewords_mapping(huffman_tree):
    codewords_mapping = {}

    def traverse_tree(node, current_codeword):
        if node.char is not None:
            codewords_mapping[node.char] = current_codeword
            return

        traverse_tree(node.left, current_codeword + '0')
        traverse_tree(node.right, current_codeword + '1')

    traverse_tree(huffman_tree, '')
    return codewords_mapping


def huffman_encode(data):
    frequency_table = build_frequency_table(data)
    huffman_tree = build_huffman_tree(frequency_table)
    codewords_mapping = build_codewords_mapping(huffman_tree)

    encoded_data = ''
    for char in data:
        encoded_data += codewords_mapping[char]

    return encoded_data, huffman_tree


def huffman_decode(encoded_data, huffman_tree):
    decoded_data = ''
    current_node = huffman_tree

    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = huffman_tree

    return decoded_data


# Example usage
data = "Hello, Huffman coding!"
encoded_data, huffman_tree = huffman_encode(data)
decoded_data = huffman_decode(encoded_data, huffman_tree)

print("Original data:", data)
print("Encoded data:", encoded_data)
print("Decoded data:", decoded_data)
