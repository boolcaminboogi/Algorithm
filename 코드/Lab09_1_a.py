def horspool(pattern, text):
    m = len(pattern)
    n = len(text)

    if m > n:
        return []

    # Preprocessing
    shift_table = {}
    for i in range(m - 1):
        shift_table[pattern[i]] = m - 1 - i

    # Searching
    i = m - 1
    result = []
    while i < n:
        k = 0
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1

        if k == m:
            result.append(i - m + 1)

        if text[i] in shift_table:
            i += shift_table[text[i]]
        else:
            i += m

    return result


def kmp(pattern, text):
    m = len(pattern)
    n = len(text)

    if m > n:
        return []

    # Preprocessing
    lps = compute_lps_array(pattern)

    # Searching
    i = j = 0
    result = []
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == m:
                result.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result


def compute_lps_array(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

# Horspool's Algorithm
horspool_result = horspool(pattern, text)
print("Horspool's Algorithm:")
if horspool_result:
    print("Pattern found at positions:", horspool_result)
else:
    print("Pattern not found")

# Knuth-Morris-Pratt (KMP) Algorithm
kmp_result = kmp(pattern, text)
print("\nKnuth-Morris-Pratt (KMP) Algorithm:")
if kmp_result:
    print("Pattern found at positions:", kmp_result)
else:
    print("Pattern not found")
