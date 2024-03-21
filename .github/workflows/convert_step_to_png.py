import Part, PartGui
# Loading test part
Part.open('docs/DCDC-FusePCB.step)
Gui.ActiveDocument.ActiveView.saveImage('test.png',1656,783,'Current')       
