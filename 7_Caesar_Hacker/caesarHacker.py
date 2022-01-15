"""Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com
This Program hacks messages encrypted with the Caesar Cipher by doing
a brute force attack against every possible key."""

print("Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com")

# let the user specify the message to hack:
print("Enter the encrypted Caesar Cipher message to hack.")
message = input(">> ")

# Every possible symbol that can be encrypted/decrypted:
# (This must match the SYMBOLS used when encrypting the message.)

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):
    translated = ''

    # Decrypt each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol) # Get the number of the Symbol
            num = num - key # Decrypt the number

            # Handle the wrap - around if the num is less than 0
            if num < 0:
                num = num + len(SYMBOLS)

            # Add decrypted numbers symbols to translated:
            translated = translated + SYMBOLS[num]
        else:
            # Just add the symbol without decrypting:
            translated = translated + symbol

    # Display the key being tested, along with its decrypted text:
    print("Key #{}: {}".format(key, translated))
