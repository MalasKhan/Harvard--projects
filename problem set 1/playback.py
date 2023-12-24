def slow_down_input(input_text):
    slowed_text = input_text.replace(' ', '...')
    return slowed_text

if __name__ == "__main__":
    user_input = input("Enter your text: ")
    slowed_down_text = slow_down_input(user_input)
    print(slowed_down_text)