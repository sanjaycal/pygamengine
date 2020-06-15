import pygame
import math
import sys

FPS = 60
Display_Size = {"x":960,"y":540}
FOV = {"x":160,"y":90}

corners = [[-0.5,-0.5,1],[-0.5,0.5,1],[0.5,-0.5,1],[0.5,0.5,1],[-0.5,-0.5,2],[-0.5,0.5,2],[0.5,-0.5,2],[0.5,0.5,2]]

pygame.init()
display = pygame.display.set_mode((Display_Size["x"],Display_Size["y"]))
pygame.display.set_caption("Test")
clock = pygame.time.Clock()

def List_to_Dict(list):
    if len(list) == 2:
        dict = {"x":list[0],"y":list[1]}
    elif len(list) == 3:
        dict = {"x":list[0],"y":list[1],"z":list[2]}
    return dict

def Radians_to_Degrees(Radian):
    degree = Radian*180/math.pi
    return degree

def Degrees_to_Radians(Degrees):
    radian = Degrees*math.pi/180
    return radian

def world_to_screen_space(x,y,z):
    a = (Radians_to_Degrees(math.atan(x/z))*Display_Size["x"]/FOV["x"]+Display_Size["x"]/2,-1*Radians_to_Degrees(math.atan(y/z))*Display_Size["y"]/FOV["y"]+Display_Size["y"]/2)
    return a

def Draw_Rect(corner1,corner2,corner3,corner4):
    corner1 = List_to_Dict(corner1)
    corner2 = List_to_Dict(corner2)
    corner3 = List_to_Dict(corner3)
    corner4 = List_to_Dict(corner4)
    ss_corner1 = (world_to_screen_space(corner1["x"],corner1["y"],corner1["z"]))
    ss_corner2 = (world_to_screen_space(corner2["x"],corner2["y"],corner2["z"]))
    ss_corner3 = (world_to_screen_space(corner3["x"],corner3["y"],corner3["z"]))
    ss_corner4 = (world_to_screen_space(corner4["x"],corner4["y"],corner4["z"]))
    pygame.draw.polygon(display,pygame.Color(100,100,100),[ss_corner1,ss_corner2,ss_corner3,ss_corner4],10)

def Draw_Rect_Prism(corners):
    corner1 = corners[0]
    corner2 = corners[1]
    corner3 = corners[2]
    corner4 = corners[3]
    corner5 = corners[4]
    corner6 = corners[5]
    corner7 = corners[6]
    corner8 = corners[7]
    Draw_Rect(corner1,corner2,corner4,corner3)
    Draw_Rect(corner5,corner6,corner8,corner7)
    Draw_Rect(corner1,corner2,corner6,corner5)
    Draw_Rect(corner3,corner4,corner8,corner7)
    Draw_Rect(corner1,corner3,corner7,corner5)
    Draw_Rect(corner2,corner4,corner8,corner6)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.draw.rect(display,pygame.Color(0,0,0),pygame.Rect(0,0,Display_Size["x"],Display_Size["y"]))
    for corner in corners:
        corner[0] = (corner[0])*math.cos(Degrees_to_Radians(2)) - (corner[2]-1.5)*math.sin(Degrees_to_Radians(2))
        corner[2] = (corner[0])*math.sin(Degrees_to_Radians(2)) + (corner[2]-1.5)*math.cos(Degrees_to_Radians(2))+1.5
        a = math.sqrt(corner[0]*corner[0]+(corner[2]-1.5)*(corner[2]-1.5))
        corner[0] = corner[0]/a
        corner[2] = (corner[2]-1.5)/a + 1.5
    Draw_Rect_Prism(corners)
    pygame.display.update()
    clock.tick(FPS)