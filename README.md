# Game Of Life
An implementation of John Conway's game of life in Python 3 for JdeRobot's Python programming challenge.

It follows the implementation from a scientific observer's viewpoint rather than an egocentric approach. [1]

It uses `numpy` for fast operations on 2D arrays as well as `scipy` for a  convolution function. Therefore, these modules must be installed beforehand. 

(Note to judges: Please let me know if I should remove the `scipy` dependency, although a custom implementation of convolution might be a bit slower) 

The following patterns are implemented (specified in `config.json`):
##### Still Lifes 
1. Block:
![Block](http://www.conwaylife.com/w/images/4/48/Block.png)
2. Bee-Hive:
![Bee-Hive](http://www.conwaylife.com/w/images/3/3c/Beehive.png)
3. Loaf:
![Loaf](http://www.conwaylife.com/w/images/b/ba/Loaf.png)
4. Boat:
![Boat](http://www.conwaylife.com/w/images/1/1e/Boat.png)
5. Tub:
![Tub](http://www.conwaylife.com/w/images/b/bf/Tub.png)

##### Oscialltors
6. Blinker
![Blinker](http://www.conwaylife.com/w/images/b/b9/Blinker.gif)
7. Toad
![Toad](http://www.conwaylife.com/w/images/c/cd/Toad.gif)
8. Beacon
![Beacon](http://www.conwaylife.com/w/images/4/4b/Beacon.gif)

##### Spaceships
9. Glider
![Glider](http://www.conwaylife.com/w/images/8/81/Glider.gif)
10. Light Weight Spaceship (LWSS):
![LWSS](http://www.conwaylife.com/w/images/2/21/Lwss.gif)
11. Medium Weight Spaceship (MWSS):
![MWSS](http://www.conwaylife.com/w/images/b/b7/Mwss.gif)
12. Heavy Weight Spaceship (HWSS):
![HWSS](http://www.conwaylife.com/w/images/d/dd/Hwss.gif)

## API Description
`gol.py` contains the `GameOfLife` class. A `GameOfLife` object must be created prior to using the API. It contains the following methods:
* `select(pattern_name)` : Selects a pattern based on the name specified by the `pattern_name` string argument
* `update()` : Performs a single iteration of the game
* `get_board()` : Returns the current state of the board. It is represented as a 2D `numpy.ndarray` with elements either being `0` (representing dead) or `1` (representing alive)
* `get_stats()` : Returns a dictionary containing the selected pattern name, number of iterations made so far, number of alive cells in the current state
* `get_options()` : Returns a dictionary representing the available configurations (as specified by `config.json`). It is indexed by the pattern name string and each value is a board representing its initial state.

## Sample Application

Run `cli.py` to launch a sample application demonstrating the use of the API


[1] https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Algorithms