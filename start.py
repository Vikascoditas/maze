from move import *
    
def start():
        try :
               Maze.print_maze()
        except Exception as error:
                print(error)   
 
        row_edge = len(Maze._maze) - 1
        column_edge = len(Maze._maze[0]) - 1
        while True:
            valid_moves= 'wasd'
            print("""press 'w' to move up
press 'a' to move leftg
press 's' to move down
press 'd' to move right
""")

            move = input()
            if move not in valid_moves:
                print("Invalid move\n")
                continue
            
            if(move == 'w'):
                Maze._move(-1, 0, 0, 0)
            if(move == 's'):
                Maze._move(1, 0, 0, row_edge)
            if(move == 'd'):
                Maze._move(0, 1, 1, column_edge)
            if(move == 'a'):
                Maze._move(0, -1, 1, 0)
            
            x, y = Maze.current_position
            if(x == row_edge and y == column_edge):
                print("you won")
                break

