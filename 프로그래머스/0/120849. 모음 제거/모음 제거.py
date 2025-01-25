def solution(my_string):
    char_rmv=["a","e","i","o","u"]
    for char in char_rmv:
        my_string=my_string.replace(char,"")
    return my_string