"""This program counts the number of vowels in a string."""

def count_vowels(string:str) -> int:
    """
        Takes in a string and returns the number of vowels in the string.

        Args:
            string (str): The string to count vowels in.

        Returns:
            int: The number of vowels in the string.
        """
    count = 0
    vowels = {"a","e","i","o","u"}
    status = True

    while status:
        for v in vowels:
            count += string.count(v)
        status = False

    return count


if __name__ == "__main__" :
    strTest = input("Aonde você quer contar? \n")
    count_vowels(strTest)
