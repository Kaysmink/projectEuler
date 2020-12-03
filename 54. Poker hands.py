# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:24:28 2019

@author: kaysm
"""

"""read in the hands and split the numbers and colours per hand per player"""
def read_input(Input):
    player1=[]
    player2=[]
    for hand in Input:
        hand=hand.split(" ")
        one=hand[0:5]
        two=hand[5:10]
        
        hand1=[]
        hand2=[]
        number1=[]
        number2=[]
        col1=[]
        col2=[]
        
        dic={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
        
        for i in range(0,len(one)):
            number1.append(dic[one[i][0]])
            col1.append(one[i][1])
            number2.append(dic[two[i][0]])
            col2.append(two[i][1])
            
        hand1.append(number1)
        hand1.append(col1)
        hand2.append(number2)
        hand2.append(col2)    
        
        player1.append(hand1)
        player2.append(hand2)
    return (player1, player2)

"""select for both players which hand they have"""
def select_which_hand(player1, player2):
    score1=[]
    score2=[]
    score1.append(check_high_card(player1))
    score1.append(check_pair(player1))
    score1.append(check_two_pair(player1))
    score1.append(check_three_of_a_kind(player1))
    score1.append(check_straight(player1))
    score1.append(check_flush(player1))
    score1.append(check_full_house(player1))
    score1.append(check_four_of_a_kind(player1))
    score1.append(check_straight_flush(player1))
    score1.append(check_royal_flush(player1))
        
    score2.append(check_high_card(player2))
    score2.append(check_pair(player2))
    score2.append(check_two_pair(player2))
    score2.append(check_three_of_a_kind(player2))
    score2.append(check_straight(player2))
    score2.append(check_flush(player2))
    score2.append(check_full_house(player2))
    score2.append(check_four_of_a_kind(player2))
    score2.append(check_straight_flush(player2))
    score2.append(check_royal_flush(player2))   
    
    return [score1, score2]

"""check who wins the match ff both players have the same hand""" 
def check_winner_if_same_hand(hand1, hand2):
    highcards1=hand1[1]
    highcards2=hand2[1]
    for i in range(0,len(highcards1)):
        if(highcards1[i]!=highcards2[i]):
            value1=highcards1[i]
            value2=highcards2[i]
            
            if(value1>value2):
                return 1 
            else:
                return 2
    return 

"""counts the number of times player 1 and player 2 wins a hand"""
def check_winner(player1, player2):
    winner1=0
    winner2=0
    for i in range(0,len(player1)):
        hand1=player1[i]
        hand2=player2[i]
        
        score1, score2 = select_which_hand(hand1, hand2)
    
        highest1=0
        highest2=0
        for i in range(9,-1,-1):
            if(score1[i][0]==True):
                if(i>highest1):
                    highest1=i
            if(score2[i][0]==True):
                if(i>highest2):
                    highest2=i
                    
        if(highest1>highest2):
            winner1=winner1+1
            
        if(highest2>highest1):
            winner2=winner2+1
        
        if(highest1==highest2):
            winner=check_winner_if_same_hand(score1[highest1], score2[highest1])
            if(winner==1):
                winner1=winner1+1
            if(winner==2):
                winner2=winner2+1
    return winner1, winner2

"""checks for all possible hands"""
def check_royal_flush(hand):
    if(hand[1].count(hand[1][0])==5):
        if(min(hand[0])==10 and max(hand[0])==14):
            return [True]    
    return [False]

def check_straight_flush(hand):
    if(hand[1].count(hand[1][0])==5):
        if(max(hand[0]) - min(hand[0])==4):
            return [True, min(hand[0])]
    return [False]

def check_four_of_a_kind(hand):
    numbers=set(hand[0])
    for i in range(0,2):
        if(hand[0].count(hand[0][i])==4):
            of=hand[0][i]
            numbers.remove(of)     
            highcard=int(list(numbers)[0])
            return [True, [of, highcard]]
    return [False]

def check_full_house(hand):
    three=check_three_of_a_kind(hand)
    pair=check_pair(hand)    
    
    if(three[0]==False):
        return [False]
    if(pair[0]==False):
        return [False]
    
    value_of_three=three[1]
    value_of_pair=pair[1]
    
    return [True, [value_of_three, value_of_pair]]

def check_flush(hand):
    if(hand[1].count(hand[1][0])==5):
        return [True, max(hand[0])]
    return [False]

def check_straight(hand):
    values=sorted(hand[0])
    if(values==list(range(min(values), max(values)+1))):
        return [True, [max(values)]]    
    
    if(all(x in hand[0] for x in [14,2,3,4,5])):
        return [True, [max(hand[0])]]
    return [False]

def check_three_of_a_kind(hand):
    numbers=set(hand[0])
    for i in range(0,3):
        if(hand[0].count(hand[0][i])==3):
            of=hand[0][i]
            numbers.remove(of)
            highcard1=max(list(numbers))
            highcard2=min(list(numbers))
            return([True, [of, highcard1, highcard2]])
    return [False]

def check_two_pair(hand):
    numbers=set(hand[0])
    pairs_of=[]
    for value in hand[0]:
        if(hand[0].count(value)==2):
            if(value not in pairs_of):
                pairs_of.append(value)
                numbers.remove(value)
    if(len(pairs_of)==2):
        return [True, [max(pairs_of), min(pairs_of), list(numbers)[0]] ]      
    return [False]

def check_pair(hand):
    numbers=set(hand[0])
    for value in hand[0]:
        if(hand[0].count(value)==2):
            numbers.remove(value)
            return [True, [value]+sorted(list(numbers), reverse=True)]
    return [False]

def check_high_card(hand):
    return [True, sorted(hand[0], reverse=True)]

"""main program"""
import time
start=time.time()
Input=open("54. Poker hands Input.txt", "r").read().split("\n")
player1, player2=read_input(Input)
win1, win2=check_winner(player1, player2)

print("player 1: ", win1, "-",win2, ":Player 2")
print("Running time is: ",round(time.time()-start,4), "Seconds")
#Running time is 0.11 Seconds


