from start import *
class Maze():
    _maze = [
        ['*', '0', '0', '0', '0'],
        ['1', '0', '0', '0', '0'],
        ['1', '0', '0', '0', '0'],
        ['1', '0', '0', '0', '0'],
        ['1', '1', '1', '1', '1'],
    ]

    current_position = [0, 0]

    @staticmethod
    def print_maze():
        for row in Maze._maze:
            for column in row:
                print(f"{column} ", end="")
            print("", end="\n")
        print("")

    @staticmethod
    def _move(x_offset, y_offset, axis_to_check, edge):
        x, y = Maze.current_position
      
        try: 
            if Maze._maze[x + x_offset][y + y_offset] == '0':
               print("Invalid Move\n")
               return
        
   
            Maze._maze[x][y] = '1'
            Maze.current_position[axis_to_check] += x_offset if axis_to_check==0 else y_offset
            x, y = Maze.current_position
            Maze._maze[x][y] = '*'
            try :
               Maze.print_maze()
            except Exception as error:
                print(error)   
 
        
        except Exception as e:
          print(e) 
       

    