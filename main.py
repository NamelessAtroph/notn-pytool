from tkinter import *
import pickle,os

#Base
global window
global year
window=Tk()
window.title("NotN Pytool")
window.resizable(0,0)

#col1
col1=Frame(window)
#col2
col2=Frame(window)
#yearFrame
yearFrame=Frame(col1)
yrLabel=Label(yearFrame,text="Year: ")
year=Entry(yearFrame)
yrBtn=Button(yearFrame,text="Open",width=4)
#coliFrame
coliFrame=Frame(col1)
coliTitle=Label(coliFrame,text="Coliseum Stats:",font='BOLD')
enText=Label(coliFrame,text="Enemies Fought: ")
enCount=Entry(coliFrame)
enUp=Button(coliFrame,text="+")
enCount.insert(0,'0')
colChestText=Label(coliFrame,text="Chests: ")
colChestCount=Entry(coliFrame)
colChestUp=Button(coliFrame,text="+")
colChestCount.insert(0,'0')
#otherFrame
otherFrame=Frame(col1)
otherTitle=Label(otherFrame,text="Other methods:",font='BOLD')
baldwinTxt=Label(otherFrame,text="Baldwin:")
bdwCount=Entry(otherFrame)
bdwUp=Button(otherFrame,text="+")
bdwCount.insert(0,'0')
swippTxt=Label(otherFrame,text="Swipp:")
swpCount=Entry(otherFrame)
swpUp=Button(otherFrame,text="+")
swpCount.insert(0,'0')
ahTxt=Label(otherFrame,text="Auction House:")
ahCount=Entry(otherFrame)
ahUp=Button(otherFrame,text="+")
ahCount.insert(0,'0')
crTxt=Label(otherFrame,text="Crossroads:")
crCount=Entry(otherFrame)
crUp=Button(otherFrame,text="+")
crCount.insert(0,'0')
gthTxt=Label(otherFrame,text="Gathering:")
gthCount=Entry(otherFrame)
gthUp=Button(otherFrame,text="+")
gthCount.insert(0,'0')
#dataFrame
dataFrame=Frame(col2)
dataLabel=Label(dataFrame,text="Stored Data:",font='BOLD')
dataInfo=Text(dataFrame,width=25,height=10,state=DISABLED)
#databtns
btnFrame=Frame(col2)
writfil=Button(btnFrame,text="Write File")
statss=Button(btnFrame,text="Stats")

#col1 Geometry
col1.grid(column=0,row=0)
#col2 Geometry
col2.grid(column=1,row=0)
#yearFrame Geometry
yearFrame.grid(row=0,column=0)
yrLabel.grid(row=0,column=0)
year.grid(row=0,column=1)
yrBtn.grid(row=0,column=2,padx=5)
#coliFrame Geometry
coliFrame.grid(row=1,pady=5,column=0)
coliTitle.grid(row=0)
enText.grid(row=1,column=0)
enCount.grid(row=1,column=1)
enUp.grid(row=1,column=2,padx=5,pady=2)
colChestText.grid(row=2,column=0)
colChestCount.grid(row=2,column=1)
colChestUp.grid(row=2,column=2,padx=5,pady=2)
#otherFrame Geometry
otherFrame.grid(row=2,pady=5,column=0)
otherTitle.grid(row=0)
baldwinTxt.grid(row=1,column=0)
bdwCount.grid(row=1,column=1)
bdwUp.grid(row=1,column=2,padx=5,pady=2)
swippTxt.grid(row=2,column=0)
swpCount.grid(row=2,column=1)
swpUp.grid(row=2,column=2,padx=5,pady=2)
ahTxt.grid(row=3,column=0)
ahCount.grid(row=3,column=1)
ahUp.grid(row=3,column=2,padx=5,pady=2)
crTxt.grid(row=4,column=0)
crCount.grid(row=4,column=1)
crUp.grid(row=4,column=2,padx=5,pady=2)
gthTxt.grid(row=5,column=0)
gthCount.grid(row=5,column=1)
gthUp.grid(row=5,column=2,padx=5,pady=2)
#dataFrame Geometry
dataFrame.grid(column=1,padx=8)
dataLabel.grid(row=1)
dataInfo.grid()
#btnFrame Geometry
btnFrame.grid(column=1,pady=5)
writfil.grid(row=2,pady=3)
statss.grid(row=3,pady=3)

#Functions
class guiFuncts:

	#File tasks
	def openFile():
		yr=year.get()
		file=open('docs/year/'+yr+'.dat','ab+')
		file.close()
		file=open('docs/year/'+yr+'.dat','rb')
		dat=pickle.load(file)
		file.close()
		dataInfo.configure(state=NORMAL)
		dataInfo.delete('1.1',END)
		dataInfo.insert('1.1',dat)
		dataInfo.configure(state=DISABLED)
		#Restore entry info
		enCount.delete(0,'end')
		enCount.insert(0,dat['enemies'])
		colChestCount.delete(0,'end')
		colChestCount.insert(0,dat['colichests'])
		bdwCount.delete(0,'end')
		bdwCount.insert(0,dat['baldchests'])
		swpCount.delete(0,'end')
		swpCount.insert(0,dat['swipchests'])
		ahCount.delete(0,'end')
		ahCount.insert(0,dat['ahchests'])
		crCount.delete(0,'end')
		crCount.insert(0,dat['crosschests'])
		gthCount.delete(0,'end')
		gthCount.insert(0,dat['gthchests'])
	def writeFile():
		c1=enCount.get()
		c2=colChestCount.get()
		c3=bdwCount.get()
		c4=swpCount.get()
		c5=ahCount.get()
		c6=crCount.get()
		c7=gthCount.get()
		counts=dict={'enemies':c1,'colichests':c2,'baldchests':c3,'swipchests':c4,'ahchests':c5,'crosschests':c6,'gthchests':c7}
		print(counts)
		dataInfo.configure(state=NORMAL)
		dataInfo.delete('1.1',END)
		dataInfo.insert('1.1',str(counts))
		dataInfo.configure(state=DISABLED)
		yr=year.get()
		file=open('docs/year/'+yr+'.dat','wb')
		pickle.dump(counts,file)

	#Coli
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

	#Other
	def bdwUpf():
		val1=bdwCount.get()
		bdwCount.delete(0,'end')
		val2=int(val1)+1
		bdwCount.insert(0,val2)
	def swpUpf():
		val1=swpCount.get()
		swpCount.delete(0,'end')
		val2=int(val1)+1
		swpCount.insert(0,val2)
	def ahUpf():
		val1=ahCount.get()
		ahCount.delete(0,'end')
		val2=int(val1)+1
		ahCount.insert(0,val2)
	def crUpf():
		val1=crCount.get()
		crCount.delete(0,'end')
		val2=int(val1)+1
		crCount.insert(0,val2)
	def gthUpf():
		val1=gthCount.get()
		gthCount.delete(0,'end')
		val2=int(val1)+1
		gthCount.insert(0,val2)

	#OtherWindows
	def stw():
		#Base
		st=Toplevel(window)
		st.title("Chest Statistics")
		#Enter year
		yearFrame=Frame(st)
		yrLabel=Label(yearFrame,text="Year: ")
		syear=Entry(yearFrame)
		yrBtn=Button(yearFrame,text="Open",width=4)
		#Stats
		stats=Frame(st)
		yscroll=Scrollbar(stats)
		stwindow=Text(stats,width=25,height=10,state=DISABLED,yscrollcommand=yscroll.set)
		yscroll.config(command=stwindow.yview)
		#Geometry
		yearFrame.grid(row=0,column=0)
		yrLabel.grid(row=0,column=0)
		syear.grid(row=0,column=1)
		yrBtn.grid(row=0,column=2,padx=5)
		stats.grid(row=1,column=0)
		stwindow.grid(row=2,column=0)
		#Do the stat thing
		def runSt():
			yr=syear.get()
			file=open('docs/year/'+yr+'.dat','rb')
			dat=pickle.load(file)
			file.close()
			stwindow.configure(state=NORMAL)
			stwindow.insert("1.1","-Stats for: "+yr+"-\n"+"Coli enemies fought: "+dat['enemies']+"\nChests from Coli: "+dat['colichests']+"\nDrop rate: "+str(int(dat['colichests'])/int(dat['enemies'])*100)+"%\nBaldwin chests: "+dat['baldchests']+"\nSwipp chests: "+dat['swipchests']+"\nAH chests: "+dat['ahchests']+"\nCR chests:"+dat['crosschests']+"\nGathering chests: "+dat['gthchests'])
			stwindow.configure(state=DISABLED)
		#btn
		yrBtn.configure(command=runSt)
	
#FileButtons
yrBtn.configure(command=guiFuncts.openFile)
#ColiButtons
enUp.configure(command=guiFuncts.enemUp)
colChestUp.configure(command=guiFuncts.colChUp)
#OtherButtons
bdwUp.configure(command=guiFuncts.bdwUpf)
swpUp.configure(command=guiFuncts.swpUpf)
ahUp.configure(command=guiFuncts.ahUpf)
crUp.configure(command=guiFuncts.crUpf)
gthUp.configure(command=guiFuncts.gthUpf)
#dataBtns
writfil.configure(command=guiFuncts.writeFile)
statss.configure(command=guiFuncts.stw)

#Run app
window.mainloop()