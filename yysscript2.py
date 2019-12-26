import pyautogui,time,random
import threading
import gc
pyautogui.FAILSAFE = True
'''PyAutoGUI提供了一个保护措施。当pyautogui.FAILSAFE = True时，如果把鼠标光标在屏幕左上角，
PyAutoGUI函数就会产生pyautogui.FailSafeException异常,用于在程序失控时退出'''
time.sleep(2)

isMark = False

class FindButton(threading.Thread):
    def __init__(self, picture, confidence, dlist):
        super(FindButton, self).__init__()
        self.picture = './img/' + picture
        self.confidence = confidence
        self.dlist = dlist

    def run(self):
        global isMark
        while True:
            try:
                if(self.picture == './img/auto.PNG' and isMark == False):
                    self.x, self.y = pyautogui.locateCenterOnScreen(self.picture, confidence=self.confidence)
                    ranx = random.randint(self.dlist[0],self.dlist[1])
                    rany = random.randint(self.dlist[2],self.dlist[3])
                    self.x += ranx
                    self.y += rany
                    isMark = True
                    # rantime = random.randint(3,5)/10
                    # time.sleep(rantime)
                    pyautogui.click(self.x + 247, self.y - 210, duration=0.25)
                elif(self.picture != './img/auto.PNG'):
                    self.x, self.y = pyautogui.locateCenterOnScreen(self.picture, confidence=self.confidence)
                    ranx = random.randint(self.dlist[0],self.dlist[1])
                    rany = random.randint(self.dlist[2],self.dlist[3])
                    self.x += ranx
                    self.y += rany
                    pyautogui.click(self.x, self.y, duration=0.25)

                    #双开
                    if(self.picture == './img/over.PNG' and self.x > 960):
                        isMark = False
                        pyautogui.click(self.x-960,self.y+1,duration=0.1)
                        pyautogui.click(self.x+1,self.y+1,duration=0.1)
                        pyautogui.click(self.x-960,self.y-1,duration=0.1)
                    if(self.picture == './img/over.PNG' and self.x < 960):
                        isMark = False
                        pyautogui.click(self.x+960,self.y+1,duration=0.1)
                        pyautogui.click(self.x+1,self.y+1,duration=0.1)
                        pyautogui.click(self.x+960,self.y-1,duration=0.1)
                    
                    # 102 723  369 542
                    #单人
                    # if(self.picture == './img_s/over.PNG'):
                    #     pyautogui.click(self.x-1,self.y+1,duration=0.1)
                    #     pyautogui.click(self.x+1,self.y+1,duration=0.1)
                    #     pyautogui.click(self.x-1,self.y-1,duration=0.1)


                rantime = random.randint(1,10)/100
                time.sleep(rantime)
                del rantime
                gc.collect()
            except TypeError:
                rantime = random.randint(1,10)/100
                time.sleep(rantime)
                del rantime
                gc.collect()

#默认分辨率
challenge = FindButton('tiaozhan.PNG',0.95,[-50,50,-10,10])
xuanshang = FindButton('xuanshang.PNG',0.95,[100,120,-25,-15])
over = FindButton('over.PNG',0.8,[-200,200,-6,6])
auto = FindButton('auto.PNG',0.8,[-10,10,-6,6])

#小分辨率
# challenge = FindButton('tiaozhan.PNG',0.95,[-10,10,-5,5])
# xuanshang = FindButton('xuanshang.PNG',0.95,[45,55,-10,2])
# over = FindButton('over.PNG',0.8,[80,120,-5,3])


challenge.start()
xuanshang.start()
over.start()
auto.start()