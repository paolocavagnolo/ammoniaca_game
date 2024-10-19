
import pygame
import os
import time

pygame.init()

DEBUG = False

WW = 1920
HH = 1080

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#screen = pygame.display.set_mode((WW, HH))

NUMBER_OF_STEPS = 21

# DEFINE SOURCE OBJS
backg_nms = list()
backg_img = list()

fixed_nms = list()
fixed_pos = list()
fixed_img = list()
fixed_rec = list()

movin_nms = list()
movin_pos = list()
movin_img = list()
movin_rec = list()
original_ = list()

dropp_pos = list()
dropp_rec = list()

final_pos = list()
final_rec = list()

for i in range(NUMBER_OF_STEPS):
  backg_nms.append('')
  fixed_nms.append(list())
  fixed_pos.append(list())
  fixed_img.append(list())
  fixed_rec.append(list())

  movin_nms.append(list())
  movin_pos.append(list())
  movin_img.append(list())
  movin_rec.append(list())
  original_.append(list())

  dropp_pos.append(list())

  final_pos.append(list())
  final_rec.append(list())



# LOAD ASSETS

## STEP 0 - START

backg_nms[0] = 'sfondi/01.png'

fixed_nms[0].append('sfondi/01_01.png') # Pulsante PLAY
fixed_pos[0].append((WW/2-40,HH/3-70))

## STEP 1 - INTRO

backg_nms[1] = 'sfondi/02.png'

movin_nms[1].append('schede/01_-10.png') # Scheda 1
movin_pos[1].append((WW/5-15,HH/2+162))

dropp_pos[1] = [WW/6*4,HH/5*3,WW/6,HH/4]

## STEP 2 - GIOCO 1

backg_nms[2] = 'sfondi/03.png'

movin_nms[2].append('schede/01_-12.png') # Scheda 1
movin_pos[2].append((WW/6*5+88,HH/5*4-10))

fixed_nms[2].append('schede/01_-12.png') # 
fixed_pos[2].append((WW/5+50,HH/4*2+30))

fixed_nms[2].append('schede/01_-12.png') # 
fixed_pos[2].append((WW/5*2+60,HH/4*2))

fixed_nms[2].append('schede/01_-12.png') # 
fixed_pos[2].append((WW/5*3+80,HH/4*2-50))

## STEP 3 - ERRORE

backg_nms[3] = 'sfondi/03_01.png'

## STEP 4 - SCHEDE INFO

backg_nms[4] = 'sfondi/04_01.png'

## STEP 5 - SCHEDE INFO

backg_nms[5] = 'sfondi/04_02.png'

## STEP 6 - SCHEDE INFO

backg_nms[6] = 'sfondi/04_03.png'

## STEP 7 - THE GGGGAME

backg_nms[7] = 'sfondi/05.png'

H1 = HH/2-80
H2 = HH/2+210

DD = 30

X1 = WW/10*2-DD
X2 = WW/10*3-DD
X3 = WW/10*4-DD
X4 = WW/10*5-DD
X5 = WW/10*6-DD

fixed_nms[7].append('schede/01_-10.png') # Pulsante PLAY
fixed_pos[7].append((WW/9*8-50,HH/2+65))

movin_nms[7].append('schede/01_-05.png') # Soda caustica no
movin_pos[7].append((X1+10,HH/2+55))

movin_nms[7].append('schede/01_-01.png') # platino ok
movin_pos[7].append((X2,H1-3))

movin_nms[7].append('schede/01_-02.png') # ghiaccio ok
movin_pos[7].append((X3-1,H1-4))

movin_nms[7].append('schede/01_-06.png') # acqua acida ok
movin_pos[7].append((X4,H1-4))

movin_nms[7].append('schede/01_-08.png') # calore ok
movin_pos[7].append((X5+15,H1-5))

movin_nms[7].append('schede/01_-04.png') # idrogeno ok
movin_pos[7].append((X2+2,H2+5))

movin_nms[7].append('schede/01_-03.png') # ossigeno no
movin_pos[7].append((X3-3,H2+5))

movin_nms[7].append('schede/01_-07.png') # anidride no
movin_pos[7].append((X4,H2+4))

movin_nms[7].append('schede/01_-09.png') # pressione ok
movin_pos[7].append((X5+17,H2+3))

ordine_step7 = [5,4,8,1,3,2]

X71 = WW/10*8+35
X72 = WW/10*9+5
Y71 = HH/6*2+70
Y72 = HH/6*3+70
Y73 = HH/6*4+70

step7_1 = (X71,Y71)
step7_2 = (X72+14,Y71)
step7_3 = (X71+14,Y72)
step7_4 = (X72,Y72)
step7_5 = (X71,Y73)
step7_6 = (X72,Y73)

step7_posizioni = [step7_1,step7_2,step7_3,step7_4,step7_5,step7_6]

## STEP 8 - THE GGGGAME WIN

backg_nms[8] = 'sfondi/05_01.png'

## STEP 8 - GIOCO 2

backg_nms[9] = 'sfondi/06.png'

movin_nms[9].append('schede/01_-11.png') # Scheda 1
movin_pos[9].append((WW/6*5+83,HH/5*3+179))

fixed_nms[9].append('schede/01_-11.png') # 
fixed_pos[9].append((WW/5+37,HH/4*2-50+30))

fixed_nms[9].append('schede/01_-11.png') # 
fixed_pos[9].append((WW/5*2+23,HH/4*2+20))

fixed_nms[9].append('schede/01_-11.png') # 
fixed_pos[9].append((WW/5*3+7,HH/4*2+60))

## STEP 10 - ELEVATO INQUINAMENTO

backg_nms[10] = 'sfondi/06_02.png'

## STEP 11 - SPAZIO ESAURITO

backg_nms[11] = 'sfondi/06_01.png'

## STEP 12 - AMMO INFO

backg_nms[12] = 'sfondi/07_01.png'

## STEP 13 - AMMO INFO

backg_nms[13] = 'sfondi/07_02.png'

## STEP 14 - AMMO INFO

backg_nms[14] = 'sfondi/07_03.png'

## STEP 15 - AMMO INFO

backg_nms[15] = 'sfondi/07_04.png'

## STEP 16 - THE GGGAME 2

backg_nms[16] = 'sfondi/08.png'

fixed_nms[16].append('schede/01_-10.png') # Pulsante PLAY
fixed_pos[16].append((WW/9*8-240,HH/2+95))

movin_nms[16].append('schede/01_-14.png') # Soda caustica no
movin_pos[16].append((WW/7*2-168,HH/4*2+93))

movin_nms[16].append('schede/01_-15.png') # platino ok
movin_pos[16].append((WW/7*3-150,HH/4*2+93))

movin_nms[16].append('schede/01_-16.png') # ghiaccio ok
movin_pos[16].append((WW/7*4-127,HH/4*2+93))

## STEP 17 - FERTILIZZANTE

backg_nms[17] = 'sfondi/09.png'

## STEP 18 - AMMO INFO

backg_nms[18] = 'sfondi/13_01.png'

movin_nms[18].append('schede/01_-13.png') # Scheda 1
movin_pos[18].append((WW/2-244,HH/2+84))

fixed_nms[18].append('schede/01_-10.png') # 
fixed_pos[18].append((WW/2+200,HH/2+80))

## STEP 19 - PERSO

backg_nms[19] = 'sfondi/14.png'

## STEP 20 - VINTO

backg_nms[20] = 'sfondi/15.png'

for img in backg_nms:

  path = 'imgs/' + img

  if os.path.isfile(path):
    backg_img.append(pygame.image.load(path))
  else:
    print("FILE",path,"NOT FOUND")
    exit()

for step, images in enumerate(fixed_nms):
  for i,img in enumerate(images):

    path = 'imgs/' + img

    if os.path.isfile(path):
      fixed_img[step].append(pygame.image.load(path))
    else:
      print("FILE",path,"NOT FOUND")
      exit()

    fixed_rec[step].append(fixed_img[step][i].get_rect())
    fixed_rec[step][i].center = fixed_pos[step][i]

for step, images in enumerate(movin_nms):
  for i,img in enumerate(images):

    path = 'imgs/' + img

    if os.path.isfile(path):
      movin_img[step].append(pygame.image.load(path))
      original_[step].append(pygame.image.load(path))
    else:
      print("FILE",path,"NOT FOUND")
      exit()


    movin_rec[step].append(movin_img[step][i].get_rect())
    movin_rec[step][i].center = movin_pos[step][i]


    #final_rec[step].append(movin_rec[step][i])
    #final_rec[step][i].center = final_pos[step][i]


for s,c in enumerate(dropp_pos):
  if len(c) == 4:
    dropp_rec.append(pygame.Rect(c[0],c[1],c[2],c[3]))
  else:
    dropp_rec.append(None)


# MAIN STEP VARIABLE
BLUE = (0, 0, 255)
RED = (255, 0, 0)
NEXT_STEP = -1
active_box = None
last_active_box = None
STEP = 0

return_home = pygame.Rect(0,0,20,20)
reset_card = pygame.Rect(WW-20,0,20,20)

# TEXT

font = pygame.font.Font('ARLRDBD.ttf', 32)
text_ok = font.render('WIN!', True, BLUE, RED)
text_ko = font.render('RITENTA', True, BLUE, RED)

text_ok_rect = text_ok.get_rect()
text_ok_rect.center = (WW // 2, HH // 2)

text_ko_rect = text_ko.get_rect()
text_ko_rect.center = (WW // 2, HH // 2)

# SOUND

#from ffpyplayer.player import MediaPlayer
pygame.mixer.init()
click_s = pygame.mixer.Sound("snds/click.mp3")
error_s = pygame.mixer.Sound("snds/error.mp3")
next_s = pygame.mixer.Sound("snds/next.mp3")
win_s = pygame.mixer.Sound("snds/win.mp3")
drop_s = pygame.mixer.Sound("snds/drop.mp3")
poof_s = pygame.mixer.Sound("snds/poof.mp3")


# GAME LOGIC

solved = False
carta_num = []
on_board = []
solution = [[],[],[],[]]

def check_solution(ll,ss):

  r = True

  for x in solution[ss]:
    if x not in ll:
      r = False

  return r

for s in range(NUMBER_OF_STEPS):
  carta_num.append(list())
  num = 1
  for i in range(len(movin_nms[s])):
    carta_num[s].append(num)
    num += 1

blocked = False
FIRST = True

def reset():
  global on_board, NUMBER_OF_STEPS, movin_img, original_, movin_rec, movin_pos, blocked, special, FIRST
  print("RESET!")

  special = (None,None)
  on_board = []
  FIRST = True
  blocked = False
  NEXT_STEP = -1

  for s in range(NUMBER_OF_STEPS):
    for i in range(len(movin_img[s])):
      movin_img[s][i] = original_[s][i]
      movin_rec[s][i] = movin_img[s][i].get_rect()
      movin_rec[s][i].center = movin_pos[s][i]

check = True
run = True
update = True
special = (None,None)

STEP = 0
reset()
while run:

  print("B",blocked)

  # SET BACKGROUND 
  screen.blit(backg_img[STEP], (0,0))
  if FIRST:
    FIRST = False
    pygame.display.flip()
    if STEP in [3,4,5]:
      time.sleep(2)
    else:
      time.sleep(0.5)

  # SET FIXED OBJECTS 
  for i,e in enumerate(fixed_img[STEP]):
    #screen.blit(e, fixed_rec[STEP][i])
    if DEBUG:
      pygame.draw.rect(screen, BLUE, fixed_rec[STEP][i], 2)

  # SET MOVABLE OBJECTS 
  last = (None, None)

  for i,e in enumerate(movin_img[STEP]):
    if i != active_box:
      screen.blit(movin_img[STEP][i], movin_rec[STEP][i])
    else:
      last = movin_img[STEP][i], movin_rec[STEP][i]
    if DEBUG:
      pygame.draw.rect(screen, BLUE, movin_rec[STEP][i], 2)

  if last[0] != None:
    screen.blit(last[0], last[1])

  #DRAW DROPP RECT
  if DEBUG:
    if dropp_rec[STEP] != None:
      pygame.draw.rect(screen, RED, dropp_rec[STEP], 2)

  # DRAW NUMBER
  # if len(solution[STEP]) > 0:
  #   text_string = str(len(on_board)) + " / " + str(len(solution[STEP]))

  #   text_num = font.render(text_string, True, (200,200,200))
  #   text_num_rect = text_num.get_rect()
  #   text_num_rect.center = (WW - 100, 100)

  #   screen.blit(text_num, text_num_rect)

  # SPECIAL CASE
  if special != (None,None):
    if special[0] == 2:
      sT = time.time()

      if special[1] == 0: 
        pygame.mixer.Sound.play(error_s)
        NEXT_STEP = 4
      elif special[1] == 1:
        pygame.mixer.Sound.play(error_s)
        NEXT_STEP = 3
      elif special[1] == 2:
        pygame.mixer.Sound.play(win_s)
        NEXT_STEP = 3

    elif special[0] == 9:
      sT = time.time()

      if special[1] == 0: 
        pygame.mixer.Sound.play(error_s)
        NEXT_STEP = 12
      elif special[1] == 1:
        pygame.mixer.Sound.play(error_s)
        NEXT_STEP = 11
      elif special[1] == 2:
        pygame.mixer.Sound.play(win_s)
        NEXT_STEP = 10

    blocked = True
    special = (None,None)

  if NEXT_STEP >= 0:
    if (time.time() - sT) > 0.7:
      STEP = NEXT_STEP
      pygame.mixer.Sound.play(next_s)
      reset()
      NEXT_STEP = -1

  if not blocked:
    for event in pygame.event.get():

      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          pygame.mixer.Sound.play(click_s)
          # RETURN TO HOME
          if return_home.collidepoint(event.pos):
            pygame.mixer.Sound.play(next_s)
            NEXT_STEP = 0
            sT = time.time()

          # RESET
          if reset_card.collidepoint(event.pos):
            pygame.mixer.Sound.play(next_s)
            NEXT_STEP = 0
            sT = time.time()



          # GAME LOGIC
          if STEP == 0:
            NEXT_STEP = 1
            sT = time.time()

          elif STEP in [1,2,7,9,16,18]:
            # ON MOVING
            for num, box in enumerate(movin_rec[STEP]):
              if box.collidepoint(event.pos):
                pygame.mixer.Sound.play(click_s)
                active_box = num
                start_position = box.center

          elif STEP == 3:
            NEXT_STEP = 2
            sT = time.time()

          elif STEP == 4:
            NEXT_STEP = 5
            sT = time.time()

          elif STEP == 5:
            NEXT_STEP = 6
            sT = time.time()

          elif STEP == 6:
            NEXT_STEP = 7
            sT = time.time()

          elif STEP == 8:
            NEXT_STEP = 9
            sT = time.time()

          elif STEP == 10:
            NEXT_STEP = 9
            sT = time.time()

          elif STEP == 11:
            NEXT_STEP = 9
            sT = time.time()

          elif STEP == 12:
            NEXT_STEP = 13
            sT = time.time()

          elif STEP == 13:
            NEXT_STEP = 14
            sT = time.time()

          elif STEP == 14:
            NEXT_STEP = 15
            sT = time.time()

          elif STEP == 15:
            NEXT_STEP = 16
            sT = time.time()

          elif STEP == 17:
            NEXT_STEP = 18
            sT = time.time()

          elif STEP == 19:
            NEXT_STEP = 16
            sT = time.time()

          elif STEP == 20:
            NEXT_STEP = 0
            sT = time.time()


      if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
          if active_box != None:  # Ho lasciato una carta
            
            if STEP == 1:
              if dropp_rec[STEP].collidepoint(event.pos):
                pygame.mixer.Sound.play(drop_s)
                NEXT_STEP = 2
                sT = time.time()
              else:
                pygame.mixer.Sound.play(poof_s)
                movin_rec[STEP][active_box].center = movin_pos[STEP][active_box]

            elif STEP == 2 or STEP == 9:
              inside = False
              for i,card_box in enumerate(fixed_rec[STEP]):

                if card_box.collidepoint(event.pos): # Sopra una carta
                  pygame.mixer.Sound.play(drop_s)
                  movin_rec[STEP][active_box].center = fixed_pos[STEP][i]  # La posiziono sotto alla carta
                  inside = True
                  special = (STEP,i)

              if not inside:
                pygame.mixer.Sound.play(poof_s)
                movin_rec[STEP][active_box].center = movin_pos[STEP][active_box]

            elif STEP == 7:

              if fixed_rec[STEP][0].collidepoint(event.pos): # sopra il barile
                if active_box not in [0,6,7]:
                  pygame.mixer.Sound.play(drop_s)
                  
                  if not fixed_rec[STEP][0].collidepoint(start_position):  # Se partiva da fuori dal pozzo

                    movin_rec[STEP][active_box].scale_by_ip(0.6)
                    movin_img[STEP][active_box] = pygame.transform.scale_by(movin_img[STEP][active_box],0.6)
                    movin_rec[STEP][active_box].center = step7_posizioni[ordine_step7.index(active_box)]

                    on_board.append(carta_num[STEP][active_box]) 
                  else:
                    movin_rec[STEP][active_box].center = step7_posizioni[ordine_step7.index(active_box)]
                else:
                  pygame.mixer.Sound.play(error_s)
                  movin_rec[STEP][active_box].center = movin_pos[STEP][active_box]

              else:
                pygame.mixer.Sound.play(poof_s)
                movin_rec[STEP][active_box].center = movin_pos[STEP][active_box]

                if fixed_rec[STEP][0].collidepoint(start_position): # Se partiva da dentro al pozzo

                  movin_rec[STEP][active_box].scale_by_ip(1/0.6)
                  movin_img[STEP][active_box] = original_[STEP][active_box]

                  on_board.remove(carta_num[STEP][active_box])

            elif STEP == 16:
              if active_box in [0,2]:
                if fixed_rec[STEP][0].collidepoint(event.pos): # sopra il barile
                  pygame.mixer.Sound.play(drop_s)
                  movin_rec[STEP][active_box].center = fixed_pos[STEP][0] 

                  if active_box == 0: # ACIDO SOLFORICO
                    end_game = False
                    NEXT_STEP = 17
                    sT = time.time()
                  elif active_box == 2:
                    end_game = True
                    NEXT_STEP = 17
                    sT = time.time()

                else:
                  pygame.mixer.Sound.play(poof_s)
                  movin_rec[STEP][active_box].center = movin_pos[STEP][active_box]

              else:
                pygame.mixer.Sound.play(poof_s)
                movin_rec[STEP][active_box].center = movin_pos[STEP][active_box]

            elif STEP == 18:

              if fixed_rec[STEP][0].collidepoint(event.pos): # sopra la pianta

                pygame.mixer.Sound.play(drop_s)
                movin_rec[STEP][active_box].center = fixed_pos[STEP][0] 

                if end_game: # ACIDO SOLFORICO
                  NEXT_STEP = 20
                  sT = time.time()
                else:
                  NEXT_STEP = 19
                  sT = time.time()


              else:
                pygame.mixer.Sound.play(poof_s)
                movin_rec[STEP][active_box].center = movin_pos[STEP][active_box]


        if len(on_board) == 6:
          pygame.mixer.Sound.play(error_s)
          NEXT_STEP = 8
          sT = time.time()

        active_box = None



      if event.type == pygame.MOUSEMOTION:
        if active_box != None:
          movin_rec[STEP][active_box].move_ip(event.rel)

      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        run = False

      if event.type == pygame.QUIT:
        run = False

      if DEBUG:
        print("STEP:",STEP)
        print("active_box:",active_box)
        print("on_board:",on_board)

  pygame.display.flip()


print("Exit gently")
pygame.quit() 