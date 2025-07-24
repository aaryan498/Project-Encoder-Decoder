import random
import string
def word_encoder(word):
    if (len(word)<3):
        rev=''.join(reversed(word))
        return rev
    else:
        random_letters1=''.join(random.choice(string.ascii_letters) for _ in range(3) )
        random_letters2=''.join(random.choice(string.ascii_letters) for _ in range(3) )
        list_word=list(word)
        first_letter=list_word[0]
        list_word.pop(0)
        list_word.append(first_letter)
        new_string=''.join(list_word)
        encoded_string=random_letters1+new_string+random_letters2
        return encoded_string
def word_decoder(word):
    if (len(word)<3):
        rev=''.join(reversed(word))
        return rev
    else:
        new_string=word[3:-3]
        letter_at_last=new_string[-1]
        list_of_new_string=list(new_string)
        list_of_new_string.pop(-1)
        list_of_new_string.insert(0,letter_at_last)
        required_word=''.join(list_of_new_string)
        return required_word
def encoder(message):
    encoded_message1=""
    for word in message.split():
        encoded_word1=word_encoder(word)
        encoded_message1+=encoded_word1+" "
    else:
        encoded_message2=encoded_message1[:-1]
    return encoded_message2
def decoder(message_decode):
    decoded_message1=''
    for word in message_decode.split():
        decoded_word1=word_decoder(word)
        decoded_message1+=decoded_word1+" "
    else:
        decoded_message2=decoded_message1[:-1]
    return decoded_message2
print("\n\n$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Welcome to Encoder/Decoder ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$\n\n")
input1=input("Do you want to OPEN Encoder/Decoder (yes/no): ")   
while (input1=="yes"):
    print("\n\nInstructions:\nTo open Encoder:\nType 'encode' or type '1'\nTo open Decoder:\nType 'decode' or type '0'\n")
    input2=input("Enter your choice: ")
    input3=input2.lower()
    if (input3=='encode' or input3=='1'):
        print("\nWrite your message to be encoded here:")
        encoding_message=input()
        encoded_message=encoder(encoding_message)
        print("\nEncoded Message:")
        print(encoded_message,"\n\n")
    elif(input3=='decode' or input3=='0'):
        print("\nWrite your message to be decoded here:")
        decoding_message=input()
        decoded_message=decoder(decoding_message)
        print("\nDecoded Message:")
        print(decoded_message,"\n\n")
    input1=input("Do you want to open Encoder/Decoder again (yes/no): ")
else:
    print("\n\nOK...SEE YOU NEXT TIME...!\n\n")