# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import fnmatch
import shutil
import pandas as pd
import json
import re
import math


root = "../MTG-ABC/data/events/"
processedroot = "../MTG-ABC/data/processedevents/"
fulldatafile = open("../MTG-ABC/data/winners_full.txt","a")
#add the header row
fulldatafile.write("eventid\twinner\tplayers\tplayerid\tdeckname\tdeckcost\tsidebarcost\tdeck\n");

datafile = open("../MTG-ABC/data/tournamentResults.txt","a")
#add the header row
datafile.write("eventid\twinner\tplayers\tplayerid\tdeckname\tdeckcost\tsidebarcost\n")

df_prices = pd.read_csv('https://raw.githubusercontent.com/Pekoe200/MTG-Easy-As-ABC/main/data/cardPrices.csv')
df_cards = pd.read_csv('https://raw.githubusercontent.com/Pekoe200/MTG-Easy-As-ABC/main/data/cards.csv')

name_uuid = df_cards[['name','uuid']]
df_comb = pd.merge(name_uuid,df_prices, on='uuid')

df_comb.info()
prices = df_comb.groupby('name').price.mean()
index = prices.index.values

#remove difficult characters from the card name
for idindex, indice in enumerate(index):
    index[idindex] = re.sub("[^A-Za-z0-9]",'',indice)

prices.index = index

subdirs =  os.listdir(root)
totalevents = 0
exported_events = 0

for subdir in subdirs:
    df = pd.read_csv(root+subdir+"/players_info.csv")
    
    
    if(df.player__id.count() >= 1):
        for pid in range(df.player__id.count()):
            totalevents+=1
            exclude = False
            #is this a winning entry?
            winner = (str(df.player_result[pid]) == "1")
            deckname = re.sub("[^A-Za-z0-9 ]",'',str(df.player_title[pid]))
            #grab the json file of the player entry and put it into a string
            jsonfile = root+subdir+"/players_decks/player_"+str(df.player__id[pid])+"_deck.json"
            try:
                jfile = open(jsonfile,"r")
                try:
                    deckjson = jfile.read()
                except:
                    exclude = True
                    print("cannot read from player file:",str(df.player__id[pid]))
                finally:
                    jfile.close()
            except:
                exclude = True
                print("cannot open player file:", str(df.player__id[pid]))
            
            #turn the json string into a python dictionary
            try:
                
                deck = json.loads(deckjson)
                #go through the main deck and get the price of the cards in it
                maindeckprice = 0
                for card in deck['main_deck']:
                    #add the price of the card times the quantity of the card to the
                    #total main deck price
                    cardprice = 0
                    try:
                        cardprice = (prices[re.sub("[^A-Za-z0-9]",'',card[0])] * int(card[1]))
                    except:
                        exclude = True
                        print("No price found for ", card[0])
                        break
                    
                    maindeckprice += cardprice 
            
                #now do the same for the sideboard
                sideboardprice = 0
                for card in deck['sideboard']:
                    cardprice = 0
                    try:
                        cardprice = (prices[re.sub("[^A-Za-z0-9]",'',card[0])] * int(card[1]))
                    except:
                        exclude = True
                        break
                        print("No price found for ", card[0])
                    
                    sideboardprice += cardprice
                
                #print("Excluded:", exclude, "Deck:", df.player_title[0], "Main Price:", maindeckprice, "Sideboard Price:", sideboardprice)
            except:
               exclude = True
               print("Could not load JSON")
            if not exclude:
                #add the entry for the full details file if not excluded
                line = str(subdir) + "\t" + str(winner) + "\t" + str(df.player__id.count()) + "\t" + str(df.player__id[pid]) + "\t" + str(deckname) + "\t" + str(round(maindeckprice,2)) + "\t" + str(round(sideboardprice,2))
                fulldatafile.write(line + "\t" + deckjson + "\n")
                #add the entry for the winners file
                datafile.write(line + "\n")
                exported_events+=1
            

    #shutil.move(root+str(subdir),processedroot)
    print("Processed Event ",subdir)
    #datafile.write(df.player__id[0] + "\t" + df.player_title[0] + "\t" + deckjson + "\n")
   # print(df.player__id[0], df.player_title[0])
   
datafile.close()
fulldatafile.close()
print("Processed ", exported_events, "of",totalevents)
