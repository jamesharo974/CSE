import random
print("Welcome to Lucky 7's")

money = 15

highestround = 0

rounds = 0

totalmoney = 0


while money > 0:
    totalnum = ((random.randint(1, 6)) + (random.randint(1, 6)))

    if totalnum == 7:
        print("You Win!, You win 4 more dollars")
        money += 4
        if money > totalmoney:
            totalmoney = money
            highestround = rounds
    else:
        print("You Lose, You Lost 1 dollar")
        money -= 1
    print("You now have $%s," % money)
    rounds += 1


print("You lost all of your money.")
print("You did %s rounds." % rounds)
print("The most money you had was $%s" % totalmoney)
print("Your highest round was %s" % highestround)
