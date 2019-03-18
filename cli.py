from gol import GameOfLife
import numpy as np

print("Welcome to the Game Of Life!")
g = GameOfLife()
configs = g.get_options()

menu = """
Available Commands:
list - show all board configurations
view pattern_name - view the board configuration for pattern_name
select pattern_name - selects the pattern_name configuration
update n - iterates the game n times, showing outcome after each step
state - Prints the game information including the selected pattern 
        and number of iterations performed
help - Display this message
quit - Quit the game
"""

def command(fn):
    def secure_fn(cmd_list):
        try:
            fn(cmd_list)
        except IndexError:
            print("Invalid format for the command")
    return secure_fn

@command
def ls(cmd):
    for k in configs.keys():
        print(k)

@command
def view(cmd):
    if cmd[1] not in configs:
        print("Invalid pattern_name")
    else:
        print(np.array(configs[cmd[1]], dtype=np.uint8))

@command
def update(cmd):
    if g.get_stats()["pattern"] is None:
        print("Please select a pattern first.")
        return

    for i in range(int(cmd[1])):
        print("\n#{}:".format(i+1))
        g.update()
        print(g.get_board())

@command
def select(cmd):
    if not g.select(cmd[1]):
        print("No pattern called {} exists!".format(cmd[1]))

cmd_map = {
    "list": ls,
    "view": view,
    "select": select,
    "update": update,
    "state": lambda cmd: print(g.get_stats()),
    "help": lambda cmd: print(menu),
    "quit": lambda cmd: exit()
}

def execute(cmd_list):
    try:
        fn = cmd_map[cmd_list[0]]
    except KeyError:
        print("{} is not a valid command!".format(cmd_list[0]))
        return
    fn(cmd_list)

#Display the help message on starting the app
execute(['help'])

while True:
    pattern = g.get_stats()["pattern"]
    
    if pattern == None:
        print(">", end=' ')
    else:
        print("{}>".format(pattern), end=' ')
    
    execute(input().split())