def hasDuplicates( text ):
    for x in text:
        while text.index(x)+1 < len(text):
            if text[text.index(x)] == text[text.index(x)+1]:
                return True
            else:
                break
    return False