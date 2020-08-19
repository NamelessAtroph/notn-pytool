from tkinter import *

#Base
global window
global year
window=Tk()

#yearFrame
yearFrame=Frame(window)
yrLabel=Label(yearFrame,text="Year: ")
year=Entry(yearFrame)
yrBtn=Button(yearFrame,text="Open",width=4)
#coliFrame
coliFrame=Frame(window)
coliTitle=Label(coliFrame,text="Coliseum Stats:",font='BOLD')
enText=Label(coliFrame,text="Enemies Fought: ")
enCount=Entry(coliFrame)
enUp=Button(coliFrame,text="+")
enCount.insert(0,'0')
colChestText=Label(coliFrame,text="Chests: ")
colChestCount=Entry(coliFrame)
colChestUp=Button(coliFrame,text="+")
colChestCount.insert(0,'0')

#yearFrame Geometry
yearFrame.grid(row=0)
yrLabel.grid(row=0,column=0)
year.grid(row=0,column=1)
yrBtn.grid(row=0,column=2,padx=5)
#coliFrame Geometry
coliFrame.grid(row=1,pady=5)
coliTitle.grid(row=0)
enText.grid(row=1,column=0)
enCount.grid(row=1,column=1)
enUp.grid(row=1,column=2,padx=5,pady=2)
colChestText.grid(row=2,column=0)
colChestCount.grid(row=2,column=1)
colChestUp.grid(row=2,column=2,padx=5,pady=2)

#Functions
class guiFuncts:

	def openFile():
		yr=year.get()
		file=open('docs/year/'+yr+'.txt','w+')

	def enemUp():
		val1=enCount.get()
		enCount.delete(0,'end')
		val2=int(val1)+1
		enCount.insert(0,val2)
	def colChUp():
		val1=colChestCount.get()
		colChestCount.delete(0,'end')
		val2=int(val1)+1
		colChestCount.insert(0,val2)

#ColiButtons
enUp.configure(command=guiFuncts.enemUp)
colChestUp.configure(command=guiFuncts.colChUp)
