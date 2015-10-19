# Automatic Zacate game player
# B551 Fall 2015
# PUT YOUR NAME AND USER ID HERE!
#
# Based on skeleton code by D. Crandall
#
# PUT YOUR REPORT HERE!
## Automatic Zacate game player
# B551 Fall 2015
# PUT YOUR NAME AND USER ID HERE!
#
# Based on skeleton code by D. Crandall
#
# 
'''
1. Roll the first die
2. Check for sameness and differentness. If more die number are same then sameness else differentness.
3. Once they are same go to the function sameness and try to optimize the result for sameness so that it gets more score.
4. Once they are different go to the function differentness and try to optimize the result for differentness so that it gets more score.
5. Categorize the result to get maximize score.

Average score is:- 167.5
Max score is:- 253
Mean score is:- 63
'''




#
#
# This is the file you should modify to create your new smart Zacate player.
# The main program calls this program three times for each turn. 
#   1. First it calls first_roll, passing in a Dice object which records the
#      result of the first roll (state of 5 dice) and current Scorecard.
#      You should implement this method so that it returns a (0-based) list 
#      of dice indices that should be re-rolled.
#   
#   2. It then re-rolls the specified dice, and calls second_roll, with
#      the new state of the dice and scorecard. This method should also return
#      a list of dice indices that should be re-rolled.
#
#   3. Finally it calls third_roll, with the final state of the dice.
#      This function should return the name of a scorecard category that 
#      this roll should be recorded under. The names of the scorecard entries
#      are given in Scorecard.Categories.
#

from ZacateState import Dice
from ZacateState import Scorecard
from collections import Counter
import operator

def most_common(lst):
    return max(set(lst), key=lst.count)
    
def sameness(dice,scorecard):
        d = Dice()
        d=dice
        unique_elements=list(set(d.dice))
        if(len(unique_elements)==1):
            if("quintupulo" not in scorecard.scorecard.keys()):
                return [-1]
            elif ("cuadruple" not in scorecard.scorecard.keys()):
                return [-1]
            elif ("triple" not in scorecard.scorecard.keys()):
                return [-1]
            elif ("elote" not in scorecard.scorecard.keys()):
                return [3,4]
            elif(most_common(d.dice)==1):
                return [i for i,val in enumerate(d.dice) if val!=1]
            elif(most_common(d.dice)==2):
                return [i for i,val in enumerate(d.dice) if val!=2]
            elif(most_common(d.dice)==3):
                return [i for i,val in enumerate(d.dice) if val!=3] 
            elif(most_common(d.dice)==4):
                return [i for i,val in enumerate(d.dice) if val!=4]
            elif(most_common(d.dice)==5):
                return [i for i,val in enumerate(d.dice) if val!=5]
            elif(most_common(d.dice)==6):
                return [i for i,val in enumerate(d.dice) if val!=6]
            else :
                return [-1]
        if(len (unique_elements)==2):
            if("quintupulo" not in scorecard.scorecard.keys()):
                return [i for i,val in enumerate(d.dice) if val!=most_common(d.dice)]
            elif ("elote" not in scorecard.scorecard.keys()):
                if(d.dice.count(most_common(d.dice))==3):
                    return [-1]
                else:
                    return [i for i,val in enumerate(d.dice) if val!=most_common(d.dice)]
            elif("cuadruple" not in scorecard.scorecard.keys()):
                if(d.dice.count(most_common(d.dice))==4):
                    return [-1]
                else:
                    return[i for i,val in enumerate(d.dice) if val!=most_common(d.dice)]
                
            elif("triple" not in scorecard.scorecard.keys()):
                return [-1]
            
            
            elif(most_common(d.dice)==1):
                return [i for i,val in enumerate(d.dice) if val!=1]
            elif(most_common(d.dice)==2):
                return [i for i,val in enumerate(d.dice) if val!=2]
            elif(most_common(d.dice)==3):
                return [i for i,val in enumerate(d.dice) if val!=3] 
            elif(most_common(d.dice)==4):
                return [i for i,val in enumerate(d.dice) if val!=4]
            elif(most_common(d.dice)==5):
                return [i for i,val in enumerate(d.dice) if val!=5]
            elif(most_common(d.dice)==6):
                return [i for i,val in enumerate(d.dice) if val!=6]
            else :
                return[-1]
                
def differentness(dice,scorecard):
        d = Dice()
        d=dice
        unique_elements=list(set(d.dice))
        if(len(unique_elements)==5):
            if("pupusa de queso" not in scorecard.scorecard.keys()):
                if([6,1] in d.dice):
                    return [d.dice.index('1')]
                else:
                    return [-1]
            elif("pupusa de frijol" not in scorecard.scorecard.keys()):
                if([1,2,6] in d.dice):
                    return [d.dice.index('6')]
                elif([2,3,6] in d.dice):
                    return [d.dice.index('6')]
                elif([1,3,6] in d.dice):
                    return [d.dice.index('1')]
                else:
                    return[4]
            elif(most_common(d.dice)==1):
                return [i for i,val in enumerate(d.dice) if val!=1]
            elif(most_common(d.dice)==2):
                return [i for i,val in enumerate(d.dice) if val!=2]
            elif(most_common(d.dice)==3):
                return [i for i,val in enumerate(d.dice) if val!=3] 
            elif(most_common(d.dice)==4):
                return [i for i,val in enumerate(d.dice) if val!=4]
            elif(most_common(d.dice)==5):
                return [i for i,val in enumerate(d.dice) if val!=5]
            elif(most_common(d.dice)==6):
                return [i for i,val in enumerate(d.dice) if val!=6]
            else :
                return [-1]
        if(len(unique_elements)==4): 
            if("pupusa de queso" not in scorecard.scorecard.keys()):          
                x=[i for i,val in enumerate(d.dice) if val==most_common(d.dice)]           
                return [x[0]]
            elif("pupusa de frijol" not in scorecard.scorecard.keys()):
                if([1,2,6] in d.dice):
                    return [d.dice.index('6')]
                elif([2,3,6] in d.dice):
                    return [d.dice.index('6')]
                elif([1,3,6] in d.dice):
                    return [d.dice.index('1')]
                else:
                    return[-1]    
            elif ("elote" not in scorecard.scorecard.keys()):
                return [i for i,val in enumerate(d.dice) if val!=most_common(d.dice)]    
            elif(most_common(d.dice)==1):
                return [i for i,val in enumerate(d.dice) if val!=1]
            elif(most_common(d.dice)==2):
                return [i for i,val in enumerate(d.dice) if val!=2]
            elif(most_common(d.dice)==3):
                return [i for i,val in enumerate(d.dice) if val!=3] 
            elif(most_common(d.dice)==4):
                return [i for i,val in enumerate(d.dice) if val!=4]
            elif(most_common(d.dice)==5):
                return [i for i,val in enumerate(d.dice) if val!=5]
            elif(most_common(d.dice)==6):
                return [i for i,val in enumerate(d.dice) if val!=6]
            else :
                return [-1]    
        if(len(unique_elements)==3):
            if ("elote" not in scorecard.scorecard.keys()):
                return [i for i,val in enumerate(d.dice) if val!=most_common(d.dice)]
            elif("pupusa de queso" not in scorecard.scorecard.keys()):
                temp1=d.dice.count(unique_elements[0])
                temp2=d.dice.count(unique_elements[1])
                temp3=d.dice.count(unique_elements[2])
                if(temp1>temp2 and temp1>temp3):
                    return [d.dice.index(unique_elements[0])]
                elif(temp2 >temp1 and temp2 >temp3): 
                    return [d.dice.index(unique_elements[1])]
                else :
                    return [d.dice.index(unique_elements[2])]
            elif("pupusa de frijol" not in scorecard.scorecard.keys()):
                temp1=d.dice.count(unique_elements[0])
                temp2=d.dice.count(unique_elements[1])
                temp3=d.dice.count(unique_elements[2])
                if(temp1>temp2 and temp1>temp3):
                    return [d.dice.index(unique_elements[0])]
                elif(temp2 >temp1 and temp2 >temp3): 
                    return [d.dice.index(unique_elements[1])]
                else :
                    return [d.dice.index(unique_elements[2])]        
            elif(most_common(d.dice)==1):
                return [i for i,val in enumerate(d.dice) if val!=1]
            elif(most_common(d.dice)==2):
                return [i for i,val in enumerate(d.dice) if val!=2]
            elif(most_common(d.dice)==3):
                return [i for i,val in enumerate(d.dice) if val!=3] 
            elif(most_common(d.dice)==4):
                return [i for i,val in enumerate(d.dice) if val!=4]
            elif(most_common(d.dice)==5):
                return [i for i,val in enumerate(d.dice) if val!=5]
            elif(most_common(d.dice)==6):
                return [i for i,val in enumerate(d.dice) if val!=6]
            else :
                return [-1]
    
class ZacateAutoPlayer:

    def __init__(self):
        pass  
    
    def first_roll(self, dice, scorecard):
        d = Dice()
        d=dice
        x=len(set(d.dice))
        if (x<3):
            return sameness(d,scorecard)
        else :
            return differentness(d,scorecard)
        #return [0] # always re-roll first die (blindly)

    def second_roll(self, dice, scorecard):
        d = Dice()
        d=dice
        x=len(set(d.dice))
        if (x<3):
            return sameness(d,scorecard)
        else :
            return differentness(d,scorecard)
        #return [1, 2] # always re-roll second and third dice (blindly)
      
    def third_roll(self, dice, scorecard):
        # stupidly just randomly choose a category to put this in
        d = Dice()
        d=dice
        x=len(set(d.dice))
        occurance=Counter(d.dice)
        sum_of_list=sum(d.dice)
        occurance.update({1 :occurance[1]*1})
        occurance.update({2 :occurance[2]*2})
        occurance.update({3 :occurance[3]*3})
        occurance.update({4 :occurance[4]*4})
        occurance.update({5 :occurance[5]*5})
        occurance.update({6 :occurance[6]*6})
        occurance.update({"tamal" :sum_of_list})
        if('seises' in scorecard.scorecard.keys()):
            occurance.pop(6)
        if('cincos' in scorecard.scorecard.keys()):
            occurance.pop(5)
        if('cuatros' in scorecard.scorecard.keys()):
            occurance.pop(4)
        if('treses' in scorecard.scorecard.keys()):
            occurance.pop(3)
        if('doses' in scorecard.scorecard.keys()):
            occurance.pop(2)
        if('unos' in scorecard.scorecard.keys()):
            occurance.pop(1)
        if('tamal' in scorecard.scorecard.keys()):
            occurance.pop("tamal")
        sorted_occurance = sorted(occurance.items(), key=operator.itemgetter(1))
        sorted_occurance.reverse()
        most_occuring_new_element=0
        if(sorted_occurance):
            most_occuring_new_element=sorted_occurance[0][0]
        
        unique_elements=list(set(d.dice))
        mostcommon=most_common(d.dice)
        
        if(x<3):
            if(len(unique_elements)==1):
                if("quintupulo" not in scorecard.scorecard.keys()):
                    return "quintupulo"
                elif(6==most_occuring_new_element):
                    return "seises"  
                elif(5==most_occuring_new_element):
                    return "cincos" 
                elif(4==most_occuring_new_element):
                    return "cuatros" 
                elif(3==most_occuring_new_element):
                    return "treses" 
                elif(2==most_occuring_new_element):
                    return "doses"
                elif(1==most_occuring_new_element):
                    return "unos" 
                elif("tamal"==most_occuring_new_element):
                    return "tamal"    
                else:
                    Scorecard.Numbers.update({len(set(scorecard.scorecard.keys())) :0})
                    return len(set(scorecard.scorecard.keys()))
            if(len (unique_elements)==2):
                if("cuadruple" not in scorecard.scorecard.keys()and d.dice.count(mostcommon)==4):
                    return "cuadruple"
                if("elote" not in scorecard.scorecard.keys()and d.dice.count(mostcommon)==3):
                    return "elote"
                if("triple" not in scorecard.scorecard.keys()and d.dice.count(mostcommon)==3):
                    return "triple"
                elif(6==most_occuring_new_element):
                    return "seises"  
                elif(5==most_occuring_new_element):
                    return "cincos" 
                elif(4==most_occuring_new_element):
                    return "cuatros" 
                elif(3==most_occuring_new_element):
                    return "treses" 
                elif(2==most_occuring_new_element):
                    return "doses"
                elif(1==most_occuring_new_element):
                    return "unos" 
                elif("tamal"==most_occuring_new_element):
                    return "tamal"
                else:
                    Scorecard.Numbers.update({len(set(scorecard.scorecard.keys())) :0})
                    return len(set(scorecard.scorecard.keys()))
        else :
            if(len (unique_elements)==3):       
                if("triple" not in scorecard.scorecard.keys() and d.dice.count(mostcommon) >=3):
                    return "triple"
                elif(6==most_occuring_new_element):
                    return "seises"  
                elif(5==most_occuring_new_element):
                    return "cincos" 
                elif(4==most_occuring_new_element):
                    return "cuatros" 
                elif(3==most_occuring_new_element):
                    return "treses" 
                elif(2==most_occuring_new_element):
                    return "doses"
                elif(1==most_occuring_new_element):
                    return "unos" 
                elif("tamal"==most_occuring_new_element):
                    return "tamal" 
                else:
                    Scorecard.Numbers.update({len(set(scorecard.scorecard.keys())) :0})
                    return len(set(scorecard.scorecard.keys()))
            if(len (unique_elements)==4):
                if("pupusa de frijol" not in scorecard.scorecard.keys() and ([1,2,3,4] ==unique_elements or [2,3,4,5] ==unique_elements or [3,4,5,6] ==unique_elements)):
                    return "pupusa de frijol"
                elif(6==most_occuring_new_element):
                    return "seises"  
                elif(5==most_occuring_new_element):
                    return "cincos" 
                elif(4==most_occuring_new_element):
                    return "cuatros" 
                elif(3==most_occuring_new_element):
                    return "treses" 
                elif(2==most_occuring_new_element):
                    return "doses"
                elif(1==most_occuring_new_element):
                    return "unos" 
                elif("tamal"==most_occuring_new_element):
                    return "tamal"
                else:
                    Scorecard.Numbers.update({len(set(scorecard.scorecard.keys())) :0})
                    return len(set(scorecard.scorecard.keys()))
            if(len (unique_elements)==5):
                if("pupusa de queso" not in scorecard.scorecard.keys() and ([1,2,3,4,5] ==unique_elements or [2,3,4,5,6] ==unique_elements)):
                    return "pupusa de queso"
                elif(6==most_occuring_new_element):
                    return "seises"  
                elif(5==most_occuring_new_element):
                    return "cincos" 
                elif(4==most_occuring_new_element):
                    return "cuatros" 
                elif(3==most_occuring_new_element):
                    return "treses" 
                elif(2==most_occuring_new_element):
                    return "doses"
                elif(1==most_occuring_new_element):
                    return "unos" 
                elif("tamal"==most_occuring_new_element):
                    return "tamal"
                else:
                    Scorecard.Numbers.update({len(set(scorecard.scorecard.keys())) :0})
                    return len(set(scorecard.scorecard.keys()))        
        
        #return random.choice( list(set(Scorecard.Categories) - set(scorecard.scorecard.keys())) )

