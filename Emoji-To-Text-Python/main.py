import demoji

# Download emoji data (required only once)
demoji.download_codes()

def convert_emoji_to_text(text):
    """
    Converts emojis in the text to their textual description.
    """
    return demoji.replace_with_desc(text)

if __name__ == "__main__":
    user_text = input("Enter text with emojis: ")
    result = convert_emoji_to_text(user_text)
    print("\nConverted Text:")
    print(result)