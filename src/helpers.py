'''Various utility functions.'''


def shorttened(s, length=40, filler='...'):
    if len(s) <= length:
        return s
    else:
        overfill = len(s) - length
        t_length = len(s)//2 - overfill//2
        return ''.join((
            s[:t_length],
            filler,
            s[t_length + overfill + len(filler):]
        ))
