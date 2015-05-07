import pygame
import collections
from random import randint

width = 800
height = width/16*9

scaling_CONSTANT = 20
hitbox_visible = True
movedist = 10

ignoredwords = ["the","to","in","on","of","and","i","a"]
punctuation = [".","?","!",")","(",":",";","'s","-"]

allHitboxes = []
allLabels = pygame.sprite.Group()

screen = pygame.display.set_mode((width,height))

def open_file(textlocation):
    print "file opened"
    file = open(textlocation,'r') # open text file
    return file.read().lower().split() # turn into list

def CountAndSort(wordstream, ignoredwords, punctuation):
    print "counted and sorted"
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

    
class Label(pygame.sprite.Sprite):
    def __init__(self,word, frequency):
        pygame.sprite.Sprite.__init__(self)
        self.xpos = width/2
        self.ypos = height/2
        colour = (randint(0, 255), randint(0, 255), randint(0, 255)) # generates colour randomly
        pygame.font.init()
        Font = pygame.font.SysFont("Fixedsys",Label.scale(self, frequency))
        text = Font.render(word, True, colour)
        hitbox = Label.generate_hitbox(self, text, colour)
    
    def generate_hitbox(self, text, colour):
        dimensions = text.get_rect() # gets the dimensions of the text object

        # allow for visible/invisible hitboxes
        if hitbox_visible == False:
            colour = (255, 255, 255)
            
        # create hitbox
        hitbox = pygame.draw.rect(text, colour, (dimensions), 1)

        # add to list of all hitboxes
        allHitboxes.append(hitbox)
        return hitbox
    
    def scale(self,frequency):
        # scales word based upon relative frequency
        scale = int(int(frequency/lowestfrequency)*scaling_CONSTANT)
        return scale

def reposition():
    print "block repositioned"
    # reposition words based upon collisions
    
def generate_WordCloud(sortedWords):
    print "wordcloud generated"
    
    for word in sortedWords:
        lab = Label(word[0],word[1])
        allLabels.add(lab)
        
##    for label in allLabels:
##        reposition(label)


def main():
    pygame.display.set_caption("Word Cloud")

    # create display
    pygame.init()
    background_colour = (255,255,255) # colour is white
    screen.fill(background_colour)
    
    #configure background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(background_colour)


    screen.blit(background, (0,0))
    
    loop = True
    
    while loop:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                loop = False
                
        pygame.display.flip()

    pygame.quit()    


wordstream = open_file("sampletext.txt")
sortedWords = CountAndSort(wordstream, ignoredwords, punctuation)
lowestfrequency = sortedWords[len(sortedWords)-1][1]

generate_WordCloud(sortedWords)

main()
