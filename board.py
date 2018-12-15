import random
import pygame
from pygame.locals import *
from sys import exit




boradSize = 480
lines = 12
step = (int)(0.8*boradSize/lines)

Colors = {'black':-1,'white':1}

def Computer():
	max = lines
	i = random.randint(0, max)
	j = random.randint(0, max)
	print((i,j))
	return (i,j)
def Hunman():
	event = pygame.event.wait()
	while (event.type == QUIT) or (event.type == MOUSEBUTTONDOWN):
		if event.type == QUIT:  # 接收到退出事件后退出程序
			exit()
		elif event.type == MOUSEBUTTONDOWN: # 鼠标按下则计算位置
			x = (int)((event.pos[0] - boradSize/10 + 0.5*step) / step)
			y = (int)((event.pos[1] - boradSize/10 + 0.5*step) / step)
			print((x,y))
			return (x,y)
		else:
			event = pygame.event.wait()
	'''
	for event in pygame.event.get():
		if event.type == QUIT:  # 接收到退出事件后退出程序
			exit()
		if event.type == MOUSEBUTTONDOWN: # 鼠标按下则计算位置
			x = (int)((event.pos[0] - boradSize/10 + 0.5*step) / step)
			y = (int)((event.pos[1] - boradSize/10 + 0.5*step) / step)
			print((x,y))
			return (x,y)
	'''	
class board:
	nowColor = -1
	nowTurns = 1
	datas = []
	#初始化大小及棋盘，用包含子列表的列表存储列表信息
	def __init__(self,sz=4):
		self.size = sz
		self.data = [[0]*sz]
		for i in range(1,sz):
			self.data.append([0]*sz)
		'''
		error!
		while
		self.data = [[0]][sz]][sz
		can't change one element by self.data[x][y]
		if self.data[1][1] = -1
		out:
		[0, -1, 0, 0]
		[0, -1, 0, 0]
		[0, -1, 0, 0]
		[0, -1, 0, 0]
		'''
		self.datas.append(self.data)
	#显示当前棋盘情况，调试用
	def display(self):
		for row in self.data:
			print (row)
		print('nowTurns:',self.nowTurns,'nowColor:',self.nowColor)
	def putAchess(self,posi):
		if(posi == None):
			return False
		x = posi[0]
		y = posi[1]
		if self.data[y][x] == 0:
			self.data[y][x] = self.nowColor
			return True
		else:
			return False
		self.data[x][y] = self.nowColor
	def action(self,who):
		#max = self.size-1
		if self.nowTurns == 1:
			#i = random.randint(0, max)
			#j = random.randint(0, max)
			while self.putAchess(who())==False:
				pass
		else:	
			for e in range(2):
				#i = random.randint(0, max)
				#j = random.randint(0, max)
				while self.putAchess(who())==False:
					#i = random.randint(0, max)
					#j = random.randint(0, max)
					pass
		print(self.nowColor,"finshed")
		self.nowTurns += 1
		self.nowColor *= -1
		self.datas.append(self.data)
class checker:
	def check(Board,M):
	    for i in range(0,M+1):
	        for j in range(0,M+1):
	            if   (i+5<=M)and(Board[i][j]==1)and(Board[i+1][j]==1)and(Board[i+2][j]==1)and(Board[i+3][j]==1)and(Board[i+4][j]==1)and(Board[i+5][j]==1):
	                print("player1 win")
	                return 1
	                break
	            elif (j+5<=M)and(Board[i][j]==1)and(Board[i][j+1]==1)and(Board[i][j+2]==1)and(Board[i][j+3]==1)and(Board[i][j+4]==1)and(Board[i][j+5]==1):
	                print("player1 win")
	                return 1
	                break
	            elif (i+5<=M)and(j+5<=M)and(Board[i][j]==1)and(Board[i+1][j+1]==1)and(Board[i+2][j+2]==1)and(Board[i+3][j+3]==1)and(Board[i+4][j+4]==1)and(Board[i+5][j+5]==1):
	                print("player1 win")
	                return 1
	                break
	            elif (j+4<=M)and(Board[M-i-1][j]==1)and(Board[(M-i-2)][j+1]==1)and(Board[(M-i-3)][j+2]==1)and(Board[(M-i-4)][j+3]==1)and(Board[(M-i-5)][j+4]==1)and(Board[(M-i-6)][j+5]==1):
	                print("player1 win")
	                return 1
	                break
	            elif (i+5<=M)and(Board[i][j]==-1)and(Board[i+1][j]==-1)and(Board[i+2][j]==-1)and(Board[i+3][j]==-1)and(Board[i+4][j]==-1)and(Board[i+5][j]==-1):
	                print("player2 win")
	                return -1
	                break
	            elif (j+5<=M)and(Board[i][j]==-1)and(Board[i][j+1]==-1)and(Board[i][j+2]==-1)and(Board[i][j+3]==-1)and(Board[i][j+4]==-1)and(Board[i][j+5]==-1):
	                print("player2 win")
	                return -1
	                break
	            elif (i+5<=M)and(j+5<=M)and(Board[i][j]==-1)and(Board[i+1][j+1]==-1)and(Board[i+2][j+2]==-1)and(Board[i+3][j+3]==-1)and(Board[i+4][j+4]==-1)and(Board[i+5][j+5]==-1):
	                print("player2 win")
	                return -1
	                break
	            elif (j+4<=M)and(Board[M-i-1][j]==-1)and(Board[(M-i-2)][j+1]==-1)and(Board[(M-i-3)][j+2]==-1)and(Board[(M-i-4)][j+3]==-1)and(Board[(M-i-5)][j+4]==-1)and(Board[(M-i-6)][j+5]==-1):
	                print("player2 win")
	                return -1
	                break
	    return 0
def drawLines(background,step):
	for i in range(0,(int)(0.8*boradSize)+1,step):
		pygame.draw.line(background, (0,0,0), (boradSize/10,boradSize/10+i), (9*boradSize/10,boradSize/10+i), 2)
		pygame.draw.line(background, (0,0,0), (boradSize/10+i,boradSize/10), (boradSize/10+i,9*boradSize/10), 2)
def drawChese(screen,posi,color):
	if(posi == None):
		return
	x0 = (int)(boradSize/10)
	if(color == -1):
		c = (0,0,0)
	elif(color == 1):
		c = (255,255,255)
	p = (posi[0]*step+x0,posi[1]*step+x0)
	pygame.draw.circle(screen, c, p, (int)(0.3*boradSize/lines), 0)
def drawALL(Board,screen):
	for i in range(Board.size):
		for j in range(Board.size):
			if Board.data[i][j] != 0:
				drawChese(screen, (j,i), Board.data[i][j])
if __name__ == "__main__":
	# pygame窗口的初始化
	pygame.init()
	font = pygame.font.SysFont("arial", 30)
	font_height = font.get_linesize()
	background = pygame.image.load('C:/Users/辜俊/Desktop/素材/棋盘.jpg')
	screen = pygame.display.set_mode((boradSize, boradSize))
	pygame.display.set_caption("六子棋")
	drawLines(background, step)
	# 棋盘数据的初始化

	x = board(lines+1)

	while True:
		screen.blit(background, (0, 0))  # 画上背景图
		drawALL(x, screen)
		pygame.display.update()
		if x.nowColor == -1 :
			x.action(Hunman)
		elif x.nowColor == 1:
			x.action(Computer)

		if checker.check(x.data, lines) != 0:
			print ("game over")
			screen.blit(background, (0, 0))  # 画上背景图
			drawALL(x, screen)
			screen.blit( font.render("Game over", True, (0, 255, 0)), (2*boradSize/5-10,boradSize/3 ) )

			break
		else:
			print ("game continue")

		x.display()
		for event in pygame.event.get():
			if event.type == QUIT:  # 接收到退出事件后退出程序
				exit()
	while True:
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == QUIT:  # 接收到退出事件后退出程序
				exit()

'''
日志
11.30

bugs暂无

需要的优化：
增加重启功能；
增加黑白方选择；
增加悔棋功能；
增加棋谱输出；


'''