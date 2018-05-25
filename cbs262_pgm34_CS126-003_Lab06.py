# Lab 06 Banners
# Colton Spector and Paul Meek
# cbs262 and pgm34
# 10/19/2017
# CS126-003

# Create the alphabet
alphabet = {"A": ['AAAA', 'A  A', 'AAAA', 'A  A', 'A  A'],
            "B": ['BBB ', 'B  B', 'BBB ', 'B  B', 'BBB '],
            "C": ['CCCC', 'C   ', 'C   ', 'C   ', 'CCCC'],
            "D": ['DDD ', 'D  D', 'D  D', 'D  D', 'DDD '],
            "E": ['EEEE', 'E   ', 'EEEE', 'E   ', 'EEEE'],
            "F": ['FFFF', 'F   ', 'FFFF', 'F   ', 'F   '],
            "G": ['GGGG', 'G   ', 'G GG', 'G  G', 'GGGG'],
            "H": ['H  H', 'H  H', 'HHHH', 'H  H', 'H  H'],
            "I": ['IIII', ' II ', ' II ', ' II ', 'IIII'],
            "J": ['JJJJ', '  J ', '  J ', 'J J ', ' JJ '],
            "K": ['K  K', 'K K ', 'KK  ', 'K K ', 'K  K'],
            "L": ['L   ', 'L   ', 'L   ', 'L   ', 'LLLL'],
            "M": ['M  M', 'MMMM', 'M MM', 'M  M', 'M  M'],
            "N": ['N  N', 'N NN', 'NNNN', 'NN N', 'N  N'],
            "O": [' OO ', 'O  O', 'O  O', 'O  O', ' OO '],
            "P": ['PPPP', 'P  P', 'PPPP', 'P   ', 'P   '],
            "Q": [' Q  ', 'Q Q ', 'Q Q ', 'Q QQ', ' Q Q'],
            "R": ['RRRR', 'R  R', 'RRRR', 'R R ', 'R  R'],
            "S": [' SSS,' 'S   ', ' SS ', '   S', 'SSS '],
            "T": ['TTTT', ' TT ', ' TT ', ' TT ', ' TT '],
            "U": ['U U ', 'U U ', 'U U ', 'U U ', ' U U'],
            "V": ['V  V', 'V  V', 'V  V', 'V  V', ' VV '],
            "W": ['W  W', 'W  W', 'W WW', 'WWWW', 'W  W'],
            "X": ['X  X', 'X  X', ' XX ', 'X  X', 'X  X'],
            "Y": ['Y  Y', 'Y  Y', ' YYY', '   Y', '   Y'],
            "Z": ['ZZZZ', '   Z', ' ZZ ', 'Z   ', 'ZZZZ']}

# User input requested
string = input("Input a word: ").upper()
position = input("Postion of word Vertical or Horizontal?: ").upper()


# Define the function test for position and begin the for loop
def print_banner(string, position):
    if position == "VERTICAL":
        for letter in string:
            for i in range(5):
                print(alphabet[letter][i])
    elif position == "HORIZONTAL":
        for i in range(5):
            for letter in string:
                print(alphabet[letter][i], end=" ")
            print()

''' Call the funtion outside of the loop so once the user inputs their data the
function print_banner can run'''
print_banner(string, position)
