adjective1 = input("Insert a word: ") #prompts the user to insert a word 
adjective2 = input("Insert a word: ")
adjective3 = input("Insert a word: ")
story = f"In the 1990s there were no {adjective1}; {adjective1} were brought by the {adjective2} when Kenya got {adjective3} inthe 2000s."

if adjective1 == "car" or adjective2 == "british" or adjective3 == "colonised":
    
    print(story)
    
else:

    print("Your story doesn't make sense")
