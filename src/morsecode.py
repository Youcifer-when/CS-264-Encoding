Morse_Code_Dictionary = {'a': '.-','b': '-...','c': '-.-.','d': '-..','e': '.','f': '..-.','g': '--.','h': '....','i': '..','j': '.---','k': '-.-','l': '.-..','m': '--','n': '-.','o': '---','p': '.--.','q': '--.-','r': '.-.','s': '...','t': '-','u': '..-','v':'...-','w': '.--','x': '-..-','y': '-.--','z': '--..', ' ': '/'} 

Reverse_Morse_Dictionary = {value: key for key, value in Morse_Code_Dictionary.items()}

def morse_to_words(morse_message): 
    words = []
    
    for code in morse_message.split(): 
        if code in Reverse_Morse_Dictionary:
            words.append(Reverse_Morse_Dictionary[code])
    return "".join(words)

def words_to_morse(message): 
    morse_message = [] 

    for char in message.lower(): 
        if char in Morse_Code_Dictionary: 
            morse_message.append(Morse_Code_Dictionary[char])       
    return "". join(morse_message)

choice = input("Morse to Word or Word to Morse: ")

if choice == "Morse to Word":
    user_morse = input("Enter morse code: ")
    print("Word:", morse_to_words(user_morse))
    
if choice == "Word to Morse": 
    user_word = input("Enter word: ")
    print("Morse: ", words_to_morse(user_word))
