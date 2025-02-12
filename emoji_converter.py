# You get emojis if you press windows key + dot (.)


def emoji_converter(message):
    words = message.split(" ")
    output = ""

    emojis = {
        ":)" : "😊",
        ":(" : "😔"
    }

    for word in words:
        output += emojis.get(word, word) + " "
    return output



message = input("> ")
print(emoji_converter(message))