from Utils import displayImg , getUserInfo , getMood , getGender , getDiseasRec , getDomHand , SAM , playSound , playMovie , trial_phase_1 , trial_phase_2  , test_phase , SaveDate , rest 
from psychopy import visual , core , event 

usrId , usrName , usrAge  = getUserInfo()

windows = visual.Window(
    size = [960, 960],
    fullscr = True,
    units = "pix",
    color = [1,1,1]
 )   

usrGender = getGender(windows)

usrLR = getDomHand(windows)

usrMood = getMood(windows)

usrDiseasRec = getDiseasRec(windows)

displayImg(windows,"instruction_0_0",0,True)
event.waitKeys()
displayImg(windows,"instruction_0_1",0,True)
event.waitKeys()

SAM_1_res_1 = SAM(windows , True)
displayImg(windows,"instruction_0_2",0,True)
event.waitKeys()
SAM_1_res_2 = SAM(windows , False) 
SAM_1_res = [SAM_1_res_1 , SAM_1_res_2]

playMovie(windows , str(usrMood))

displayImg(windows,"instruction_1_0",0,True)
event.waitKeys()
displayImg(windows,"instruction_1_1",0,True)
event.waitKeys()
SAM_2_res_1 = SAM(windows , True)
displayImg(windows,"instruction_1_2",0,True)
event.waitKeys()
SAM_2_res_2 = SAM(windows , False)


SAM_2_res = [SAM_2_res_1 , SAM_2_res_2]

SAM_res = [SAM_1_res , SAM_2_res]

displayImg(windows,"startGreeting",0,True)
event.waitKeys()

displayImg(windows,"instruction",0,True)
event.waitKeys()
'''
Trial Phases :
    1- 12 trial 
    2- 16 trial and test with feedback
    
Anchor Duration :
    short_t : 0.2 , 
    long_t : 0.8
    
alternation for counterbalance :
    
    if userId is even squence will be : short - long - short - long ...
    
    else : long - short - long - short ...
'''
short_t , long_t = 0.2 , 0.8


if usrId % 2 == 0 :
    sequence = [short_t , long_t]
    key_conterblnc_dir = True # d = short , k = long
else :
    sequence = [long_t , short_t]
    key_conterblnc_dir = False # k = short , d = long
    
trial_phase_1(usrId , windows , short_t , long_t , sequence , 0.5,key_conterblnc_dir)
trial_phase_2(windows , sequence , key_conterblnc_dir)    

'''
Test Phase

. Intermediate Duration (0.2 - 0.8) : 
    
    0.238, 0.283, 0.336, 0.476, 0.566, 0.673
    
. 8 block :
    
    each block 32 Trial
    
    after each block 1min delay
    
    
'''
Trial , RT , RK , Choice , Cond , Block , A_V = test_phase (windows , key_conterblnc_dir, usrId , usrName , usrAge , usrGender , usrLR , usrMood , usrDiseasRec , SAM_res)

SaveDate(usrId , usrName , usrAge , usrGender ,usrLR ,usrMood , usrDiseasRec , SAM_res , Trial , RT , RK , Choice , Cond  , Block , A_V)


windows.close()
