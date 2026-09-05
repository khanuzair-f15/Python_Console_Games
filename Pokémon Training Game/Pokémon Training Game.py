"""
A Pokémon trainer catches Pokémon one by one, each having a power level represented by a
positive integer. After every catch, the trainer updates the collection and displays the minimum and
maximum power levels among all Pokémon caught so far to track the team’s strength. For Example:

Input: Pokémon powers caught in order - 3 8 9 7
Output:        3  3
               3  8
               3  9
               3  9

Explanation:

After catching Pokémon with power 3 -> min = 3, max = 3
After catching Pokémon with power 8 -> min = 3, max = 8
After catching Pokémon with power 9 -> min = 3, max = 9
After catching Pokémon with power 7 -> min = 3, max = 9
"""

power = [3, 8, 9, 7]

mini = maxi = power[0]
print(mini, maxi)

for power in power[1:]:
    mini = min(mini, power)
    maxi = max(maxi, power)
    print(mini, maxi)
