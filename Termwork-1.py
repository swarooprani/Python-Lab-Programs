'''Task:
Create a Python program that manages a dictionary of words and their meanings. The program should provide the following options for the user:

1.Add a new word – Allow the user to add a word along with its meaning.
2.Find the meaning of a word – Let the user search for a word and display its meaning if it exists.
3.Display the dictionary – Show all words along with their meanings.
4.Delete a word – Remove a word from the dictionary.
5.Modify the meaning of a word – Update the meaning of an existing word.
6.Quit – Exit the program.
The program should continue running until the user chooses to quit.'''

dictionary = {}
while(True):
    print("1.Add new word\n2.Find meaning of the word\n3.Display dictionary\n4.Delete a word\n5.Modify the meaning of the word\n6.Quit")
    choice=int(input("Enter your choice: "))
    
    if choice==1:
        word=input("Which word would you like to add to the dictionary?")
        if word in dictionary:
            print(word," already exists")
        else:
            meaning=input("What is the meaning of the word? ")
            dictionary[word]=meaning
        
    elif choice==2:
        word=input("Which word's meaning are you looking for? ")
        if word not in dictionary:
            print("No such word exists in the dictionary")
            
        else:
            print(dictionary[word])
            
    elif choice==3:
        for key,value in dictionary.items():
            print(key,value)
            
    elif choice==4:
        word=input("Which word you want to delete? ")
        if word in dictionary:
            del dictionary[word]
        else:
            print("No such word")
            
    elif choice==5:
        word=input("Which word's meaning you would like to change? ")
        if word not in dictionary:
            print("No such word in the dictionary")
        else:
            meaning=input("What's the meaning? ")
            dictionary[word]=meaning
            
    elif choice==6:
        print("Thank you! visit again!")
        break
    else:
        print("Invalid choice")





