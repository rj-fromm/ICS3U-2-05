#!/usr/bin/env python 3

# Created by: RJ Fromm
# Created on: Sept 2019
# This program shows how local and global variables work

# global variable
variable_x = 25


def local_variable ():
    # This shows what happens with local and global variables 
    
    variable_x = 10
    variable_y = 30
    variable_z = variable_y + variable_x
    print("|Local variable_x, variable_y, variable_z: {0} + {1} = {2}".
    format(variable_x, variable_y, variable_z))
    
def global_variable():
    # This shows what happens with global variables
    
    global variable_x
    variable_x = variable_x + 1
    variable_y = 30
    variable_z = variable_x + variable_y
    print("Global variable_x, variable_y, variable_z : {0} + {1} = {2}"
    .format(variable_x, variable_y, variable_z))
    
def main():
    #this program shows how local and global variables work
    
    local_variable()
    global_variable()

if __name__ == "__main__":
    main()