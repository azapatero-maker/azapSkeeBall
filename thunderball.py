#! /usr/bin/python
## \file  thunderball.py

# Alfredo Zapatero
# Last updated on 6-30-2019
# Fixed quit logic and game over logic for each game
# Game 1 Done!
# Game 2 Started trying the countdown timer but not working yet.  30 second timer would be a great start. 
# Game 3 Works! Needs graphics upgrade. Correctly selects a "fire" hole randomly at start. scoring works.  Need to create point system
# Game 4 Shows masks when hit. Scoring bonuses, totals, and next level logic is not working yet
# Sounds and music arent working at all.  Try another menuclick sound. Check out bitrates and test to see if that's it.



import sys, pygame, random
from random import randint

#Initialize sounds
pygame.mixer.pre_init (44100,16,2,4096)

def main():
	# Initialize Pygame and create screensize
	pygame.init()
	screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 
	
	#screen.fill(background)
	#fonts
	scoreFont = pygame.font.SysFont("Ariel", 380)
	ballsFont = pygame.font.SysFont("Ariel", 80)
	
	#music and sounds
	pygame.mixer.music.set_volume(0.9)
	menu_sound = pygame.mixer.Sound("nenadsimicmenuclick.wav")
	point_sound = pygame.mixer.Sound("scrampunk__okay.wav")
	select_sound = pygame.mixer.Sound("josepharaoh99__select.wav")
	
	#load images
	bg = pygame.image.load("background.jpg") 
	mm = pygame.image.load("mainmenuwithbuttons.jpg")
	mmsplash = pygame.image.load("mainmenuspashscreen.jpg") 
	qu = pygame.image.load("sure-exit.jpg") 
	go = pygame.image.load("gameover.jpg")
	main01 = pygame.image.load("main1-classicskee.jpg") 
	main02 = pygame.image.load("main2-timedskee.jpg") 
	main03 = pygame.image.load("main3-onfire.jpg") 
	main04 = pygame.image.load("main4-skillz.jpg") 
	
	#set background image 
	screen.blit(mm, (0, 0))
	pygame.display.flip()
    
    # Ignore mouse motion (greatly reduces resources when not needed)
	pygame.event.set_blocked(pygame.MOUSEMOTION)
    	
	menustatus = 0
	gameselection = 0
	gamestart =0
	
	#Menu Loop
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_c:
					pygame.mixer.Sound.play(select_sound) 
					menustatus = 1
					gameselection = 1
					gamestart = 1
					main1()
				if event.key == pygame.K_v:
					pygame.mixer.Sound.play(select_sound) 
					#intro = False
					menustatus = 1
					gameselection =2
					main2()
				if event.key == pygame.K_p:
					pygame.mixer.Sound.play(select_sound) 
					#intro = False
					menustatus = 1
					gameselection = 3
					main3()
				if event.key == pygame.K_1:
					pygame.mixer.Sound.play(select_sound) 
					#intro = False
					menustatus = 1
					gameselection = 4
					main4()
				if event.key == pygame.K_w:
					quitgame = True
					intro = False
					pygame.quit()
					quit()
	
#Classic skeeball game
def gameLoop1():

	#Background Music and Sounds
	#pygame.mixer.music.load("hackthepolice.mp3")
	pygame.mixer.music.set_volume(0.5)
	#pygame.mixer.music.play(-1)
	point_sound = pygame.mixer.Sound("scrampunk__okay.wav")
	select_sound = pygame.mixer.Sound("josepharaoh99__select.wav")

	gameExit = False
	ballsOver = False

	score = 0
	balls = 9
	
	while not gameExit:
		
		while ballsOver == True: 
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						score = 0	
						gameLoop()
					if event.key == pygame.K_x:
						gameExit = True	
						ballsOver = False
						yousure()			
				
		for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_a:
						score += 10
						balls -= 1
						pygame.mixer.Sound.play(point_sound) 
					if event.key == pygame.K_s:
						score += 20
						balls -= 1
						pygame.mixer.Sound.play(point_sound)
					if event.key == pygame.K_d:
						score += 30
						balls -= 1
						pygame.mixer.Sound.play(point_sound)
					if event.key == pygame.K_f:
						score += 40
						balls -= 1
						pygame.mixer.Sound.play(point_sound)
					if event.key == pygame.K_g:
						score += 50
						balls -= 1
						pygame.mixer.Sound.play(point_sound)
					if event.key == pygame.K_l:
						score += 100
						balls -= 1
						pygame.mixer.Sound.play(point_sound)
					if event.key == pygame.K_j:
						score += 100
						balls -= 1
						pygame.mixer.Sound.play(point_sound)
					if event.key == pygame.K_p:
						score = 0
						balls = 9											
					if event.key == pygame.K_x:
						gameExit = True	
						yousure()
					if balls == 0:
						gameExit = True
						go = pygame.image.load("gameover.jpg") 
						screen.blit(go, (0, 0))
						pygame.display.flip()   
						oldlace = (253,245,230)
						black = (0,0,0)
						sienna = (160,82,45)
						myfont = pygame.font.Font("DS-DIGIB.TTF", 180) #Large font for score 
						label = myfont.render(str(score), 1, black) #for the scoring
						screen.blit(label, (380,100)) #put the score text on the screen
						pygame.display.update()	
						 
						showit1 = True
						while showit1:
							for event in pygame.event.get():
								if event.type == pygame.QUIT:
									pygame.quit()
									quit()
								if event.type ==pygame.KEYDOWN:
									if event.key == pygame.K_z:
										pygame.mixer.Sound.play(select_sound) 
										gameLoop1()
										showit1 = False
									if event.key == pygame.K_x:
										pygame.mixer.Sound.play(select_sound) 
										#screen.blit(mm, (0, 0))
										#pygame.display.flip()											
										splash1()
										showit1 = False
												 
		screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 
		screen2 = pygame.display.set_mode((800,480), pygame.NOFRAME) 
		bg = pygame.image.load("background.jpg") 
		cadetblue = (95,158,160)
		black = (0,0,0)
		sienna = (160,82,45)
		green = (0,255,0)
		myfont = pygame.font.Font('DS-DIGIB.TTF', 380) #pygame.font.SysFont("DS-DIGIB", 450) #Large font for score
		ballsfont = pygame.font.Font("DS-DIGIB.TTF", 118) #Small font for ball count
		label = myfont.render(str(score), 1, black) #for the scoring
		label2 = ballsfont.render(str(balls), 1, green) #for the balls
		
		screen.blit(bg,(0,0))
		screen2.set_alpha(15)
		pygame.draw.rect(screen2, black, [700,360,90,90]) 
		screen.blit(label, (180,20)) #put the score text on the screen
		screen.blit(label2, (722,345)) #put the ballcount text on the screen
		
		pygame.display.update()		
		
		
			

#Timed skeeball game
def gameLoop2():

	#Background Music and Sounds
	#pygame.mixer.music.load("hackthepolice.mp3")
	#pygame.mixer.music.set_volume(0.5)
	#pygame.mixer.music.play(-1)
	point_sound = pygame.mixer.Sound("scrampunk__okay.wav")
	select_sound = pygame.mixer.Sound("josepharaoh99__select.wav")
	
	gameExit = False
	ballsOver = False

	score = 0
	countdownclock = 10
	
	screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 
	screen2 = pygame.display.set_mode((800,480), pygame.NOFRAME) 
	bg = pygame.image.load("background.jpg") 
	cadetblue = (95,158,160)
	black = (0,0,0)
	sienna = (160,82,45)
	myfont = pygame.font.SysFont("Ariel", 450) #Large font for score
	ballsfont = pygame.font.SysFont("Ariel", 118) #Small font for ball count
	label = myfont.render(str(score), 1, black) #for the scoring
	label2 = ballsfont.render(str(countdownclock), 1, black) #for the clock
		
	screen.blit(bg,(0,0))
	#screen2.set_alpha(15)
	pygame.draw.rect(screen2, cadetblue, [700,300,90,90]) 
	screen.blit(label, (180,20)) #put the score text on the screen
	screen.blit(label2, (722,300)) #put the ballcount text on the screen
		
	while not gameExit:
		
		while ballsOver == True:
			
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						score = 0	
						gameLoop2()
					if event.key == pygame.K_x:
						gameExit = True	
						ballsOver = False
						yousure()	
		
		for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_a:
						score += 10
						#pygame.mixer.Sound.play(point_sound) 
					if event.key == pygame.K_s:
						score += 20
						#pygame.mixer.Sound.play(point_sound)
					if event.key == pygame.K_d:
						score += 30
						#pygame.mixer.Sound.play(point_sound)
					if event.key == pygame.K_f:
						score += 40
						#pygame.mixer.Sound.play(point_sound)
					if event.key == pygame.K_g:
						score += 50
						#pygame.mixer.Sound.play(point_sound)
					if event.key == pygame.K_l:
						score += 100
						#pygame.mixer.Sound.play(point_sound)
					if event.key == pygame.K_j:
						score += 100
						#pygame.mixer.Sound.play(point_sound)
					if event.key == pygame.K_p:
						score = 0											
					if event.key == pygame.K_x:
						gameExit = True	
						yousure2()
					if countdownclock == 0:
						gameExit = True
						showscore2()
		countdownclock -=1
		pygame.time.delay(1000)	

		pygame.display.update()		

#Fire skeeball game
def gameLoop3():

	#Background Music and Sounds
	#pygame.mixer.music.load("hackthepolice.mp3")
	#pygame.mixer.music.set_volume(0.5)
	#pygame.mixer.music.play(-1)
	point_sound = pygame.mixer.Sound("scrampunk__okay.wav")
	select_sound = pygame.mixer.Sound("josepharaoh99__select.wav")
	
	gameExit = False
	ballsOver = False

	score = 0
	balls = 9
	screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 
	screen2 = pygame.display.set_mode((800,480), pygame.NOFRAME) 
	bg = pygame.image.load("skillzbackground.jpg") 
	cadetblue = (95,158,160)
	black = (0,0,0)
	sienna = (160,82,45)
	myfont = pygame.font.SysFont("Ariel", 150) #Large font for score
	ballsfont = pygame.font.SysFont("Ariel", 118) #Small font for ball count
	firehole = random.randint(1,7)
	screen.blit(bg,(0,0))
	pygame.draw.rect(screen2, cadetblue, [700,300,90,90]) 
	
	while not gameExit:
		
		while ballsOver == True:
			
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_x:
						gameExit = True	
						ballsOver = False
						yousure3()	
									
		for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_a:  
						if firehole == 1:
							score += 1
							balls -= 1
							pygame.mixer.Sound.play(point_sound)
						else:
							balls -= 1	 
					if event.key == pygame.K_s:
						if firehole == 2:
							score += 1
							balls -= 1
							pygame.mixer.Sound.play(point_sound)	
						else:
							balls -= 1
					if event.key == pygame.K_d:
						if firehole == 3:
							score += 1
							balls -= 1
							pygame.mixer.Sound.play(point_sound)	
						else:
							balls -= 1
					if event.key == pygame.K_f:
						if firehole == 4:
							score += 1
							balls -= 1
							pygame.mixer.Sound.play(point_sound)
						else:
							balls -= 1
					if event.key == pygame.K_g:
						if firehole == 5:
							score += 1
							balls -= 1
							pygame.mixer.Sound.play(point_sound)
						else:
							balls -= 1
					if event.key == pygame.K_l:
						if firehole == 6:
							score += 1
							balls -= 1
							pygame.mixer.Sound.play(point_sound)
						else:
							balls -= 1
					if event.key == pygame.K_j:
						if firehole == 7:
							score += 1
							balls -= 1
							pygame.mixer.Sound.play(point_sound)
						else:
							balls -= 1
					if event.key == pygame.K_p:
						score = 0
						balls = 9											
					if event.key == pygame.K_x:
						gameExit = True	
						yousure3()
					if balls == 0:
						gameExit = True
						go = pygame.image.load("gameover.jpg") 
						screen.blit(go, (0, 0))
						pygame.display.flip()   
						oldlace = (253,245,230)
						black = (0,0,0)
						sienna = (160,82,45)
						myfont = pygame.font.Font("DS-DIGIB.TTF", 110) #Large font for score 
						label = myfont.render(str(score), 1, black) #for the scoring
						screen.blit(label, (380,100)) #put the score text on the screen
						pygame.display.update()	
						 
						showit1 = True
						while showit1:
							for event in pygame.event.get():
								if event.type == pygame.QUIT:
									pygame.quit()
									quit()
								if event.type ==pygame.KEYDOWN:
									if event.key == pygame.K_z:
										pygame.mixer.Sound.play(select_sound) 
										gameLoop3()
										showit1 = False
									if event.key == pygame.K_x:
										pygame.mixer.Sound.play(select_sound) 
										#screen.blit(mm, (0, 0))
										#pygame.display.flip()											
										splash1()
										showit1 = False
						
						#gameExit = True
						#showscore3()
		
		label = myfont.render(str(score), 1, black) #for the scoring
		label2 = ballsfont.render(str(balls), 1, black) #for the balls
		screen.blit(bg,(0,0)) # Displays background image
		screen.blit(label, (600,10)) #put the score text on the screen
		screen.blit(label2, (722,300)) #put the ballcount text on the screen
				
		#Displays the image on the hole that was randomly selected		
		if firehole == 1:
			mask = pygame.image.load("fsocietymask.jpg") 
			screen.blit(mask, (400,280))
		if firehole == 2:
			mask = pygame.image.load("fsocietymask.jpg") 
			screen.blit(mask, (400,220))
		if firehole == 3:
			mask = pygame.image.load("fsocietymask.jpg") 
			screen.blit(mask, (400,145))
		if firehole == 4:
			mask = pygame.image.load("fsocietymask.jpg") 
			screen.blit(mask, (400,60))
		if firehole == 5:
			mask = pygame.image.load("fsocietymask.jpg") 
			screen.blit(mask, (400,05))
		if firehole == 6:
			mask = pygame.image.load("fsocietymask.jpg") 
			screen.blit(mask, (300,05))
		if firehole == 7:
			mask = pygame.image.load("fsocietymask.jpg") 
			screen.blit(mask, (500,05))	
		
		pygame.display.update()

	 
#Skillz skeeball game
def gameLoop4():

	#Background Music and Sounds
	#pygame.mixer.music.load("hackthepolice.mp3")
	#pygame.mixer.music.set_volume(0.5)
	#pygame.mixer.music.play(-1)
	point_sound = pygame.mixer.Sound("scrampunk__okay.wav")
	select_sound = pygame.mixer.Sound("josepharaoh99__select.wav")

	gameExit = False
	ballsOver = False

	score = 0
	balls = 9
	tenpoints =0
	twentypoints = 0
	thirtypoints = 0
	fourtypoints = 0
	fiftypoints = 0
	hundredpoints = 0
	hundredpoints2 = 0


	while not gameExit:
		
		while ballsOver == True:
			
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						score = 0	
						gameLoop4()
					if event.key == pygame.K_x:
						gameExit = True	
						ballsOver = False
						yousure4()	
								
		for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_a:
						score += 10
						balls -= 1
						tenpoints += 1
						pygame.mixer.Sound.play(point_sound) 
					if event.key == pygame.K_s:
						score += 20
						balls -= 1
						twentypoints = 1
						pygame.mixer.Sound.play(point_sound)
					if event.key == pygame.K_d:
						score += 30
						balls -= 1
						thirtypoints += 1
						pygame.mixer.Sound.play(point_sound)
					if event.key == pygame.K_f:
						score += 40
						balls -= 1
						fourtypoints += 1
						pygame.mixer.Sound.play(point_sound)
					if event.key == pygame.K_g:
						score += 50
						balls -= 1
						fiftypoints += 1
						pygame.mixer.Sound.play(point_sound)
					if event.key == pygame.K_l:
						
						score += 100
						balls -= 1
						hundredpoints += 1
						pygame.mixer.Sound.play(point_sound)
					if event.key == pygame.K_j:
						score += 100
						balls -= 1
						pygame.mixer.Sound.play(point_sound)
						hundredpoints2 += 1
					if event.key == pygame.K_p:
						score = 0
						balls = 9											
					if event.key == pygame.K_x:
						gameExit = True	
						yousure4()
					if tenpoints == 1 and twentypoints == 1 and thirtypoints == 1 and fourtypoints == 1 and fiftypoints == 1 and hundredpoints == 1 and hundredpoints2 == 1:
						score += 1000
						balls += 9
					#   pygame.mixer.Sound.play(wowwwwwwza_sound)
					if tenpoints == 2 and twentypoints == 2 and thirtypoints == 2 and fourtypoints == 2 and fiftypoints == 2 and hundredpoints == 2 and hundredpoints2 == 2:
						score += 2000
						balls += 9
					#   pygame.mixer.Sound.play(wowwwwwwza_sound)
					if tenpoints >= 3 and twentypoints >= 3 and thirtypoints >= 3 and fourtypoints >= 3 and fiftypoints >= 3 and hundredpoints >= 3 and hundredpoints2 >= 3:
						score += 3000
						balls += 9
					#   pygame.mixer.Sound.play(wowwwwwwza_sound)
					if tenpoints >= 4 and twentypoints >= 4 and thirtypoints >= 4 and fourtypoints >= 4 and fiftypoints >= 4 and hundredpoints >= 4 and hundredpoints2 >= 4:
						score += 4000
						balls += 9
					#   pygame.mixer.Sound.play(wowwwwwwza_sound)
					if tenpoints >= 5 and twentypoints >= 5 and thirtypoints >= 5 and fourtypoints >= 5 and fiftypoints >= 5 and hundredpoints >= 5 and hundredpoints2 >= 5:
						score += 5000
						balls += 9
					#   pygame.mixer.Sound.play(wowwwwwwza_sound)
					if tenpoints >= 6 and twentypoints >= 6 and thirtypoints >= 6 and fourtypoints >= 6 and fiftypoints >= 6 and hundredpoints >= 6 and hundredpoints2 >= 6:
						score += 6000
						balls += 9
					#   pygame.mixer.Sound.play(wowwwwwwza_sound)
					
					if balls == 0:
						gameExit = True
						go = pygame.image.load("gameover.jpg") 
						screen.blit(go, (0, 0))
						pygame.display.flip()   
						oldlace = (253,245,230)
						black = (0,0,0)
						sienna = (160,82,45)
						myfont = pygame.font.Font("DS-DIGIB.TTF", 110) #Large font for score 
						label = myfont.render(str(score), 1, black) #for the scoring
						screen.blit(label, (380,100)) #put the score text on the screen
						pygame.display.update()	
						 
						showit1 = True
						while showit1:
							for event in pygame.event.get():
								if event.type == pygame.QUIT:
									pygame.quit()
									quit()
								if event.type ==pygame.KEYDOWN:
									if event.key == pygame.K_z:
										pygame.mixer.Sound.play(select_sound) 
										gameLoop4()
										showit1 = False
									if event.key == pygame.K_x:
										pygame.mixer.Sound.play(select_sound) 
										#screen.blit(mm, (0, 0))
										#pygame.display.flip()											
										splash1()
										showit1 = False
						#gameExit = True
						#showscore4()
												 
		screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 
		screen2 = pygame.display.set_mode((800,480), pygame.NOFRAME) 
		bg = pygame.image.load("skillzbackground.jpg") 
		cadetblue = (95,158,160)
		black = (0,0,0)
		sienna = (160,82,45)
		myfont = pygame.font.SysFont("Ariel", 150) #Large font for score
		ballsfont = pygame.font.SysFont("Ariel", 118) #Small font for ball count
		label = myfont.render(str(score), 1, black) #for the scoring
		label2 = ballsfont.render(str(balls), 1, black) #for the balls
		
		screen.blit(bg,(0,0))
		pygame.draw.rect(screen2, cadetblue, [700,300,90,90]) 
		screen.blit(label, (600,10)) #put the score text on the screen
		screen.blit(label2, (710,300)) #put the ballcount text on the screen
		
		if tenpoints > 0:
			mask = pygame.image.load("fsocietymask.jpg") 
			screen.blit(mask, (400,280))
		if twentypoints > 0:
			mask = pygame.image.load("fsocietymask.jpg") 
			screen.blit(mask, (400,220))
		if thirtypoints > 0:
			mask = pygame.image.load("fsocietymask.jpg") 
			screen.blit(mask, (400,145))
		if fourtypoints > 0:
			mask = pygame.image.load("fsocietymask.jpg") 
			screen.blit(mask, (400,60))
		if fiftypoints > 0:
			mask = pygame.image.load("fsocietymask.jpg") 
			screen.blit(mask, (400,05))
		if hundredpoints > 0:
			mask = pygame.image.load("fsocietymask.jpg") 
			screen.blit(mask, (300,05))
		if hundredpoints2 > 0:
			mask = pygame.image.load("fsocietymask.jpg") 
			screen.blit(mask, (500,05))	
			
		pygame.display.update()
 
def splash1():
  screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 
  splash01 = pygame.image.load("mainspash1.jpg")
  splash02 = pygame.image.load("mainspash2.jpg") 
  mm = pygame.image.load("mainmenuwithbuttons.jpg")
  #pygame.mixer.music.set_volume(0.9)
  #select_sound = pygame.mixer.Sound("josepharaoh99__select.wav")
  splash001 = True
  while splash001:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type ==pygame.KEYDOWN:	
				if event.key == pygame.K_z:
					#pygame.mixer.Sound.play(select_sound) 
					screen.blit(mm, (0, 0))
					pygame.display.flip()
					main()
					splash001 = False
		screen.blit(splash01, (0, 0))
		pygame.display.flip()
		pygame.time.wait(200)
		screen.blit(splash02, (0, 0))
		pygame.display.flip()
		pygame.time.wait(200)
  


def main1():
  screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 
  main01 = pygame.image.load("main1-classicskee.jpg") 
  mm = pygame.image.load("mainmenuwithbuttons.jpg")
  select_sound = pygame.mixer.Sound("josepharaoh99__select.wav")
  screen.blit(main01, (0, 0))
  pygame.display.flip()
  intro1 = True
  while intro1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_z:
					pygame.mixer.Sound.play(select_sound) 
					gameLoop1()
					intro1 = False
				if event.key == pygame.K_x:
					pygame.mixer.Sound.play(select_sound)  
					screen.blit(mm, (0, 0))
					pygame.display.flip()
					splash1()
					intro1 = False

def main2():
  screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 
  main02 = pygame.image.load("main2-timedskee.jpg") 
  mm = pygame.image.load("mainmenuwithbuttons.jpg")
  select_sound = pygame.mixer.Sound("josepharaoh99__select.wav")
  screen.blit(main02, (0, 0))
  pygame.display.flip()
  intro2 = True
  while intro2:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_z:
					pygame.mixer.Sound.play(select_sound)
					gameLoop2()
					intro2 = False
				if event.key == pygame.K_x:
					pygame.mixer.Sound.play(select_sound) 
					screen.blit(mm, (0, 0))
					pygame.display.flip()
					splash1()
					intro2 = False

def main3():
  screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 
  main03 = pygame.image.load("main3-onfire.jpg") 
  mm = pygame.image.load("mainmenuwithbuttons.jpg")
  select_sound = pygame.mixer.Sound("josepharaoh99__select.wav")
  screen.blit(main03, (0, 0))
  pygame.display.flip()
  intro3 = True
  while intro3:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_z:
					pygame.mixer.Sound.play(select_sound)
					gameLoop3()
					intro3 = False
				if event.key == pygame.K_x:
					pygame.mixer.Sound.play(select_sound)
					screen.blit(mm, (0, 0))
					pygame.display.flip()
					splash1()
					intro3 = False


def main4():
  screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 
  main04 = pygame.image.load("main4-skillz.jpg") 
  mm = pygame.image.load("mainmenuwithbuttons.jpg")
  select_sound = pygame.mixer.Sound("josepharaoh99__select.wav")
  screen.blit(main04, (0, 0))
  pygame.display.flip()
  intro4 = True
  while intro4:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_z:
					pygame.mixer.Sound.play(select_sound)
					gameLoop4()
					intro4 = False
				if event.key == pygame.K_x:
					pygame.mixer.Sound.play(select_sound)
					screen.blit(mm, (0, 0))
					pygame.display.flip()
					splash1()
					intro4 = False
					 
def yousure():
  screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 
  qu = pygame.image.load("sure-exit.jpg") 
  mm = pygame.image.load("mainmenuwithbuttons.jpg")
  select_sound = pygame.mixer.Sound("josepharaoh99__select.wav")
  screen.blit(qu, (0, 0))
  pygame.display.flip()
  quit1 = True
  while quit1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_x:
					pygame.mixer.Sound.play(select_sound)
					gameLoop1()
					quit1 = False
				if event.key == pygame.K_z:
					pygame.mixer.Sound.play(select_sound)
					#screen.blit(mm, (0, 0))
					#pygame.display.flip()
					splash1()
					quit1 = False
  
def yousure2():
  screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 
  qu = pygame.image.load("sure-exit.jpg") 
  mm = pygame.image.load("mainmenuwithbuttons.jpg")
  select_sound = pygame.mixer.Sound("josepharaoh99__select.wav")
  screen.blit(qu, (0, 0))
  pygame.display.flip()
  quit1 = True
  while quit1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_x:
					pygame.mixer.Sound.play(select_sound)
					gameLoop2()
					quit1 = False
				if event.key == pygame.K_z:
					pygame.mixer.Sound.play(select_sound)
					#screen.blit(mm, (0, 0))
					#pygame.display.flip()
					splash1()
					quit1 = False  

def yousure3():
  screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 
  qu = pygame.image.load("sure-exit.jpg") 
  mm = pygame.image.load("mainmenuwithbuttons.jpg")
  select_sound = pygame.mixer.Sound("josepharaoh99__select.wav")
  screen.blit(qu, (0, 0))
  pygame.display.flip()
  quit1 = True
  while quit1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_x:
					pygame.mixer.Sound.play(select_sound)
					gameLoop3()
					quit1 = False
				if event.key == pygame.K_z:
					pygame.mixer.Sound.play(select_sound)
					#screen.blit(mm, (0, 0))
					#pygame.display.flip()
					splash1()
					quit1 = False
  
def yousure4():
  screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 
  qu = pygame.image.load("sure-exit.jpg") 
  mm = pygame.image.load("mainmenuwithbuttons.jpg")
  select_sound = pygame.mixer.Sound("josepharaoh99__select.wav")
  screen.blit(qu, (0, 0))
  pygame.display.flip()
  quit1 = True
  while quit1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_x:
					pygame.mixer.Sound.play(select_sound)
					gameLoop4()
					quit1 = False
				if event.key == pygame.K_z:
					pygame.mixer.Sound.play(select_sound) 
					#screen.blit(mm, (0, 0))
					#pygame.display.flip()
					splash1()
					quit1 = False
  


def showscore2():
  screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 
  go = pygame.image.load("gameover.jpg") 
  mm = pygame.image.load("mainmenuwithbuttons.jpg")
  screen.blit(go, (0, 0))
  pygame.display.flip() 
  
  score=00
  oldlace = (253,245,230)
  black = (0,0,0)
  sienna = (160,82,45)
  myfont = pygame.font.SysFont("Ariel", 150) #Large font for score
  #pygame.draw.rect(screen, oldlace
  #, [476,135,180,100]) 
  label = myfont.render(str(score), 1, black) #for the scoring
  screen.blit(label, (380,100)) #put the score text on the screen
  pygame.display.update()	
  
  showit1 = True
  while showit1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_z:
					#pygame.mixer.Sound.play(select_sound)
					gameLoop2()
					showit1 = False
				if event.key == pygame.K_x:
					#pygame.mixer.Sound.play(select_sound)
					#screen.blit(mm, (0, 0))
					#pygame.display.flip()
					splash1()
					showit1 = False
 
def showscore4():
  screen = pygame.display.set_mode((800,480), pygame.NOFRAME) 
  go = pygame.image.load("gameover.jpg") 
  mm = pygame.image.load("mainmenuwithbuttons.jpg")
  screen.blit(go, (0, 0))
  pygame.display.flip() 
  
  score=00
  oldlace = (253,245,230)
  black = (0,0,0)
  sienna = (160,82,45)
  myfont = pygame.font.SysFont("Ariel", 150) #Large font for score
  #pygame.draw.rect(screen, oldlace
  #, [476,135,180,100]) 
  label = myfont.render(str(score), 1, black) #for the scoring
  screen.blit(label, (380,100)) #put the score text on the screen
  pygame.display.update()	
  
  showit1 = True
  while showit1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_z:
					#pygame.mixer.Sound.play(point_sound) 
					gameLoop4()
					showit1 = False
				if event.key == pygame.K_x:
					#pygame.mixer.Sound.play(menu_sound) 
					#screen.blit(mm, (0, 0))
					#pygame.display.flip()
					splash1()
					showit1 = False
 
   ## ---[ The python script starts here! ]----------------------------------------
   # Run the script
if __name__ == "__main__":
  splash1()
   
   
	
