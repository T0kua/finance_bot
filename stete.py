import pygame
from pygame.locals import *
import sqlite3
import datetime
import os
from PIL import Image, ImageGrab
pygame.init()
def get():
	div = (__file__[0:-8]) #путь к папке файлом
	db = sqlite3.connect("test.db",check_same_thread=False)
	sql = db.cursor()
	db.commit()

	width = 800
	height = 480
	screen = pygame.display.set_mode((width,height))
	#font = pygame.font.SysFont("comicsansms", 15)

	time = datetime.datetime.today()
	date = str(time)[:10]#age   month     day
	age = int(date[:4])
	month = int(date[5:7])
	def flip():
		pygame.display.flip()
	List = []					
	for val in sql.execute(f"SELECT * FROM tabl WHERE age = {age}"):
		if val[3] == month:
			List.append([val[2],val[0]])
	week = []
	for j in range(1,32):
		plus = 0
		munus = 0
		for i in range(len(List)):
			if List[i][0] == j :
				if List[i][1] > 0 :
					plus += List[i][1]
				else :
					munus += List[i][1]
				if len(week) >= 1 :
					for w in range(len(week)):
						if week[w][0] == j :
							week[w][0] = j
							week[w][1] = plus
							week[w][2] = munus
						else :
							week.append([j,plus,munus])
				else :
					week.append([j,plus,munus])
	days = []
	for i in range(len(week)):
		if week[i] in week :
			if week[i] in days :
				pass
			else :
				days.append(week[i])
	print(days)
	maxsize = 0
	font = pygame.font.SysFont("comicsansms", 15)
	for i in range(len(days)) :
		if days[i][1] > maxsize :
			maxsize = days[i][1]
	def draw(days):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		screen.fill( (255,255,255))
		for n in range(len(days)):
			y = 40
			w = 450 / len(days) -1
			if n == 0 :
				x = 1
			else:
				x = ((n + 1)  + n * w)
			h = maxsize / 450
			h1 = days[n][1] * h #plus
			h2 = days[n][2] * h #munus
			pls = str(days[n][1])
			mns = str(-days[n][2])
			vpls = font.render(pls, True,(255,255,255))
			vmns = font.render(mns, True,(255,255,255))
			daz = font.render(str(days[n][0]),True,(0,0,0))
			screen.blit(daz,[x + w/2,20])
			if days[n][1] > days[n][2] :
							# red green blue
				pygame.draw.rect(screen, (200,0,0) , (x,y,w,h1),0) #plus
				screen.blit(vpls, [x + w/2,h1])
				pygame.draw.rect(screen, (0,0,200) , (x,y,w,-h2),0) #munus
				screen.blit(vmns,[x + w/2,-h2])
			elif days[n][2] > days[n][1] :
				pygame.draw.rect(screen, (0,0,200) , (x,y,w,-h2),0) #munus
				screen.blit(vmns,[x + w/2,-h2])
				pygame.draw.rect(screen, (200,0,0) , (x,y,w,h1),0) #plus
				screen.blit(vpls, [x + w/2,h1])
			else :
				pygame.draw.rect(screen, (30,30,30) , (x,y,w,maxsize / 50),0) #zero
	for i in range(100):
		pygame.display.flip()
		draw(days)

	img = ImageGrab.grab()
	img.save(f"{div}table.jpg","BMP")
	im = Image.open(f'{div}table.jpg')
	im.crop((600,300,1360,780)).save(f'{div}table.jpg', quality=95)
if __name__ == "__main__" :
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		get()
