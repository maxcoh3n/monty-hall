The Monty Hall Problem is something that interests me a lot.

[You can read about it more here](https://en.wikipedia.org/wiki/Monty_Hall_problem), but basically, the idea is that on the show, there are 3 doors. One contains a prize,
and the other 2 contain goats. You select a door, and the host reveals another door with a goat, and asks if you want to swap doors. 
According to mathemeticians, if you don't swap, the chance is 1/3. If you do swap, the chance is 2/3.

The way I have coded it up here in the default case corroborates this claim. 
You can try for yourself, and I recommend at elast 10 trials to let random noise even out.
You can also let the program run 1000 trials by itself either always choosing the swap strategy, or never choosing the swap strategy.
However, what happens if the host is more mischevious? After all, these game shows are often rigged for contestants to fail.
In the original pitch for the Problem, there is no guarantee that the host was going to reveal a door in every case. I.e. in the case that your original door contains a goat, or a prize.

So, in this program, I have also included an option to play against an evil host, which the original problem doesn't preclude the existence of.
Play a few rounds for yourself, and you'll see what the issue is, which makes me hesitant to want to swap in the original problem in a one-game scenario. I guarantee that there's no coding tricks to sway probabilities or swap the location of the prize, everything works exactly like it would
in an actual game show.

To try for yourself, download the code and simply run python3 ./monty-hall.py in the same directory as the program. 

I included some more thoughts in Spoiler.md