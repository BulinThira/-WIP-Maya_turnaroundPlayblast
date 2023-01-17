import maya.cmds as mc

#mc.playblast(p=100, wh=[1920,1080], format="qt", filename ="C:/Users/ICT/Documents/maya/projects/default/movies/test_playblast02.mov")

def turnaroundPlayblast():
    if mc.window('trP_window', q=True, ex=True):
        mc.deleteUI('trP_window', window=True)
    mc.window('trP_window', title='Turnaround Playblast')
    mc.columnLayout(adj=True)
    
    mc.frameLayout(label='Select model', bgc=(0.1, 0.5, 0.5))
    mc.rowLayout(numberOfColumns=3)
    mc.text(label='model name')
    mc.textField('model_TF', w=150)
    mc.button(label='Get', w=50, c=getModel)
    mc.setParent('..')
    
    mc.frameLayout(label='Set start/end frame', bgc=(0.1, 0.5, 0.5))
    mc.rowLayout(numberOfColumns=2)
    mc.text(label='duration (sec)')
    mc.textField('dur_TF', w=150, it='3')
    mc.setParent('..')
    mc.button('turnaround_but', label='Create turnaround', c=spinModel)
    
    mc.frameLayout(label='Playblast directory setting', bgc=(0.1, 0.5, 0.5))
    mc.textField('fileDir_TF', w=150, it='movies/')
    mc.button('playblast_but', label='playblast', c=playblastCmd)
    
    mc.showWindow('trP_window')
    mc.window('trP_window', e=True, wh=(300,220))

def getModel(*args):
    sels = mc.ls(sl=True)
    
    if sels:
        mc.textField('model_TF', e=True, tx=sels[0])
    else:
        mc.textField('model_TF', e=True, tx='')
        
def spinModel(*args):
    modelName = mc.textField('model_TF', q=True, tx=True)
    #secondCall = mc.intField('dur_TF', q=True, v=True)
    
    
    mc.currentUnit(time='film')
    mc.setKeyframe( modelName, attribute='rotateY', t=['0sec','3sec'] )
    mc.currentTime(72)
    mc.rotate(0,"360deg",0)
    mc.keyTangent(modelName, edit=True, time=(0,0), itt="linear", ott="linear")
    mc.keyTangent(modelName, edit=True, time=(72,72), itt="linear", ott="linear")
    
    mc.select(cl=True)
    

def playblastCmd(*args):
    modelName = mc.textField('model_TF', q=True, tx=True)
    directory = mc.textField('fileDir_TF', q=True, tx=True)
    fullDir = directory.replace("\\","/")
    filenameEdited = f"{fullDir}/{modelName}_playblast.mov"
    print(filenameEdited)
    
    mc.playblast(p=100, wh=[1920,1080], format="qt", st=0, et=72, fo=True, v=True, filename = filenameEdited)
    
    
turnaroundPlayblast()