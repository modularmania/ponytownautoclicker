import time
import pyautogui
import random

screenWidth, screenHeight = pyautogui.size()
while True:
     pyautogui.PAUSE = 1
     def runAround():
          pyautogui.PAUSE = 0.8
          for _ in range(random.randrange(4,12)):
               with pyautogui.hold('shift'):
                    pyautogui.keyDown('left')
                    pyautogui.keyDown('up')
                    pyautogui.keyUp('left')
                    pyautogui.keyDown('right')
                    pyautogui.keyUp('left')
                    pyautogui.keyDown('down')
                    pyautogui.keyUp('right')
                    pyautogui.keyDown('left')
                    pyautogui.keyUp('left')

          stand()



     def standLay():
          pyautogui.press('x')
          pyautogui.PAUSE = 0.7
          pyautogui.press('x')
          time.sleep(random.randrange(100, 340))

          if random.randrange(1, 3) == 1:
                pyautogui.click(random.randrange(1,screenWidth), random.randrange(1, screenHeight))

          else:
                pyautogui.doubleClick(random.randrange(1,screenWidth), random.randrange(1, screenHeight))

          pyautogui.moveTo(random.randrange(1,screenWidth), random.randrange(1, screenHeight))
          RAND = random.randrange(101)

          if RAND <= 15:
               runAround()

          elif RAND <= 30:
               stand()

          elif RAND <= 45:
               laySit()

          elif RAND <= 60:
               layFly()

          elif RAND <= 85:
               layPushUp()

          elif RAND <= 100:
               sendMessage()



     def standSit():
          pyautogui.press('x')
          time.sleep(random.randrange(300, 540))

          if random.randrange(1, 3) == 1:
                pyautogui.click(random.randrange(1,screenWidth), random.randrange(1, screenHeight))

          else:
                pyautogui.doubleClick(random.randrange(1,screenWidth), random.randrange(1, screenHeight))

          RAND = random.randrange(101)

          if RAND <= 15:
               runAround()

          elif RAND <= 30:
               stand()

          elif RAND <= 45:
               sitLay()

          elif RAND <= 60:
               sitFly()

          elif RAND <= 85:
               sitPushUp()

          elif RAND <= 100:
               sendMessage()



     def standFly():
          pyautogui.press('c')
          time.sleep(6)

          if random.randrange(1, 3) == 1:
                pyautogui.click(random.randrange(1,screenWidth), random.randrange(1, screenHeight))

          else:
                pyautogui.doubleClick(random.randrange(1,screenWidth), random.randrange(1, screenHeight))

          pyautogui.moveTo(random.randrange(1,screenWidth), random.randrange(1, screenHeight))
          RAND = random.randrange(101)

          if RAND <= 15:
               runAround()

          elif RAND <= 30:
               stand()

          elif RAND <= 45:
               flySit()

          elif RAND <= 60:
               flyLay()

          elif RAND <= 85:
               time.sleep(1)
               pyautogui.press('b')
               time.sleep(1)
               pyautogui.press('b')
               time.sleep(2)
               pyautogui.press('b')
               hop()

          elif RAND <= 100:
               sendMessage()



     def sendMessage():
         pyautogui.press('enter')
         pyautogui.PAUSE = 1.2
         pyautogui.write('Test.', interval = 0.25)
         pyautogui.press('enter')

         stand()



     def clickPlus():
          pyautogui.click()

          pyautogui.PAUSE = 1.5

          time.sleep(3)
          pyautogui.click(random.randrange(1, screenWidth), random.randrange(1, screenHeight))
          pyautogui.doubleClick(random.randrange(1, screenWidth), random.randrange(1, screenHeight))
          pyautogui.moveTo(random.randrange(1, screenWidth), random.randrange(1, screenHeight))
          time.sleep(2)

          pyautogui.keyDown('left')
          time.sleep(0.1)
          pyautogui.click()
          pyautogui.press('left')

          stand()



     def sitLay():
          pyautogui.press('x')
          time.sleep(random.randrange(100, 340))

          if random.randrange(1, 3) == 1:
               pyautogui.click(random.randrange(1, screenWidth), random.randrange(1, screenHeight))

          else:
               pyautogui.doubleClick(random.randrange(1, screenWidth), random.randrange(1, screenHeight))
               pyautogui.PAUSE = 1.3

          pyautogui.moveTo(random.randrange(1, screenWidth), random.randrange(1, screenHeight))
          RAND = random.randrange(101)

          if RAND <= 15:
               runAround()

          elif RAND <= 30:
               stand()

          elif RAND <= 45:
               sitLay()

          elif RAND <= 60:
               sitFly()

          elif RAND <= 85:
               sitPushUp()

          elif RAND <= 100:
               sendMessage()



     def sitPushUp():
          pyautogui.doubleClick(random.randrange(1, screenWidth), random.randrange(1, screenHeight))
          pyautogui.PAUSE = 0.8

          for _ in range(random.randrange(4, 12)):
               pyautogui.press('down')
               pyautogui.press('up')

               RAND = random.randrange(101)

               if RAND <= 15:
                    runAround()

               elif (RAND <= 30):
                    stand()

               elif (RAND <= 45):
                    sitLay()

               elif (RAND <= 60):
                    sitFly()

               elif (RAND <= 85):
                    sitPushUp()

               elif (RAND <= 100):
                    sendMessage()



     def sitFly():
          pyautogui.press('c')
          pyautogui.press('c')
          time.sleep(10)

          if random.randrange(1, 3) == 1:
               pyautogui.click(random.randrange(1, screenWidth), random.randrange(1, screenHeight))

          else:
               pyautogui.doubleClick(random.randrange(1, screenWidth), random.randrange(1, screenHeight))

          pyautogui.moveTo(random.randrange(1, screenWidth), random.randrange(1, screenHeight))
          RAND = random.randrange(101)

          if (RAND <= 15):
               runAround()

          elif (RAND <= 30):
               stand()

          elif (RAND <= 45):
               flySit()

          elif (RAND <= 60):
               flyLay()

          elif (RAND <= 85):
               time.sleep(1)
               pyautogui.press('b')
               time.sleep(1)
               hop()

          elif (RAND <= 100):
               sendMessage()



     def layPushUp():
          pyautogui.doubleClick(random.randrange(1,screenWidth), random.randrange(1, screenHeight))
          pyautogui.PAUSE = 0.8
          for _ in range(random.randrange(4,12)):
               pyautogui.press('up')
               pyautogui.press('down')

          RAND = random.randrange(101)

          if RAND <= 15:
               runAround()

          elif RAND <= 30:
               stand()

          elif RAND <= 45:
               laySit()

          elif RAND <= 60:
               layFly()

          elif RAND <= 85:
               layPushUp()

          elif RAND <= 100:
               sendMessage()



     def laySit():
          pyautogui.press('c')
          time.sleep(random.randrange(200, 440))

          if random.randrange(1, 3) == 1:
                pyautogui.click(random.randrange(1,screenWidth), random.randrange(1, screenHeight))

          else:
                pyautogui.doubleClick(random.randrange(1,screenWidth), random.randrange(1, screenHeight))

          RAND = random.randrange(101)

          if RAND <= 15:
               runAround()

          elif RAND <= 30:
               stand()

          elif RAND <= 45:
               sitLay()

          elif RAND <= 60:
               sitFly()

          elif RAND <= 85:
               sitPushUp()

          elif RAND <= 100:
               sendMessage()



     def layFly():
          pyautogui.PAUSE = 1.2
          pyautogui.press('c')
          pyautogui.press('c')
          pyautogui.press('c')
          time.sleep(3)

          if random.randrange(1, 3) == 1:
                pyautogui.click(random.randrange(1,screenWidth), random.randrange(1, screenHeight))

          else:
                pyautogui.doubleClick(random.randrange(1,screenWidth), random.randrange(1, screenHeight))

          pyautogui.moveTo(random.randrange(1,screenWidth), random.randrange(1, screenHeight))
          RAND = random.randrange(101)

          if RAND <= 15:
               runAround()

          elif RAND <= 30:
               stand()

          elif RAND <= 45:
               flySit()

          elif RAND <= 60:
               flyLay()

          elif RAND <= 85:
               time.sleep(1)
               pyautogui.press('b')
               time.sleep(1)
               pyautogui.press('b')
               time.sleep(2)
               pyautogui.press('b')
               hop()

          elif (RAND <= 100):
               sendMessage()



     def flySit():
          pyautogui.press('c')
          pyautogui.press('c')
          time.sleep(random.randrange(150, 590))

          RAND = random.randrange(101)

          if RAND <= 15:
               runAround()

          elif RAND <= 30:
               stand()

          elif RAND <= 45:
               sitLay()

          elif RAND <= 60:
               sitFly()

          elif RAND <= 85:
               sitPushUp()

          elif RAND <= 100:
               sendMessage()



     def flyLay():
          pyautogui.press('x')
          pyautogui.press('x')
          pyautogui.PAUSE = 0.5
          pyautogui.press('x')
          time.sleep(random.randrange(100, 340))

          if random.randrange(1, 3) == 1:
               pyautogui.click(random.randrange(1, screenWidth), random.randrange(1, screenHeight))

          else:
               pyautogui.doubleClick(random.randrange(1, screenWidth), random.randrange(1, screenHeight))

          pyautogui.moveTo(random.randrange(1, screenWidth), random.randrange(1, screenHeight))
          RAND = random.randrange(101)

          if RAND <= 15:
               runAround()

          elif RAND <= 30:
               stand()

          elif RAND <= 45:
               laySit()

          elif RAND <= 60:
               layFly()

          elif RAND <= 85:
               layPushUp()

          elif RAND <= 100:
               sendMessage()

     def hop():
          pyautogui.doubleClick(random.randrange(1, screenWidth), random.randrange(1, screenHeight))
          for _ in range(random.randrange(2, 10)):
               pyautogui.press('down')
               pyautogui.press('up')

          stand()

     def stand():
          pyautogui.PAUSE = 1
          pyautogui.press('x')
          pyautogui.press('x')
          pyautogui.press('x')
          time.sleep(random.randrange(300, 540))
          RAND = random.randrange(101)

          if RAND % 2 == 0:
               pyautogui.press('x')
               pyautogui.press('x')
               pyautogui.PAUSE = 0.5
               pyautogui.press('x')
               pyautogui.press('c')
               pyautogui.PAUSE = 1
               pyautogui.press('c')

          else:
               pyautogui.press('c')
               pyautogui.press('c')
               pyautogui.PAUSE = 0.7
               pyautogui.press('c')
               pyautogui.PAUSE = 1
               pyautogui.press('x')

          if RAND <= 15:
               runAround()

          elif RAND <= 30:
               standLay()

          elif RAND <= 45:
               standSit()

          elif RAND <= 60:
               standFly()

          elif RAND <= 85:
               clickPlus()

          elif RAND <= 100:
               sendMessage()

     stand()