""" DESCRIPTION
Develop a function that will receive as input a text string formed by digits and letters that will return the unique numbers formed by the consecutive digits, ordered and without duplicates considering letters as numbers separators.

Ex: "A56B455VB23GTY23J" -> {23, 56, 455}

Note:
1. The input string can be huge.

Return a list with the numbers in ascending order.

You may use the standard or base library included with the language of your choice. Your solution will be evaluated on correctness, runtime complexity (big-O), and adherence to coding best practices.
A complete answer will include the following:
1. List the language you’re using.
2. Document your assumptions.
3. Explain your approach and how you intend to solve the problem.
4. Provide code comments where applicable.
5. Explain the big-O run time complexity of your solution. Justify your answer.
6. Identify any additional data structure you used and justify why you used them.

You should start by using the example function prototype listed below or recreate in the language of your choice.

You can assume this method will be called with input data.

class ExtractNumbers {
  public static List<Integer> getNumbers(String text) {
    // TODO: get the unique numbers from the string an return them in ascending order.
  }
}
"""

# 1. Python 3.7
# 2. I assume that the text param always will be a string with digits an some other chars
#    I use python best practices describes in PEP8 and PEP257.
# 3. I use TDD, so I begin with the tests.
#    I iterate over the input string and check if the char is a digit or not.
#    When a number begins I save the value in a temporary variable while I get a non numeric char.
#    When the number ends I add the whole number to a python set.
#    Any non numeric char will be skipped.
# 4. Ok
# 5. Time complexite depends only of n, the length of the input text. In the worst case it could be O(n^2)
#    if the python set (hash table) load factor is high. (See https://wiki.python.org/moin/TimeComplexity).
#    See get_numbers function for more details.
# 6. I've used sets because the elements are unique and stay ordered

"""This program extract unique numbers for the given text.
"""

def get_numbers(text: str) -> set():
    """Extracts unique numbers for the given text.

    :param text: input string
    :returns: A set with the unique numbers ordered
    """
    res = set()
    current_number = None
    for char_ in text:  # O(n)
        # Check if we have some previous digits
        if current_number:
            if char_.isdigit():
                # Add the current digit to the number. Use new f-strings (python >= 3.6)
                current_number = f'{current_number}{char_}'
            else:
                # No more digits, the number is completed
                res.add(int(current_number))  # O(1) average O(n) worst
                current_number = None
        else:
            # If is a digit then we begin a new number
            if char_.isdigit():
                current_number = char_
    # I muss check if the last char was a number (see fifth example in test case)
    if current_number:
        res.add(int(current_number))
    return res
