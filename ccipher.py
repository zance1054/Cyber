'''
    Simple ceaser cipher
    Alexander Fielding
    Markus Ahling
    Inputs: plaintext file to be encoded
    Outputs: ciphertext file

    Program Description here
'''

#testing my first commit!

def writeToFile():

    filename = input("Enter the file name (case sensitive)")
    file = open(filename, 'w')

    msg = input("enter message \n")

    file.write(msg)

    file.close()


#Main

writeToFile()
