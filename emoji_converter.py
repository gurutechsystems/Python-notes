#EXAMPLE-1(emoji converter)
message=input('>') #the ">" is an indicator for a user to type a message
words=message.split(' ') #with the space, the split uses the space as a boundary to seperate multiple words into a list of strings
emojis = {
    ':)':'😂',
    ':(':'😒'
}
output=""
for word in words:
    output += emojis.get(word, word) + ' ' #if the user input is not in emoji, it will return "word"

print(output)

#EXAMPLE-2(Using functions to make the code portable and re-usable)
def emoji_converter(message):
    words=message.split(' ') #with the space, the split uses the space as a boundary to seperate multiple words into a list of strings
    emojis = {
    ':)':'😂',
    ':(':'😒'
    }
    output=""
    for word in words:
        output += emojis.get(word, word) + ' ' #if the user input is not in emoji, it will return "word"
    return output


message=input('>')
emoji_converter(message)
print(emoji_converter(message))


