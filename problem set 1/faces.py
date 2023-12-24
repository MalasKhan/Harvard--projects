def emojis(inut):
    inut = inut.replace(":)", "🙂")
    inut = inut.replace(":(", "🙁")
    return inut

def main():
    inut = input("enter your text:\n")
    print(emojis(inut))

if __name__ == "__main__":
    main()