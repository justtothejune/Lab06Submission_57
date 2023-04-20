import sys 
import pygame as pg


class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0): #ตัวแปรที่เอาไว้แทนค่าตัวมันเอง
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(120,20,220),(self.x,self.y,self.w,self.h))

pg.init()
run = True
win_x, win_y = 800, 480
px = 200
py = 200
screen = pg.display.set_mode((win_x, win_y))
firstObject = Rectangle(px,py,100,100) # สร้าง Object จากคลาส Rectangle ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    firstObject.draw(screen) # ใส่ screen เข้าไปด้วยเพราะว่าคำสั่ง pg.draw.rect จะเป็นจะต้องระบุระนาบว่าต้องการสร้างรูปบนระนาบใด
    pg.time.delay(50)
    
    for event in pg.event.get(): #มีไว้ดึง event ทั้งหมดที่ค้างใน queue ออกมาแล้วคืนค่าเป็น list ของ object ประเภท pygame.event 
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w :
                firstObject.y -= 5 
                print("Key W")
            elif event.key == pg.K_s:
                firstObject.y += 5 
                print("Key S")
            elif event.key == pg.K_d:
                firstObject.x += 5 
                print("Key D")
            elif event.key == pg.K_a:
                firstObject.x -= 5 
                print("Key A")
    pg.display.update()

    