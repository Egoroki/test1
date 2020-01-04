def to_camel_case(text):
    output = ''.join(x for x in text.title() if x not in '-' '_')
    try:
        return text[0] + output[1:]
    except Exception:
        return ''

    # new comment
    # result = []
    # counter = 0
    # for word in text:
    #     if word not in '-' '_':
    #         result.append(word)
    #         counter += 1
    #     else
    # return result
    # # return str(''.join(result))


print(to_camel_case("в_-ыаыва"))
print(to_camel_case("в_-ыаыва"))
