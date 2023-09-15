text1 = "if(num > 1){}"
text2 = "if(num > 1)if"
text3 = "if(num > 1)}{"
text4 = "if(num > 1)("

def check_validity(text):
    parans1 = ["(", ")", "{", "}", "[", "]"]
    parans2 = ["()", "{}", "[]"]
    pair = ''
    i = 0
    validity_count = 0

    if len(text) < 2:
        return False
    while i < len(text):
        if text[i] in parans1:
            pair += text[i]
            if len(pair) > 1:
                if pair in parans2 and i == len(text) - 1:
                    return True
                if pair in parans2:
                    pair = ''
                    validity_count += 1
                    i += 1
                    continue
                return False
        elif text[i] not in parans1 and i == len(text) - 1 and validity_count > 0:
            return True
        i += 1

    return False

print(check_validity(text1)) # True
print(check_validity(text2)) # True
print(check_validity(text3)) # False
print(check_validity(text4)) # False
