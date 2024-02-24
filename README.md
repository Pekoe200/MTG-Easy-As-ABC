# MTG-Easy-As-ABC
Magic the Gathering Predictive Analytics

Introduction

The purpose of this project is to develop a predictive model that estimates the probability of a given deck winning in a Magic: The Gathering tournament based on the overall deck price. Is a deck that is more expensive more likely to win in a tournament than a deck made up of less expensive cards? 

Selection of Data

The datasets being used come from a few different sources. The data set being used for card information and pricing comes from www.MTGJSON.com. This up-to-date data will be used to determine the individual cost of each card used in each deck, then added together to calculate the overall cost of each individual deck. The tournament win data comes from www.kaggle.com. This data will be used to find the top winning decks from tournaments, so that each card can be analyzed for price. The card price was contained in CSV format. Some feature engineering was required for the tournament data so that it could be presented in a digestible form (see tournament.py for more details).  
Sources:

Card Data: https://mtgjson.com/api/v5/csv/cardPrices.csv

Tournament Data: https://www.kaggle.com/datasets/camilonunez/magic-the-gathering-top8-some-decks-and-events

Methods: 

The MTGJSON API was extremely helpful in providing the necessary card information. This API maintained up-to-date information on many of the details surrounding the Magic: The Gathering game. Data was clean, well-organized, and most importantly, current. 

Results: 

The most likely answer to our proposed research question was “no”. The results showed that there wasn’t a direct correlation between the deck price and the probability of winning. The regression model used showed that there was no regression in the data used, and that an expensive deck was just as likely to win in a tournament setting as a deck that cost much less. 

Discussion: 

The results of our investigation imply that there are more elements at play than deck cost alone when it comes to being successful in Magic: The Gathering at the tournament level. Skill and variety are two alluring aspects that draw players into this game, and our data suggests that if we wanted a model that produces more defining results, there might be other data points that would need to be considered. The results of this investigation match follow suit with the current expectations for the cost of a standard deck that follows the “meta”. Our results found that a deck would need to start around the $100-$200 mark for it to start being competitive and we have found that same sentiment shared across various Magic: The Gathering boards, blogs, and news sites. For future research, a more defined model will need to be produced; one that takes in different data points than just price alone. 
Sources:

https://www.mtggoldfish.com/metagame/standard#paper

https://draftsim.com/mtg-deck-price/ 

Summary: 

The most important finding from this research is the obvious one that has been repeated throughout this report: a relatively inexpensive deck can be just as competitive as an expensive deck in a tournament setting. To elaborate on the importance of this finding, Magic: The Gathering is an incredibly popular game, whose success and popularity are directly tied to the variety of play that its users enjoy. The success of competitive trading card games can suffer from a lack of variety, creating a stale atmosphere for its player base. The findings from this project confirm that variety is alive and well in this competitive classic. 

Team:

Charles Zieres

Brandon Pimentel

Anthony Broussard

https://github.com/Pekoe200/MTG-Easy-As-ABC
Link to Video: https://drive.google.com/file/d/1KLQCTRSE-JiRMs7mFJUUZ13_fsemOaFX/view?usp=drive_link
