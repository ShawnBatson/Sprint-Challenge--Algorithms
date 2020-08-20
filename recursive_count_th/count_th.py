'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, counter=0, total=0):  # add blanks for recursive tracking
    if len(word) == 0:  # if the length of the word == 0, return 0.
        return 0  # set the base case
    # set a letter counter
    # set a total for accrued "th" occurences:
    # comparing two, we must stop one early since the last letter won't need to take the place of the first placeholder
    if counter <= len(word) - 2:
        # make comparison variables that look at two letters at a time
        firstLetter = counter  # first letter
        secondLetter = counter + 1  # second letter
        if word[firstLetter] == 't' and word[secondLetter] == 'h':  # set the if
            total += 1  # add a total
        counter += 1  # add to counter regardless
        return count_th(word, counter, total)  # recurse
    return total  # return total at the end
