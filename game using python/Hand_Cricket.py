import random as r

choice = [i for i in range(7)]
choice1 = [i for i in range(11)]
choice2 = [i for i in range(16)]

print(f'''
      1. {choice}
      2. {choice1}
      3. {choice2}''')

ch = int(input("Enter your choice (1,2,3) : "))


def toss():
    global ch1,ch2
    if (x := input("Enter E for even and O for odd : ")) == 'E':
        n = int(input("Enter a value for toss : "))
        m = r.choice(choice1)
        if (n+m) % 2 == 0:
            ch1 = input("Enter B if u want to bat else W : ")
            if ch1 == "batting":
                ch2 = "bowling"
            elif ch1 == "bowling":
                ch2 = "batting"
        elif (n+m) % 2 != 0:
            ch2 = r.choice(["batting", "bowling"])
            if ch2 == "batting":
                ch1 = "bowling"
            elif ch2 == "bowling":
                ch1 = "batting"
    elif x == 'O':
        n = int(input("Enter a value for toss : "))
        m = r.choice(choice1)
        if (n+m) % 2 == 0:
            ch2 = r.choice(["batting", "bowling"])
            if ch2 == "batting":
                ch1 = "bowling"
            elif ch2 == "bowling":
                ch1 = "batting"
        elif (n+m) % 2 != 0:
            ch1 = input("Enter B if u want to bat else W : ")
            if ch1 == "batting":
                ch2 = "bowling"
            elif ch1 == "bowling":
                ch2 = "batting"
    return [ch1, ch2, x, n, m]


var = toss()


def game(choices: list, verb, verb2):
    batter = 0
    l = [0, ]
    while batter >= 0:
        batter = int(input(f"Enter a value for {verb} : "))
        bowler = r.choice(choices)
        print(
            F"{(verb[:4] + 'er')} chooses {batter} and {verb2[:4] + 'er'} choose {bowler}")
        if batter == bowler:
            break
        elif batter == 0:
            l.append(bowler)
        else:
            l.append(batter)

    print("Target : ", sum(l))

    bowler = 0
    l1 = [0, ]
    while bowler >= 0:
        batter = int(input(f"Enter a value for {verb2} : "))
        bowler = r.choice(choices)
        print(
            F"{verb2[:4] + 'er'} chooses {batter} and {verb[:4] + 'er'} choose {bowler}")
        if (batter == bowler) and (sum(l) > sum(l1)):
            f = 1
            break
        elif sum(l1) >= sum(l):
            f = 0
            break
        elif batter == 0:
            l1.append(bowler)
        else:
            l1.append(batter)
    if verb == 'batting':
        batter = 'user'
        bowler = 'computer'
    elif verb == 'bowling':
        batter = 'computer'
        bowler = 'user'
    if f == 1:
        print(f"{batter} wins")
    elif f == 0:
        print(f"{bowler} wins")


print(F'''User chooses {var[-3]} and user enters {var[-2]} and comp chooses {var[-1]}
user gets {var[0]} and computer has to {var[1][:4]}.''')
if ch == 1:
    game(choice, var[0], var[1])
elif ch == 2:
    game(choice1, var[0], var[1])
elif ch == 3:
    game(choice2, var[0], var[1])
else:
    print("Enter an appropriate choice!")
