## imports
import pygame
import collections
from random import randint

file = open("sampletext.txt",'r') # open text file
wordstream = file.read().lower().split() # turn into list

# things to remove
ignoredwords = ["the","to","in","on","of","and","i","a"]
punctuation = [".","?","!",")","(",":",";","'s","-"]

# constants
scaling_CONSTANT = 20
hitbox_visible = True
movedist = 100

## DISPLAY

# dimensions
width = 800
height = width/16*9

pygame.init()

screen = pygame.display.set_mode((width,height))

# colour
background_colour = (255,255,255) # colour is white
screen.fill(background_colour)

#configure background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(background_colour)

screen.blit(background, (0,0))

# of all hitboxes on the stage
allhitboxes = []

## COUNT WORDS ##
def CountAndSort(wordstream, ignoredwords, punctuation):
    # remove ignored words
    wordstream = [item for item in wordstream if item not in ignoredwords]

    # strip punctuation
    for word in wordstream:
        for punct in punctuation:
            if punct in word:
                word = word.replace(punct,"")

    # get 50 most common words
    sortedWords = collections.Counter(wordstream).most_common(50)
    return sortedWords


def generate_hitbox(label,posx,posy,colour):
    dimensions = label.get_rect() # gets the dimensions of the text object

    # allow for visible/invisible hitboxes
    if hitbox_visible == False:
        colour = (255, 255, 255)
        
    # create hitbox
    hitbox = pygame.draw.rect(label, colour, (dimensions), 1)

    # add to list of all hitboxes
    allhitboxes.append(hitbox)
    return hitbox


def reposition(label, hitbox):
    currx = width/2
    curry = height/2
    # move until no longer colliding
    xrand = randint(1,2) #left or right
    yrand = randint(1,2) #up or down
    newx = movedist * (-1)^xrand
    newy = movedist * (-1)^yrand

    # test collision
    for otherhitbox in allhitboxes:
        while hitbox.colliderect(otherhitbox) == True:        
            currx += newx
            curry += newy

            hitbox = hitbox.move(newx, newy)
            screen.blit(background, label.get_rect())
            screen.blit(label, (currx, curry))
        
        
                
    
    # move block randomly until it no longer collides
    
def place(word, frequency, posx, posy):
    pygame.font.init()

    # generates colour randomly
    colour = (randint(0, 255), randint(0, 255), randint(0, 255))
    Font = pygame.font.SysFont("Fixedsys",scale(word[1]))
    label = Font.render(word[0], True, colour)


    hitbox = generate_hitbox(label,posx,posy,colour)

    #reposition(label, hitbox)
                              
    # for testing purposes
    #print "COORDS of","'"+word[0]+"'", "x:",posx, "y:",posy,"|| Font Size", scale(word[1])

    screen.blit(label,(posx,posy))
        

def generateCloud():
    for word in sortedWords:
        #Randomise (temp)
        ranx  = randint(0,width)
        rany = randint(0,height)
        ## places words at the centre
        ranx = width/2
        rany = height/2
        place(word, word[0], ranx, rany)
        
        
def scale(frequency):
    ## apply scaling
    ## scaling variable^frequency/lowest frequency
    scale = int(int(frequency/lowestfrequency)*scaling_CONSTANT)
    return scale



## MAIN LOOP ##
def main(): 
    pygame.display.set_caption("Word Bubble")
    clock = pygame.time.Clock()
    
    pygame.mouse.set_visible(True)

    ## pygame loop
    loop = True

    generateCloud()

 

    while loop:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                loop = False
                clock.tick(500)

        pygame.display.flip()

    pygame.quit()    
  


sortedWords = CountAndSort(wordstream, ignoredwords, punctuation)
lowestfrequency = sortedWords[49][1]
main()

    
