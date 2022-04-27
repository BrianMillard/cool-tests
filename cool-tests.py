from cmu_graphics import *
response = app.getTextInput("1, 2, or 3?")
if (response == '1'):
    #####just a little aiming/debug menu test
    ###theese make the objects
    app.background = 'black'
    app.stepsPerSecond = 100
    target = Circle(0, 0, 30, fill='white')
    targetcenter = Circle(0, 0, 5, fill='red')
    targetline1 = Circle(0, 0, 15, fill=None, border='red', borderWidth=5)
    targetline2 = Circle(0, 0, 25, fill=None, border='red', borderWidth=5)
    def crosshair(color):
        Line(180, 200, 220, 200, opacity=70, fill=color)
        Line(200, 180, 200, 220, opacity=70, fill=color)
    crosshair('red')
    missorhit = Label('null', 200, 50, size=50, fill='blue', visible=False)
    score = Label(0, 10, 10, size=25, fill='blue')
    mouse = Circle(0, 0, 1, visible=False)
    timer = 0
    winloss = "null"
    mx = 0
    my = 0
    ###this prints the debug menu
    def onStep():
        global timer
        timer+=1
        print('X =',mx,'Y =',my,'time =',timer,'hit or miss? =',missorhit.value)
        if (timer>=150):
            if (score.value < 0):
                missorhit.visible = True
                missorhit.value = 'You Lost'
                winloss = "loss"
                app.stop()
                print(winloss)
    ###theese movethe target/change the bg/does basicly everything
    def onMouseMove(mouseX, mouseY):
        global mx
        global my
        mx = mouseX
        my = mouseY
        mouse.centerX = mouseX
        mouse.centerY = mouseY
        target.centerX = 400-mouseX
        target.centerY = 400-mouseY
        targetcenter.centerX = 400-mouseX
        targetcenter.centerY = 400-mouseY
        targetline1.centerX = 400-mouseX
        targetline1.centerY = 400-mouseY
        targetline2.centerX = 400-mouseX
        targetline2.centerY = 400-mouseY
        if (mouseY < 200):
            if (mouseX < 200):
                app.background = rgb(mouseY, mouseX, 0)
            else:
                app.background = rgb(mouseY, 400-mouseX, 0)
        else:
            if (mouseX < 200):
                app.background = rgb(400-mouseY, mouseX, 0)
            else:
                app.background = rgb(400-mouseY, 400-mouseX, 0)
    def onMousePress(mouseX, mouseY):
        if (mouse.hitsShape(targetcenter) == True):
            target.fill = 'red'
            targetcenter.fill = 'white'
            targetline1.border = 'white'
            targetline2.border = 'white'
            missorhit.visible = True
            missorhit.value = 'Hit'
            score.value += 1
        else:
                missorhit.visible = True
                missorhit.value = 'Miss'
                score.value -= 1
        if (score.value >= 10):
            missorhit.visible = True
            missorhit.value = 'You Win!'
            winloss = "win"
            app.stop()
            print(winloss)
    def onMouseRelease(mouseX, mouseY):
        target.fill = 'white'
        targetcenter.fill = 'red'
        targetline1.border = 'red'
        targetline2.border = 'red'
        if (score.value < 10):
            missorhit.visible = False
            missorhit.value = "null"
        else:
            missorhit.visible = True
        if (score.value == 10):
            score.value -= 10
        if (score.value <= 10):
            missorhit.visible = False
            missorhit.value = "null"
if (response == '2'):
    ##### This is a dispay of random integers and functions and general chaos
    ### self explanitory
    app.stepsPerSecond = 100
    ### this makes the starting screen
    app.background = 'black'
    mouse = Circle(0 , 0, 20, fill='purple', visible=False)
    light = Circle(0, 0, 15, fill='white', visible=False)
    light2 = Circle(0, 0, 15, fill='white', visible=False)
    light3 = Circle(0, 0, 15, fill='white', visible=False)
    light4 = Circle(0, 0, 15, fill='white', visible=False)
    light5 = Circle(0, 0, 15, fill='white', visible=False)
    warning = Label('Seizure warning', 200, 200, fill='red', border='white', size=50, visible=True)
    ### justsome varibles dont worry about theese
    mx = 0
    my = 0
    keydown = "no"
    timer = 0
    mousecheck = "null"
    def onMouseMove(mouseX, mouseY):
        global mx
        global my
        mx=mouseX
        my=mouseY
    ### basicly gives you a seizure 
    def onStep():
        global keydown
        global timer
        global mx
        global my
        timer+=1
        print('X =',mx,'Y =',my, 'time =', timer,'mouse pressed? =', keydown)
        if (timer > 100):
            if (keydown == "no"):
                mouse.centerX = mx
                mouse.centerY = my
                light.centerX = int(random() * 400)
                light.centerY = int(random() * 400)
                light.opacity = int(random() * 100)
                light2.centerX = int(random() * 400)
                light2.centerY = int(random() * 400)
                light2.opacity = int(random() * 100)
                light3.centerX = int(random() * 400)
                light3.centerY = int(random() * 400)
                light3.opacity = int(random() * 100)
                light4.centerX = int(random() * 400)
                light4.centerY = int(random() * 400)
                light4.opacity = int(random() * 100)
                light5.centerX = int(random() * 400)
                light5.centerY = int(random() * 400)
                light5.opacity = int(random() * 100)
                light.visible = True
                light2.visible = True
                light3.visible = True
                light4.visible = True
                light5.visible = True
                mouse.visible = True
                mouse.fill = rgb(int(random() * 255), int(random() * 255), int(random() * 255))
                light.fill = rgb(int(random() * 255), int(random() * 255), int(random() * 255))
                light2.fill = rgb(int(random() * 255), int(random() * 255), int(random() * 255))
                light3.fill = rgb(int(random() * 255), int(random() * 255), int(random() * 255))
                light4.fill = rgb(int(random() * 255), int(random() * 255), int(random() * 255))
                light5.fill = rgb(int(random() * 255), int(random() * 255), int(random() * 255))
                warning.visible = False
    ### these two make the bg go crazy
    def onMouseDrag(mouseX, mouseY):
        global keydown
        global timer
        global mx
        global my
        mx=mouseX
        my=mouseY
        if (timer > 100):
            mouse.centerX = mouseX
            mouse.centerY = mouseY
            mouse.fill = rgb(int(random() * 255), int(random() * 255), int(random() * 255))
            app.background = rgb(int(random() * 255), int(random() * 255), int(random() * 255))
            light.visible = False
            light2.visible = False
            light3.visible = False
            light4.visible = False
            light5.visible = False
            warning.visible = False
            mouse.visible = True
    def onMousePress(mouseX, mouseY):    
        global keydown
        global timer
        global mx
        global my
        keydown = "yes"
        if (keydown == "yes"):
            print("mouse pressed")
        if (timer > 100):
            light.visible = False
            light2.visible = False
            light3.visible = False
            light4.visible = False
            light5.visible = False
            app.background = rgb(int(random() * 255), int(random() * 255), int(random() * 255))
            warning.visible = False
            mouse.visible = True
            mouse.fill = rgb(int(random() * 255), int(random() * 255), int(random() * 255))
    ### this just resets it back to the starting screen
    def onKeyPress(key):
        global keydown
        global timer
        global mx
        global my
        app.background = 'black'
        light.visible = False
        light2.visible = False
        light3.visible = False
        light4.visible = False
        light5.visible = False
        warning.visible = True
        mouse.visible = False
    ### just debug stuff dont mind this
    def onMouseRelease(mouseX, mouseY):
        global keydown
        global timer
        global mx
        global my
        keydown = "no"
        if (keydown == "no"):
            print("mouse released")
if (response == '3'):
  Label("
We're waiting every night
To finally roam and invite
Newcomers to play with us
For many years we've been all alone

We're forced to be still and play
The same songs we've known since that day
An imposter took our life away
Now we're stuck here to decay

Please let us get in!
Don't lock us away!
We're not like what you're thinking

We're poor little souls
Who have lost all control
And we're forced here to take that role

We've been all alone
Stuck in our little zone
Since 1987

Join us, be our friend
Or just be stuck and defend
After all you only got

Five nights at Freddy's
Is this where you wanna be?
I just don't get it
Why do you want to stay?

Five nights at Freddy's
Is this where you wanna be?
I just don't get it
Why do you want to stay?

Five nights at Freddy's

We're really quite surprised
We get to see you another night
You should have looked for another job
You should have said to this place good-bye

It's like there's so much more
Maybe you've been in this place before
We remember a face like yours
You seem acquainted with those doors

Please let us get in!
Don't lock us away!
We're not like what you're thinking

We're poor little souls
Who have lost all control
And we're forced here to take that role

We've been all alone
Stuck in our little zone
Since 1987

Join us, be our friend
Or just be stuck and defend
After all you only got

Five nights at Freddy's
Is this where you wanna be?
I just don't get it
Why do you want to stay?

Five nights at Freddy's
Is this where you wanna be?
I just don't get it
Why do you want to stay?

Five nights at Freddy's",200,200)
cmu_graphics.run()
