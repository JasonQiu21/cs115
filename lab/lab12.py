# I pledge my honor that I have abided by the Stevens Honor System.
#
# 
# Jason Qiu
# 2021-11-17

from random import randint
try:
    import re
    regex = True
except ImportError:
    regex = False
def shuffledNumbers(n: int) -> list:
    """
    Returns a shuffled list of length n of numbers.
    """
    out = list(map(lambda x: x+1, range(n)))
    for i in range(n-1):
        j = randint(0, i)
        if j < i:
            out[i], out[j] = out[j], out[i]
    return out
# print(shuffledNumbers(52))

def string_times(s: str, n: int) -> str:
    """
    String multiplier
    """
    # String multiplication already exists in python, so the following the code is equivalent to
    # return s * n
    out = ''
    for i in range(n):
        out += s
    return out
# print(string_times('asdf', 5))

def front_times(s: str, n: int) -> str:
    """
    String multiplier of first three characters
    """
    # String multiplication already exists in python, so the following the code is equivalent to
    # return s[0:3] * n
    out = ''
    for i in range(n):
        out += s[0:3]
    return out
# print(front_times('asdfjkl', 5))

def string_splosion(s: str) -> str:
    """
    Given a non-empty string like "Code" return a string like "CCoCodCode". 
    """
    if not s:
        raise Excpetion("s must be a non-empty string.")
    out = ''
    for i in range(len(s)):
        out += s[0:i+1]
    return out
# print(string_splosion('asdf'))

def last2(s: str) -> int:
    """
    Given a string, return the count of the number of times that a substring 
    length 2 appears in the string and also as the last 2 chars of the string
    """
    last2 = s[-2:]
    out = 0
    s = s[0:-2]
    for i in range(len(s)):
        if s[i:i+2] == last2:
            out += 1
    return out
# print(last2('axxxaaxx'))

def array_count9(nums: list) -> int:
    """
    Count the number of 9's in nums
    """
    out = 0
    for i in nums:
        if i == 9:
            out += 1
    return out
# print(array_count9([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,9,5,9,3,2]))

def array_front9(nums: list) -> bool:
    """
    Determine whether or not a list contains 9 in the first 4 elements
    """
    try:
        nums = nums[0:4]
    except IndexError:
        pass
    for i in nums:
        if i == 9:
            return True
    return False
# print(array_front9([1,2,3]))
# print(array_front9([1,2,3,9,23452,4,1,4,6,7,1,1,]))

def array123(nums: list) -> bool:
    """
    Determine whether or not a list contains 1,2,3 in itself
    """
    for i in nums:
        if nums[i:i+3] == [1,2,3]:
            return True
    return False
# print(array123([1,1,2,3,5,6,2,1,23,4]))
# print(array123([1,1,2,4,5,6,2,1,23,4]))

def string_match(a: str, b:str) -> int:
    """
    Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
    """
    out = 0
    if len(a) > len(b):
        for i in range(len(a)-1):
            try:
                if a[i:i+2] == b[i:i+2]:
                    out += 1
            except IndexError:
                break
        return out
    else:
        for i in range(len(b)-1):
            try:
                if a[i:i+2] == b[i:i+2]:
                    out += 1
            except IndexError:
                break
        return out
# print(string_match('xxcaazz', 'xxbaaz'))
# print(string_match('abc', 'abc'))
# print(string_match('abc', 'axc'))

def count_evens(nums: list) -> int:
    """
    Count number of even numbers in nums
    """
    out = 0
    for i in nums:
        out += 1 if i%2==0 else 0
    return out
# print(count_evens([2, 1, 2, 3, 4]))

def big_diff(nums: list) -> int:
    """
    Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. 
    """
    return max(nums) - min(nums)

def centered_average(nums: list[int]) -> int:
    """
    Return of mean of a list with smallest and largest dropped
    """
    nums.remove(max(nums))
    nums.remove(min(nums))
    avg = 0
    for i in nums:
        avg += i/len(nums)
    return avg
# print(centered_average([1, 2, 3, 4, 100]))

def sum13(nums: list) -> int:
    """
    Sum of a list, except 13 doesn't count and numeber directly after 13 doesn't
    """
    s = 0
    prev = 0
    for i in nums:
        if i == 13 or prev == 13:
            prev = i
            continue
        s += i
        prev = i
    return s
def sum67(nums: list) -> int:
    ignore = False
    out = 0
    for i in nums:
        if not ignore:
            if i == 6:
                ignore = True
            else:
                out += i
        if i == 7:
            ignore = False
    return out
# print(
#     sum67([1, 2, 2]),
#     sum67([1, 2, 2, 6, 99, 99, 7]),
#     sum67([1, 1, 6, 7, 2]))

def has22(nums: list) -> bool:
    prev = 0
    for i in nums:
        if prev == 2:
            if i == 2:
                return True
        prev = i
    return False
# print(
#     has22([1, 2, 2]),
#     has22([1, 2, 1, 2]),
#     has22([2, 1, 2]))

def double_char(s: str) -> str:
    out = ''
    for i in s:
        out += i*2
    return out
# print(double_char('asdf'))

def count_hi(s: str) -> str:
    out = 0
    for i in range(len(s)):
        if s[i:i+2] == 'hi':
            out += 1
    return out
# print(
#     count_hi('abc hi ho'),
#     count_hi('ABChi hi'),
#     count_hi('hihi'))

def cat_dog(s: str) -> bool:
    catCount = 0
    dogCount = 0
    for i in range(len(s)):
        if s[i:i+3] == 'cat':
            catCount += 1
        elif s[i:i+3] == 'dog':
            dogCount += 1
    if dogCount == catCount:
        return True
    return False
# print(
#     cat_dog('catdog'),
#     cat_dog('catcat'),
#     cat_dog('1cat1cadodog'))

def count_code(s: str) -> int:
    global regex
    out = 0
    if regex:
        for i in range(len(s)):
            if bool(re.match('co.e', s[i:i+4])):
                out += 1
    else:
        for i in range(len(s)):
            if s[i:i+2] == 'co' and s[i+3] == 'e':
                out += 1
    return out
# print(
#     count_code('aaacodebbb'),
#     count_code('codexxcode'),
#     count_code('cozexxcope'))

def end_other(a: str, b: str) -> bool:
    if len(a) > len(b):
        return True if a[-len(b):].lower() == b.lower() else False
    if len(b) > len(a):
        return True if b[-len(a):].lower() == a.lower() else False
# print(
#     end_other('Hiabc', 'abc'),
#     end_other('AbC', 'HiaBc'),
#     end_other('abdc', 'abXabc'))

def xyz_there(s: str) -> bool:
    global regex
    if regex:
        if bool(re.match('.*([^.]|^)xyz', s)):
            return True
        return False
    else:
        for i in range(len(s)):
            if s[i:i+3] == 'xyz' and (i == 0 or s[i-1] != '.'):
                return True
        return False
# print(
#     xyz_there('abcxyz'),
#     xyz_there('abc.xyz'),
#     xyz_there('xyz.abc'))