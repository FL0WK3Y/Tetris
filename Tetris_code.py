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

colors = [ 
(250,0,90) , (90,250,120),(90,100,250), (150,58,100), (100, 50 ,200),(150,0,0)  ,(0,0,150)
]
class Block:
    def __init__(self,x,y) :
        self.x= x
        self.y= y
        self.type =  random.randint(0,len(blocks)-1)
        self.rotation = 0
        self.colors = colors[random.randint(0,len(colors)-1)]
    def shape(self):
      return blocks[self.type][self.rotation] 
def draw_block():
    for y in range(3):
        for x in range(3) :
           # this is flattening the array and then it checks if it has the index inside of the block shape 
           # rambow color block //pygame.draw.rect(screen,(random.randint(0,255),random.randint(0,255),random.randint(0,255))
           if y * 3 + x in block.shape():
               pygame.draw.rect(screen,block.colors,
                                [(x+block.x)*grid_size + x_gap+1, (y + block.y) * grid_size + y_gap + 1, grid_size -2 , grid_size -2] )

def rotate():
    last_rotation = block.rotation 
    block.rotation = (block.rotation+ 1)% len(blocks[block.type])
    can_rotate = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                if collides(0,0):
                    can_rotate = False
    if not can_rotate:
        block.rotation = last_rotation
def draw_grid():
    for y in range(rows): 
        #this is to make the horizantal collums in the grid
        for x in range (cols):
    
        #this is to make the grid for tetris
            pygame.draw.rect(screen,(100,100,100), [x * grid_size + x_gap , y * grid_size + y_gap ,grid_size,grid_size],1)    
            if game_board[x][y] !=(0,0,0):
                pygame.draw.rect(screen,game_board[x][y], [x * grid_size + x_gap +1 , y * grid_size + y_gap +1 ,grid_size -1,grid_size -1])    
            
def collides(nx,ny):
    collision =False
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                if x +block.x + nx <0 or x +block.x +nx > cols -1:
                    collision = True
                    break
                if y +block.y + ny <0 or y +block.y +ny > rows -1:
                    collision = True
                    break
                if game_board[x+ block.x +nx][y+block.y +ny] != (0,0,0):
                    collision= True
                    break 
    return collision


# this function drops the block to the bottom of the grid and stops it 
def drop_block():
    can_drop =True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                if collides(0,1):
                    can_drop = False
    if can_drop:
        block.y += 1
    else:
        for y in range(3):
           for x in range(3):
               if y * 3 + x in block.shape():
                   game_board[x + block.x][y+block.y]= block.colors
    return can_drop
                   
#this funtion make the left and right borders and does not let you go passed them  
def side_move(dx):
    can_move = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                if collides(dx,0):
                    can_move=False
                
    if can_move:                
        block.x +=dx
    else: 
        drop_block()
# This code is to delete a line of blocks. once the game board have no more black spots in a line on the x axis then it get rid of that line
def find_lines():
    lines = 0
    for y in range(rows):
        empty = 0
        for x in range (cols):
            if game_board[x][y] ==(0,0,0):
              empty += 1
        if empty == 0:
            lines += 1
            for y2 in range(y,1,-1):
                for x2 in range(cols):
                    game_board[x2][y2] = game_board[x2][y2 - 1]
    return lines

grid_size = 30 
pygame.init()
screen = pygame.display.set_mode((400,800))
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
score = 0
font = pygame.font.SysFont('Arial',35, True, False)
font2 = pygame.font.SysFont('Arial',70, True, False)
finished_text = font2.render("Game Over ", True, (255,255,255),(1,1,1))
game_finished = False
ftpos = ((screen.get_width()-finished_text.get_width())//2,(screen.get_height()-finished_text.get_height())//2)
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
            if not drop_block() and not game_finished:
                score += find_lines()
                block = Block(random.randint(2,cols -5),0)
                if collides(0,0):
                    game_finished = True
    
    # this code displays and updates the score
    text = font.render("Score: " + str(score), True , (2,2,2),(150,150,150) ) 
    if game_finished == True:
        screen.blit(finished_text,ftpos)
    
    screen.blit(text ,[0,0]) 
    pygame.display.update()
    
pygame.quit()