import collections


def canConstruct(ransomNote: str, magazine: str) -> bool:
    """ Given an arbitrary note string and another string containing letters 
    from all the magazines, write a function that will retrurn True:
        - if the ransom note can be constructed from the magazines; 
        - otherwise, it will retrurn False.

    Each letter in the magazine string can only* be used once in your ransom note."""
    mag_dict = collections.defaultdict(int)
    for char in magazine:
        mag_dict[char] += 1
    for char in ransomNote:
        mag_dict[char] -= 1
        if mag_dict[char] < 0:
            return False
    return True


print(canConstruct('abcc', 'aabbcc'))
