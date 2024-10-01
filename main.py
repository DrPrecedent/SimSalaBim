#Sim Sala Bim - Python Practice


def deal_cards(deck):
    end = len(deck)
    a, b, c = [], [], []
    place = int(0)
    while place < end:
        a.append(deck[place])
        b.append(deck[place +1])
        c.append(deck[place +2])
        place = place + 3
    return a,b,c

def show_cards(deck):
    a,b,c = deal_cards(deck)

    print("A = {0}".format(a))
    print("B = {0}".format(b))
    print("C = {0}".format(c))
    return a,b,c

def combine_stacks(a,b,c):
    new_deck = stack_deck(a,b,c)
    print(new_deck)
    return new_deck

def stack_deck(a,b,c):
    new_deck = []
    new_deck.extend(a)
    new_deck.extend(b)
    new_deck.extend(c)
    return new_deck

def pick_containing_stack(a,b,c):
    containing_deck = input("Which stack contains your number? A, B, or C? ")
    selection = containing_deck.lower()
    print("")
    if selection != 'a' and selection != 'b' and selection != 'c':
        print('Please input a valid answer')
        return
    else:
        return selection

def reassign_stack_from_selection(a,b,c,selection):
    temp = []

    if selection == 'b':
        return a,b,c
    else:
        temp = b
        if selection == 'a':
            b = a
            a = temp
        elif selection == 'c':
            b = c
            c = temp
        else:
            print('Please input a valid answer')
            return
    return a,b,c




def prompt_stacks(deck):
    waiting = True
    while waiting:
        a, b, c = show_cards(deck)
        selection = pick_containing_stack(a,b,c)
        if selection:
            a,b,c = reassign_stack_from_selection(a,b,c,selection)
            waiting = False
        else:
            selection = pick_containing_stack(a, b, c)
    return a,b,c

def main():
    deck = []
    selection = ''
    waiting = False

    #Start with 21 cards
    n = 21
    #Loop 3 times
    m = 3

    for i in range(n):
        deck.append(i)
    print("Pick a number from the following and remember it:\n{0}\n".format(deck))

    for j in range(m):
        a,b,c = prompt_stacks(deck)
        deck = stack_deck(a,b,c)

    print("Your number is {0}".format(deck[10]))

if __name__ == "__main__" or __name__ == "main":
    main()




