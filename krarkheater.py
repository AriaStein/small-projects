import math

threshold = .99

def winOdds (flips, mana):
    if ( (2 + flips + branchOdds(flips, 2)) / (2 ** flips) ) <= (1.0 - threshold):
        return 1.0
    else:
        winrate = 0.0
        for i in range (0, flips):
            if (i + mana) >= 3:
                winrate += winOdds(flips + i, mana + i - 3) * branchOdds(flips, i)
        return winrate

def branchOdds (flips, heads):
    return ( math.factorial(flips) / ( math.factorial(heads) * math.factorial(flips - heads) ) ) / 2 ** (flips)

for flips in range (2, 11):
    outputText = ""
    for mana in range (0,11):
        outputText += str(winOdds(flips, mana))
        outputText +=","
    print(outputText)
