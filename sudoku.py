'''
This is an interactive sudoku game
Author: arkyaC
Date of Creation: 3rd April 2k16
'''

import pygame,sys,random,time
from pygame.locals import *

WINDOWHEIGHT = 500
WINDOWWIDTH = 500

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)

BOXCOLOUR = GRAY
HIGHLIGHT = CYAN
CLICKED = BLUE
BGCOLOUR = NAVYBLUE
TEXTCOLOUR = BLACK


def main():
	global FPSCLOCK, DISPLAYSURF
	pygame.init()
	FPSCLOCK=pygame.time.Clock()
	DISPLAYSURF=pygame.display.set_mode((WINDOWHEIGHT,WINDOWWIDTH))
	pygame.display.set_caption('Sudoku Masters')
	global smallFont
	smallFont=pygame.font.Font('./fonts/arial.ttf',16)
	global largeFont
	largeFont=pygame.font.Font('./fonts/arial.ttf',28)
	largeFont.set_italic(True)
	print 'init done'


	welcomeScr()

	mousex = 0
	mousey = 0
	board = [[0 for x in range(9)] for x in range(9)]
	#print board
	x=fillUp(board)
	printBoard(board)
	print 'filled up'

	displayedBoard = board
	makeSpaces(displayedBoard,board)
	printBoard( displayedBoard)
	print "stage 1 complete"

	#welcomeScr()

	DISPLAYSURF.fill(BGCOLOUR)
	
	#textSurfaceObj=fontObj.render('Welcome to Sudoku Masters!',True,(0,0,0))
	#textRectObj=textSurfaceObj.get_rect()
	#textRectObj.center=(200,150)

	while True:
		mouseClicked = False

        DISPLAYSURF.fill(BGCOLOUR) # drawing the window
        

        for event in pygame.event.get():
	        if event.type == QUIT:
	            pygame.quit()
	            sys.exit()



def fillUp(board):
	pos = [0,0]
	if not findUnassigned(board,pos):
		return True
	for i in range(1,10):
		if(isSafe(board,pos[0],pos[1],i)):
			board[pos[0]][pos[1]]=i
			if(fillUp(board)): #solvable
				return True
			board[pos[0]][pos[1]]=0
	return False #backtrack

def isSafe(board,row,col,num):
	for i in range (9):
		if board[i][col]==num:
			return False
		if board[row][i]==num:
			return False
	for i in range (row/3*3,row/3*3+3):
		for j in range (col/3*3,col/3*3+3):
			if board[i][j]==num:
				return False
	return True


def makeSpaces(displayedBoard,board):
	ctr=0
	while ctr<50: #make 50 (1) empty cells
		for i in range(0,9):
			a=random.randint(0,8)
			while displayedBoard[i][a]==0:
				a=random.randint(0,8)
			displayedBoard[i][a]=0
			ctr+=1
			if not unique(displayedBoard):
				displayedBoard[i][a]=board[i][a]
				ctr-=1
		for i in range(0,9):
			a=random.randint(0,8)
			while displayedBoard[a][i]==0:
				a=random.randint(0,8)
			displayedBoard[a][i]=0
			ctr+=1
			if not unique(displayedBoard):
				displayedBoard[a][i]=board[a][i]
				ctr-=1

def unique(displayedBoard):
	testBoard=displayedBoard
	if not fillUp(testBoard):
		return False
	board1=displayedBoard
	board2=displayedBoard
	fillUp(board1)
	fillUp(board2)
	for i in range(0,8):
		for j in range(0,8):
			if board1[i][j]!=board2[i][j]:
				return False
	return True


def findUnassigned(board,pos):
	for i in range (9):
		for j in range(9):
			if board[i][j]==0:
				pos[0]=i
				pos[1]=j
				return True
	return False
	
def welcomeScr():
	DISPLAYSURF.fill(BGCOLOUR)
	welcomeMessage=largeFont.render('Welcome to Sudoku Masters',True,WHITE)
	welcomeRect=welcomeMessage.get_rect()
	welcomeRect.center=(WINDOWWIDTH/2,WINDOWHEIGHT/2)
	DISPLAYSURF.blit(welcomeMessage,welcomeRect)
	pygame.display.update()
	time.sleep(1)
	DISPLAYSURF.fill(BGCOLOUR)
	welcomeMessage=smallFont.render('Created by blah blah...',True,WHITE)
	welcomeRect=welcomeMessage.get_rect()
	welcomeRect.center=(WINDOWWIDTH/2+100,WINDOWHEIGHT/2+100)
	DISPLAYSURF.blit(welcomeMessage,welcomeRect)
	pygame.display.update()
	time.sleep(1)
	DISPLAYSURF.fill(BGCOLOUR)
	pygame.display.update()

def printBoard(board):
	for i in range(0,9):
		print board[i]
main()