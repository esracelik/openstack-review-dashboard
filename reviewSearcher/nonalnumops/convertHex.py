
def convertNonAlNumtoHex(line):
    cline = ""
    if not line.isalnum():
        i = 0
        while i < len(line):
            c = line[i]
            cp = line[i-1] if i > 0 else None
            if not c.isalnum():
                if c == ' ':  # SPACE
                    cline += "+"
                elif c.encode("hex").upper() == "0A":  # NEW LINE
                    None  # do nothing
                elif c == '-':
                    cline += c
                elif c == '&':
                    cline += c
                elif c == '\\':
                    None  # do nothing
                elif c == '=' and cp is not None and cp == '\\':
                    cline += c
                else:
                    cline += "%"+c.encode("hex").upper()
            else:
                cline += c
            i += 1
    else:
        cline = line

    return cline
