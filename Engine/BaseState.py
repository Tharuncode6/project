from pygame import rect
from Engine.DebugLog import Debug
from Engine.Vector2 import Vector2
import pygame

class Entity:
    def __init__(self, texName, position, rotation, scale):
        self.name = texName
        self.position = position
        self.rotation = rotation
        self.scale = scale

class BaseState:
    def __init__(self, rm, win, name):
        self.rm = rm # Resource Manager 
        self.backgroundColor = (255,255,255)
        self.renderList = []
        self.debuglines = []
        self.debugrects = []
        self.window = win
        self.name = name
        self.eventlist =[]

    def Load(self):
        Debug.Log(f'Loading... {self.name}')
        
    def Unload(self):
        Debug.Log(f'Unloading... {self.name}')

    def Update(self, dt):
        pass

    def AddDrawCall(self, texName, position = Vector2(), rotation = 0, scale = Vector2()):
        self.renderList.append(Entity(texName, position, rotation, scale))
    
    def AddDrawDebugLineCall(self, start, end, color):
        self.debuglines.append((start, end, color))

    def AddDrawDebugRectCall(self, topleft, dim, color):
        self.debugrects.append((topleft, dim, color))

    def Draw(self):
        # Background
        self.window.fill(self.backgroundColor)
        # Draw all Object
        for entity in self.renderList:
            texture = self.rm.GetTexture(entity.name)
            if texture != None:
                self.window.blit(texture.tex, (entity.position.x, entity.position.y))
            else:
                Debug.Error(f'{entity.name} is not loaded...')
        # Draw all debug
        for line in self.debuglines:
            pygame.draw.line(self.window, line[2], line[0], line[1], 2)
        for sq in self.debugrects:
            pygame.draw.rect(self.window, sq[2], pygame.Rect(sq[0].x,sq[0].y,sq[1].x,sq[1].y), 2)
        # Refresh
        pygame.display.update()
        self.renderList.clear()
        self.debuglines.clear()
        self.debugrects.clear()
        
    def LogInfo(self):
        Debug.Log(f'Level name : {self.name}')