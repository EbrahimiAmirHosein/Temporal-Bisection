from psychopy import visual , core , event , gui , sound 
import pandas as pd
import random

def getUserInfo():
    DialogGui = gui.Dlg()
    DialogGui.addField(" ID: ")
    DialogGui.addField(" SurName: ")
    DialogGui.addField(" Age: ")
    DialogGui.show()

    return int(DialogGui.data[0]) , DialogGui.data[1] , int(DialogGui.data[2])
    

        
def playSound(soundName , duration , win):
    c4 = sound.Sound( "stimuli\AuditoryStimuli\\" + soundName + ".wav")
    c4.play()
    c4.setSound(value = 500 , secs=duration)
    core.wait(duration)
    
def playMovie(windows , movieName):
    if movieName == "Anger" :
        movieName = 'AmericanHistory'
    if movieName == "Fear" :
        movieName = 'Roadkill'
    if movieName == "Disgust" :
        movieName = 'Hellraiser'
    if movieName == "Sadness" :
        movieName = 'TheChamp'
    if movieName == "Neutral" :
        movieName = 'TheChamp'
    if movieName == "Happiness" :
        movieName = 'Mr.Been.Exam'
    if movieName == "Tenderness" :
        movieName = 'The.dead.poets.society'
        
    mov = visual.MovieStim3(win = windows, filename = "stimuli\Videos\\" + movieName + ".mkv", flipVert=False , colorSpace='rgb' , size=(1700, 960))
    while mov.status != visual.FINISHED:
        mov.draw()
        windows.flip()
        intrupt = event.getKeys(['q'])
        if 'q' in intrupt:
            break 
    
def displayImg(win ,imgName , duration , instr):
    img = visual.ImageStim(
    win = win,
    image = "stimuli\VisualStimuli\\" + imgName + ".png"
    )
    if instr :
        img.draw()
        win.flip() 
    else :
        imgClk = core.Clock()
        while (imgClk.getTime() < duration):
            img.draw()
            win.flip() 
        win.flip()
    
def getMood(windows):
    displayImg(windows,"moodSel",0,True)
    numK = event.waitKeys(keyList=['1','2','3','4','5','6','7'] , clearEvents = True)
    if '1' in numK :
        Usrmood = 'Fear'
    elif '2' in numK :
        Usrmood = 'Disgust'
    elif '3' in numK :
        Usrmood = 'Anger'
    elif '4' in numK :
        Usrmood = 'Sadness'
    elif '5' in numK : 
        Usrmood = 'Neutral'
    elif '6' in numK :
        Usrmood = 'Happiness'
    else :
        Usrmood = 'Tenderness'
    
    return Usrmood
    
def getGender(windows):
    displayImg(windows,"M_F",0,True)
    GenK = event.waitKeys(keyList=['m' , 'M' , 'f' , 'F'] , clearEvents = True)
    
    if 'm' in GenK or 'M' in GenK :
        Gender = 'Male'
    else:
        Gender = 'Female'
    return Gender
    
def getDomHand(windows):
    displayImg(windows,"L_R",0,True)
    DomK = event.waitKeys(keyList=['l' , 'L' , 'r' , 'R'] , clearEvents = True)
    
    if 'l' in DomK or 'L' in DomK :
        DominH = 'Left handed'
    else:
        DominH = 'Right handed'
    return DominH
def getDiseasRec(windows):
    displayImg(windows,"DiseaseRec",0,True)
    resK = event.waitKeys(keyList=['y' , 'Y' , 'n' , 'N'] , clearEvents = True)
    
    if 'y' in resK or 'Y' in resK :
        Rec = 'Yes'
    else:
        Rec = 'No'
    return Rec
    
def SAM(windows , first):
    
    if first :
        name = 'SAM'
    else :
        name = 'SAM2'
    mouse = event.Mouse(visible=True, newPos=None, win=windows)
    background_image = visual.ImageStim(windows,image= 'stimuli\VisualStimuli\\' + name + '.png')
    Y_up = -22
    Y_down = -69
    again = False
    while ( not again ) :
        background_image.draw()
        pos = mouse.getPos()                 
        flip_time=windows.flip()
        
        clickedX , clickedY = pos[0] , pos[1]
        if (mouse.getPressed() == [1,0,0]):
            if clickedX > -437.5 and clickedX < -385.5 and clickedY < Y_up and clickedY > Y_down:
                moodNum = 1
                again = True
            elif clickedX > -341.5 and clickedX < -289.5 and clickedY < Y_up and clickedY > Y_down:
                moodNum = 2
                again = True
            elif clickedX > -245.5 and clickedX < -191.5 and clickedY < Y_up and clickedY > Y_down:
                moodNum = 3
                again = True
            elif clickedX > -142.5 and clickedX < -91.5 and clickedY < Y_up and clickedY > Y_down:
                moodNum = 4
                again = True
            elif clickedX > -41.5 and clickedX < 6.5 and clickedY < Y_up and clickedY > Y_down:
                moodNum = 5
                again = True
            elif clickedX > 54.5 and clickedX < 106.5 and clickedY < Y_up and clickedY > Y_down:
                moodNum = 6
                again = True
            elif clickedX > 153.5 and clickedX < 206.5 and clickedY < Y_up and clickedY > Y_down:
                moodNum = 7
                again = True
            elif clickedX > 251.5 and clickedX < 301.5 and clickedY < Y_up and clickedY > Y_down:
                moodNum = 8
                again = True
            elif clickedX > 352.5 and clickedX < 403.5 and clickedY < Y_up and clickedY > Y_down:
                moodNum = 9
                again = True
            else:
                again = False
    return moodNum
def trial_phase_1(usrId , windows , short_t , long_t , sequence , instr_del ,key_conterblnc_dir):
    for i_iterate in range (12):
        if  i_iterate < 5 :
            if  i_iterate %  2 == 0 :
                if key_conterblnc_dir :
                    #play (short/long) music
                    displayImg(windows , "listen" , instr_del ,  False)
                    playSound("piano" , sequence[0] , windows)
                    displayImg(windows , "short" , 2 ,  False)
                else :
                    #show (long/short) Image
                    displayImg(windows , "see" , instr_del ,  False)
                    displayImg(windows , "blackCircle" , sequence[0] ,  False)
                    displayImg(windows , "long" , 2 ,  False)
            else :
                if key_conterblnc_dir :
                    #show (long/short) Image
                    displayImg(windows , "see" , instr_del ,  False)
                    displayImg(windows , "blackCircle" , sequence[1] ,  False)
                    displayImg(windows , "long" , 2 ,  False)
                else :
                    #play (short/long) music
                    displayImg(windows , "listen" , instr_del ,  False)
                    playSound("piano" , sequence[1] , windows)       
                    displayImg(windows , "short" , 2 ,  False)
        else :
            if  i_iterate %  2 == 0 :
                if key_conterblnc_dir :
                    #play (short/long) music
                    displayImg(windows , "listen" , instr_del ,  False)
                    playSound("piano" , sequence[1] , windows)
                    displayImg(windows , "long" , 2 ,  False)
                else :
                    #show (long/short) Image
                    displayImg(windows , "see" , instr_del ,  False)
                    displayImg(windows , "blackCircle" , sequence[1] ,  False) 
                    displayImg(windows , "short" , 2 ,  False)
            else :
                if key_conterblnc_dir :
                    #show (long/short) Image
                    displayImg(windows , "see" , instr_del ,  False)
                    displayImg(windows , "blackCircle" , sequence[0] ,  False)  
                    displayImg(windows , "short" , 2 ,  False)
                else :
                    #play (short/long) music
                    displayImg(windows , "listen" , instr_del ,  False)
                    playSound("piano" , sequence[0] , windows)  
                    displayImg(windows , "long" , 2 ,  False)
              
def trial_phase_2(windows , sequence , key_conterblnc_dir  ):
    
    if key_conterblnc_dir :
        displayImg(windows,"instruction_2_2",0,True)
        event.waitKeys()
    else:
        displayImg(windows,"instruction_2_1",0,True)
        event.waitKeys()   
        
                
    true_cnt = 0
    correct_cnt = str(true_cnt)
    while ( true_cnt < 12):
        true_cnt  = 0
        idx_list  = random.sample(range(0, 16), 16)
        for i_iterate in idx_list:
            instr_del = random.uniform(1,3)
            if i_iterate % 2 == 0 :
                if i_iterate % 4 == 0 :
                    displayImg(windows , "see" , instr_del ,  False)
                    displayImg(windows , "blackCircle" , sequence[0] ,  False)
                    keys = event.waitKeys(keyList=['k', 'd', 'K' , 'D', 'q' , 'Q'] , maxWait = 3 , clearEvents = True)
                    if keys == None :
                       displayImg(windows , "payatt" , instr_del ,  False)
                       keys = event.waitKeys(keyList=['k', 'd', 'K' , 'D' , 'q'] , clearEvents = True)
                    
                    if key_conterblnc_dir : 
                        if keys[0][0] == 'd' or keys[0][0] == 'D' :
                            true_cnt = true_cnt + 1
                            displayImg(windows , "Correct" , instr_del ,  False)
                        elif keys[0][0] == 'k' or keys[0][0] == 'K' :
                            displayImg(windows , "Incorrect" , instr_del ,  False)
                        elif keys[0][0] ==  'q' or keys[0][0] ==  'Q':
                            core.quit()
                    else :
                        if keys[0][0] == 'd' or keys[0][0] == 'D' :
                            true_cnt = true_cnt + 1
                            displayImg(windows , "Correct" , instr_del ,  False)
                        elif keys[0][0] == 'k' or keys[0][0] == 'K' :
                            displayImg(windows , "Incorrect" , instr_del ,  False)
                        elif keys[0][0] ==  'q' or keys[0][0] ==  'Q':
                            core.quit()                            
                else:
                    displayImg(windows , "see" , instr_del ,  False)                 
                    displayImg(windows , "blackCircle" , sequence[1] ,  False)
                    
                    keys = event.waitKeys(keyList=['k', 'd', 'K' , 'D', 'q' , 'Q']  , maxWait = 3, clearEvents = True)
                    if keys == None :
                       displayImg(windows , "payatt" , instr_del ,  False) 
                       keys = event.waitKeys(keyList=['k', 'd', 'K' , 'D', 'q' , 'Q'] , clearEvents = True)
                       
                    if key_conterblnc_dir : 
                        if keys[0][0] == 'k' or keys[0][0] == 'K' :
                            true_cnt = true_cnt + 1
                            displayImg(windows , "Correct" , instr_del ,  False)
                        elif keys[0][0] == 'd' or keys[0][0] == 'D' :
                            displayImg(windows , "Incorrect" , instr_del ,  False)
                        elif keys[0][0] ==  'q' or keys[0][0] ==  'Q':
                            core.quit()                            
                    else :
                        if keys[0][0] == 'k' or keys[0][0] == 'K' :
                            true_cnt = true_cnt + 1    
                            displayImg(windows , "Correct" , instr_del ,  False)
                        elif keys[0][0] == 'd' or keys[0][0] == 'D' :
                            displayImg(windows , "Incorrect" , instr_del ,  False)
                        elif keys[0][0] ==  'q' or keys[0][0] ==  'Q':
                            core.quit()                    
            else :
                if i_iterate % 4 == 1 :
                    displayImg(windows , "listen" , instr_del ,  False)
                    playSound("piano" , sequence[0] , windows) 

                    keys = event.waitKeys(keyList=['k', 'd', 'K' , 'D', 'q' , 'Q'] , maxWait = 3, clearEvents = True )
                    
                    if keys == None :
                       displayImg(windows , "payatt" , instr_del ,  False) 
                       keys = event.waitKeys(keyList=['k', 'd', 'K' , 'D', 'q' , 'Q'], clearEvents = True)
                    if key_conterblnc_dir : 
                        if keys[0][0] == 'd' or keys[0][0] == 'D' :
                            true_cnt = true_cnt + 1
                            displayImg(windows , "Correct" , instr_del ,  False)
                        elif keys[0][0] == 'k' or keys[0][0] == 'K' :
                            displayImg(windows , "Incorrect" , instr_del ,  False) 
                        elif keys[0][0] ==  'q' or keys[0][0] ==  'Q':
                            core.quit()                            
                    else :
                        if keys[0][0] == 'd' or keys[0][0] == 'D' :
                            true_cnt = true_cnt + 1
                            displayImg(windows , "Correct" , instr_del ,  False)
                        elif keys[0][0] == 'k' or keys[0][0] == 'K' :
                            displayImg(windows , "Incorrect" , instr_del ,  False)  
                        elif keys[0][0] ==  'q' or keys[0][0] ==  'Q':
                            core.quit()
                else:
                    displayImg(windows , "listen" , instr_del ,  False)
                    playSound("piano" , sequence[1] , windows) 

                    keys = event.waitKeys(keyList=['k', 'd', 'K' , 'D', 'q' , 'Q'] ,maxWait = 3, clearEvents = True)
                    if keys == None :
                       displayImg(windows , "payatt" , instr_del ,  False) 
                       keys = event.waitKeys(keyList=['k', 'd', 'K' , 'D', 'q' , 'Q'], clearEvents = True )
                    if key_conterblnc_dir : 
                        if keys[0][0] == 'k' or keys[0][0] == 'K' :
                            true_cnt = true_cnt + 1
                            displayImg(windows , "Correct" , instr_del ,  False)
                        elif keys[0][0] == 'd' or keys[0][0] == 'D' :
                            displayImg(windows , "Incorrect" , instr_del ,  False)     
                        elif keys[0][0] ==  'q' or keys[0][0] ==  'Q':
                            core.quit()                            
                    else :
                        if keys[0][0] == 'K' or keys[0][0] == 'k' :
                            true_cnt = true_cnt + 1
                            displayImg(windows , "Correct" , instr_del ,  False)
                        elif keys[0][0] == 'D' or keys[0][0] == 'd' :
                            displayImg(windows , "Incorrect" , instr_del ,  False)
                        elif keys[0][0] ==  'q' or keys[0][0] ==  'Q':
                            core.quit()                            


def test_phase (windows  , key_conterblnc_dir , usrId , usrName , usrAge , usrGender , usrLR , usrMood , usrDiseasRec , SAM_res):
    displayImg(windows,"instruction_3",0,True)
    event.waitKeys()

    
    Trial = []
    RT = []
    Choice = []
    Cond = []
    Block = []
    A_V = []
    RK = []
    clk = core.Clock()
    last_rest = True
    l =[0.2 , 0.238, 0.283, 0.336, 0.476, 0.566, 0.673 , 0.8 ,0.2 , 0.238, 0.283, 0.336, 0.476, 0.566, 0.673 , 0.8,0.2 , 0.238, 0.283, 0.336, 0.476, 0.566, 0.673 , 0.8,0.2 , 0.238, 0.283, 0.336, 0.476, 0.566, 0.673 , 0.8]
    for block_ind in range (8):
        idx_list  = random.sample(range(0, 32), 32)
        if block_ind == 7 : last_rest = False
        Trial_cnt = 1
        for i_iterate in idx_list:
            Block.append(block_ind+1)
            Trial.append(Trial_cnt)
            Trial_cnt = Trial_cnt + 1
            
            instr_del = random.uniform(1,3)
            if i_iterate % 2 == 0 :
                #see
                A_V.append("V")
                displayImg(windows , "see" , instr_del ,  False)
                dur = l[i_iterate]
                Cond.append(dur)
                displayImg(windows , "blackCircle" , dur ,  False)
                clk.reset()
                keys = event.waitKeys(keyList=['k', 'd', 'K' , 'D', 'q' , 'Q'] , maxWait = 3 , clearEvents = True , timeStamped = clk)

                
                if keys == None:
                    displayImg(windows , "payatt" , instr_del ,  False)
                    RT.append(0)
                    RK.append("None")
                    Choice.append("None(too late)")                
                    continue
                if (key_conterblnc_dir) :
                    if ((keys[0][0]) == 'd' or (keys[0][0]) == 'D'):
                        Choice.append("S") 
                    elif ((keys[0][0]) == 'k' or (keys[0][0]) == 'K') : 
                        Choice.append("L")
                    elif keys[0][0] ==  'q' or keys[0][0] ==  'Q':
                        SaveDate(usrId , usrName , usrAge , usrGender , usrLR , usrMood , usrDiseasRec , SAM_res , Trial , RT , RK , Choice , Cond  , Block , A_V)
                        core.quit()
                        
                    
                else :
                    if ((keys[0][0]) == 'd' or (keys[0][0]) == 'D'):
                        Choice.append("L") 
                    elif ((keys[0][0]) == 'k' or (keys[0][0]) == 'K') :  
                        Choice.append("S")
                    elif keys[0][0] ==  'q' or keys[0][0] ==  'Q':
                        SaveDate(usrId , usrName , usrAge , usrGender , usrLR , usrMood , usrDiseasRec , SAM_res , Trial , RT , RK , Choice , Cond  , Block , A_V)
                        core.quit()                  
                RK.append((keys[0][0]))
                RT.append((keys[0][1])+dur)
                
                  
            else :
                #listen
                A_V.append("A")
                displayImg(windows , "listen" , instr_del ,  False)
                dur = l[i_iterate]
                Cond.append(dur)
                playSound("piano" ,  dur , windows)
                clk.reset()
                keys = event.waitKeys(keyList=['k', 'd', 'K' , 'D', 'q' , 'Q'] ,maxWait = 3 , clearEvents = True , timeStamped = clk)

                if keys == None:
                    displayImg(windows , "payatt" , instr_del ,  False)
                    RT.append(0)
                    RK.append("None")
                    Choice.append("None(too late)")
                    continue
                if (key_conterblnc_dir) :
                    if ((keys[0][0]) == 'd' or (keys[0][0]) == 'D'):
                        Choice.append("S") 
                    elif ((keys[0][0]) == 'k' or (keys[0][0]) == 'K') :  
                        Choice.append("L")
                    elif keys[0][0] == 'q'or keys[0][0] ==  'Q':
                        SaveDate(usrId , usrName , usrAge , usrGender , usrLR , usrMood , usrDiseasRec , SAM_res , Trial , RT , RK , Choice , Cond  , Block , A_V)
                        core.quit()                      
                        
                else :
                    if ((keys[0][0]) == 'd' or (keys[0][0]) == 'D'):
                        Choice.append("L") 
                    elif ((keys[0][0]) == 'k' or (keys[0][0]) == 'K') :  
                        Choice.append("S")
                    elif keys[0][0] ==  'q' or keys[0][0] ==  'Q':
                        SaveDate(usrId , usrName , usrAge , usrGender , usrLR , usrMood , usrDiseasRec , SAM_res , Trial , RT , RK , Choice , Cond  , Block , A_V)
                        core.quit()                      

                RK.append(keys[0][0])
                RT.append((keys[0][1])+dur)
                
        displayImg(windows , "block_done_" + str(block_ind+1) , 2 ,  False)
        if last_rest :
            if (block_ind < 1 ):
                rest(windows , 10 , "rest_1")    
                event.waitKeys()
            else :
                rest(windows , 10 , "rest_2")    
                event.waitKeys()
 
                    
    return Trial , RT , RK , Choice , Cond , Block , A_V 
    
    
def rest(windows , timer , img):

    background_image = visual.ImageStim(windows,image= 'stimuli\VisualStimuli\\' + img + '.png')
    while timer > 0 :
        background_image.draw()
        Timer=visual.TextBox(window=windows, 
                             text=str(timer),
                             font_size=100,
                             font_color=[0,0,0], 
                             size=(1.3,1.3),
                             border_color=[1,1,1,1],
                             grid_horz_justification='center',
                             grid_vert_justification='bottom',
                             units='norm',
                             )
                             
        background_image.autoDraw = False
        Timer.draw()
        flip_time=windows.flip()
        timer = timer-1
        core.wait(1)
        windows.flip()
        interupt = event.getKeys(['space'])
        if 'space' in interupt:
            break
    

def Index_check(arr , maxim):
    for i in range(maxim-len(arr)) :
        arr.append('-')
    
    

def SaveDate(usrId , usrName , usrAge , usrGender , usrLR , usrMood , usrDiseasRec , SAM_res , Trial , RT , RK , Choice , Cond , Block , A_V):
    Id = []
    Name = []
    Age = []
    Gender = []
    DomHand = []
    Mood = []
    Record = []
    beforSAM_1 = []
    beforSAM_2 = []
    afterSAM_1 = []
    afterSAM_2 = []
    maxim = max(len(RT),len(RK),len(Choice),len(Cond),len(Block),len(A_V),len(Trial))
    for i in range (maxim):
        Id.append('-')
        Name.append('-') 
        Age.append('-') 
        Gender.append('-') 
        DomHand.append('-')
        Mood.append('-')
        Record.append('-')
        beforSAM_1.append('-')
        beforSAM_2.append('-')
        afterSAM_1.append('-')
        afterSAM_2.append('-')
        
    Id[0] = usrId
    Name[0] = usrName
    Age[0] = usrAge
    Gender[0] = usrGender
    DomHand[0] = usrLR
    Mood[0] = usrMood
    Record[0] = usrDiseasRec
    beforSAM_1[0] = SAM_res[0][0]
    beforSAM_2[0] = SAM_res[0][1]
    afterSAM_1[0] = SAM_res[1][0]
    afterSAM_2[0] = SAM_res[1][1]
    
    if ((len(RT)+len(RK)+len(Choice)+len(Cond)+len(Block)+len(A_V)+len(Trial) / 7 )!= maxim):
        l = [Trial , RT , RK , Choice , Cond , Block , A_V]
        for ind_l in l:
            Index_check(ind_l,maxim)
    data_dict = {
    "Id" : Id ,
    "Name" : Name ,
    "Age" : Age ,
    "Gender" : Gender ,
    "Dominant Hand" : DomHand,
    "Mood" : Mood ,
    "Disease Record": Record ,
    "SAM_1 result 1" : beforSAM_1 ,
    "SAM_1 result 2" : beforSAM_2,
    "SAM_2 result 1" : afterSAM_1 ,
    "SAM_2 result 2" : afterSAM_2 ,
    "Block" : Block ,
    "A_V" : A_V ,
    "Cond" : Cond , 
    "Trial" : Trial ,
    "Choice" : Choice , 
    "RT" : RT , 
    "RK" : RK
    }
    UserInfoDF = pd.DataFrame(data_dict,columns= ['Id', 'Name' ,'Age' , 'Gender' , 'Dominant Hand' ,'Mood' , 'Disease Record' , 'SAM_1 result 1 P.U' , 'SAM_1 result 2 AR' , 'SAM_2 result 1 P.U' , 'SAM_2 result 2 AR' , 'Block','A_V' , 'Cond' , 'Trial' , 'Choice' , 'RT' , 'RK'])
    UserInfoDF.to_csv( str(usrId) + '_' + usrName + '.csv' ,index=False,header=True , line_terminator='\r\n')
