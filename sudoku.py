'''
This is an interactive sudoku game
Author: arkyaC
Date of Creation: 3rd April 2k16
'''

import pygame,sys,random,time
from pygame.locals import *
from copy import deepcopy

WINDOWHEIGHT = 500
WINDOWWIDTH = 500
BOXSIZE = 50
LEFTMARGIN = 25
TOPMARGIN = 20
BOXMARGIN = 2
BOXEFF = BOXSIZE - 2*BOXMARGIN

FPS = 30

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
ORIGINAL = (128, 128, 255)
LINECOLOUR = ORANGE

pygame.init()

DISPLAYSURF=pygame.display.set_mode((WINDOWHEIGHT,WINDOWWIDTH))
FPSCLOCK=pygame.time.Clock()
pygame.display.set_caption('Sudoku Masters')

#Font
smallFont=pygame.font.Font('./arial.ttf',16)
largeFont=pygame.font.Font('./arial.ttf',28)
largeFont.set_italic(True)



def main():

	mousex = 0
	mousey = 0



	board = [[0 for x in range(9)] for x in range(9)]
	fillUp(board)


	displayedBoard = [[0 for x in range(9)] for x in range(9)]
	originalBoard = [[0 for x in range(9)] for x in range(9)]
	for i in range(9):
		for j in range(9):
			displayedBoard[i][j]=board[i][j]

	#printBoard(board)
	#print 'filled up'


	#displayedBoard = deepcopy(board)
	makeSpaces(displayedBoard,board)
	#originalBoard = deepcopy(displayedBoard)
	
	for i in range(9):
		for j in range(9):
			originalBoard[i][j]=displayedBoard[i][j]

	welcomeScr()
	DISPLAYSURF.fill(BGCOLOUR)
	smallFont.set_bold(True)

	while True:
		mouseClicked = False
		#print 1
		DISPLAYSURF.fill(BGCOLOUR) # drawing the window
		displayCurrent(displayedBoard,originalBoard)
		#displayCurrent(board)

		for event in pygame.event.get():

			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			
			elif event.type==MOUSEMOTION:
				mousex,mousey=event.pos
				#print 1
			elif event.type==MOUSEBUTTONUP:
				mousex,mousey=event.pos
				mouseClicked=True
				#print 2

		row,col = getBoxAtPixel(mousex,mousey)
		#print row,col
		if row!=None and col!=None:
			if displayedBoard[row][col]==0:
				highLight(row,col,displayedBoard,originalBoard)
			if mouseClicked==True:
				print 100
		pygame.display.update()
		FPSCLOCK.tick(FPS)

def fillUp(board):
	box = [0,0]
	if not findUnassigned(board,box):
		return True
	for i in range(1,10):
		if(isSafe(board,box[0],box[1],i)):
			board[box[0]][box[1]]=i
			if(fillUp(board)): #solvable
				return True
			board[box[0]][box[1]]=0
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
	while ctr<50: #make 50 empty cells
		print ctr
		for i in range(0,9):
			a=random.randint(0,8)
			#print a
			while displayedBoard[i][a]==0:
				a=random.randint(0,8)
			displayedBoard[i][a]=0
			printBoard(displayedBoard)
			ctr+=1
			#print unique(displayedBoard)
			if not unique(displayedBoard):
				displayedBoard[i][a]=board[i][a]
				ctr-=1
				#print 1
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
	
	testBoard = [[0 for x in range(9)] for x in range(9)]
	for i in range(9):
		for j in range(9):
			testBoard[i][j]=displayedBoard[i][j]
	if not fillUp(testBoard):
		return False
	

	board1 = [[0 for x in range(9)] for x in range(9)]
	for i in range(9):
		for j in range(9):
			board1[i][j]=displayedBoard[i][j]

	board2 = [[0 for x in range(9)] for x in range(9)]
	for i in range(9):
		for j in range(9):
			board2[i][j]=displayedBoard[i][j]

	fillUp(board1)
	fillUp(board2)
	for i in range(0,9):
		for j in range(0,9):
			if board1[i][j]!=board2[i][j]:
				return False
	return True


'''def findUnassigned(board,box):
	for i in range (9):
		for j in range(9):
			if board[i][j]==0:
				box[0]=i
				box[1]=j
				return True
	return False'''

def findUnassigned(board,box):
	unassigned=[]
	for i in range (9):
		for j in range(9):
			if board[i][j]==0:
				unassigned.append([i,j])
				if len(unassigned)>1:
					break
		else:
			continue
		break
	print unassigned
	if len(unassigned)==0:
		return False
	else:
		random.shuffle(unassigned)
		box[0]=unassigned[0][0]
		box[1]=unassigned[0][1]
		return True

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

def displayCurrent(board,originalBoard):
	for row in range(9):
		for col in range(9):
			if board[row][col]!=0:
				currBox=pygame.Rect(LEFTMARGIN+BOXMARGIN+BOXSIZE*col,TOPMARGIN+BOXMARGIN+BOXSIZE*row,BOXEFF,BOXEFF)
				if originalBoard[row][col]==0:
					pygame.draw.rect(DISPLAYSURF,CLICKED,currBox)
				else:
					pygame.draw.rect(DISPLAYSURF,ORIGINAL,currBox)
				data=smallFont.render(str(board[row][col]),True,TEXTCOLOUR)
				dataRect=data.get_rect()
				dataRect.center=currBox.center
				DISPLAYSURF.blit(data,dataRect)
			else:
				pygame.draw.rect(DISPLAYSURF,BOXCOLOUR,(LEFTMARGIN+BOXMARGIN+BOXSIZE*col,TOPMARGIN+BOXMARGIN+BOXSIZE*row,BOXEFF,BOXEFF))
	for row in range(8):
		width=2
		if row==2 or row==5:
			width=4
		pygame.draw.line(DISPLAYSURF,LINECOLOUR,(LEFTMARGIN,TOPMARGIN+(row+1)*BOXSIZE),(WINDOWWIDTH-LEFTMARGIN,TOPMARGIN+(row+1)*BOXSIZE),width)
	for col in range(8):
		width=2
		if col==2 or col==5:
			width=4
		pygame.draw.line(DISPLAYSURF,LINECOLOUR,(LEFTMARGIN+(col+1)*BOXSIZE,TOPMARGIN),(LEFTMARGIN+(col+1)*BOXSIZE,TOPMARGIN+9*BOXSIZE),width)
	pygame.draw.rect(DISPLAYSURF,LINECOLOUR,(LEFTMARGIN,TOPMARGIN,BOXSIZE*9,BOXSIZE*9),4)
	pygame.display.update()

def leftTopCoordsOfBox(boxx, boxy):
	left=LEFTMARGIN+boxx*BOXSIZE+BOXMARGIN
	top=TOPMARGIN+boxy*BOXSIZE+BOXMARGIN
	return (left,top)

def getBoxAtPixel(x,y):
	for row in range(0,9):
		for col in range(0,9):
			left, top = leftTopCoordsOfBox(col, row)
	   		boxRect = pygame.Rect(left,top,BOXEFF,BOXEFF)
	   		#print left,top
	   		if boxRect.collidepoint(x, y):
	   		    #print 'found box'
	   			return (row, col)
	return (None,None)

def highLight(row,col,displayedBoard,originalBoard):
	#pygame.draw.rect(DISPLAYSURF,HIGHLIGHT,(LEFTMARGIN+BOXMARGIN+BOXSIZE*col,TOPMARGIN+BOXMARGIN+BOXSIZE*row,BOXEFF,BOXEFF))
	if originalBoard[row][col]!=0:
		#print 1
		return
	currBox=pygame.Rect(LEFTMARGIN+BOXMARGIN+BOXSIZE*col,TOPMARGIN+BOXMARGIN+BOXSIZE*row,BOXEFF,BOXEFF)
	pygame.draw.rect(DISPLAYSURF,HIGHLIGHT,currBox)
	if displayedBoard[row][col]==0:
		return
	data=smallFont.render(str(board[row][col]),True,TEXTCOLOUR)
	dataRect=data.get_rect()
	dataRect.center=currBox.center
	DISPLAYSURF.blit(data,dataRect)


def printBoard(board):
	for i in range(0,9):
		print board[i]

if __name__ == '__main__':
    main()