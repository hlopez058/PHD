# MakeHackathon 2018 FAU

## Objective

Hackathon Objective: Use the TJ-Bot from IBM and the IBM Watson Webservices to build out a clever product. 

> Big Idea : A TjBot Game I can play with my freinds.

Ideal State : 
1. A playable game that is curated by TjBot
2. Multiplayer
3. Accessories such as figurines, and a game board/ cards.
4. Dynamically changing game diffuculty
5. Simple and Intuitive
6. Adjustable Scenarios / Puzzle / Adventure /Action

## Product Scope
Lets narrow the scope of the ideal state by creating a matrix that will scale our requirements. I created a few catagories. Difficulty refers to how hard it is the implement the feature. GamePlay is the value added to the game. Hackage is the measurement of how well the feature shows the abilities of the TjBot and the usage of the Watson Services. The scale for difficulty is (1-10) . I added the hackage and gameplay categories then subtracted the difficutly to get a "weight". 
The top weighted features are the ones we should focus on.

| Features                     | Difficulty | Hackage | GamePlay | Total |
|------------------------------|------------|---------|----------|-------|
| Led indicator                | 5          | 10      | 8        | 13    |
| NPC   Chatbots               | 7          | 10      | 8        | 11    |
| Store Game Context           | 6          | 8       | 9        | 11    |
| Multiplayer                  | 10         | 10      | 10       | 10    |
| NLP user input               | 7          | 10      | 7        | 10    |
| Scripted Game                | 3          | 6       | 7        | 10    |
| TjBot Personality            | 8          | 10      | 7        | 9     |
| Board w/ Image   Recognition | 10         | 10      | 8        | 8     |
| Dynamic Game Difficulty      | 10         | 8       | 10       | 8     |
| Procedural Game              | 9          | 7       | 10       | 8     |
| Game for all ages            | 7          | 4       | 10       | 7     |
| Incorporate   arm movment    | 7          | 7       | 6        | 6     |
| Many Campaigns               | 10         | 4       | 10       | 4     |
| Accesories                   | 2          | 4       | 2        | 4     |
| Detect player emotion        | 9          | 9       | 2        | 2     |


## Requirements

By analayzing our matrix we can pick the top features that are the best to focus the product scope on. On closer inspection these do seem like the most important tasks to work on in the beginning. 

### Design Goals
* Led indicator
* NPC Chatbots
* Store Game Context
* Multiplayer
* NLP user input
* Scripted Game

Using the design goals we can start to draft a game plan that could help us acheive the goals. We can start by breaking down what these goals are trying to achieve as use cases :

### Use Case : Scripted Game Scenario 
1. Multiple people want to play a game with TjBot. 
2. TjBot starts up and initiates a conversation to start a new game or load a previous one.
3. The game begins by following a script and asking the players to perform actions.
4. Players ask Tjbot for help on possible actions and it response with information in the game but also as an AI. 
5. When players want to interact with characters in the game the LED of tjbot changes indicating that its no longer the narrator but a character in the game. 
6. Players interview NPC's for answers to solve the puzzles or finish the scripted adventure.
7. Completed objectives, Scores,Equipment, Player names are all stored for the next time a game starts.

The use case allows us to envision an overall outline of what the product cant acheive. We can start to break down functional components of the design with these expectations. 

### Process Flow

#### General Gameplay :

1. Supplier : Human Player (Requests Game Start)
2. Start TjBot
4. Start New Game or Load Game
    - New Game -> Request Game Settings
    - Load Game -> Read local storage and get Game Settings
5. Load Game State 
6. TjBot Narrates A Game State Objective
7. TjBot Waits for any player
8. Player requests to perform action 
9. TjBot Interprets Requests using NLP
    - Valid Request -> Change Game State & Jump to '5'
    - Invalid Request -> Ask for clarification & jump to '6'

#### General Game State-Machine

Lets create a very high-level flowchart of the statemachine that can run our process. I define the game script as the story that we will have to build. This would be the overall direction of the game. The script will contain several _objectives_ , The objectives are like tiny scenes that force the player to complete it by answering correctly or requesting to change something in the game state. The _game state_ , is the state of all the variables in the game. We can hold a series of variables in memory at the start of the game. 

1. System Start
2. Load Game Script
2. Loop:
    1. Load Game Context
    2. Load "Uncompleted" Objectives from Script
    4. Choose (Next) Objective
    6. Loop :
        1. Change game context variables
        2. Update game objective w/ game context 
        2. Narrate game objective
        1. Player Requests to change context variables : go to 1
        2. Player Requests more info on objective : go to 2
        3. Game objective complete : exit loop 
    5. Update Objective to "Completed"  in Game Context 

#### Psuedo Code

An objective for the game could be seen as a JSON object. The data it holds can be used to describe the scene to the player and then if more information is needed the player can request an inventory of the items in the scene.

```javascript

var objective = {
        "Name":"Escape the Room",
        "Description" :"You are in a very small room. I suggest you leave.",
        "Scene":
				[
					{ "obj": "Door", "dtl": "The door is flimsy."},
				]
}
        
```

If we could create a way for the users to interact with the "scene" in a calcualted way then it would be more of a structured game than just guessing what they will ask to do. So i would suggest using what most game systems do , create a character stat sheet and give the character limited actions to use when interacting with its world. 

```javascript

var player = {
    "Name":"Bob",
    "Health":100,
    "Strength":10,
    "Speed":3,
    "Actions" : [
        "Punch", "Kick", "Grab","Investigate","Touch","Run Away" // we can add more..
    ]
}

```
With a structured player object we can now structure the scenes to have items that can interact with the same structure. What if we create _events_ that can occur based on specific conditions. In the world we are creating i would try to break it down into 3 simplistic action types. 

1. Passive interaction  , p
    - Open a door or window
    - Pickup an item
    - Lay down on Bed
2. Kinetic interaction  , k
    - Kick down the door
    - Swing a sword
    - Sneak into the room
3. information query , q
    - Look around the corner
    - Read the note
    - Listen closer

I can use the p,k,q action types along with ha similar definition that can be used for generic object types. Objects in the world could also be sorted very simplistically. 

1. Soft Objects , s
2. Hard objects ,h
3. Informative Object, i

The p,k,q and the s,h,i categories are ways to define objects and actions. Every action can have a certain amount of each of the p,k,q, components. Similarly the s,h,i  compoments can be used to describe an object. 
The objects with certain amount of softness should be more accessible with passive interactions than kinetic interactions. Objects with more hardness should be effected more by the kinetic interactions. Objects with lots of information should be very susceptible to actions that are inquisitive. 

Lets create a "object type" vector `OT` and a "action type" vector, `AT`. 

```javascript

//Object Types
var OT = {
    "s":0.1, //soft
    "h":0.1, //hard
    "i":0.1, //info
}

//Action Types
var AT = {
    "p":0.1,//passive
    "k":0.1,//kinetic
    "q":0.1,//query
}

```

So now that the objects have a structure, what can we do with that? Well we can try to use the structure to define a particular outcome or event from the structure. Each action acting on an object is seeking to trigger an event of somekind. The events are consequences of what happens when an action interacts with an object. So we can create a formula for the event outcome . The event outcome would then be a vector of three choices. Lets also add an amount of randomness to the mix with a Noise() vector, and a player stat vector that will augment or hinder the success of an action based on the previous game outcomes. The E vector can then be normalized to 1 and used to choose the event option in the list according to the index that is equal to 1. 


`E= AT * OT * Noise() * Bonus() * Effects() `

```javascript

//Expectation list for the given object
var E = {
    {"event":"The item has opened","result":"exit"},//sp
    {"event":"The item explodes","result":"damage"},//hk
    {"event":"The item has scratches","result":""},//iq
}

```

So for every object in the scene i would need to create a OT and an E vector with object type information and Expected outcomes of the object. For every player's actions i would need to create a AT vector. The actions from the player would come from the game states input. The bonus and effects vectors could come from the players game state as well. The noise vector can be generated at the time the Expected state is going to be chosen. 

The results of the E vector , are used as reserved results that can be sent back to the game engine. It can determine if the objective is completed or if there is something else that needs to be done.  

```javascript
function OnRequest(Requested) {

    //get the player in the party 
    var player = Game.Party[Requested.player];
    // todo : check if player exists

    //get the request from player
    var act = player.Actions[Requested.action];
    // todo : check if action is valid

    var obj = Game.getObject(Requested.object);
    // todo : check if object is valid in the scene

    //get the outcome of the action on the object
    out = Outcome(act,obj,player);
    // Narrate the event that occurred
    tjbot.Speak(out.event)
    // Update based on events result
    Game.Update(out.result,obj,act,player)

    //a:Action, o:Object, p:Player
    function Outcome(a,o,p){
        arr = normalize(a*o*p.noise(a)*p.effects(a)*p.bonus(a));
        i = nonzero_indices(arr);
        return o.E[i];
    }
}
```

I use a class that i havent defined yet , "Game". By creating the functional pieces i saw a need for an overall game class that cna hold the current objective with its scene and objects. I would access the game class directly to pull back the latest stats and then use the Update method to provide a result a in the game and allow the game class to handle what should happen.

Lets try to define the game class

```javascript

var Game = {
    Party : null, // Players
    Objective : null, // from json dataset
    Create : function(party){
        var obj = Object.create(this);
        obj.Party = party;
        obj.Objective = this.GetObjective();
    },
    GetObjective : function(){
        //search through local json dataset 
        //for objective that is not completed
    }
    GetObject : function (obj){
        //find the object in 
        return this.Objective.Scene[obj];
    }
    HideObject : function (obj){
        //remove the object 
        return this.Objective.Scene[obj].pop();
    }
    Update : function(result,obj,act,player){
        switch(result){
           case "exit" : this.Objective.exit();break;
           case "damage" : this.Party[player].TakeDamage(obj); break;
           case "hide" : this.HideObject(obj); break;
           case "activate" : this.Objective.activate(obj); break;
        }
    }
}

```


#### Multiplayer

To create multiple players a player class can be instantiated for each. We established that each player requires special stats. Upon creation of a new player those stats can be created and a verbal description can be provided.
The players can be distinguished by having each player have thier own name. The players can say the "name" of the character before the request to indicate wich player to use when calculating the event. The tjbot can also repeat the player names and thier description if someone forgets who is in the party. 


### Software Design

JSON DataSets :

1. Player Actions {name,{p,k,q}}
2. Objects {name,{s,h,i},E[]}
3. Objectives {name,desc,objects[]}

Game State Software Diagram :


![lec01](reference/tjbot_v1.PNG "diagram")






# Orientation 
Process 
Workshops on bluemix, nodered amd hardware

Live and recorded on webex.

Hakacthon testing  on wednesday . the goal is to build solutions to problems that provided on the 2/16. The next day you can present your presentation. 

go to Meets for webex for the all the recordings

Sensors connected to the  TJbot.

Hackathon Teams : Self Signup. 

Bluemix account setup : hlopez5@fau.edu
10-**

Operating System is running On NOOBS

Watson Services :

Image recognition through classification
Discovery services , pull out data from text.
access news in real time
monitor trends and surface patterns
sentimient analysis
conversation and vitural agent


## Procedure
1. Bootstrap the Raspberry PI
2. Use recipes to interact witht eh sensors and rpi
3. Register the rpi to the fau network
4. configure the rpi to a hdmi port or run headless.
5. the configuration of hte rpi , needs to load from the distro'd version of the bootstrapped noobs. 




#Software 

Configuration script in order to start communicating with the ibm services. 

`// Create the credentials object for export

exports.credentials = {};

// Watson Speech to Text
// https://www.ibm.com/watson/developercloud/speech-to-text.html

exports.credentials.speech_to_text = {

    password: '',

    username: ''

};`

 text-to-speech 
 speech-to-text
 conversation
 sentiment analysis

 Node-sqldaatabase called cloudant. 


 Almost all services are available through the api. 
 Use the chat interface for question and answer  and semantic recognition. 

 We wil be using Node Red for hte flows and modeling into the raspberry PI. We could use this instead of programming hte node js. 

run all the code on docker porgras?

