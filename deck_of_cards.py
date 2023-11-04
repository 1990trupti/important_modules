"""
there are 52 cards
4 shapes---- Heart,club,Diamond,spade
13 different numbers for each shapes----------
    A,2,3,4,5,6,7,8,9,10,J,Q,K

"""

numbers = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
# shapes = ["Heart","club","Diamond","spade"]
shapes =["\u2663", "\u2665", "\u2666", "\u2660"]

for i in range(len(numbers)):
    for j in range(len(shapes)):
        print(numbers[i], shapes[j])
























