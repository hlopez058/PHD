# Ideas for the TJBot

With all the available services provided by IBM what can be built with the TJBot. 

What if the tjbot was a dungeon master? 

bot is started by asking it to begin the game.

see a board and then detect players position relative to other players?
 we would need specialized pieces that have a position associated with it?


it can hold a gamestate?

it could simulate NPC's?

it can simulate the emotions of a character?


DM objectives:
1. convert speech to text and then interpret the text to be keywords

Help Requests:
- list of (typed) actions a character can take
- list of available action types for character
- health of character
- what does characer have as far as items
- what does character have equipped?
- Who is nearby the character?
- describe the scene
    - whats is going on?
    - what is happening?
    - i am lost?
    - what can i do? 

- Add a ne wplayer
- Start the game
- Stop the game
- Resume the game
- History of the game
- Profile of the character
- decribe what a {race} is?
- describe what a {class} is?

Once the characters are created they can only die in the campaign. 

- start a new campaign, name of cmapaign.
- what are the current cmapins?
- whats the name of the city ?



NPC Talk Request

Request: 
{NPC or DM} + {CharacterName} + {Action} + {}

"DM" + "characterName" + "takes/does" + "free/minor/major/move" + "action" + "title of action" + "against/with/to/etc." + "character/player"

Action Type:
"free"
"move"
"minor"
"major"


Generic movements:
attck, push, pull , kick, stab...etc. (all of these will be allocated to movements) a database of these actions mapped to ascoiated key words would be needed.

Req. Functions
GetRandomName(class,race)
GetRandomStats()


New Campaign Script
{Start Campaign}
- What is the name for the campaign?
{Campaign Name}
- How many adventurers will join us on the {campaign name} quest?
{Number of players}
- Place the adventurer on the map one at a time.
[
    Create a platform that can identify the characers?

    view the map and recognize the figurines (color coded)
    green-ranger class
    red-warrior class
    blue-sorcerer class

each figurine should have three versions for reaces making 9 figurines in total
the shade of the color can be used to identify each. even though they are visually different.

   light color-elf
   medium color - human
   dark color - dwarf

Randomize all the stats for each character and give them a name.
]
- Welcome [characterName] the [class],[race]. You are endowed with [strength value],[speed value],[agility value][wisdom value], [charisma value],[intelligence], [Health].
- Do you accept your fate?
{Yes | NO} (if no run the stats again and randmize it)

- Next adventurer please.

.. Continue until all adventurers are on the board. 




