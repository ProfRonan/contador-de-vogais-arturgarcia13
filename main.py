"""This program counts the number of vowels in a string."""

def count_vowels(string:str) -> int:
    stringF = string.casefold()
    """
        Takes in a string and returns the number of vowels in the string.

        Args:
            string (str): The string to count vowels in.

        Returns:
            int: The number of vowels in the string.
        """
    print(f'Irei contar aqui {stringF}\n')
    count = 0
    vowels = {"a","e","i","o","u"}
    status = True

    while status:
        for v in vowels:
            count += stringF.count(v)
            print(f'Ja encontrei {count} vogais')
        status = False

    return print(count)


if __name__ == "__main__" :
    strTest = input("Aonde você quer contar? \n")
    count_vowels(strTest)
