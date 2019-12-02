import gevent
import pyautogui
import random

def click(picture):
    picture = './img/' + picture
    while True:
        try:
            point = pyautogui.locateCenterOnScreen(picture, confidence=0.95)
            if point is None:
                gevent.sleep(0.2)
            else:
                pyautogui.click(point, duration=0.35)
        except TypeError:
            gevent.sleep(0.2)

def clicktiaozhan(picture):
    picture = './img/' + picture
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen(picture, confidence=0.95)

            ranx = random.randint(-50,50)
            rany = random.randint(-10,10)
            x += ranx
            y += rany
            pyautogui.click(x, y, duration=0.35)
            rantime = random.randint(1,5)/10
            gevent.sleep(rantime)
        except TypeError:
            rantime = random.randint(1,5)/10
            gevent.sleep(rantime)

def clickover(picture):
    picture = './img/' + picture
    while True:
        rantime = random.randint(0,1)/10
        gevent.sleep(rantime)
        loclist = pyautogui.locateAllOnScreen(picture, confidence=0.8)      
        for pos in loclist:
            x, y = pyautogui.center(pos)
            ranx = random.randint(-200,200)
            rany = random.randint(-10,10)
            x += ranx
            y += rany
            pyautogui.click(x, y, duration=0.25)
            rantime = random.randint(1,3)/10
            gevent.sleep(rantime)

def clickxuanshang(picture):
    picture = './img/' + picture
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen(picture, confidence=0.95)
            ranx = random.randint(5,15)
            rany = random.randint(1,5)
            x = x + 80 + ranx
            y = y - 25 - rany
            pyautogui.click(x, y, duration=0.35)
            rantime = random.randint(1,5)/10
            gevent.sleep(rantime)
        except TypeError:
            rantime = random.randint(1,5)/10
            gevent.sleep(rantime)

def cycle_fight():
    '''用于循环重复的战斗场景，如果刷觉醒材料，刷御魂'''
    gevent.joinall([        #利用joinall方法将每一步操作加入协程池中
        gevent.spawn(clicktiaozhan,'tiaozhan.png'),   #每一个协程的加入方法是：（函数名，参数）
        gevent.spawn(clickxuanshang,'xuanshang.png'),
        gevent.spawn(clickover,'over.png')
    ])

def story_task():
    ''''用于过废话连篇的剧情任务'''
    gevent.joinall([
        gevent.spawn(click, 'dialogue.PNG'),
        gevent.spawn(click, 'tiaoguo.PNG'),
        gevent.spawn(click, 'storyJump.PNG'),
        gevent.spawn(click, 'fight.PNG'),
        gevent.spawn(click, 'zhunbei.PNG'),
        gevent.spawn(click, 'over.PNG')
    ])
def explore_task():
    '''用于过探索副本'''
    gevent.joinall([
        gevent.spawn(click, 'fight.PNG'),
        gevent.spawn(click, 'masterFight.PNG'),
        gevent.spawn(click, 'zhunbei.PNG'),
        gevent.spawn(click, 'over.PNG')
    ])

cycle_fight()
# point = pyautogui.locateCenterOnScreen('tiaozhan.png', confidence=0.8)
# print(point)
# # if point is None:
# #     print(123)
# # else:
# #     pyautogui.click(point, duration=0.5)