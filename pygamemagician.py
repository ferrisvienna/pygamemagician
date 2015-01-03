#004BB1#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Disco Defense
Open source game by Ferris (FerrisofVienna) Bartak
using python3 and pygame
"""

#the next line is only needed for python2.x and not necessary for python3.x
from __future__ import print_function, division
import random
import pygame
import time as t
import easygui as e

class Game(object):
    LIVES = 20
    FORCE_OF_GRAVITY = 3
    ACTORSPEEDMAX = 20
    ACTORSPEEDMIN = 10
    DISCTHROWERRANGE = 150
    DISCMAXSPEED = 100
    SPAWNRATE = 0.005
    SECURITYSPAWNRATE = 0.0005
    SPAWNRATE2 = 0.005
    XP = 0.00
    ACTOR_NEEDEDXP = 300
    ACTOR_REGEN = 0.4
    ACTOR_ATKDMG = 10
    ACTOR_DEF = 0.5
    ACTOR_SPEED = 3
    ACTOR_KB = 10
    ACTOR_LVL = 1
    KILLS = 0
    MAGIC_POWER = 1.00
    
#rebalance
    def __init__(self):

        Monster.images.append(pygame.image.load("data/discodudel.png")) # 0
        Monster.images[0].set_colorkey((255,0,182))
        Monster.images.append(pygame.image.load("data/discodudel4.png")) # 1
        Monster.images[1].set_colorkey((255,0,182))
        Monster.images.append(pygame.image.load("data/discodudel.png")) # 2
        Monster.images[2].set_colorkey((255,0,182))
        Monster.images.append(pygame.image.load("data/discodudel2.png")) # 3
        Monster.images[3].set_colorkey((255,0,182))
        Monster.images.append(pygame.image.load("data/discodudel3.png")) # 4
        Monster.images[4].set_colorkey((255,0,182))
        Monster.images.append(pygame.image.load("data/discodudel2.png")) # 5
        Monster.images[5].set_colorkey((255,0,182))
        Monster.images[0].convert_alpha()
        Monster.images[1].convert_alpha()
        Monster.images[2].convert_alpha()
        Monster.images[3].convert_alpha()
        Monster.images[4].convert_alpha()
        Monster.images[5].convert_alpha()
        
        Monster2.images.append(pygame.image.load("data/rockdudel.png")) # 0
        Monster2.images[0].set_colorkey((255,0,182))
        Monster2.images.append(pygame.image.load("data/rockdudel1.png")) # 1
        Monster2.images[1].set_colorkey((255,0,182))
        Monster2.images.append(pygame.image.load("data/rockdudel.png")) # 2
        Monster2.images[2].set_colorkey((255,0,182))
        Monster2.images.append(pygame.image.load("data/rockdudel1.png")) # 3
        Monster2.images[3].set_colorkey((255,0,182))
        Monster2.images.append(pygame.image.load("data/rockdudel.png")) # 4
        Monster2.images[4].set_colorkey((255,0,182))
        Monster2.images.append(pygame.image.load("data/rockdudel1.png")) # 5
        Monster2.images[5].set_colorkey((255,0,182))
        Monster2.images[0].convert_alpha()
        Monster2.images[1].convert_alpha()
        Monster2.images[2].convert_alpha()
        Monster2.images[3].convert_alpha()
        Monster2.images[4].convert_alpha()
        Monster2.images[5].convert_alpha()
        
        #Monster_rare.images.append(pygame.image.load("data/walkll1.png")) # 0
        #Monster_rare.images[0].set_colorkey((255,0,182))
        #Monster_rare.images.append(pygame.image.load("data/walkll2.png")) # 1
        #Monster_rare.images[1].set_colorkey((255,0,182))
        #Monster1.images.append(pygame.image.load("data/walkll3.png")) # 2
        #Monster1.images[2].set_colorkey((255,0,182))
        #Monster1.images.append(pygame.image.load("data/walkll1.png")) # 3
        #Monster1.images[3].set_colorkey((255,0,182))
        #Monster1.images.append(pygame.image.load("data/walkll2.png")) # 4
        #Monster1.images[4].set_colorkey((255,0,182))
        #Monster1.images.append(pygame.image.load("data/walkll3.png")) # 5
        #Monster1.images[5].set_colorkey((255,0,182))
        #Monster1.images[0].convert_alpha()
        #Monster1.images[1].convert_alpha()
        #Monster1.images[2].convert_alpha()
        #Monster1.images[3].convert_alpha()
        #Monster1.images[4].convert_alpha()
        #Monster1.images[5].convert_alpha()
        
        Security.images.append(pygame.image.load("data/securityw1.png")) # 0
        Security.images[0].set_colorkey((255,0,182))
        Security.images.append(pygame.image.load("data/securityw2.png")) # 1
        Security.images[1].set_colorkey((255,0,182))
        Security.images.append(pygame.image.load("data/securityw1.png")) # 2
        Security.images[2].set_colorkey((255,0,182))
        Security.images.append(pygame.image.load("data/securityw2.png")) # 3
        Security.images[3].set_colorkey((255,0,182))
        Security.images.append(pygame.image.load("data/securityw1.png")) # 4
        Security.images[4].set_colorkey((255,0,182))
        Security.images.append(pygame.image.load("data/securityw2.png")) # 5
        Security.images[5].set_colorkey((255,0,182))
        Security.images.append(pygame.image.load("data/securityw2.png")) # 5
        Security.images[6].set_colorkey((255,0,182))
        Security.images.append(pygame.image.load("data/securitywa1.png")) #6
        Security.images[7].set_colorkey((255,0,182))
        Security.images.append(pygame.image.load("data/securitywa2.png")) #7
        Security.images[8].set_colorkey((255,0,182))
        
        
        Security.images[0].convert_alpha()
        Security.images[1].convert_alpha()
        Security.images[2].convert_alpha()
        Security.images[3].convert_alpha()
        Security.images[4].convert_alpha()
        Security.images[5].convert_alpha()
        Security.images[6].convert_alpha()
        Security.images[7].convert_alpha()

        self.h= [pygame.image.load("data/h0.png"),
                 pygame.image.load("data/h1.png"),
                 pygame.image.load("data/h2.png"),
                 pygame.image.load("data/h3.png"),
                 pygame.image.load("data/h4.png"),
                 pygame.image.load("data/h5.png")]
        self.h[0].set_colorkey((255,0,182))
        self.h[1].set_colorkey((255,0,182))
        self.h[2].set_colorkey((255,0,182))
        self.h[3].set_colorkey((255,0,182))
        self.h[4].set_colorkey((255,0,182))
        self.h[5].set_colorkey((255,0,182))
        self.p= pygame.image.load("data/p.png")
        self.p.set_colorkey((255,0,182))
        self.e= pygame.image.load("data/protect.png")
        self.p.set_colorkey((255,0,182))
        self.i= [pygame.image.load("data/i0.png"),
                 pygame.image.load("data/i1.png"),
                 pygame.image.load("data/i2.png"),
                 pygame.image.load("data/i3.png"),
                 pygame.image.load("data/i4.png"),
                 pygame.image.load("data/i5.png")]
        self.i[1].set_colorkey((255,0,182))
        self.i[2].set_colorkey((255,0,182))
        self.i[3].set_colorkey((255,0,182))
        self.i[4].set_colorkey((255,0,182))
        self.i[5].set_colorkey((255,0,182))
        self.i[0].set_colorkey((255,0,182))
        self.d= [pygame.image.load("data/d0.png"),
                 pygame.image.load("data/d1.png"),
                 pygame.image.load("data/d2.png"),
                 pygame.image.load("data/d3.png"),
                 pygame.image.load("data/d4.png"),
                 pygame.image.load("data/d5.png")]
        self.g= [pygame.image.load("data/g0.png"),
                 pygame.image.load("data/g1.png"),
                 pygame.image.load("data/g2.png"),
                 pygame.image.load("data/g3.png"),
                 pygame.image.load("data/g4.png"),
                 pygame.image.load("data/g5.png")]
        self.v= [pygame.image.load("data/discodiscgunf.png"),
                 pygame.image.load("data/discodiscgunl.png"),
                 pygame.image.load("data/discodiscgunb.png"),
                 pygame.image.load("data/discodiscgunr.png"),
                 pygame.image.load("data/discodiscgunr.png"),
                 pygame.image.load("data/discodiscgunr.png")]
        self.k= [pygame.image.load("data/konfettif.png"),
                 pygame.image.load("data/konfettir.png"),
                 pygame.image.load("data/konfettib.png"),
                 pygame.image.load("data/konfettil.png"),
                 pygame.image.load("data/konfettil.png"),
                 pygame.image.load("data/konfettil.png")]
        self.w= [pygame.image.load("data/discogunf.png"),
                 pygame.image.load("data/discogunr.png"),
                 pygame.image.load("data/discogunb.png"),
                 pygame.image.load("data/discogunl.png"),
                 pygame.image.load("data/discogunl.png"),
                 pygame.image.load("data/discogunl.png")]         
        self.w[1].set_colorkey((255,0,182))
        self.w[2].set_colorkey((255,0,182))
        self.w[3].set_colorkey((255,0,182))
        self.w[4].set_colorkey((255,0,182))
        self.w[5].set_colorkey((255,0,182))
        self.w[0].set_colorkey((255,0,182))
        self.anim=0
        self.o= [pygame.image.load("data/discoball.png"),
                 pygame.image.load("data/discoball2.png")]
        self.o[0].set_colorkey((255,0,182))
        self.o[1].set_colorkey((255,0,182))
        self.anim=0         
        self.level=["hpppppoppppppwppppppe",
                    "ihpppppppppihippppope",
                    "idddgddddddhidvddddde",
                    "ddddgddddddddddddddde",
                    "gdddgddgdvddddkddddve",
                    "ddddgddddddddggddddde",
                    "ddddgdddddddddvddddde",
                    "gggggggdgggdggdggggge"]
        anim = 0
        self.legende={"h":self.h[anim],#towertop
                      "p":self.p,#nothing
                      "i":self.i[anim],#dirt
                      "g":self.g[anim],#lava
                      "d":self.d[anim], #grass
                      "v":self.v[anim], #discodiscgun
                      "w":self.w[anim], #discogun
                      "k":self.k[anim], #konfettigun
                      "e":self.e, #end of world
                      "o":self.o[anim] #discoball
                      }
    #def update(self,seconds):
        #neededcoins = self.ACTOR_LVL * 20 +100


class Fragment(pygame.sprite.Sprite):
        """a fragment of an exploding Bird"""
        gravity = True # fragments fall down ?
        def __init__(self, pos):
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.pos = [0.0,0.0]
            self.pos[0] = pos[0]
            self.pos[1] = pos[1]
            self.image = pygame.Surface((10,10))
            self.image.set_colorkey((0,0,0)) # black transparent
            pygame.draw.circle(self.image, (random.randint(20,230),random.randint(20,230),random.randint(20,230)), (5,5),
                                            random.randint(3,10))
            self.image = self.image.convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = self.pos #if you forget this line the sprite sit in the topleft corner
            self.lifetime = 1 + random.random()*5 # max 6 seconds
            self.time = 0.0
            self.fragmentmaxspeed = 200  # try out other factors !
            self.dx = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)
            self.dy = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)

        def update(self, seconds):
            self.time += seconds
            if self.time > self.lifetime:
                self.kill()
            self.pos[0] += self.dx * seconds
            self.pos[1] += self.dy * seconds
            if Fragment.gravity:
                self.dy += Game.FORCE_OF_GRAVITY # gravity suck fragments down
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)
class Explosion(pygame.sprite.Sprite):
        gravity = False # fragments fall down ?
        def __init__(self, pos):
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.pos = [0.0,0.0]
            self.pos[0] = pos[0]
            self.pos[1] = pos[1]
            self.image = pygame.Surface((10,10))
            self.image.set_colorkey((0,0,0)) # black transparent
            pygame.draw.circle(self.image, (random.randint(200,255),random.randint(1,70),random.randint(1,70)), (5,5),
                                            random.randint(3,10))
            self.image = self.image.convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = self.pos #if you forget this line the sprite sit in the topleft corner
            self.lifetime = 1 + random.random()*3 # max 6 seconds
            self.time = 0.0
            self.fragmentmaxspeed = 300  # try out other factors !
            self.dx = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)
            self.dy = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)

        def update(self, seconds):
            self.time += seconds
            if self.time > self.lifetime:
                self.kill()
            self.pos[0] += self.dx * seconds
            self.pos[1] += self.dy * seconds
            #if Fragment.gravity:
                #self.dy += Game.FORCE_OF_GRAVITY # gravity suck fragments down
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)
class Fireball(pygame.sprite.Sprite):
        gravity = False # fragments fall down ?
        def __init__(self, pos):
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.pos = [0.0,0.0]
            self.pos[0] = pos[0]
            self.pos[1] = pos[1]
            self.image = pygame.Surface((10,10))
            self.image.set_colorkey((0,0,0)) # black transparent
            pygame.draw.circle(self.image, (random.randint(200,255),random.randint(1,255),random.randint(1,10)), (5,5),
                                            random.randint(3,10))
            self.image = self.image.convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = self.pos #if you forget this line the sprite sit in the topleft corner
            self.lifetime = 1 + random.random()*3 # max 6 seconds
            self.time = 0.0
            self.fragmentmaxspeed = 300  # try out other factors !
            self.dx = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)
            self.dy = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)

        def update(self, seconds):
            self.time += seconds
            if self.time > self.lifetime:
                self.kill()
            self.pos[0] += self.dx * seconds
            self.pos[1] += self.dy * seconds
            #if Fragment.gravity:
                #self.dy += Game.FORCE_OF_GRAVITY # gravity suck fragments down
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)
class Porters(pygame.sprite.Sprite):
        gravity = False # fragments fall down ?
        def __init__(self, pos):
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.pos = [0.0,0.0]
            self.pos[0] = pos[0]
            self.pos[1] = pos[1]
            self.image = pygame.Surface((10,10))
            self.image.set_colorkey((0,0,0)) # black transparent
            pygame.draw.circle(self.image, (random.randint(0,50),random.randint(100,255),random.randint(1,50)), (5,5),
                                            random.randint(3,10))
            self.image = self.image.convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = self.pos #if you forget this line the sprite sit in the topleft corner
            self.lifetime = 1 + random.random()*4 # max 6 seconds
            self.time = 0.0
            self.fragmentmaxspeed = 200  # try out other factors !
            self.dx = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)
            self.dy = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)

        def update(self, seconds):
            self.time += seconds
            if self.time > self.lifetime:
                self.kill()
            self.pos[0] += self.dx * seconds
            self.pos[1] += self.dy * seconds
            #if Fragment.gravity:
                #self.dy += Game.FORCE_OF_GRAVITY # gravity suck fragments down
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)
class E_Explosion(pygame.sprite.Sprite):
        gravity = False # fragments fall down ?
        def __init__(self, pos):
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.pos = [0.0,0.0]
            self.pos[0] = pos[0]
            self.pos[1] = pos[1]
            self.image = pygame.Surface((10,10))
            self.image.set_colorkey((0,0,0)) # black transparent
            pygame.draw.circle(self.image, (random.randint(200,255),random.randint(1,70),random.randint(1,70)), (5,5),
                                            random.randint(3,10))
            self.image = self.image.convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = self.pos #if you forget this line the sprite sit in the topleft corner
            self.lifetime = 1 + random.random()*3 # max 6 seconds
            self.time = 0.0
            self.fragmentmaxspeed = 300  # try out other factors !
            self.dx = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)
            self.dy = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)

        def update(self, seconds):
            self.time += seconds
            if self.time > self.lifetime:
                self.kill()
            self.pos[0] += self.dx * seconds
            self.pos[1] += self.dy * seconds
            #if Fragment.gravity:
                #self.dy += Game.FORCE_OF_GRAVITY # gravity suck fragments down
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)
class E_Fireball(pygame.sprite.Sprite):
        gravity = False # fragments fall down ?
        def __init__(self, pos):
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.pos = [0.0,0.0]
            self.pos[0] = pos[0]
            self.pos[1] = pos[1]
            self.image = pygame.Surface((10,10))
            self.image.set_colorkey((0,0,0)) # black transparent
            pygame.draw.circle(self.image, (random.randint(200,255),random.randint(1,255),random.randint(1,10)), (5,5),
                                            random.randint(3,10))
            self.image = self.image.convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = self.pos #if you forget this line the sprite sit in the topleft corner
            self.lifetime = 1 + random.random()*3 # max 6 seconds
            self.time = 0.0
            self.fragmentmaxspeed = 300  # try out other factors !
            self.dx = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)
            self.dy = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)

        def update(self, seconds):
            self.time += seconds
            if self.time > self.lifetime:
                self.kill()
            self.pos[0] += self.dx * seconds
            self.pos[1] += self.dy * seconds
            #if Fragment.gravity:
                #self.dy += Game.FORCE_OF_GRAVITY # gravity suck fragments down
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)
class E_Porters(pygame.sprite.Sprite):
        gravity = False # fragments fall down ?
        def __init__(self, pos):
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.pos = [0.0,0.0]
            self.pos[0] = pos[0]
            self.pos[1] = pos[1]
            self.image = pygame.Surface((10,10))
            self.image.set_colorkey((0,0,0)) # black transparent
            pygame.draw.circle(self.image, (random.randint(0,50),random.randint(100,255),random.randint(1,50)), (5,5),
                                            random.randint(3,10))
            self.image = self.image.convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = self.pos #if you forget this line the sprite sit in the topleft corner
            self.lifetime = 1 + random.random()*4 # max 6 seconds
            self.time = 0.0
            self.fragmentmaxspeed = 200  # try out other factors !
            self.dx = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)
            self.dy = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)

        def update(self, seconds):
            self.time += seconds
            if self.time > self.lifetime:
                self.kill()
            self.pos[0] += self.dx * seconds
            self.pos[1] += self.dy * seconds
            #if Fragment.gravity:
                #self.dy += Game.FORCE_OF_GRAVITY # gravity suck fragments down
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)
#class DiscoLaserCannon(pygame.sprite.Sprite):
    ##a laser gun
    #gravity= False
    #image=pygame.image.load("data/discogun.png")
    #number = 0
    #discoLaserCannons = {}
    
    #def __init__(self,x,y, screen):
        #pygame.sprite.Sprite.__init__(self, self.groups)
        #self.hitpoints = 300.0
        #self.hitpointsfull = 300.0
        #self.reload_time = 0.2
        #self.reload_time_full = 0.2#
        #self.image = DiscoLaserCannon.image
        ##for in images:
        #self.image.set_colorkey((255,0,182))
        #self.rect = self.image.get_rect()
        #self.screen = screen
        #self.x = x
        #self.y = y
        #self.rect.centerx = self.x
        #self.rect.centery = self.y
        #self.lasermaxburntime =  random.random()*2+2
        #self.laserburntime = 0
        #self.beam = False
        #self.Victimnumber = None
        #self.number = DiscoLaserCannon.number
        ##DiscoLaserCannon.number += 1
        #DiscoLaserCannon.number += 1           # increase the number for next Bird
        #DiscoLaserCannon.discoLaserCannons[self.number] = self
        #Healthbar(self)
        
        
    #def update(self,seconds):
        #self.reload_time += seconds
        #if self.hitpoints < 1:
            #self.kill()
        #if self.reload_time > self.reload_time_full:
            ## choose new target
            ##Victimnumber = None
            #if len(Monster.monsters) > 0:
                      #self.Victimnumber = random.choice(list(Monster.monsters.keys()))
                      #self.Victim = Monster.monsters[self.Victimnumber]  
                      ##lasertimer = 4 #rebalance
             
            #if self.beam: 
                #self.laserburntime += seconds
                #if self.laserburntime > self.lasermaxburntime:
                      #self.reload_time = 0
                      #self.laserburntime = 0
                     ## t.sleep(2)
                      #self.beam = False

                ##lasertimer -= seconds
            ## gibt es ein Victim?
            #if self.Victimnumber != None:
                    ##existiert das Victim noch in der Monstergruppe ?
                    #if self.Victimnumber in Monster.monsters:
                                                ## tödlicher weißer laser
                        #pygame.draw.line(self.screen,
                             #(random.randint(200,255),
                              #random.randint(200,255),
                              #random.randint(200,255)),
                             #(self.x,self.y),
                             #(self.Victim.pos[0], self.Victim.pos[1]),7)
                        #self.Victim.hitpoints-= 1.0
                        #self.Victim.burntime = 4.0
                        ##Victim.pos[0] -= 3
                        #self.beam = True
                       
        
        
#class DiscoLaserCannon(pygame.sprite.Sprite):
    ##a laser gun
    #gravity= False
    #image=pygame.image.load("data/discogun.png")
    #number = 0
    
    #def __init__(self,x,y, screen):
        #pygame.sprite.Sprite.__init__(self, self.groups)
        #self.hitpoints = 300.0
        #self.hitpointsfull = 300.0
        #self.reload_time = 0.2
        #self.reload_time_full = 0.2#
        #self.image = DiscoLaserCannon.image
        ##efor  in images:
        #self.image.set_colorkey((255,0,182))
        #self.rect = self.image.get_rect()
        #self.screen = screen
        #self.x = x
        #self.y = y
        #self.rect.centerx = self.x
        #self.rect.centery = self.y
        #self.lasermaxburntime =  random.random()*2+2
        #self.laserburntime = 0
        #self.beam = False
        #self.Victimnumber = None
        #self.number = DiscoLaserCannon.number
        #DiscoLaserCannon.number += 1
        ##DiscoLaserCannonCannon.number += 1           # increase the number for next Bird
        ##DiscoLaserCannon.DiscoLaserCannons[self.number] = self
        #Healthbar(self)
        ##self.has_target = False
        #self.lasertargettime = 0
        #self.lasertargettimefull = 1

    #def update(self,seconds):
        #self.reload_time += seconds
        #if self.hitpoints < 1:
            #self.kill()
        
        #if self.reload_time > self.reload_time_full:
            ## choose new target
            ##Victimnumber = None
            #if self.Victimnumber is None:
                   #if len(Monster.monsters) > 0:
                      #self.Victimnumber = random.choice(list(Monster.monsters.keys()))
                      #self.Victim = Monster.monsters[self.Victimnumber]
                      #self.lasertargettime = 0
                      ##self.has_target = True
                      ##lasertimer = 4 #rebalance
             
            #if self.beam:
                #self.laserburntime += seconds
                #if self.laserburntime > self.lasermaxburntime:
                      #self.reload_time = 0
                      #self.laserburntime = 0
                      
                      
                      #self.beam = False
                      #self.Victimnumber = None

                ##lasertimer -= seconds
            ## is the a Victim?
            #if self.Victimnumber != None:
                    ## does the victim still exist in the Monsterclass?
                    #if self.Victimnumber in Monster.monsters:
                                                ## tödlicher weißer laser
                        #pygame.draw.line(self.screen,
                             #(random.randint(200,255),
                              #random.randint(200,255),
                              #random.randint(200,255)),
                             #(self.x,self.y),
                             #(self.Victim.pos[0], self.Victim.pos[1]),7)
                        #self.Victim.hitpoints-= 1.0
                        #self.Victim.burntime = 4.0
                        ##self.hitpoints -= 1
                        ##victim.pos[0] -= 3
                        #self.beam = True
                    #else:
                        #self.victimnumber = None   
#class DiscProjectile(pygame.sprite.Sprite):
        #"""a projectile of a Disc gun"""
        #gravity = False # fragments fall down ?
        #image=pygame.image.load("data/disc.png")
        #def __init__(self, startpos=(random.randint(640,1024),random.randint(100,300)),
                           #targetpos=(random.randint(640,1024),random.randint(100,300))):
            ##         dx=random.randint(-Game.DISCMAXSPEED,Game.DISCMAXSPEED),
            ##         dy=random.randint(-Game.DISCMAXSPEED,Game.DISCMAXSPEED)):
            #pygame.sprite.Sprite.__init__(self, self.groups)
            #self.pos = [0.0,0.0]
            #self.startpos = startpos
            #self.targetpos = targetpos
            #distancex = -self.startpos[0] + self.targetpos[0]
            #distancey = -self.startpos[1] + self.targetpos[1]
            #distance = (distancex**2 + distancey**2)**0.5
            #if distance > Game.DISCTHROWERRANGE:
                #self.kill()
            #self.dx = distancex / distance                              
            #self.dy = distancey / distance
            #self.dx *= Game.DISCMAXSPEED
            #self.dy *= Game.DISCMAXSPEED
            #self.hitpoints = 10
            #self.pos[0] = startpos[0]
            #self.pos[1] = startpos[1]
            #self.image = DiscProjectile.image
            #self.image.set_colorkey((255,0,182)) # black transparent
            ##pygame.draw.circle(self.image, (random.randint(1,255),0,0), (5,5),
                                            ##random.randint(2,5))
            #self.image = self.image.convert_alpha()
            #self.rect = self.image.get_rect()
            #self.rect.center = self.pos #if you forget this line the sprite sit in the topleft corner
            #self.lifetime = 1 + random.random()*5 # max 6 seconds
            #self.time = 0.0
            ##self.fragmentmaxspeed = 200  # try out other factors !
            ##self.dx = dx
            ##self.dy = dy

        #def update(self, seconds):
            #self.time += seconds
            #if self.time > self.lifetime:
                #self.kill()
            #if self.hitpoints <= 0:
                #self.kill()
                 
             
            #self.pos[0] += self.dx * seconds
            #self.pos[1] += self.dy * seconds
            ##if Fragment.gravity:
             ##   self.dy += FORCE_OF_GRAVITY # gravity suck fragments down
            #self.rect.centerx = round(self.pos[0],0)
            #self.rect.centery = round(self.pos[1],0)

class Flame (pygame.sprite.Sprite):
    images = []
    images.append(pygame.image.load("data/flamme.png"))
    images.append(pygame.image.load("data/flamme2.png"))
    for img in images:
        img.set_colorkey((255,0,182))
        #img.convert_alpha()
        
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.image = random.choice(Flame.images)
        self.rect = self.image.get_rect()
        self.x  = x
        self.y  = y
        self.rect.centerx = x
        self.rect.centery = y
    
    def update(self, seconds):
        self.kill()
        
        
#class Mouse (pygame.sprite.Sprite):
      #images = []
      #images.append(pygame.image.load("data/Point.png"))
    ##images.append(pygame.image.load("data/flamme2.png"))
      #for img in images:
        #img.set_colorkey((255,0,182))
        ##img.convert_alpha()
      #mouses ={}
        
      #def __init__(self, startpos=(100,100)):
        #pygame.sprite.Sprite.__init__(self,self.groups)
        #self.image = random.choice(Mouse.images)
        #self.rect = self.image.get_rect()
        ##self.pos() = pygame.mouse.get_pos()
        ##self.rect.centerx = x
        ##self.rect.centery = y
        #self.mouse = pygame.mouse.get_pos()
        ##self.pos = [float(startpos[0]),float(startpos[1])]
        #self.x= self.mouse
        #self.y= self.mouse
        #self.pos = (self.x,self.y)
      #def update(self, seconds):
          #self.mouse=pygame.mouse.get_pos()
            ##pygame.mouse.set_pos(self.mouse[0]-5,self.mouse[1]-5)
          
          #self.x = self.mouse[0]
          #print(self.x, self.y, self.pos, self.mouse)
          
          #self.y = self.mouse[1]
          #self.pos = (self.x,self.y)
        
        
        
class Healthbar(pygame.sprite.Sprite):
    """shows a bar with the hitpoints of a Bird sprite"""
    def __init__(self, boss):
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.boss = boss
        self.image = pygame.Surface((self.boss.rect.width,7))
        self.image.set_colorkey((3,3,3)) # black transparent
        pygame.draw.rect(self.image, (1,1,1), (0,0,self.boss.rect.width,7),1)
        self.rect = self.image.get_rect()
        self.oldpercent = 0
        self.bossnumber = self.boss.number # the unique number (name)

    def update(self, time):
        self.percent = self.boss.hitpoints / self.boss.hitpointsfull * 1.0
        if self.percent != self.oldpercent:
            pygame.draw.rect(self.image, (77,77,77), (1,1,self.boss.rect.width-2,5)) # fill black
            pygame.draw.rect(self.image, (222,22,2), (1,1,
                int(self.boss.rect.width * self.percent),5),0) # fill green
        self.oldpercent = self.percent
        self.rect.centerx = self.boss.rect.centerx
        self.rect.centery = self.boss.rect.centery - self.boss.rect.height /2 - 10
        #check if boss is still alive if not
        if self.boss.hitpoints<1:
         self.kill()


class Magicbar(pygame.sprite.Sprite):
    """shows a bar with the hitpoints of a Bird sprite"""
    def __init__(self, boss):
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.boss = boss
        self.image = pygame.Surface((self.boss.rect.width,7))
        self.image.set_colorkey((3,3,3)) # black transparent
        pygame.draw.rect(self.image, (1,1,1), (0,0,self.boss.rect.width,7),1)
        self.rect = self.image.get_rect()
        self.oldpercent = 0
        self.bossnumber = self.boss.number # the unique number (name)

    def update(self, time):
        self.percent = self.boss.magic / self.boss.magicfull * 1.0
        if self.percent != self.oldpercent:
            pygame.draw.rect(self.image, (77,77,77), (1,1,self.boss.rect.width-2,5)) # fill black
            pygame.draw.rect(self.image, (5,20,124), (1,1,
                int(self.boss.rect.width * self.percent),5),0) # fill green
        self.oldpercent = self.percent
        self.rect.centerx = self.boss.rect.centerx
        self.rect.centery = self.boss.rect.centery - self.boss.rect.height /2 - 20
        #check if boss is still alive if not
        if self.boss.magic< 100 :
         self.boss.hitpoints -= 0.5
        if self.boss.hitpoints < 0:
            self.kill()


class Monster(pygame.sprite.Sprite):  #DISCO GARY GLITTER
        """Generic Monster"""
        images=[]  # list of all images
        # not necessary:
        monsters = {} # a dictionary of all monsters
        number = 0

        def __init__(self, level, startpos=(0,200), hitpointsfull=600):
        #rebalance

            pygame.sprite.Sprite.__init__(self, self.groups ) #call parent class. NEVER FORGET !
            self.burntime = 0.0
            self.z = 0 # animationsnumber
            self.duration = 0.0 # how long was the current animation visible in seconds
            self.level=level
            self.nomove = False
            #startpos=(0,screen.get_rect().center[1])
            startpos=(0,random.randint(100,350))
            self.pos = [float(startpos[0]),float (startpos[1])] # dummy values to create a list
            #self.pos[0] = float(startpos[0]) # float for more precise calculation
            #self.pos[1] = float(startpos[1])
           # self.area = screen.get_rect()
            self.area = pygame.Rect(0,100,1024,300)
            self.image = Monster.images[self.z]
            self.hitpointsfull = float(hitpointsfull) # maximal hitpoints , float makes decimal
            self.hitpoints = float(hitpointsfull) # actual hitpoints
            self.rect = self.image.get_rect()
            self.radius = max(self.rect.width, self.rect.height) / 2.0
            self.dx= random.random()*10+20
            self.dy= random.randint(-70,70)#rebalance
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)
            #--- not necessary:
            self.number = Monster.number # get my personal Birdnumber
            Monster.number+= 1           # increase the number for next Bird
            Monster.monsters[self.number] = self #
            Healthbar(self)
        def getChar(self):
            #Tile = 50*50
            x=int(self.pos[0]/50)
            y=int(self.pos[1]/50)+0 # correction value to get the tile under the feet doesn't actually work :\
            try:
                char=self.level[y][x]
            except:
                char="?"
            return char
        def update(self, seconds):
            #------ check if lava
            #Animation#
            # 6 bilder sind in Monster.images []
            
            self.duration += seconds
            if self.duration > 0.5:
                self.duration= 0
                self.z  +=1
                if self.z >= len(Monster.images):
                    self.z = 0
                self.image=Monster.images[self.z]
            #-------
            if self.getChar()=="g":
                #self.hitpoints-=1 #lava?
                self.burntime += 1.0
            if self.getChar()=="?":
                self.hitpoints = 0
            if self.getChar()=="e":
                self.hitpoints= 0
                Game.LIVES-=1
            if self.getChar()=="h":
                self.nomove = True
            self.dy=random.randint(-10, 10)
            self.dx= 20#random.randint(10,10)
            if self.nomove:
                self.dx = 0
            self.pos[0] += self.dx * seconds
            self.pos[1] += self.dy * seconds
            # -- check if Bird out of screen
            if not self.area.contains(self.rect):
                #self.crashing = True # change colour later
                # --- compare self.rect and area.rect
                if self.pos[0] + self.rect.width/2 > self.area.right:
                    self.pos[0] = self.area.right - self.rect.width/2
                if self.pos[0] - self.rect.width/2 < self.area.left:
                    self.pos[0] = self.area.left + self.rect.width/2
                if self.pos[1] + self.rect.height/2 > self.area.bottom:
                    self.pos[1] = self.area.bottom - self.rect.height/2
                if self.pos[1] - self.rect.height/2 < self.area.top:
                    self.pos[1] = self.area.top + self.rect.height/2
            #--- calculate new position on screen -----
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)
            #--- loose hitpoins
            #if self.crashing:
             #self.hitpoints -=1
            
            if self.burntime > 0 :
                self.hitpoints -= 1.0
                # reduce burntime
                self.burntime -= 0.4
                Flame(self.rect.centerx, self.rect.centery)
            
            if self.hitpoints <= 0:
                self.kill()
        def kill(self):
            for _ in range(random.randint(7,20)):
                    Fragment(self.pos)
                    #Monster.monsters[self.number] = None # kill Bird in sprite dictionary
            del(Monster.monsters[self.number]) 
            pygame.sprite.Sprite.kill(self) # kill the actual Monster
            Game.XP += 50
class EvilMagician(pygame.sprite.Sprite):  #DISCO GARY GLITTER
        images=[]  # list of all images
        # not necessary:
        evilmagicians = {} # a dictionary of all monsters
        number = 0

        def __init__(self, level, startpos=(100,100), hitpointsfull=600):
        #rebalance

            pygame.sprite.Sprite.__init__(self, self.groups ) #call parent class. NEVER FORGET !
            self.burntime = 0.0
            #print("i bin do")
            EvilMagician.x = startpos[0]
            EvilMagician.y = startpos[1]
            self.z = 0 # animationsnumber
            self.magic_reload = 0
            self.magic_reload_full = 5
            self.magic = 1000
            self.magicfull = 1000
            self.duration = 0.0 # how long was the current animation visible in seconds
            self.level=level
            self.nomove = False
            self.Actornumber = None
            Actortarget = None
            #self.stats{Game.ACTOR_ATKDMG : "Dmg",Game.ACTOR_SPEED : "speed", Game.ACTOR_DEF : "Def"}
            #startpos=(0,screen.get_rect().center[1])
            self.pos= startpos
            self.pos = [float(startpos[0]),float (startpos[1])] # dummy values to create a list
            #self.pos[0] = float(startpos[0]) # float for more precise calculation
            #self.pos[1] = float(startpos[1])
            #self.area = screen.get_rect()
            self.area = pygame.Rect(0,100,1024,300)
            self.image = Monster.images[1]
            self.hitpointsfull = float(hitpointsfull) # maximal hitpoints , float makes decimal
            self.hitpoints = float(hitpointsfull) # actual hitpoints
            self.rect = self.image.get_rect()
            self.radius = max(self.rect.width, self.rect.height) / 2.0
            self.dx = 0
            self.dy = 0
            #self.regen = 0.5
            #self.dx = random.random()*10+20
            #self.dy= random.randint(-70,70)#rebalance
            self.rect.centerx = self.x
            self.rect.centery = self.y
            #--- not necessary:
            self.number = EvilMagician.number # get my personal Birdnumber
            EvilMagician.number+= 1
            EvilMagician.evilmagicians[self.number] = self
            Healthbar(self)
            Magicbar(self)
            
        def getChar(self):
            #Tile = 50*50
            x=int(self.pos[0]/50)
            y=int(self.pos[1]/50)+0 # correction value to get the tile under the feet doesn't actually work :\
            try:
                char=Game.level[y][x]
            except:
                char="?"
            return char
            
        def update(self, seconds):
            self.magic_reload += seconds
            if len(Actor.actors) > 0:
                      #print(len(Actor.actors))
                      self.victimnumber = random.choice(list(Actor.actors.keys()))
                      self.victim = Actor.actors[self.victimnumber]
                      if self.victim.x > self.x:
                         self.x += 1.5 
                      if self.victim.x < self.x:
                         self.x -= 1.5
                      if self.victim.x == self.x:
                         self.x = self.x
                      if self.victim.y < self.y:
                         self.y -= 1.5
                      if self.victim.y > self.y:
                         self.y += 1.5
                      if self.victim.y == self.y:
                         self.y = self.y
            elif len(Actor.actors) == 0:
                pass
            self.rect.centerx = self.x
            self.rect.centery = self.y
            if self.hitpoints < self.hitpointsfull:
                self.hitpoints += 0.5
            if self.magic < self.magicfull:
                self.magic += 0.1
            if self.magic_reload > self.magic_reload_full:
                self.magic_reload = 0
                if len(Actor.actors) > 0:
                    if self.hitpoints > 500:
                        if random.random() < 0.1:
                            for x in range(4000):
                                E_Explosion((self.x,self.y))
                            self.hitpoints -= 500
                    if self.magic >= 400:
                        if self.hitpoints > 200:
                            if random.random() < 0.2:
                                for x in range(20):
                                    E_Fireball((self.x,self.y))
                                    E_Explosion((self.x,self.y))
                                    E_Porters((self.x,self.y))
                                self.magic -= 400
                                self.hitpoints -= 200
                        else:
                            if random.random() < 0.25:
                                self.hitpoints += self.hitpointsfull/2
                                self.magic -= 400
                    if self.magic >= 300:
                        if self.victim.x < self.x: 
                         if random.random() < 0.3:
                            for x in range (500):
                                E_Explosion((self.x+300,self.y))
                            self.magic -= 300
                    if self.magic >= 250:
                        if random.random() < 0.125:
                            for x in range(50):
                                E_Fireball((self.x-100,self.y))
                                E_Explosion((self.x-100,self.y))
                            self.victim.stunned += 1
                    if self.magic >= 200:
                        if random.random() < 0.35:
                            for x in range (100):
                                E_Explosion((self.x-100,self.y))
                                E_Explosion((self.x+100,self.y))
                                E_Explosion((self.x,self.y-100))
                                E_Explosion((self.x,self.y+100))
                                E_Explosion((self.x-75,self.y+75))
                                E_Explosion((self.x+75,self.y-75))
                                E_Explosion((self.x+75,self.y+75))
                                E_Explosion((self.x-75,self.y-75))
                            self.magic -= 200
                    if self.magic >= 50:
                        if random.random() < 0.4:
                            for x in range(30):
                                E_Explosion((self.x,self.y))
                            self.x += 100
                            self.hitpoints -= 50
                            self.magic -= 50
                    if self.magic >= 200:
                        if random.random() < 0.45:
                           if self.victim.x > self.x:
                            for x in range(5):
                                E_Porters((self.x+150,self.y))
                    if self.magic >= 300:
                        if random.random()< 0.45:
                          if self.victim.x > self.x:
                            for x in range(200):
                                    E_Fireball((self.x +300,self.y))
                            self.magic -= 300
                            pass
                    if self.hitpoints > 300:
                        if random.random()< 0.5:
                            for x in range(200):
                                E_Porters((self.x,self.y))
                            self.hitpoints -= 300
            #self.mouse=pygame.mouse.get_pos()
            #pygame.mouse.set_pos(self.mouse[0]-5,self.mouse[1]-5)
            
            #self.x=self.mouse[0]
            #self.y=self.mouse[1]
            
            if self.getChar()=="p":
                self.hitpoints = 1
            
            if self.hitpoints <= 0:
                self.kill()
            
            if self.burntime > 0 :
                self.hitpoints -= 1.0
                # reduce burntime
                self.burntime -= 0.4
                Flame(self.rect.centerx, self.rect.centery)
    

        def kill(self):
            for _ in range(random.randint(7,20)):
                    Fragment((self.x,self.y))
                    #Monster.monsters[self.number] = None # kill Bird in sprite dictionary
            del(EvilMagician.evilmagicians[self.number]) 
            pygame.sprite.Sprite.kill(self) # kill the actual MonsteR
            Game.KILLS += 1
            print("kills:", Game.KILLS)
            Game.ACTOR_REGEN += 0.025


class EvilMagician2(pygame.sprite.Sprite):  #DISCO GARY GLITTER
        images=[]  # list of all images
        # not necessary:
        evilmagicians2 = {} # a dictionary of all monsters
        number = 0

        def __init__(self, level, startpos=(100,100), hitpointsfull=600):
        #rebalance

            pygame.sprite.Sprite.__init__(self, self.groups ) #call parent class. NEVER FORGET !
            self.burntime = 0.0
            #print("i bin do")
            EvilMagician2.x = startpos[0]
            EvilMagician2.y = startpos[1]
            self.z = 0 # animationsnumber
            self.magic_reload = 0
            self.magic_reload_full = 5
            self.magic = 1000
            self.magicfull = 1000
            self.duration = 0.0 # how long was the current animation visible in seconds
            self.level=level
            self.nomove = False
            self.Actornumber = None
            Actortarget = None
            #self.stats{Game.ACTOR_ATKDMG : "Dmg",Game.ACTOR_SPEED : "speed", Game.ACTOR_DEF : "Def"}
            #startpos=(0,screen.get_rect().center[1])
            self.pos= startpos
            self.pos = [float(startpos[0]),float (startpos[1])] # dummy values to create a list
            #self.pos[0] = float(startpos[0]) # float for more precise calculation
            #self.pos[1] = float(startpos[1])
            #self.area = screen.get_rect()
            self.area = pygame.Rect(0,100,1024,300)
            self.image = Security.images[2]
            self.hitpointsfull = float(hitpointsfull) # maximal hitpoints , float makes decimal
            self.hitpoints = float(hitpointsfull) # actual hitpoints
            self.rect = self.image.get_rect()
            self.radius = max(self.rect.width, self.rect.height) / 2.0
            self.dx = 0
            self.dy = 0
            #self.regen = 0.5
            #self.dx = random.random()*10+20
            #self.dy= random.randint(-70,70)#rebalance
            self.rect.centerx = self.x
            self.rect.centery = self.y
            #--- not necessary:
            self.number = EvilMagician2.number # get my personal Birdnumber
            EvilMagician2.number+= 1
            EvilMagician2.evilmagicians2[self.number] = self
            Healthbar(self)
            Magicbar(self)
            
        def getChar(self):
            #Tile = 50*50
            x=int(self.pos[0]/50)
            y=int(self.pos[1]/50)+0 # correction value to get the tile under the feet doesn't actually work :\
            try:
                char=Game.level[y][x]
            except:
                char="?"
            return char
            
        def update(self, seconds):
            if len(Actor.actors) > 0:
                      #print(len(Actor.actors))
                      self.victimnumber = random.choice(list(Actor.actors.keys()))
                      self.victim = Actor.actors[self.victimnumber]
                      if self.victim.x > self.x:
                         self.x += 1.5
                      if self.victim.x < self.x:
                         self.x -= 1.5
                      if self.victim.x == self.x:
                         self.x = self.x
                      if self.victim.y < self.y:
                         self.y -= 1.5
                      if self.victim.y > self.y:
                         self.y += 1.5
                      if self.victim.y == self.y:
                         self.y = self.y
            elif len(Actor.actors) == 0:
                pass
            self.rect.centerx = self.x
            self.rect.centery = self.y
            if self.hitpoints < self.hitpointsfull:
                self.hitpoints += 0.5
            if self.magic < self.magicfull:
                self.magic += 0.1
            if self.magic_reload >= self.magic_reload_full:
                self.magic_reload = 0
                if len(Actor.actors) > 0:
                    if self.hitpoints > 500:
                        if random.random() < 0.9:
                            for x in range(4000):
                                E_Explosion((self.x,self.y))
                            self.hitpoints -= 500
                    if self.magic >= 400:
                        if self.hitpoints > 200:
                            if random.random() < 0.2:
                                for x in range(20):
                                    E_Fireball((self.x,self.y))
                                    E_Explosion((self.x,self.y))
                                    E_Porters((self.x,self.y))
                                self.magic -= 400
                                self.hitpoints -= 200
                                pass
                        else:
                            if random.random() < 0.25:
                                self.hitpoints += self.hitpointsfull/2
                                self.magic -= 400
                    if self.magic >= 300:
                        if self.victim.x < self.x:
                         if random.random() < 0.3:
                            for x in range (500):
                                E_Explosion((self.x+300,self.y))
                            self.magic -= 300
                    if self.magic >= 250:
                        if random.random() < 0.125:
                            for x in range(50):
                                E_Fireball((self.x-100,self.y))
                                E_Explosion((self.x-100,self.y))
                            MagicBomber((self.x,self.y))
                            self.x -= 100
                            #print("worked")
                    if self.magic >= 200:
                        if random.random() < 0.35:
                            for x in range (100):
                                E_Explosion((self.x-100,self.y))
                                E_Explosion((self.x+100,self.y))
                                E_Explosion((self.x,self.y-100))
                                E_Explosion((self.x,self.y+100))
                                E_Explosion((self.x-75,self.y+75))
                                E_Explosion((self.x+75,self.y-75))
                                E_Explosion((self.x+75,self.y+75))
                                E_Explosion((self.x-75,self.y-75))
                            self.magic -= 200
                    if self.magic >= 50:
                        if random.random() < 0.4:
                            for x in range(30):
                                E_Explosion((self.x,self.y))
                            self.x += 100
                            self.hitpoints -= 50
                            self.magic -= 50
                    if self.magic >= 200:
                        if random.random() < 0.45:
                           if self.victim.x > self.x:
                            for x in range(5):
                                E_Porters((self.x+150,self.y))
                    if self.magic >= 300:
                        if random.random()< 0.45:
                          if self.victim.x > self.x:
                            for x in range(200):
                                    E_Fireball((self.x +300,self.y))
                            self.magic -= 300
                            pass
                    if self.hitpoints > 300:
                        if random.random()< 0.5:
                            for x in range(200):
                                E_Porters((self.x,self.y))
                            self.hitpoints -= 300
            #self.mouse=pygame.mouse.get_pos()
            #pygame.mouse.set_pos(self.mouse[0]-5,self.mouse[1]-5)
            
            #self.x=self.mouse[0]
            #self.y=self.mouse[1]
            
            if self.getChar()=="p":
                self.hitpoints = 1
            
            if self.hitpoints <= 0:
                self.kill()
            
            if self.burntime > 0 :
                self.hitpoints -= 1.0
                # reduce burntime
                self.burntime -= 0.4
                Flame(self.rect.centerx, self.rect.centery)
            
            
        def kill(self):
            for _ in range(random.randint(7,20)):
                    Fragment((self.x,self.y))
                    #Monster.monsters[self.number] = None # kill Bird in sprite dictionary
            del(EvilMagician2.evilmagicians2[self.number]) 
            pygame.sprite.Sprite.kill(self) # kill the actual MonsteR
            Game.KILLS += 1
            print("kills:", Game.KILLS)
            Game.ACTOR_REGEN += 0.025
class MagicBomber(pygame.sprite.Sprite):  #DISCO GARY GLITTER
        images=[]  # list of all images
        # not necessary:
        magicbombers = {} # a dictionary of all monsters
        number = 0

        def __init__(self, level, startpos=(512.5,200)):
        #rebalance

            pygame.sprite.Sprite.__init__(self, self.groups ) #call parent class. NEVER FORGET !
            #self.burntime = 0.0
            #print("i bin do")
            MagicBomber.x = startpos[0]
            MagicBomber.y = startpos[1]
            self.z = 0 # animationsnumber
            self.duration = 0.0 # how long was the current animation visible in seconds
            self.level=level
            self.nomove = False
            self.Actornumber = None
            Actortarget = None
            self.Boom = 0
            self.lifetime = 0
            #self.stats{Game.ACTOR_ATKDMG : "Dmg",Game.ACTOR_SPEED : "speed", Game.ACTOR_DEF : "Def"}
            #startpos=(0,screen.get_rect().center[1])
            self.pos= startpos
            self.pos = [float(startpos[0]),float (startpos[1])] # dummy values to create a list
            #self.pos[0] = float(startpos[0]) # float for more precise calculation
            #self.pos[1] = float(startpos[1])
            #self.area = screen.get_rect()
            self.area = pygame.Rect(0,100,1024,300)
            self.image = Security.images[1]
            #self.hitpointsfull = float(hitpointsfull) # maximal hitpoints , float makes decimal
            #self.hitpoints = float(hitpointsfull) # actual hitpoints
            self.rect = self.image.get_rect()
            self.radius = max(self.rect.width, self.rect.height) / 2.0
            self.dx = 0
            self.dy = 0
            #self.regen = 0.5
            #self.dx = random.random()*10+20
            #self.dy= random.randint(-70,70)#rebalance
            self.rect.centerx = self.x
            self.rect.centery = self.y
            #--- not necessary:
            self.number = MagicBomber.number # get my personal Birdnumber
            MagicBomber.number+= 1
            MagicBomber.magicbombers[self.number] = self
            #Healthbar(self)
            #Magicbar(self)
            
        def getChar(self):
            #Tile = 50*50
            x=int(self.pos[0]/50)
            y=int(self.pos[1]/50)+0 # correction value to get the tile under the feet doesn't actually work :\
            try:
                char=Game.level[y][x]
            except:
                char="?"
            return char
            
        def update(self, seconds):
            #self.magic_reload += seconds
            if len(Actor.actors) > 0:
                      #print(len(Actor.actors))
                      self.victimnumber = random.choice(list(Actor.actors.keys()))
                      self.victim = Actor.actors[self.victimnumber]
                      if self.victim.x > self.x:
                         self.x += 3 
                      if self.victim.x < self.x:
                         self.x -= 3
                      if self.victim.x == self.x:
                         self.x = self.x
                      if self.victim.y < self.y:
                         self.y -= 3
                      if self.victim.y > self.y:
                         self.y += 3
                      if self.victim.y == self.y:
                         self.y = self.y
                      if self.lifetime < 5:
                          self.lifetime += seconds
            elif len(Actor.actors) == 0:
                pass
            self.rect.centerx = self.x
            self.rect.centery = self.y
            #if self.hitpoints < self.hitpointsfull:
                #self.hitpoints += 0.5
            #if self.magic < self.magicfull:
             #   self.magic += 0.1
            #if self.magic_reload > self.magic_reload_full:
            if self.Boom > 0:
                    print("BOOOM:",self.Boom)
                    print("hello")
                    self.victim.nomove = 2
                    for x in range(4000):
                        E_Explosion((self.x,self.y))
                    for x in range(20):
                        E_Fireball((self.x,self.y))
                        E_Explosion((self.x,self.y))
                        E_Porters((self.x,self.y))
                    for x in range(500):
                        E_Explosion((self.x+300,self.y))
                    for x in range(50):
                            E_Fireball((self.x-100,self.y))
                            E_Explosion((self.x-100,self.y))
                    for x in range(100):
                            E_Explosion((self.x-100,self.y))
                            E_Explosion((self.x+100,self.y))
                            E_Explosion((self.x,self.y-100))
                            E_Explosion((self.x,self.y+100))
                            E_Explosion((self.x-75,self.y+75))
                            E_Explosion((self.x+75,self.y-75))
                            E_Explosion((self.x+75,self.y+75))
                            E_Explosion((self.x-75,self.y-75))
                    for x in range(30):
                            E_Explosion((self.x,self.y))
                    for x in range(5):
                            E_Porters((self.x+150,self.y))
                
                    for x in range(200):
                            E_Fireball((self.x +300,self.y))
                        
                    for x in range(200):
                            E_Porters((self.x,self.y))
                    self.kill()
            elif self.lifetime > 5:
                self.kill()
            #self.mouse=pygame.mouse.get_pos()
            #pygame.mouse.set_pos(self.mouse[0]-5,self.mouse[1]-5)
            
            #self.x=self.mouse[0]
            #self.y=self.mouse[1]
            
            #if self.getChar()=="p":
             #   self.hitpoints = 1
            
            #if self.hitpoints <= 0:
                #self.kill()
            
            #if self.burntime > 0 :
             #   self.hitpoints -= 1.0
                # reduce burntime
              #  self.burntime -= 0.4
               # Flame(self.rect.centerx, self.rect.centery)
            
            
        def kill(self):
            for _ in range(random.randint(7,20)):
                    Fragment((self.x,self.y))
                    #Monster.monsters[self.number] = None # kill Bird in sprite dictionary
            del(MagicBomber.magicbombers[self.number]) 
            pygame.sprite.Sprite.kill(self) # kill the actual MonsteR
            Game.KILLS += 1
            print("kills:", Game.KILLS)
            #Game.ACTOR_REGEN += 0.025
class Actor(pygame.sprite.Sprite):  
        """Generic Monster"""
        images=[]  # list of all images
        # not necessary:
        actors = {} # a dictionary of all monsters
        number = 0

        def __init__(self, level, startpos=(700,100), hitpointsfull=600):
        #rebalance

            pygame.sprite.Sprite.__init__(self, self.groups ) #call parent class. NEVER FORGET !
            self.burntime = 0.0
            #print("i bin do")
            self.stunned = 0
            Actor.x = startpos[0]
            Actor.y = startpos[1]
            self.z = 0 # animationsnumber
            self.magic = 1000
            self.magicfull = 1000
            self.duration = 0.0 # how long was the current animation visible in seconds
            self.level=level
            self.nomove = False
            #self.stats{Game.ACTOR_ATKDMG : "Dmg",Game.ACTOR_SPEED : "speed", Game.ACTOR_DEF : "Def"}
            #startpos=(0,screen.get_rect().center[1])
            self.pos=startpos
            self.pos = [float(startpos[0]),float (startpos[1])] # dummy values to create a list
            #self.pos[0] = float(startpos[0]) # float for more precise calculation
            #self.pos[1] = float(startpos[1])
            #self.area = screen.get_rect()
            self.area = pygame.Rect(0,100,1024,300)
            self.image = Security.images[1]
            self.hitpointsfull = float(hitpointsfull) # maximal hitpoints , float makes decimal
            self.hitpoints = float(hitpointsfull) # actual hitpoints
            self.rect = self.image.get_rect()
            self.radius = max(self.rect.width, self.rect.height) / 2.0
            self.dx = 0
            self.dy = 0
            #self.regen = 0.5
            #self.dx = random.random()*10+20
            #self.dy= random.randint(-70,70)#rebalance
            self.rect.centerx = self.x
            self.rect.centery = self.y
            #--- not necessary:
            self.number = Actor.number # get my personal Birdnumber
            Actor.number+= 1           
            Actor.actors[self.number] = self
            Healthbar(self)
            Magicbar(self)
            
        def getChar(self):
            #Tile = 50*50
            x=int(self.pos[0]/50)
            y=int(self.pos[1]/50)+0 # correction value to get the tile under the feet doesn't actually work :\
            try:
                char=Game.level[y][x]
            except:
                char="?"
            return char
            
        def update(self, seconds):
            pressed_keys = pygame.key.get_pressed()
            self.rect.centerx = self.x
            self.rect.centery = self.y
            if self.stunned > 0:
                self.stunned -= seconds
            if self.stunned < 1:
                if pressed_keys[pygame.K_UP]:
                    self.y -= Game.ACTOR_SPEED
                if pressed_keys[pygame.K_DOWN]:
                    self.y += Game.ACTOR_SPEED
                if pressed_keys[pygame.K_LEFT]:
                    self.x -= Game.ACTOR_SPEED
                if pressed_keys[pygame.K_RIGHT]:
                    self.x += Game.ACTOR_SPEED
                if pressed_keys[pygame.K_w]:
                    self.y -= 5
                    self.hitpoints -=1.5
                if pressed_keys[pygame.K_s]:
                    self.y += 5
                    self.hitpoints -=1.5
                if pressed_keys[pygame.K_a]:
                    self.x -= 5
                    self.hitpoints -= 1.5
                if pressed_keys[pygame.K_d]:
                    self.x += 5
                    self.hitpoints -=1.5
                if self.stunned < 0:
                    self.stunned = 0
                if self.hitpoints< self.hitpointsfull:
                    self.hitpoints+= Game.ACTOR_REGEN
                if self.hitpoints< 30:
                    self.magic-= 10
                if self.magic < self.magicfull:
                    self.magic += 0.1
                for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if self.magic >= 50:
                                if event.key == pygame.K_3:
                                    for x in range(30):
                                        Explosion((self.x,self.y))
                                    self.x += 100
                                    self.hitpoints -= 50
                                    self.magic -= 50
                            if self.magic >= 200:
                                if event.key == pygame.K_1:
                                    for x in range (100):
                                        Explosion((self.x-100,self.y))
                                        Explosion((self.x+100,self.y))
                                        Explosion((self.x,self.y-100))
                                        Explosion((self.x,self.y+100))
                                        Explosion((self.x-75,self.y+75))
                                        Explosion((self.x+75,self.y-75))
                                        Explosion((self.x+75,self.y+75))
                                        Explosion((self.x-75,self.y-75))
                                    self.magic -= 200
                                if event.key == pygame.K_6:
                                    for x in range(5):
                                        Porters((self.x-150,self.y))
                            if self.magic >= 300:
                                if event.key == pygame.K_2:
                                    for x in range (500):
                                        Explosion((self.x-300,self.y))
                                    self.magic -= 300
                                if event.key == pygame.K_8:
                                    for x in range(200):
                                        Fireball((self.x- 300,self.y))
                                    self.magic -= 300
                            if self.magic >= 400:
                                if event.key == pygame.K_4:
                                    self.hitpoints += self.hitpointsfull/2
                                    self.magic -= 400
                            if self.magic >= 400:
                                if self.hitpoints > 200:
                                    if event.key == pygame.K_9:
                                        for x in range(20):
                                            Fireball((self.x,self.y))
                                            Explosion((self.x,self.y))
                                            Porters((self.x,self.y))
                                        self.magic -= 400
                                        self.hitpoints -= 200
                            if self.hitpoints > 500:
                                if event.key == pygame.K_5:
                                    for x in range(3000):
                                        Explosion((self.x,self.y))
                                    self.hitpoints -= 500
                            if self.hitpoints > 300:
                                if event.key == pygame.K_7:
                                    for x in range(200):
                                        Porters((self.x,self.y))
                                    self.hitpoints -= 300
                            if event.key == pygame.K_0:
                                if random.random() <0.9:
                                    self.hitpoints = 10
                                else:
                                    Game.ACTOR_REGEN += 0.05
                                    print("congrats")
                            if event.key == pygame.K_h:
                                self.hitpoints = self.hitpointsfull
                                self.magic = self.magicfull
            #self.mouse=pygame.mouse.get_pos()
            #pygame.mouse.set_pos(self.mouse[0]-5,self.mouse[1]-5)
            
            #self.x=self.mouse[0]
            #self.y=self.mouse[1]
            
            if self.getChar()=="p":
                self.hitpoints = 1
            
            
            if self.burntime > 0 :
                self.hitpoints -= 1.0
                # reduce burntime
                self.burntime -= 0.4
                Flame(self.rect.centerx, self.rect.centery)
            
            if self.hitpoints <= 0:
                self.kill()
            
            
            
            
        def kill(self):
            for _ in range(random.randint(7,20)):
                    Fragment((self.x,self.y))
                    #Monster.monsters[self.number] = None # kill Bird in sprite dictionary
            del(Actor.actors[self.number])
            self.actors = {}
            pygame.sprite.Sprite.kill(self) # kill the actual Actor
class Mouse(pygame.sprite.Sprite):  
        """Generic Monster"""
        images=[]  # list of all images
        # not necessary:
        mouses = {} # a dictionary of all monsters
        number = 0

        def __init__(self, level, startpos=(700,100)):
        #rebalance

            pygame.sprite.Sprite.__init__(self, self.groups ) #call parent class. NEVER FORGET !
            self.burntime = 0.0
            #print("i bin do")
            self.stunned = 0
            
            self.z = 0 # animationsnumber
            self.magic = 1000
            self.magicfull = 1000
            self.duration = 0.0 # how long was the current animation visible in seconds
            self.level=level
            self.nomove = False
            #self.stats{Game.ACTOR_ATKDMG : "Dmg",Game.ACTOR_SPEED : "speed", Game.ACTOR_DEF : "Def"}
            #startpos=(0,screen.get_rect().center[1])
            self.pos=startpos
            self.pos = [float(startpos[0]),float (startpos[1])] # dummy values to create a list
            self.pos[0] = float(startpos[0]) # float for more precise calculation
            self.pos[1] = float(startpos[1])
            #self.area = screen.get_rect()
            self.area = pygame.Rect(0,100,1024,300)
            self.image = Security.images[0]
            #self.hitpointsfull = float(hitpointsfull) # maximal hitpoints , float makes decimal
            #self.hitpoints = float(hitpointsfull) # actual hitpoints
            self.rect = self.image.get_rect()
            self.radius = max(self.rect.width, self.rect.height) / 2.0
            self.dx = 0
            self.dy = 0
            #self.regen = 0.5
            #self.dx = random.random()*10+20
            #self.dy= random.randint(-70,70)#rebalance
            self.rect.centerx = self.pos[0]
            self.rect.centery = self.pos[1]
            #--- not necessary:
            self.number = Mouse.number # get my personal Birdnumber
            Mouse.number+= 1           
            Mouse.mouses[self.number] = self
            
        def getChar(self):
            #Tile = 50*50
            x=int(self.pos[0]/50)
            y=int(self.pos[1]/50)+0 # correction value to get the tile under the feet doesn't actually work :\
            try:
                char=Game.level[y][x]
            except:
                char="?"
            return char
            
        def update(self, seconds):
            self.pos=pygame.mouse.get_pos()
            #pygame.mouse.set_pos(self.mouse[0]-5,self.mouse[1]-5)
            
            self.mouse = self.pos
            #print(self.mouse)
            
            if self.getChar()=="p":
                self.hitpoints = 1
            
            
            #if self.burntime > 0 :
                #self.hitpoints -= 1.0
                # reduce burntime
               # self.burntime -= 0.4
                #Flame(self.rect.centerx, self.rect.centery)
            
            #if self.hitpoints <= 0:
                #self.kill()
            #
            
            
            
        #def kill(self):
            #for _ in range(random.randint(7,20)):
                    #Fragment((self.x,self.y))
                    #Monster.monsters[self.number] = None # kill Bird in sprite dictionary
            #del(Actor.actors[self.number])
            #self.actors = {}
            #pygame.sprite.Sprite.kill(self) # kill the actual Actor
class Actor2(pygame.sprite.Sprite):  
        """Generic Monster"""
        images=[]  # list of all images
        # not necessary:
        actors2 = {} # a dictionary of all monsters
        number = 0

        def __init__(self, level, startpos=(700,400), hitpointsfull=600):
        #rebalance

            pygame.sprite.Sprite.__init__(self, self.groups ) #call parent class. NEVER FORGET !
            self.burntime = 0.0
            #print("i bin do")
            self.stunned = 0
            Actor2.x = startpos[0]
            Actor2.y = startpos[1]
            self.z = 0 # animationsnumber
            self.magic = 1000
            self.magicfull = 1000
            self.duration = 0.0 # how long was the current animation visible in seconds
            self.level=level
            self.nomove = False
            #self.stats{Game.ACTOR_ATKDMG : "Dmg",Game.ACTOR_SPEED : "speed", Game.ACTOR_DEF : "Def"}
            #startpos=(0,screen.get_rect().center[1])
            self.pos=startpos
            self.pos = [float(startpos[0]),float (startpos[1])] # dummy values to create a list
            #self.pos[0] = float(startpos[0]) # float for more precise calculation
            #self.pos[1] = float(startpos[1])
            #self.area = screen.get_rect()
            self.area = pygame.Rect(0,100,1024,300)
            self.image = Security.images[1]
            self.hitpointsfull = float(hitpointsfull) # maximal hitpoints , float makes decimal
            self.hitpoints = float(hitpointsfull) # actual hitpoints
            self.rect = self.image.get_rect()
            self.radius = max(self.rect.width, self.rect.height) / 2.0
            self.dx = 0
            self.dy = 0
            #self.regen = 0.5
            #self.dx = random.random()*10+20
            #self.dy= random.randint(-70,70)#rebalance
            self.rect.centerx = self.x
            self.rect.centery = self.y
            #--- not necessary:
            self.number = Actor.number # get my personal Birdnumber
            Actor2.number+= 1           
            Actor2.actors2[self.number] = self
            Healthbar(self)
            Magicbar(self)
            
        def getChar(self):
            #Tile = 50*50
            x=int(self.pos[0]/50)
            y=int(self.pos[1]/50)+0 # correction value to get the tile under the feet doesn't actually work :\
            try:
                char=Game.level[y][x]
            except:
                char="?"
            return char
            
        def update(self, seconds):
            pressed_keys = pygame.key.get_pressed()
            self.rect.centerx = self.x
            self.rect.centery = self.y
            if self.stunned > 0:
                self.stunned -= seconds
            if len(Mouse.mouses) > 0:
                      #print(len(Actor.actors))
                      self.victimnumber = random.choice(list(Mouse.mouses.keys()))
                      self.victim = Mouse.mouses[self.victimnumber]
                      if self.victim.pos[0] > self.x:
                         self.x += 3 
                      if self.victim.pos[0] < self.x:
                         self.x -= 3
                      if self.victim.pos[0] == self.x:
                         self.x = self.x
                      if self.victim.pos[1] < self.y:
                         self.y -= 3
                      if self.victim.pos[1] > self.y:
                         self.y += 3
                      if self.victim.pos[1] == self.y:
                         self.y = self.y
            elif len(Mouse.mouses) == 0:
                pass
            
            #print(pressed_keys)
            #if self.stunned < 1:
                ##if self.y > Mouse.x:
                    ##self.y -= Game.ACTOR_SPEED
                #if pressed_keys[pygame.K_DOWN]:
                    #self.y += Game.ACTOR_SPEED
                #if pressed_keys[pygame.K_LEFT]:
                    #self.x -= Game.ACTOR_SPEED
                #if pressed_keys[pygame.K_RIGHT]:
                    #self.x += Game.ACTOR_SPEED
                #if pressed_keys[pygame.K_w]:
                    #self.y -= 5
                    #self.hitpoints -=1.5
                #if pressed_keys[pygame.K_s]:
                    #self.y += 5
                    #self.hitpoints -=1.5
                #if pressed_keys[pygame.K_a]:
                    #self.x -= 5
                    #self.hitpoints -= 1.5
                #if pressed_keys[pygame.K_d]:
                    #self.x += 5
                    #self.hitpoints -=1.5
                #if self.stunned < 0:
                    #self.stunned = 0
                #if self.hitpoints < self.hitpointsfull:
                    #self.hitpoints+= Game.ACTOR_REGEN
                #if self.hitpoints< 30:
                    #self.magic-= 10
                #if self.magic < self.magicfull:
                    #self.magic += 0.1
                #for event in pygame.event.get():
                        #if event.type == pygame.KEYDOWN:
                            #if self.magic >= 50:
                                #if event.key == pygame.K_3:
                                    #for x in range(30):
                                        #Explosion((self.x,self.y))
                                    #self.x += 100
                                    #self.hitpoints -= 50
                                    #self.magic -= 50
                            #if self.magic >= 200:
                                #if event.key == pygame.K_1:
                                    #for x in range (100):
                                        #Explosion((self.x-100,self.y))
                                        #Explosion((self.x+100,self.y))
                                        #Explosion((self.x,self.y-100))
                                        #Explosion((self.x,self.y+100))
                                        #Explosion((self.x-75,self.y+75))
                                        #Explosion((self.x+75,self.y-75))
                                        #Explosion((self.x+75,self.y+75))
                                        #Explosion((self.x-75,self.y-75))
                                    #self.magic -= 200
                                #if event.key == pygame.K_6:
                                    #for x in range(5):
                                        #Porters((self.x-150,self.y))
                            #if self.magic >= 300:
                                #if event.key == pygame.K_2:
                                    #for x in range (500):
                                        #Explosion((self.x-300,self.y))
                                    #self.magic -= 300
                                #if event.key == pygame.K_8:
                                    #for x in range(200):
                                        #Fireball((self.x- 300,self.y))
                                    #self.magic -= 300
                            #if self.magic >= 400:
                                #if event.key == pygame.K_4:
                                    #self.hitpoints += self.hitpointsfull/2
                                    #self.magic -= 400
                            #if self.magic >= 400:
                                #if self.hitpoints > 200:
                                    #if event.key == pygame.K_9:
                                        #for x in range(20):
                                            #Fireball((self.x,self.y))
                                            #Explosion((self.x,self.y))
                                            #Porters((self.x,self.y))
                                        #self.magic -= 400
                                        #self.hitpoints -= 200
                            #if self.hitpoints > 500:
                                #if event.key == pygame.K_5:
                                    #for x in range(3000):
                                        #Explosion((self.x,self.y))
                                    #self.hitpoints -= 500
                            #if self.hitpoints > 300:
                                #if event.key == pygame.K_7:
                                    #for x in range(200):
                                        #Porters((self.x,self.y))
                                    #self.hitpoints -= 300
                            #if event.key == pygame.K_0:
                                #if random.random() <0.9:
                                    #self.hitpoints = 10
                                #else:
                                    #Game.ACTOR_REGEN += 0.05
                                    #print("congrats")
                            #if event.key == pygame.K_h:
                                #self.hitpoints = self.hitpointsfull
                                #self.magic = self.magicfull
            #self.mouse=pygame.mouse.get_pos()
            #pygame.mouse.set_pos(self.mouse[0]-5,self.mouse[1]-5)
            
            #self.x=self.mouse[0]
            #self.y=self.mouse[1]
            
            if self.getChar()=="p":
                self.hitpoints = 1
            
            
            if self.burntime > 0 :
                self.hitpoints -= 1.0
                # reduce burntime
                self.burntime -= 0.4
                Flame(self.rect.centerx, self.rect.centery)
            
            if self.hitpoints <= 0:
                self.kill()
            
            
            
            
        def kill(self):
            for _ in range(random.randint(7,20)):
                    Fragment((self.x,self.y))
                    #Monster.monsters[self.number] = None # kill Bird in sprite dictionary
            del(Actor2.actors2[self.number])
            self.actors = {}
            pygame.sprite.Sprite.kill(self) # kill the actual Actor

class Monster2(pygame.sprite.Sprite): 
        """Generic Monster"""
        images=[]  # list of all images
        # not necessary:
        monsters2 = {} # a dictionary of all monsters
        number2 = 0

        def __init__(self, level, startpos=(0,200), hitpointsfull=1000):
        #rebalance

            pygame.sprite.Sprite.__init__(self, self.groups ) #call parent class. NEVER FORGET !
            self.burntime = 0.0
            self.z = 0 # animationsnumber
            self.duration = 0.0 # how long was the current animation visible in seconds
            self.level=level
            self.nomove = False
            #startpos=(0,screen.get_rect().center[1])
            startpos2=(0,random.randint(100,350))
            self.pos = [float(startpos2[0]),float (startpos2[1])] # dummy values to create a list
            #self.pos[0] = float(startpos[0]) # float for more precise calculation
            #self.pos[1] = float(startpos[1])
           # self.area = screen.get_rect()
            self.area = pygame.Rect(0,100,1024,300)
            self.image = Monster2.images[self.z]
            self.hitpointsfull = float(hitpointsfull) # maximal hitpoints , float makes decimal
            self.hitpoints = float(hitpointsfull) # actual hitpoints
            self.rect = self.image.get_rect()
            self.radius = max(self.rect.width, self.rect.height) / 2.0
            self.dx= random.random()*10+20
            self.dy= random.randint(-70,70)#rebalance
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)
            #--- not necessary:
            self.number = Monster2.number2 # get my personal Birdnumber
            Monster2.number2+= 1           # increase the number for next Bird
            Monster2.monsters2[self.number] = self #
            Healthbar(self)
        def getChar(self):
            #Tile = 50*50
            x=int(self.pos[0]/50)
            y=int(self.pos[1]/50)+0 # correction value to get the tile under the feet doesn't actually work :\
            try:
                char=self.level[y][x]
            except:
                char="?"
            return char






        def update(self, seconds):
            self.duration += seconds
            if self.duration > 0.5:
                self.duration= 0
                self.z  +=1
                if self.z >= len(Monster2.images):
                    self.z = 0
                self.image=Monster2.images[self.z]

            #-------
            if self.getChar()=="g":
                self.hitpoints-= 0.5 #lava?
                self.burntime += 1.0
            if self.getChar()=="?":
                self.hitpoints=0
            if self.getChar()=="e":
                self.hitpoints=0
                Game.LIVES-=1
            if self.getChar()=="h":
                self.nomove = True

            
            if len(Actor.actors) > 0:
                      #print(len(Actor.actors))
                      self.victimnumber = random.choice(list(Actor.actors.keys()))
                      self.victim = Actor.actors[self.victimnumber]
                      if self.victim.x > self.pos[0]:
                        if self.victim.y < self.pos[1]:
                            self.pos[1]-=0.1
                        if self.victim.y > self.pos[1]:
                            self.pos[1]+=0.1
                        if self.victim.y == self.pos[1]:
                            self.pos[1]=self.pos[1]
                        
            elif(Actor.actors) == 0:
                self.dy = random.randint(-20,20)
            
            self.dx= 20
            if self.nomove:
                self.dx = 0
            self.pos[0] += self.dx * seconds
            #self.pos[1] += self.dy * seconds
            # -- check if monster is on screen
            if not self.area.contains(self.rect):
                
                # --- compare self.rect and area.rect
                if self.pos[0] + self.rect.width/2 > self.area.right:
                    self.pos[0] = self.area.right - self.rect.width/2
                if self.pos[0] - self.rect.width/2 < self.area.left:
                    self.pos[0] = self.area.left + self.rect.width/2
                if self.pos[1] + self.rect.height/2 > self.area.bottom:
                    self.pos[1] = self.area.bottom - self.rect.height/2
                if self.pos[1] - self.rect.height/2 < self.area.top:
                    self.pos[1] = self.area.top + self.rect.height/2
            #--- calculate new position on screen -----
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)
            #--- loose hitpoints
            
            if self.burntime > 0 :
                self.hitpoints -= 1.0
                # reduce burntime
                self.burntime -= 0.4
                Flame(self.rect.centerx, self.rect.centery)
            
            if self.hitpoints <= 0:
                self.kill()


        def kill(self):
            for _ in range(random.randint(7,20)):
                    Fragment(self.pos)
                    #Monster.monsters[self.number] = None # kill Bird in sprite dictionary
            del(Monster2.monsters2[self.number]) 
            pygame.sprite.Sprite.kill(self) # kill the actual Monster
            Game.XP += 50


   
class Security(pygame.sprite.Sprite):
        """Generic Monster"""
        images=[]  # list of all images
        # not necessary:
        securitys = {} # a dictionary of all monsters
        number = 0

        def __init__(self, level, startpos=(-1,200), hitpointsfull=1200):


            pygame.sprite.Sprite.__init__(self, self.groups ) #call parent class. NEVER FORGET !
            self.burntime = 0.0
            if startpos[0]== -1:
                startpos=(Viewer.screenwidth, random.randint(150,250))
            self.z = 0 # animationsnumber
            self.duration = 0.0 # how long was the current animation visible in seconds
            self.level=level
            self.nomove = False
            #startpos=(0,screen.get_rect().center[1])
            startpos=(Viewer.screenwidth,random.randint(100,350))
            self.pos = [float(startpos[0]),float (startpos[1])] # dummy values to create a list
            #self.pos[0] = float(startpos[0]) # float for more precise calculation
            #self.pos[1] = float(startpos[1])
           # self.area = screen.get_rect()
            self.area = pygame.Rect(0,100,1024,300)
            self.image = Security.images[self.z]
            self.hitpointsfull = float(hitpointsfull) # maximal hitpoints , float makes decimal
            self.hitpoints = float(hitpointsfull) # actual hitpoints
            self.rect = self.image.get_rect()
            self.radius = max(self.rect.width, self.rect.height) / 2.0
            self.dx= random.random()*-10+20
            self.dy= random.randint(-70,70)
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)
            #--- not necessary:
            self.taser = False
            self.number = Security.number # get my personal Birdnumber
            Security.number+= 1           # increase the number for next Bird
            Security.securitys[self.number] = self #
            Healthbar(self)


        #def newspeed(self):
            # new birdspeed, but not 0
            #speedrandom = random.choice([-1,1]) # flip a coin
            #self.dx = random.random() * ACTORSPEEDMAX * speedrandom + speedrandom
            #self.dy = random.random() * ACTORSPEEDMAX * speedrandom + speedrandom
        def getChar(self):
            #Tile = 50*50
            x=int(self.pos[0]/50)
            y=int(self.pos[1]/50)+0 # correction value to get the tile under the feet doesn't actually work :\
            try:
                char=self.level[y][x]
            except:
                char="?"
            return char


        def kill(self):
            for _ in range(random.randint(10,30)):
                Fragment(self.pos)
            Security.securitys[self.number] = None # kill Bird in sprite dictionary
            Game.XP += 60
            pygame.sprite.Sprite.kill(self) # kill the actual Bird
            

        def update(self, seconds):
            self.duration += seconds
            if self.duration > 0.5:
                self.duration= 0
                self.z  +=1
                if self.z >= len(Security.images):
                    self.z = 0
                self.image=Security.images[self.z]

            #-------
            #if self.getChar()=="g":
                #self.hitpoints-=1 #lava?
                #self.burntime += 1.0
            if self.getChar()=="?":
                self.hitpoints=0
            #if self.getChar()=="e":
                #self.hitpoints=0
                #Game.LIVES-=1
            if self.getChar()=="h":
                self.nomove = True
            else:
                self.nomove = False
            self.dy=random.randint(-50, 50)
            self.dx= -25#random.randint(10,10)
            if self.nomove:
                self.dx = 0
            self.pos[0] += self.dx * seconds
            self.pos[1] += self.dy * seconds
            # -- check if Bird out of screen
            if not self.area.contains(self.rect):
                #self.crashing = True # change colour later
                # --- compare self.rect and area.rect
                if self.pos[0] + self.rect.width/2 > self.area.right:
                    self.pos[0] = self.area.right - self.rect.width/2
                if self.pos[0] - self.rect.width/2 < self.area.left:
                    self.pos[0] = self.area.left + self.rect.width/2
                if self.pos[1] + self.rect.height/2 > self.area.bottom:
                    self.pos[1] = self.area.bottom - self.rect.height/2
                if self.pos[1] - self.rect.height/2 < self.area.top:
                    self.pos[1] = self.area.top + self.rect.height/2
                #self.newspeed() # calculate a new direction
            #--- calculate actual image: crasing, catched, both, nothing ?
            #self.image = Bird.image[self.crashing + self.catched*2]
            #--- calculate new position on screen -----
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)
            #--- loose hitpoins
            #if self.crashing:
             #self.hitpoints -=1
            #if self.burntime > 0 :
                #self.hitpoints -= 1.0
                # reduce burntime
                #self.burntime -= 0.4
                #Flame(self.rect.centerx, self.rect.centery)
            
            if self.hitpoints <= 0:
                self.kill()


class Viewer(object):

     screenwidth = 1025
     screenheight = 400
     
     def __init__(self, width=0, height=0, fps=30):
        """Initialize pygame, window, background, font,...
           default arguments
        """
        
        

        pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = height
        if self.width == 0:
            self.width = Viewer.screenwidth
        else:
            Viewer.screenwidth = width
        if self.height == 0:
            self.height = Viewer.screenheight
        else:
            Viewer.screenheight = self.height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        #self.background.fill((255,255,255)) # fill background white
        self.background.fill((1,75,176))     # fill the background white (red,green,blue)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 24, bold=True)

        # sprite groups
        self.playergroup = pygame.sprite.LayeredUpdates()
        self.mousegroup = pygame.sprite.Group()
        self.bargroup = pygame.sprite.Group()
        self.stuffgroup = pygame.sprite.Group()
        self.fragmentgroup = pygame.sprite.Group()
        self.portersgroup = pygame.sprite.Group()
        self.fballgroup = pygame.sprite.Group()
        self.e_portersgroup = pygame.sprite.Group()
        self.e_fballgroup = pygame.sprite.Group()
        self.allgroup = pygame.sprite.LayeredUpdates()
        self.monstergroup=pygame.sprite.Group()
        self.evilmagiciangroup = pygame.sprite.Group()
        self.evilmagiciangroup2 = pygame.sprite.Group()
        self.magicbombergroup = pygame.sprite.Group()
        self.allgroup = pygame.sprite.LayeredUpdates()
        self.bargroup = pygame.sprite.Group()
        self.fragmentgroup = pygame.sprite.Group()
        self.explosiongroup = pygame.sprite.Group()
        self.e_explosiongroup = pygame.sprite.Group()
        #self.securitygroup= pygame.sprite.Group()
        self.actorgroup = pygame.sprite.Group()

        #DiscProjectile.groups = self.allgroup, self.projectilegroup
        #DiscoLaserCannon.groups = self.allgroup, self.cannongroup
        Monster.groups = self.allgroup, self.monstergroup
        Monster2.groups =  self.allgroup, self.monstergroup
        EvilMagician.groups =  self.allgroup, self.monstergroup, self.evilmagiciangroup
        EvilMagician2.groups =  self.allgroup, self.monstergroup, self.evilmagiciangroup, self.evilmagiciangroup2
        MagicBomber.groups =  self.allgroup, self.evilmagiciangroup, self.evilmagiciangroup2, self.magicbombergroup
        E_Explosion.groups = self.allgroup, self.e_explosiongroup
        E_Fireball.groups = self.allgroup, self.e_fballgroup
        E_Porters.groups = self.allgroup, self.e_portersgroup
        Fragment.groups = self.allgroup, self.fragmentgroup
        Explosion.groups = self.allgroup, self.explosiongroup
        Fireball.groups = self.allgroup, self.fballgroup
        Porters.groups = self.allgroup, self.portersgroup
        Healthbar.groups = self.allgroup, self.bargroup
        Magicbar.groups = self.allgroup, self.bargroup
        Flame.groups = self.allgroup
        #Security.groups = self.allgroup, self.securitygroup
        Actor.groups = self.allgroup, self.actorgroup
        Actor2.groups = self.allgroup, self.actorgroup
        Mouse.groups = self.allgroup, self.mousegroup
        self.game = Game()
        
        
     def paint(self):
        # paint the level of self.game
        x=0
        y=0
        self.game.fleckanim=[]
        for zeile in self.game.level:
          for fleck in zeile:
               self.game.fleckanim.append(0)
               self.background.blit(self.game.legende[fleck],(x,y))
               x+=50
          y+=50
          x=0
        #DiscoLaserCannon(500,100, self.screen) 
        #DiscoLaserCannon(700,100, self.screen) 
        #DiscoLaserCannon(600,100, self.screen) 
        #DiscoLaserCannon(400,100, self.screen) 
        #DiscoLaserCannon(900,100, self.screen) 
        #DiscoLaserCannon(500,200, self.screen) 
        #DiscoLaserCannon(700,350, self.screen) 
        #DiscoLaserCannon(600,350, self.screen) 
        #DiscoLaserCannon(400,450, self.screen) 
        #DiscoLaserCannon(900,550, self.screen) 
        #DiscoLaserCannon()
        #print("Action....")
        Actor((100,100))
        Actor2((300,400))
        Mouse((100,100))
        print("""1 for ring of magic\n 2 for big boom\n 3 to tp, simple Blood and port magic
4 to heal\n5bloodmagic: BIG BANG\n6 Green porter balls, port enemys at they're spawn
7 Blood- and portmagic : MOOOOORE PORTER BALLS\n7 fire storm Fire Magic\n8 bigger fire storm, BLOOD AND FIREMAGIC\n9 mix:blood fire and port magic\n0: High risk magic 1:10 chance to loose halve the magic and get exactly ten live""")          
     def run(self):
        """The mainloop
        """
        lasertimer = 0.0 # ....klasse !!
        victimnumber = None
        self.paint()
        running = True
        millis = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key==pygame.K_F2:
                        for px in range (0,5):
                            Security(self.game.level, hitpointsfull = 2000)
                    if event.key == pygame.K_F3:
                            Actor((random.randint(0,7),random.randint(1,5)))
                    if event.key == pygame.K_p:
                        Actor.x +=50
                        Actor.hitpoints -= 50
                    self.pressed_keys = pygame.key.get_pressed()
            if Game.XP >= Game.ACTOR_NEEDEDXP:
                Game.ACTOR_LVL += 1
                Game.ACTOR_ATKDMG += 5
                Game.ACTOR_DEF += 0.5
                Game.ACTOR_KB += 0.5
                Game.ACTOR_REGEN += 0.05
                Game.ACTOR_SPEED += 0.05
                Game.MAGIC_POWER += 0.1
                Game.XP -= Game.ACTOR_NEEDEDXP
                Game.ACTOR_NEEDEDXP = Game.ACTOR_LVL * 100 + 100
                #print(Game.ACTOR_LVL * 100 + 100)
                #print(Game.ACTOR_NEEDEDXP)
                e.msgbox("""LVL UP:{}\n,DMG:{},\nDEF:{},\nknockback:{}, \nSPEED:{},\nREGEN:{}",nextlvl UP:{},\nGame is running on even if easygui is open. close soon""".format(Game.ACTOR_LVL,Game.ACTOR_ATKDMG,Game.ACTOR_DEF,Game.ACTOR_KB,Game.ACTOR_SPEED,Game.ACTOR_REGEN, Game.ACTOR_NEEDEDXP)
                        )
                    # ------CHEAT KEY----------
                    
                    #if event.key==pygame.K_F1:
                       #for px in range (0,240):
                           #DiscProjectile(pos=(random.randint(540,1024),random.randint(100,400)))12
            
            self.pressed_keys = pygame.key.get_pressed()
            
            milliseconds = self.clock.tick(self.fps)
            millis += milliseconds
            seconds=milliseconds /1000.0
            self.playtime += milliseconds / 1000.0
            self.playtime += milliseconds / 1000.0
            self.draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS, Xp:{}".format(
                           self.clock.get_fps(), " "*5, self.playtime, Game.XP))

            pygame.display.flip()
            self.screen.blit(self.background, (0, 0)) # alles löschen
            # level aufbauen

            # monster spawn
            if random.random()<self.game.SPAWNRATE:
               Monster(self.game.level)
               
            if random.random()<self.game.SPAWNRATE2:
               Monster2(self.game.level)
               
            #if random.random()<self.game.SECURITYSPAWNRATE:
             #  Security(self.game.level)
               
            if pygame.K_s in self.pressed_keys:
                Actor(self.game.level)
            
            if len(EvilMagician.evilmagicians) + len(EvilMagician2.evilmagicians2) < 1:
                magician = random.random()
                if magician <= 0.5:
                    EvilMagician(self.game.level)
                if magician > 0.5:
                    EvilMagician2(self.game.level)
                print (len(EvilMagician.evilmagicians) + len(EvilMagician2.evilmagicians2))
            # spritecollide
            
            if millis > 500: # jede halbe sekunde neue animation
                millis=0
                z=0
                x=0
                y=0
                for zeile in self.game.level:
                    for fleck in zeile:
                        if fleck == "d" and self.game.fleckanim[z] == 0:      
                            if random.random() < 0.005:
                                self.game.fleckanim[z] += 1
                        elif fleck == "g" and self.game.fleckanim[z] == 0:
                            if random.random() < 0.5:
                                self.game.fleckanim[z] += 1
                        else:
                            self.game.fleckanim[z] += 1 # normaler fleck
                        if fleck == "v":
                            targetlist=[]
                            for target in self.monstergroup:
                                #pass # pythagoras distanz ausrechnen
                                #ziel wird gesucht reichweite getestet
                                #zufälliges ziel wird abgeschossen
                                distx=abs(target.pos[0]-x)
                                disty=abs(target.pos[1]-y)
                                dist=(distx**2+disty**2)**0.5
                                if dist<self.game.DISCTHROWERRANGE:
                                    targetlist.append(target)
                            if len(targetlist)>0:
                                target=random.choice(targetlist)
                                #print("taget found{}".format(target.pos) )
                                #schuss
                                #  fliegt nur nach rechts unten
                                if target.pos[0]> x:
                                    xsign = 1
                                else:
                                    xsign = -1
                                if target.pos[1]> y:
                                    ysign = 1
                                else:
                                    ysign = -1
                                #DiscProjectile((x,y),(target.pos[0], target.pos[1]))
                            #else:
                             #   print("No target found")
                        if self.game.fleckanim[z] > 5:
                            self.game.fleckanim[z] = 0       
                        z+=1
                        x+=50
                    y+=50
                    x=0
                 
            
            # monster take damage from discs
            #for mymonster in self.monstergroup:
                #crashgroup = pygame.sprite.spritecollide(mymonster, self.projectilegroup, False)
                #for myprojectile in crashgroup:
                      #mymonster.hitpoints-=0.25
                      ##mymonster.pos[0] -= 5 # test for collision with bullet
                      #myprojectile.hitpoints-=0.25
            ##for mymonster in self.monstergroup:
                #crashgroup = pygame.sprite.spritecollide(mymonster, self.cannongroup, False)
                #for mycannon in crashgroup:
                      ##mymonster.hitpoints-=0.25
                      #mymonster.pos[0] -= 5 # test for collision with bullet
                      #mycannon.hitpoints-=0.25
            for mymonster in self.monstergroup:
                crashgroup = pygame.sprite.spritecollide(mymonster, self.actorgroup, False)
                for myactor in crashgroup:
                      mymonster.hitpoints-= Game.ACTOR_ATKDMG
                      mymonster.pos[0] -= 10
                      myactor.x += 10
                      myactor.magic += 1
                      myactor.hitpoints-=30.00 - Game.ACTOR_DEF
            for mymonster in self.monstergroup:
                crashgroup = pygame.sprite.spritecollide(mymonster, self.explosiongroup, False)
                for myexplosion in crashgroup:
                      mymonster.hitpoints-= 0.2 * Game.MAGIC_POWER
            for mymonster in self.monstergroup:
                crashgroup = pygame.sprite.spritecollide(mymonster, self.portersgroup, False)
                for myporters in crashgroup:
                      mymonster.pos[0] = 0
            for mymonster in self.monstergroup:
                crashgroup = pygame.sprite.spritecollide(mymonster, self.fballgroup, False)
                for myporters in crashgroup:
                      mymonster.burntime += 5 * Game.MAGIC_POWER
            for myactor in self.actorgroup:
                crashgroup = pygame.sprite.spritecollide(myactor, self.e_explosiongroup, False)
                for mye_explosion in crashgroup:
                      myactor.hitpoints-= 0.2
            for myactor in self.actorgroup:
                crashgroup = pygame.sprite.spritecollide(myactor, self.e_portersgroup, False)
                for mye_porters in crashgroup:
                      myactor.pos[0] = 1025
            for myactor in self.actorgroup:
                crashgroup = pygame.sprite.spritecollide(myactor, self.e_fballgroup, False)
                for mye_fballs in crashgroup:
                      myactor.burntime += 5
            for myactor in self.actorgroup:
                crashgroup = pygame.sprite.spritecollide(myactor, self.fragmentgroup, True)
                for myfragment in crashgroup:
                      myactor.magic += 5
            for myactor in self.actorgroup:
                crashgroup = pygame.sprite.spritecollide(myactor, self.magicbombergroup, False)
                for mymagicbomber in crashgroup:
                      mymagicbomber.Boom = 1
            #and securitys
            #for mysecurity in self.securitygroup:
                #crashgroup = pygame.sprite.spritecollide(mysecurity, self.monstergroup, False)
                #mysecurity.taser = False
                #for mymonster in crashgroup:
                      #mymonster.hitpoints-=4 # test for collision with bullet
                      #mymonster.pos[0]-=random.randint(5,20)
                      #mysecurity.hitpoints-=5
                      #mysecurity.pos[0]+=random.randint(1,7)
                      #mysecurity.taser = True
            #for mymouse in self.Actorgroup:
                #crashgroup = pygame.sprite.spritecollide(mysecurity, self.actorgroup, False)
                #mysecurity.taser = False
                #for mymonster in crashgroup:
                      #mymonster.hitpoints-=4 # test for collision with bullet
                      #mymonster.pos[0]-=random.randint(5,20)
                      #mysecurity.hitpoints-=5
                      #mysecurity.pos[0]+=random.randint(1,7)
                      #mysecurity.taser = True
            # laser # soll eine Klasse werden!!!

                #pygame.draw.line #rebalance
                
            # bunter lichtlaser
            #pygame.draw.line(self.screen,(random.randint(0,255),random.randint(0,255),
                             #random.randint(0,255)),(925,25),(random.randint(0,950),
                             #random.randint(0,500)),random.randint(5,15))
            # bunter lichtlaser
            #pygame.draw.line(self.screen,(random.randint(0,255),random.randint(0,255),
                             #random.randint(0,255)),(325,25),(random.randint(0,950),
                             #random.randint(0,500)),random.randint(5,15))
            
         
            #allgroup.clear(screen, background)
            self.allgroup.update(seconds)
            self.allgroup.draw(self.screen)

        pygame.quit()
        #name = e.enterbox("name","Whats your name?")
        #f=open("high_scores.txt","w")
        #if Game.KILLS == 1:
            #s=""
        #else:
            #s="s"
        #f.("{} killed {} Magician{}.\n".format(name,Game.KILLS,s))
        #f.close()


     def draw_text(self, text):
        """Center text in window
        """
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(surface, (25,5))


## code on module level
if __name__ == '__main__':

    # call with width of window and fps
    Viewer().run()
