def main():
    emoticon = input()
    convert(emoticon)
def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    print(text)
main()
