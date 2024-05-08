import random
import pgzrun
FONT_COLOR=(255,255,255)
WIDTH=800
HEIGHT=600
score=0
CENTER_X=WIDTH/2
CENTER_Y=HEIGHT/2
CENTER=(CENTER_X,CENTER_Y)
FINAL_LEVEL=2
START_speed=10
game_timer = 10 
COLORS= ["green", "blue"]
game_over = False 
game_complete = False 
current_level = 1
dots = [] 

basket=Actor('basket2')
basket.x = WIDTH // 2
basket.y = HEIGHT - 40
def draw():
    
    global dots,current_level,game_over,game_complete
    screen.clear
    screen.fill('blue')
    screen.draw.text("score: "+str(score),color="black",topleft=(10,10))
    if game_over:
        display_message('GAME OVER!',"good luck next time")
        dots=[]
    elif game_complete:
        display_message('finished ','come and win again')
        dots=[]
    else:
        for dot in dots:  
            dot.draw()
            level()    
        basket.draw()

def move_basket():
    if keyboard.left:
        basket.x -= 5
    elif keyboard.right:
        basket.x += 5
    global score    
for dot in dots:   
    dot_collected=basket.colliderect(dot)
    if(dot_collected):
        score=score+10    
    if(score==50):
        current_level=current_level+1
def update():
    move_basket()
    global dots
    global current_level
    if len(dots)==0:
        dots=make_dots(current_level)
    for dot in dots:
        global score
        if dot.y > HEIGHT + 40:
           position_dot()
        else:
            dot.y += 10
        if dot.colliderect(basket):
           score += 10
           print(score)
           position_dot() 
        
def create_dots(colors_to_create):
    new_dots=[]
    for color in colors_to_create:
         dot=Actor(color+"-dot")
         new_dots.append(dot)
    return new_dots          
def make_dots(number_of_extra_dots):
    colors_to_create=get_colors_to_create(number_of_extra_dots)
    new_dots = create_dots(colors_to_create)
    layout_dots(new_dots)
    return new_dots
def get_colors_to_create(number_of_extra_dots):
    colors_to_create=['red']
    for i in range(0,number_of_extra_dots):
        random_color=random.choice(COLORS)
        colors_to_create.append(random_color)
        return colors_to_create
        



def layout_dots(dots_to_layout):
    number_of_gaps = len(dots_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(dots_to_layout)
    for index, dot in enumerate(dots_to_layout):
        new_x_pos = (index + 1) * gap_size
        dot.x = new_x_pos
  


def handle_game_over():   
    global game_over
    game_over = True

def position_dot():
    for dot in dots:
        dot.x = random.randint(40, WIDTH - 40)
        dot.y = -100

 
def level():
    global current_level, dots, game_complete,score
    if score == 200:
       game_complete = True
       dots = []
    else:
        if(score==50):
            display_message('level 2',"play fast")
           
def time_up():
    if(game_complete==False):
        global game_over
        game_over=True
def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize=60, center=CENTER, color=FONT_COLOR)
    screen.draw.text(sub_heading_text, 
    fontsize=30, 
    center=(CENTER_X, CENTER_Y + 30), 
    color=FONT_COLOR)
clock.schedule(time_up,30.0)    
pgzrun.go()



