import numpy as np


#O(mn) complexity since it iterates through a loop of m + 1 size and a loop of n + 1 size words.
def edit_Distance(word1, word2):

    edit = np.zeros([len(word1) + 1, len(word2)+1])
    

    for x in range(0, len(word1)+1):
        for y in range(0, len(word2)+1):
            if(x == 0):
                edit[x][y] = y
            elif(y == 0):
                edit[x][y] = x
            
            else:
                value1 = edit[x-1][y-1] #up - left
                value2 = edit[x-1][y] + 1   #vertical
                value3 = edit[x][y-1] + 1   #horizontal

                if (word1[x-1] != word2[y-1]):
                    value1 += 1
                
                if value1 <= value2 and value1 <= value3:
                    edit[x][y] = value1
                if value2 <= value1 and value2 <= value3:
                    edit[x][y] = value2
                if value3 <= value1 and value3 <= value2:
                    edit[x][y] = value3

                pass


    return edit

#O(mn) complexity to print out the resulting 2d list of the edit distance.
def print_edit_distance(edit):
    print("\nThe matrix:")
    print()

    for count in range(0, len(edit[0])):
        print("{:>7}".format(count), end="")
    
    for x in range(0, len(edit)):
        for y in range(0, len(edit[0])):
            if y == 0:
                print()
                separator = "-------"
                separator = separator * len(edit[0])
                separator += "---"
                print(separator)
                print(str(int(edit[x][y])).rjust(2) + " |", end="")
            
            print("{:>5} :".format(int(edit[x][y])), end="")
    
    print()
    

#this function job is to print out the alignment of the words.
#essentially it's gonna travel through the 
def global_alignment(edit, word1, word2):
    print("Alignment is: ")
    word1_count = len(word1) - 1
    word2_count = len(word2) - 1
    word1_alignment = ""
    word2_alignment = ""
    row = len(word1)
    column = len(word2) 

    #worst case this loop will run O(m + n) times where m is the length of word1 and n is word2.
    while(row > 0 or column > 0):
        value1 = edit[row-1][column] # vertical up'
        value2 = edit[row-1][column-1] #up-left
        value3 = edit[row][column-1] # horizontal left
        #print("row :" + str(row) + " column: " + str(column))
        if value2 <= value1 and value2 <= value3 and row > 0 and column > 0:
            word1_alignment = word1[word1_count] + word1_alignment
            word2_alignment = word2[word2_count] + word2_alignment
            word1_count -= 1
            word2_count -= 1
            row -= 1
            column -= 1
        elif value1 <= value2 and value1 <=value3 and row > 0:
            word1_alignment = word1[word1_count] + word1_alignment
            word1_count-=1
            word2_alignment = "_" + word2_alignment
            row -=1 
        
        elif value3 <= value1 and value3 <= value2 and column > 0:
            word2_alignment = word2[word2_count] + word2_alignment
            word2_count -= 1
            word1_alignment = "_" + word1_alignment
            column -=1
        
    print(word1_alignment)
    print(word2_alignment)
    print()



    



def main():
    print("Please input two words for the edit distance: ")
    word1 = input("The first word: ")
    word2 = input("The second word: ")

    edit = edit_Distance(word1, word2)
    print_edit_distance(edit)
    print("\nThe edit distance is: " + str(int(edit[len(word1)][len(word2)])) + "\n")

    global_alignment(edit, word1, word2)








if __name__ == '__main__':
    main()