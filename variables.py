import pygame
import os
import time

pygame.init()

DEBUG = True

WW = 1500
HH = 1080

#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((WW, HH))

NUMBER_OF_STEPS = 6

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

backg_nms[0] = 'Sfondi/01_copertina.png'

fixed_nms[0].append('Sfondi/01_Bottone_BG_01.png') # Pulsante PLAY
fixed_pos[0].append((WW/2-62,HH/3-80))

## STEP 1 - INTRO

backg_nms[1] = 'Sfondi/02_bg.png'

movin_nms[1].append('Schede/01_Gasolio.png') # Scheda 1
movin_pos[1].append((WW/5+226,HH/2+96))

dropp_pos[1] = [WW/6*4,HH/5*3,WW/6,HH/4]

## STEP 2 - GIOCO 1

backg_nms[2] = 'Sfondi/03_bg.png'

movin_nms[2].append('Schede/01_Gasolio.png') # Scheda 1
movin_pos[2].append((WW/6+34,HH/2+91))

fixed_nms[2].append('Schede/04_Versare_nel_motore.png') # Pulsante PLAY
fixed_pos[2].append((WW/5*2+120,HH/4*2+87))

fixed_nms[2].append('Schede/06_Distillare.png') # Pulsante PLAY
fixed_pos[2].append((WW/5*3+45,HH/4*2+87))

fixed_nms[2].append('Schede/07_Pretrattare.png') # Pulsante PLAY
fixed_pos[2].append((WW/5*4-55,HH/4*2+87))


## STEP 3 - GIOCO 1 - ERRORE 1

backg_nms[3] = 'Sfondi/04_bg_barca.png'

## STEP 4 - GIOCO 1 - ERRORE 2

backg_nms[4] = 'Sfondi/04_bg_distillare.png'

## STEP 5 - INFO

backg_nms[5] = 'Sfondi/05_bg_pretrattare_testo.png'


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