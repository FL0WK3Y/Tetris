import pygame 
import random 
blocks = [
# This is the blocks data structure
# all blocks are in a 3 by 3 grid like the one shown bellow 
#  |_0_|_1_|_2_|
#  |_3_|_4_|_5_|
#  |_6_|_7_|_8_|

#flaten values in a 3 by 3 matrix 
[[1, 4, 7],[3, 4, 5]], #<--- the STRAIGHT block  
[[1, 3, 4, 5, 7]], #<--- the CROSS block  
[[0, 1, 4, 5], [1, 3, 4, 6]], #<---the TWO_BY_TWO type 1 block  
[[1, 2, 3, 4], [0, 3, 4, 7]], #<---the TWO_BY_TWO type 2 block 
[[0, 1, 3, 6], [0, 1, 2, 5], [2, 5, 7, 8],[3, 6, 7, 8]], #<---the L_BLOCK  type 1    
[[1, 2, 5, 8], [5, 6, 7, 8], [0, 3, 6, 7],[0, 1, 2, 3]], #<---the L_BLOCK  type 2    
[[4, 6, 7, 8], [0, 3, 4, 6], [0, 1, 2, 4],[2, 4, 5, 8]] #<---the ONE_ON_THREE_BLOCK  
] 
class Block:
    def __init__(self,x,y) :
        self.x= x
        self.y= y
        self.type = random.randint(0,6)
        self.rotation = 0
    def shape(self):
      return blocks[self.type][self.rotation] 
def draw_block():
    for y in range(3):
        for x in range(3) :
           # this is flattening the array and then it checks if it has the index inside of the block shape 
           if y * 3 + x in block.shape():
               pygame.draw.rect(screen,(80,55,55),
                                [(x+block.x)*grid_size + x_gap+1, (y + block.y) * grid_size + y_gap + 1, grid_size -2 , grid_size -2] )

def rotate():
    block.rotation = (block.rotation+ 1)% len(blocks[block.type])

def draw_grid():
    for y in range(rows): 
        #this is to make the horizantal collums in the grid
        for x in range (cols):
    
        #this is to make the grid for tetris
            pygame.draw.rect(screen,(100,100,100), [x * grid_size + x_gap , y * grid_size + y_gap ,grid_size,grid_size],1)    
            if game_board[x][y] !=(0,0,0):
                pygame.draw.rect(screen,game_board[x][y], [x * grid_size + x_gap +1 , y * grid_size + y_gap +1 ,grid_size -1,grid_size -1])    
            
            
# this function drops the block to the bottom of the grid and stops it 
def drop_block():
    can_drop =True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                if block.y +y >= rows - 1:
                    can_drop = False
    if can_drop:
        block.y += 1
    else:
        for y in range(3):
           for x in range(3):
               if y * 3 + x in block.shape():
                   game_board[x + block.x][y+block.y]= (0,255,0)
    return can_drop
                   
#this funtion make the left and right borders and does not let you go passed them  
def side_move(dx):
    can_move = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                if x +block.x >=cols -1 and dx == 1:
                    can_move=False
                elif x+block.x< 1 and dx == -1:
                    can_move=False
    if can_move:                
        block.x +=dx
    else: 
        drop_block()



grid_size = 30 
pygame.init()
screen = pygame.display.set_mode((800,400))
rows = screen.get_height() //grid_size
cols = screen.get_width()// grid_size
x_gap = (screen.get_width()- cols * grid_size)//2
y_gap = (screen.get_height()- rows * grid_size)//2
# block start location
block =Block((cols - 1 )//2,0)
# this is the title if the window
pygame.display.set_caption("Tetris")
game_over = False
clock =pygame.time.Clock()
# this speeds up or slow downs the game play 
fps = 10
#this code will store the grid internally and it will store the block as a color in the grid
game_board = []
for i in range(cols):
   new_col = []   
   game_board.append(new_col)
   for j in range(rows):   
       new_col.append((0,0,0))

# this is the game loop for tetris
while not game_over:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            continue
    #this event is checking if the left or right key was pressed 
        
    if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_LEFT:
            side_move(-1)
        if event.key == pygame.K_RIGHT:
            side_move(+1)
            
    if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_UP:
                rotate()    
    screen.fill((210,210,210))
        #this is to make the vertical rows in the grid
    draw_grid()
    if block is not None:
        draw_block()
    #this event make the "gravity stop when you hold the left and right keys  "
        if event.type != pygame.KEYDOWN:
            if not drop_block():
                block = Block(random.randint(5,cols -5),0)
            
    pygame.display.update()
pygame.quit()