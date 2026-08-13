# mahjong-hands
This is a personal project to determine the likelihood of various Mahjong hands given the tiles I pull throughout the game. 

Given the 13 tiles you pull, this provides a direction of which Mahjong hands to target, chosen from the list of 85k+ combinations of potential Mahjong hands. I added some variability based on the number of Jokers you pull as well, given that it is unlikely for you to have all 8 jokers, for example. 

Given the current tiles in your hand, the tool tells you: 
- what is the % of overlapping tiles with a Mahjong hand
- what are the total possible combinations for that given hand (a.k.a. "yes, I might have the majority of the tiles for this hand already, but this only happens 1/85,000 times)
- what specific tiles left do I need to win Mahjong
