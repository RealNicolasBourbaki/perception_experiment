

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.2),
    on September 11, 2017, at 19:48
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
"""
import psychopy
psychopy.useVersion('latest')

from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle#!/usr/bin/env python2
"""
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.2),
    on September 05, 2017, at 13:12
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

import psychopy
#psychopy.useVersion('latest')

from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))#.decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'perception-task'  # from the Builder filename that created this script
expInfo = {u'participant': u'000'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    # originPath=u'C:\\Dropbox\\RyanCallihan_Fabian\\Recording_Morphology_Experiment\\perception-task\\perception-task.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1600, 900), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
instuctions = visual.TextStim(win=win, name='instuctions',
    text='You are about to hear a word.\n\nIt will be either present or past tense.\n\nPress "D" if you heard past tense\nPress "K" if you heard present tense\nD: past\nK: present\n\nPlease press spacebar to start a short training round.',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "test"
testClock = core.Clock()
test_sound = sound.Sound('A', secs=-1)
test_sound.setVolume(1)
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
response = visual.TextStim(win=win, name='response',
    text='Which tense did you hear?\n\nD: past\n\nK: present\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "begin_instructions"
begin_instructionsClock = core.Clock()
begin_instructions_text = visual.TextStim(win=win, name='begin_instructions_text',
    text='You are now ready to begin. Please hit spacebar when ready.',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "block"
blockClock = core.Clock()
fixation_block = visual.TextStim(win=win, name='fixation_block',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
block_sound = sound.Sound('A', secs=-1)
block_sound.setVolume(1)
block_response = visual.TextStim(win=win, name='block_response',
    text='Which tense did you hear?\n\nD: past\n\nK: present\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thankyou = visual.TextStim(win=win, name='thankyou',
    text='Thank you very much.',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
end_instructions = event.BuilderKeyResponse()
# keep track of which components have finished
trialComponents = [ISI, instuctions, end_instructions]
for thisComponent in trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instuctions* updates
    if t >= 0.0 and instuctions.status == NOT_STARTED:
        # keep track of start time/frame for later
        instuctions.tStart = t
        instuctions.frameNStart = frameN  # exact frame index
        instuctions.setAutoDraw(True)
    
    # *end_instructions* updates
    if t >= 0.0 and end_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_instructions.tStart = t
        end_instructions.frameNStart = frameN  # exact frame index
        end_instructions.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(end_instructions.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if end_instructions.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            end_instructions.keys = theseKeys[-1]  # just the last key pressed
            end_instructions.rt = end_instructions.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    # *ISI* period
    if t >= 0.0 and ISI.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI.tStart = t
        ISI.frameNStart = frameN  # exact frame index
        ISI.start(0.5)
    elif ISI.status == STARTED:  # one frame should pass before updating params and completing
        ISI.complete()  # finish the static period
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_instructions.keys in ['', [], None]:  # No response was made
    end_instructions.keys=None
thisExp.addData('end_instructions.keys',end_instructions.keys)
if end_instructions.keys != None:  # we had a response
    thisExp.addData('end_instructions.rt', end_instructions.rt)
thisExp.nextEntry()
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
test_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('test_list.csv'),
    seed=None, name='test_loop')
thisExp.addLoop(test_loop)  # add the loop to the experiment
thisTest_loop = test_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest_loop.rgb)
if thisTest_loop != None:
    for paramName in thisTest_loop.keys():
        exec(paramName + '= thisTest_loop.' + paramName)

for thisTest_loop in test_loop:
    currentLoop = test_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTest_loop.rgb)
    if thisTest_loop != None:
        for paramName in thisTest_loop.keys():
            exec(paramName + '= thisTest_loop.' + paramName)
    
    # ------Prepare to start Routine "test"-------
    t = 0
    testClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    test_sound.setSound(file, secs=-1)
    test_key_resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    testComponents = [test_sound, fixation, test_key_resp, response]
    for thisComponent in testComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "test"-------
    while continueRoutine:
        # get current time
        t = testClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop test_sound
        if t >= 1.2 and test_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            test_sound.tStart = t
            test_sound.frameNStart = frameN  # exact frame index
            test_sound.play()  # start the sound (it finishes automatically)
        
        # *fixation* updates
        if t >= 0.0 and fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation.tStart = t
            fixation.frameNStart = frameN  # exact frame index
            fixation.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation.status == STARTED and t >= frameRemains:
            fixation.setAutoDraw(False)
        
        # *test_key_resp* updates
        if t >= 1.4 and test_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            test_key_resp.tStart = t
            test_key_resp.frameNStart = frameN  # exact frame index
            test_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(test_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if test_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['d', 'k'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                test_key_resp.keys = theseKeys[-1]  # just the last key pressed
                test_key_resp.rt = test_key_resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *response* updates
        if t >= 1.4 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t
            response.frameNStart = frameN  # exact frame index
            response.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test"-------
    for thisComponent in testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    test_sound.stop()  # ensure sound has stopped at end of routine
    # check responses
    if test_key_resp.keys in ['', [], None]:  # No response was made
        test_key_resp.keys=None
    test_loop.addData('test_key_resp.keys',test_key_resp.keys)
    if test_key_resp.keys != None:  # we had a response
        test_loop.addData('test_key_resp.rt', test_key_resp.rt)
    # the Routine "test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'test_loop'


# ------Prepare to start Routine "begin_instructions"-------
t = 0
begin_instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
begin_instructionsComponents = [begin_instructions_text, key_resp_2]
for thisComponent in begin_instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "begin_instructions"-------
while continueRoutine:
    # get current time
    t = begin_instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *begin_instructions_text* updates
    if t >= 0.0 and begin_instructions_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        begin_instructions_text.tStart = t
        begin_instructions_text.frameNStart = frameN  # exact frame index
        begin_instructions_text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in begin_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "begin_instructions"-------
for thisComponent in begin_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "begin_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# selects appropriate list based on participant number
condition_list = ''

if int(expInfo['participant']) % 4 == 1:
    condition_list = 'perception_stimuli_list_a.csv'
elif int(expInfo['participant']) % 4 == 2:
    condition_list = 'perception_stimuli_list_b.csv'
elif int(expInfo['participant']) % 4 == 3:
    condition_list = 'perception_stimuli_list_c.csv'
else:
    condition_list = 'perception_stimuli_list_d.csv'
    

# set up handler to look after randomisation of conditions etc
block_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(condition_list),
    seed=None, name='block_loop')
thisExp.addLoop(block_loop)  # add the loop to the experiment
thisBlock_loop = block_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_loop.rgb)
if thisBlock_loop != None:
    for paramName in thisBlock_loop.keys():
        exec(paramName + '= thisBlock_loop.' + paramName)

for thisBlock_loop in block_loop:
    currentLoop = block_loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_loop.rgb)
    if thisBlock_loop != None:
        for paramName in thisBlock_loop.keys():
            exec(paramName + '= thisBlock_loop.' + paramName)
    
    # ------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    block_sound.setSound(file, secs=-1)
    block_key_resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    blockComponents = [fixation_block, block_sound, block_response, block_key_resp]
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "block"-------
    while continueRoutine:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_block* updates
        if t >= 0.0 and fixation_block.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_block.tStart = t
            fixation_block.frameNStart = frameN  # exact frame index
            fixation_block.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_block.status == STARTED and t >= frameRemains:
            fixation_block.setAutoDraw(False)
        # start/stop block_sound
        if t >= 1.2 and block_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            block_sound.tStart = t
            block_sound.frameNStart = frameN  # exact frame index
            block_sound.play()  # start the sound (it finishes automatically)
        
        # *block_response* updates
        if t >= 1.4 and block_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            block_response.tStart = t
            block_response.frameNStart = frameN  # exact frame index
            block_response.setAutoDraw(True)
        
        # *block_key_resp* updates
        if t >= 1.4 and block_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            block_key_resp.tStart = t
            block_key_resp.frameNStart = frameN  # exact frame index
            block_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(block_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if block_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['d', 'k'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                block_key_resp.keys = theseKeys[-1]  # just the last key pressed
                block_key_resp.rt = block_key_resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_sound.stop()  # ensure sound has stopped at end of routine
    # check responses
    if block_key_resp.keys in ['', [], None]:  # No response was made
        block_key_resp.keys=None
    block_loop.addData('block_key_resp.keys',block_key_resp.keys)
    if block_key_resp.keys != None:  # we had a response
        block_loop.addData('block_key_resp.rt', block_key_resp.rt)
    # the Routine "block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'block_loop'


# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thankyou]
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thankyou* updates
    if t >= 0.0 and thankyou.status == NOT_STARTED:
        # keep track of start time/frame for later
        thankyou.tStart = t
        thankyou.frameNStart = frameN  # exact frame index
        thankyou.setAutoDraw(True)
    frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if thankyou.status == STARTED and t >= frameRemains:
        thankyou.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'perception-task'  # from the Builder filename that created this script
expInfo = {u'participant': u'1', u'second language': u'', u'first language': u'english', u'age': u'25', u'handedness': u'right', u'sex': u'female', u'session': u'001', u'english dialect': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1680, 1050), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
instuctions = visual.TextStim(win=win, name='instuctions',
    text='You are about to hear a word.\n\nIt will be either present or past tense.\n\nPress "D" if you heard past tense\nPress "K" if you heard present tense\nD: past\nK: present\n\nPlease press spacebar to start a short training round.',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "test"
testClock = core.Clock()
test_sound = sound.Sound('A', secs=-1)
test_sound.setVolume(1)
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
response = visual.TextStim(win=win, name='response',
    text='Which tense did you hear?\n\nA: past\n\nL: present\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "begin_instructions"
begin_instructionsClock = core.Clock()
begin_instructions_text = visual.TextStim(win=win, name='begin_instructions_text',
    text='You are now ready to begin. Please hit spacebar when ready.',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "block"
blockClock = core.Clock()
fixation_block = visual.TextStim(win=win, name='fixation_block',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
block_sound = sound.Sound('A', secs=-1)
block_sound.setVolume(1)
block_response = visual.TextStim(win=win, name='block_response',
    text='Which tense did you hear?\n\nA: past\n\nL: present\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thankyou = visual.TextStim(win=win, name='thankyou',
    text='Thank you very much.',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
end_instructions = event.BuilderKeyResponse()
# keep track of which components have finished
trialComponents = [ISI, instuctions, end_instructions]
for thisComponent in trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instuctions* updates
    if t >= 0.0 and instuctions.status == NOT_STARTED:
        # keep track of start time/frame for later
        instuctions.tStart = t
        instuctions.frameNStart = frameN  # exact frame index
        instuctions.setAutoDraw(True)
    
    # *end_instructions* updates
    if t >= 0.0 and end_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_instructions.tStart = t
        end_instructions.frameNStart = frameN  # exact frame index
        end_instructions.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(end_instructions.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if end_instructions.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            end_instructions.keys = theseKeys[-1]  # just the last key pressed
            end_instructions.rt = end_instructions.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    # *ISI* period
    if t >= 0.0 and ISI.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI.tStart = t
        ISI.frameNStart = frameN  # exact frame index
        ISI.start(0.5)
    elif ISI.status == STARTED:  # one frame should pass before updating params and completing
        ISI.complete()  # finish the static period
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_instructions.keys in ['', [], None]:  # No response was made
    end_instructions.keys=None
thisExp.addData('end_instructions.keys',end_instructions.keys)
if end_instructions.keys != None:  # we had a response
    thisExp.addData('end_instructions.rt', end_instructions.rt)
thisExp.nextEntry()
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
test_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('test_list.csv'),
    seed=None, name='test_loop')
thisExp.addLoop(test_loop)  # add the loop to the experiment
thisTest_loop = test_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest_loop.rgb)
if thisTest_loop != None:
    for paramName in thisTest_loop.keys():
        exec(paramName + '= thisTest_loop.' + paramName)

for thisTest_loop in test_loop:
    currentLoop = test_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTest_loop.rgb)
    if thisTest_loop != None:
        for paramName in thisTest_loop.keys():
            exec(paramName + '= thisTest_loop.' + paramName)
    
    # ------Prepare to start Routine "test"-------
    t = 0
    testClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    test_sound.setSound(stimuli, secs=-1)
    test_key_resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    testComponents = [test_sound, fixation, test_key_resp, response]
    for thisComponent in testComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "test"-------
    while continueRoutine:
        # get current time
        t = testClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop test_sound
        if t >= 1.2 and test_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            test_sound.tStart = t
            test_sound.frameNStart = frameN  # exact frame index
            test_sound.play()  # start the sound (it finishes automatically)
        
        # *fixation* updates
        if t >= 0.0 and fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation.tStart = t
            fixation.frameNStart = frameN  # exact frame index
            fixation.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation.status == STARTED and t >= frameRemains:
            fixation.setAutoDraw(False)
        
        # *test_key_resp* updates
        if t >= 1.4 and test_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            test_key_resp.tStart = t
            test_key_resp.frameNStart = frameN  # exact frame index
            test_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(test_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if test_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['a', 'l'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                test_key_resp.keys = theseKeys[-1]  # just the last key pressed
                test_key_resp.rt = test_key_resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *response* updates
        if t >= 1.4 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t
            response.frameNStart = frameN  # exact frame index
            response.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test"-------
    for thisComponent in testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    test_sound.stop()  # ensure sound has stopped at end of routine
    # check responses
    if test_key_resp.keys in ['', [], None]:  # No response was made
        test_key_resp.keys=None
    test_loop.addData('test_key_resp.keys',test_key_resp.keys)
    if test_key_resp.keys != None:  # we had a response
        test_loop.addData('test_key_resp.rt', test_key_resp.rt)
    # the Routine "test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'test_loop'


# ------Prepare to start Routine "begin_instructions"-------
t = 0
begin_instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
begin_instructionsComponents = [begin_instructions_text, key_resp_2]
for thisComponent in begin_instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "begin_instructions"-------
while continueRoutine:
    # get current time
    t = begin_instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *begin_instructions_text* updates
    if t >= 0.0 and begin_instructions_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        begin_instructions_text.tStart = t
        begin_instructions_text.frameNStart = frameN  # exact frame index
        begin_instructions_text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in begin_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "begin_instructions"-------
for thisComponent in begin_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "begin_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(expInfo['condition_file']),
    seed=None, name='block_loop')
thisExp.addLoop(block_loop)  # add the loop to the experiment
thisBlock_loop = block_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_loop.rgb)
if thisBlock_loop != None:
    for paramName in thisBlock_loop.keys():
        exec(paramName + '= thisBlock_loop.' + paramName)

for thisBlock_loop in block_loop:
    currentLoop = block_loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_loop.rgb)
    if thisBlock_loop != None:
        for paramName in thisBlock_loop.keys():
            exec(paramName + '= thisBlock_loop.' + paramName)
    
    # ------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    block_sound.setSound(stimuli, secs=-1)
    block_key_resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    blockComponents = [fixation_block, block_sound, block_response, block_key_resp]
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "block"-------
    while continueRoutine:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_block* updates
        if t >= 0.0 and fixation_block.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_block.tStart = t
            fixation_block.frameNStart = frameN  # exact frame index
            fixation_block.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_block.status == STARTED and t >= frameRemains:
            fixation_block.setAutoDraw(False)
        # start/stop block_sound
        if t >= 1.2 and block_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            block_sound.tStart = t
            block_sound.frameNStart = frameN  # exact frame index
            block_sound.play()  # start the sound (it finishes automatically)
        
        # *block_response* updates
        if t >= 1.4 and block_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            block_response.tStart = t
            block_response.frameNStart = frameN  # exact frame index
            block_response.setAutoDraw(True)
        
        # *block_key_resp* updates
        if t >= 1.4 and block_key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            block_key_resp.tStart = t
            block_key_resp.frameNStart = frameN  # exact frame index
            block_key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(block_key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if block_key_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['a', 'l'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                block_key_resp.keys = theseKeys[-1]  # just the last key pressed
                block_key_resp.rt = block_key_resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_sound.stop()  # ensure sound has stopped at end of routine
    # check responses
    if block_key_resp.keys in ['', [], None]:  # No response was made
        block_key_resp.keys=None
    block_loop.addData('block_key_resp.keys',block_key_resp.keys)
    if block_key_resp.keys != None:  # we had a response
        block_loop.addData('block_key_resp.rt', block_key_resp.rt)
    # the Routine "block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'block_loop'


# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thankyou]
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thankyou* updates
    if t >= 0.0 and thankyou.status == NOT_STARTED:
        # keep track of start time/frame for later
        thankyou.tStart = t
        thankyou.frameNStart = frameN  # exact frame index
        thankyou.setAutoDraw(True)
    frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if thankyou.status == STARTED and t >= frameRemains:
        thankyou.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
