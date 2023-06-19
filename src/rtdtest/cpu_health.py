import rtdtest.utilities as utilities

def square(x):
    """    
    This function returns the square of a number.

    Parameters:
        x (int): The input number.

    Returns:
        int: The square of the input number.
    """
    return x ** 2

def cube(x):
    """    
    This function returns the cube of a number.

    Parameters:
        x (int): The input number.

    Returns:
        int: The cube of the input number.
    """
    return x ** 3

if __name__ == '__main__':
    print('running directly')
    print('This is the output of ls in this folder')
    print(utilities.run_command('ls').stdout)
