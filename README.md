# AI fantasy adventure text game

![Unknown-2](https://github.com/TimotheeGayet/AI-Adventure/assets/79696450/95f382d3-56da-4742-8a98-205e57b42f66)

This is a little demonstration of what is possible when combining games and LLM.

The usage of python seemed logic since it is one of the most learned languages amongst beginners allowing them to try and update the project and it is very well updated and documented. 
I chose to use Groq API for the AI generation requests for the following reasons :
- It's free to use at the time I write this line.
- There is more choices than with LLM constructors API.
- The usage of LPU makes the API request way faster than with other APIs.

### devlog
Since this project is very basic, some functions for a possible amelioration are coded but not implemented.
It is the case for the Character class for example, where I want to add a character physical state in the future, describing when the hero lost a leg or an arm or is sick.
This would help to add realismm and continuity between the calls to the AI.

## How to install
Even though the game is fairly simple, it has some requirements.
The following lines of code must be used inside of a terminal and the last one must be used more specifically when inside the project folder.

Since the game is using Groq API, you need to export your Groq API key in your env :
```
export  GROQ_API_KEY=<your api key here>
```

You'll also need to install the Groq lib, here's how to do it with pip3 :
```
pip3 install groq
```

Then you can execute the main.py file, here's an example using python3 :
```
python3 main.py
```


## The Game
Once you've executed the forementionned line to execute the program, you'll see a game menu inviting you to choose amongst the following option :
- Start a new game
- Continue a game
- Quit

When beginning a new game, you'll see the differents saves of the project which you can choose from.
Input the number of the one you want to erase or continue if you choosed continue.

You shall now see a line prompting ```You: ```

Your story now begins !
Just write a starting sentence like : ```I am ready for adventure !```
And the AI will send you her response after a few seconds.

You'll see that often, the AI will give you options at the end of her paragraph, which doesn't mean you can't go off-script.

Have fun !

## Changing the API
If you already have a subscription to another LLM API, the good news is it's pretty simple to switch between those since they use nearly the same architecture.
You just have to change the call to the client api :
```
#srcs/AI_requests.py

from groq import Groq

client = Groq()
```
by whatever API you want to use instead.
Refer to the documentation of the said API if you have difficulties changing it.
