import numpy as np
import time
class ME461Group:
    '''
    This is the random player used in the colab example.
    Edit this file properly to turn it into your submission or generate a similar file that has the same minimal class structure.
    You have to replace the name of the class (ME461Group) with one of the following (exactly as given below) to match your group name
        atlas
        backspacex
        ducati
        hepsi1
        mechrix
        meturoam
        nebula
        ohmygroup
        tulumba
    After you edit this class, save it as groupname.py where groupname again is exactly one of the above
    '''
    def __init__(self, userName, clrDictionary, maxStepSize, maxTime):
        self.name = userName # your object will be given a user name, i.e. your group name
        self.maxStep = maxStepSize # maximum length of the returned path from run()
        self.maxTime = maxTime # run() is supposed to return before maxTime
        self.clrDictionary = clrDictionary

    def run(self, img, info):
        myinfo = info[self.name]
        imS = img.shape[0] # assume square image and get size
        loc, game_point = info[self.name]
        y,x = loc # get current y,x coordinates
        yonepix,xonepix = y//50,x//50
        # a very simple randomizer
        maxL = self.maxStep # total travel
        newMap = np.zeros((15,15),dtype=int)
        for i in range(7):
            for j in range(7):
                if img[75+100*i,75+100*j,0] == self.clrDictionary['clr100'][0][0] and img[75+100*i,75+100*j,1] == self.clrDictionary['clr100'][0][1] and img[75+100*i,75+100*j,2] == self.clrDictionary['clr100'][0][2]:
                    newMap[2*i+1,2*j+1] = self.clrDictionary['clr100'][1]
                elif img[75+100*i,75+100*j,0] == self.clrDictionary['clr50'][0][0] and img[75+100*i,75+100*j,1] == self.clrDictionary['clr50'][0][1] and img[75+100*i,75+100*j,2] == self.clrDictionary['clr50'][0][2]:
                    newMap[2*i+1,2*j+1] = self.clrDictionary['clr50'][1]
                elif img[75+100*i,75+100*j,0] == self.clrDictionary['clr30'][0][0] and img[75+100*i,75+100*j,1] == self.clrDictionary['clr30'][0][1] and img[75+100*i,75+100*j,2] == self.clrDictionary['clr30'][0][2]:
                    newMap[2*i+1,2*j+1] = self.clrDictionary['clr30'][1]
                elif img[75+100*i,75+100*j,0] == self.clrDictionary['clr20'][0][0] and img[75+100*i,75+100*j,1] == self.clrDictionary['clr20'][0][1] and img[75+100*i,75+100*j,2] == self.clrDictionary['clr20'][0][2]:
                    newMap[2*i+1,2*j+1] = self.clrDictionary['clr20'][1]
                elif img[75+100*i,75+100*j,0] == self.clrDictionary['clr10'][0][0] and img[75+100*i,75+100*j,1] == self.clrDictionary['clr10'][0][1] and img[75+100*i,75+100*j,2] == self.clrDictionary['clr10'][0][2]:
                    newMap[2*i+1,2*j+1] = self.clrDictionary['clr10'][1]
                elif img[75+100*i,75+100*j,0] == self.clrDictionary['clr9'][0][0] and img[75+100*i,75+100*j,1] == self.clrDictionary['clr9'][0][1] and img[75+100*i,75+100*j,2] == self.clrDictionary['clr9'][0][2]:
                    newMap[2*i+1,2*j+1] = self.clrDictionary['clr9'][1]
                elif img[75+100*i,75+100*j,0] == self.clrDictionary['clr8'][0][0] and img[75+100*i,75+100*j,1] == self.clrDictionary['clr8'][0][1] and img[75+100*i,75+100*j,2] == self.clrDictionary['clr8'][0][2]:
                    newMap[2*i+1,2*j+1] = self.clrDictionary['clr8'][1]
                elif img[75+100*i,75+100*j,0] == self.clrDictionary['clr7'][0][0] and img[75+100*i,75+100*j,1] == self.clrDictionary['clr7'][0][1] and img[75+100*i,75+100*j,2] == self.clrDictionary['clr7'][0][2]:
                    newMap[2*i+1,2*j+1] = self.clrDictionary['clr7'][1]
                elif img[75+100*i,75+100*j,0] == self.clrDictionary['clr6'][0][0] and img[75+100*i,75+100*j,1] == self.clrDictionary['clr6'][0][1] and img[75+100*i,75+100*j,2] == self.clrDictionary['clr6'][0][2]:
                    newMap[2*i+1,2*j+1] = self.clrDictionary['clr6'][1]
                elif img[75+100*i,75+100*j,0] == self.clrDictionary['clr5'][0][0] and img[75+100*i,75+100*j,1] == self.clrDictionary['clr5'][0][1] and img[75+100*i,75+100*j,2] == self.clrDictionary['clr5'][0][2]:
                    newMap[2*i+1,2*j+1] = self.clrDictionary['clr5'][1]
                elif img[75+100*i,75+100*j,0] == self.clrDictionary['clr4'][0][0] and img[75+100*i,75+100*j,1] == self.clrDictionary['clr4'][0][1] and img[75+100*i,75+100*j,2] == self.clrDictionary['clr4'][0][2]:
                    newMap[2*i+1,2*j+1] = self.clrDictionary['clr4'][1]
                elif img[75+100*i,75+100*j,0] == self.clrDictionary['clr3'][0][0] and img[75+100*i,75+100*j,1] == self.clrDictionary['clr3'][0][1] and img[75+100*i,75+100*j,2] == self.clrDictionary['clr3'][0][2]:
                    newMap[2*i+1,2*j+1] = self.clrDictionary['clr3'][1]
                elif img[75+100*i,75+100*j,0] == self.clrDictionary['clr2'][0][0] and img[75+100*i,75+100*j,1] == self.clrDictionary['clr2'][0][1] and img[75+100*i,75+100*j,2] == self.clrDictionary['clr2'][0][2]:
                    newMap[2*i+1,2*j+1] = self.clrDictionary['clr2'][1]
                elif img[75+100*i,75+100*j,0] == self.clrDictionary['clr1'][0][0] and img[75+100*i,75+100*j,1] == self.clrDictionary['clr1'][0][1] and img[75+100*i,75+100*j,2] == self.clrDictionary['clr1'][0][2]:
                    newMap[2*i+1,2*j+1] = self.clrDictionary['clr1'][1]
        num_neighbor = 2

        left = max(0,yonepix-num_neighbor)
        right = max(0,yonepix+num_neighbor+1)

        bottom = max(0,xonepix-num_neighbor)
        top = max(0,xonepix+num_neighbor+1)

        sample = newMap[left:right,bottom:top]
        sample[0,0], sample[np.shape(sample)[0]-3,np.shape(sample)[1]-3], sample[0,np.shape(sample)[1]-1], sample[np.shape(sample)[0]-1,0], sample[np.shape(sample)[0]-1,np.shape(sample)[1]-1] = 0, 0, 0, 0, 0
        max_neighbour = np.max(sample)
        index = np.where(sample == max_neighbour)
        dy = (index[0][0]-np.shape(sample)[0]+3)*50
        dx = (index[1][0]-np.shape(sample)[1]+3)*50
        xtarget = x + dx
        ytarget = y + dy
        print(self.clrDictionary)
        return[[y,xtarget],[ytarget,xtarget]]

