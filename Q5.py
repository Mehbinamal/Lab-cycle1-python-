def substrings(a):
    result = []
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            if a[i:j] not in result:
                result.append(a[i:j])
    return result


def length(a, k):
    result = []
    subs = substrings(a)
    for i in subs:
        if i not in result and len(i) == k:
            result.append(i)
    return result


def distinct(a, k, n):
    result = []
    subs = length(a, k)
    for i in subs:
        chars = set()
        count = 0
        for j in i:
            if j not in chars:
                chars.add(j)
                count += 1
        if count == n and i not in result:
            result.append(i)
    return result


def palindromes(a):
    result = []
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            subp = a[i:j]
            if subp == subp[::-1] and len(subp) > 1 and subp not in result:
                result.append(subp)
    return result


s = input("Enter a string: ")
print(substrings(s))

s1 = input("Enter a string: ")
m = int(input("Length of substrings needed: "))
print(length(s1, m))

s2 = input("Enter a string: ")
m1 = int(input("Length of substrings needed: "))
d = int(input("Enter the number of Distinct Characters needed: "))
print(distinct(s2, m1, d))

s3 = input("Enter a string: ")
print(f"All palindrome substrings: {palindromes(s3)}")
