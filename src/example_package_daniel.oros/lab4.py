def rev_str(s):
    if isinstance(s, str) and s.strip():
        result = ''
        for word in str(s).split():
            x = list(filter(str.isalpha, word[::-1]))
            for index, char in enumerate(word):
                if not char.isalpha():
                    x.insert(index, char)
            result += ''.join(x) + ' '
        return result.strip()
    elif isinstance(s, str):
        return ''
    else:
        raise TypeError('Input must be a string')
