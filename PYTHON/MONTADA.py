""" 
Create a console application that reads and parses user input as an integer. Validate the value (min. 1, max. 5) and draw a Snowman. This will be done by drawing rectangles similar to how we did it in Task 1. Stack a total of 3 rectangles, where rectangle 2 is 2 characters wider than the first and the third is again 2 characters wider than the second. 
Bonus: Draw buttons and a face, maximum allowed input can be increased for this
"""

def snowman(num:int) -> str:
    """
    Draws a snowman with '*' with the number you choose
    
    Args:
        num : the number that the peson chooses
    Returns:
        The drawing of a snowman
    Raises
        In case num is not between 1 and 5
    """


    if 1 <= num <= 5:
     
     dibujo = ''
     for block in range(3): 
   
         addition = block * 2 
         width = num + addition
         height = num + addition
         blank = 2 - block
         for row in range (1, height +1):
             if row == 1 or row == height:
                 dibujo += (blank * ' ' + width * '*') + "\n"
             else:
                 dibujo += (blank * ' ' + '*' + (height - 2) * ' ' + '*') + "\n"
        
    
    else:
        print('Not a valid number, try again')

    return dibujo 



# Main part of the code

num = int(input('What number do you choose??: '))


print(snowman(num))


# We ask for a number four our program to print

#============================
#SECOND OPTION, NOT WELL OPTIMIZED
#============================
# if 1 <= num <= 30:
#      for row in range(1, num + 1):
#          if row == 1 or row == num:
#              print('  ' + num*'*')
#          else:
#              print('  *' + (num-2)*' ' + '*')

#      for row2 in range(1, num +3):
#          if row2 == 1 or row2 == num + 2:
#              print(' ' + (num+2)*'*')
#          else:
#              print(' *' + (num)*' ' + '*')
             
#      for row3 in range(1, num +5):
#          if row3 == 1 or row3 == num + 4:
#              print((num + 4)*'*')
#          else:
#              print('*' + (num + 2)*' ' + '*')
         
# else:
#     print('Not a valid number, try again')



