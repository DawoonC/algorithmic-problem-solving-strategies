# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# add spaces in s to construct a sentence where each word is a valid dictionary word.
# Return all such possible sentences.
#
# Note:
# - The same word in the dictionary may be reused multiple times in the segmentation.
# - You may assume the dictionary does not contain duplicate words.

from collections import defaultdict


def get_word_breaks(i, s, n, word_dict, cache):
    if i == n:
        return None
    result = cache[i]
    if result is not None:
        return result
    result = []
    for j in xrange(i + 1, n + 1):
        if s[i:j] in word_dict:
            words = get_word_breaks(j, s, n, word_dict, cache)
            if words is None:
                result.append(s[i:j])
            else:
                for w in words:
                    result.append(' '.join((s[i:j], w)))
    cache[i] = result
    return result


def word_break(s, word_dict):
    cache = defaultdict(lambda: None)
    return get_word_breaks(0, s, len(s), set(word_dict), cache)


def test():
    # Input:
    # s = "catsanddog"
    # wordDict = ["cat", "cats", "and", "sand", "dog"]
    # Output: ["cats and dog", "cat sand dog"]
    s = "catsanddog"
    word_dict = ["cat", "cats", "and", "sand", "dog"]
    result = word_break(s, word_dict)
    assert sorted(result) == sorted(["cats and dog", "cat sand dog"])
    # Input:
    # s = "pineapplepenapple"
    # wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    # Output: ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
    s = "pineapplepenapple"
    word_dict = ["apple", "pen", "applepen", "pine", "pineapple"]
    result = word_break(s, word_dict)
    assert sorted(result) == sorted(["pine apple pen apple", "pineapple pen apple", "pine applepen apple"])
    # Input:
    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]
    # Output: []
    s = "catsandog"
    word_dict = ["cats", "dog", "sand", "and", "cat"]
    result = word_break(s, word_dict)
    assert result == []
    print 'test success!'


if __name__ == '__main__':
    test()  # run
