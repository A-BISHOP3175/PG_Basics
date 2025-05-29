a = "カミュ"

print(a[0])
print(a[1])
print(a[2])

letter = input("手紙は何を書いたの？: ")
mother = input("誰に送ったの？: ")

r = "私は昨日{}を書いて、{}に送った！".format(letter, mother)

print(r)

def capitalize_first_letter(sentence):
    if not sentence:
        return sentence
    return sentence[0].upper() + sentence[1:]

text = "aldous Huxley was born in 1894"
result = capitalize_first_letter(text)
print(result)  # Output: "Aldous Huxley was born in 1894"

text_list = "どこで？""だれが？""いつ？".split("?")
print(text_list)

words = ["The", "fox", "jumped", "over", "the", "fence", "."]
one = "".join(words)
print(one)

one = " ".join(words)
print(one)


equ = "A screaming comes across from the sky."
equ = equ.replace("s","z")
print(equ)

print("Hemingway".index("m"))

quote = "\"I AM SAM. I AM SAM. SAM I AM.\""
print(quote)

words = ["three", "three", "three"]
one = "".join(words)
print(one)

one = " ".join(words)
print(one)

text = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"

# 「、」の位置を探す
comma_index = text.index("、")

# スライスして「、」の前の部分を取り出す
before_comma = text[:comma_index]

print(before_comma)

