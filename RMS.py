import datetime
from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
#functions

def send():



   root2=Toplevel()

   root2.title("Send Bill")
   root2.config(bg='red4')

   logoImaage = PhotoImage(file='C:/Users/user/Desktop/download.png')
   label = Label(root2,image=logoImaage, bg='red4')
   label.pack(pady=5)

   numberLabel=Label(root2,text='Mobile Number',font=('arial',18,'bold underline'),bg='red4',fg='white')
   numberLabel.pack(pady=5)
   numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=24)
   numberfield.pack(pady=5)
   billLabel = Label(root2, text='Bill details', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
   billLabel.pack(pady=5)

   textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=14)
   textarea.pack(pady=5)
   textarea.insert(END,'receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n\n')

   if CostOfFoodVar.get() != '0 UGX':
       textarea.insert(END, f'Cost Of Food\t\t\t{PriceofFood}UGX\n')
   if CostOfDrinksVar.get() != '0 UGX':
       textarea.insert(END, f'Cost Of Drinks\t\t\t{PriceofDrinks}UGX\n')

   textarea.insert(END, f'Sub Total\t\t\t{subtotalofitems}UGX\n')
   textarea.insert(END, f'Service Tax\t\t\t{0}UGX\n\n')
   textarea.insert(END, f'Total Cost\t\t\t{subtotalofitems + 0}UGX\n')
   sendButton=Button(root2,text='SEND',font=('arial',19,'bold'),bg='white',fg='red4',bd=7,relief=GROOVE,command=send_msg)
   sendButton.pack(pady=5)





   root2.mainloop()




def Save():
    url=filedialog.asksaveasfile(mode='w',defaultextension=',text')

    bill_data=textreciept.get(1.0,END)
    url.write(bill_data)
    url.close()
    messagebox.showinfo('Xog-Ururin','Biilashada Si guul leh ayaa loo keydiyey')




def receipt():
    global billnumber,date
    textreciept.delete(1.0,END)
    x=random.randint(1,1000)
    billnumber='BILL'+str(x)
    date=time.strftime('%d/%m/%y')
    textreciept.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
    textreciept.insert(END,'*************************************************************\n')
    textreciept.insert(END,'Items:\t\t Cost Of Items(UGX)\n')
    textreciept.insert(END, '**************************************************************\n')
    if e_Chapati.get()!='0':
        textreciept.insert(END,f'Chapati\t\t\t{int(e_Chapati.get())*1000}\n\n')
    if e_fish.get() != '0':
        textreciept.insert(END, f'Fish\t\t\t{int(e_fish.get()) * 5000}\n\n')
    if e_canjerosomali.get() != '0':
        textreciept.insert(END, f'Canjerosomali\t\t\t{int(e_canjerosomali.get()) * 500}\n\n')
    if e_Bariis.get() != '0':
        textreciept.insert(END, f'Bariis\t\t\t{int(e_Bariis.get()) * 3000}\n\n')
    if e_Baasto.get() != '0':
        textreciept.insert(END, f'Baasto\t\t\t{int(e_Baasto.get()) * 3000}\n\n')
    if e_Liver.get()!='0':
        textreciept.insert(END,f'Liver\t\t\t{int(e_Liver.get())*4000}\n\n')
    if e_Baastomakrooni.get()!='0':
        textreciept.insert(END,f'Baastomakroni\t\t\t{int(e_Baastomakrooni.get())*3000}\n\n')
    if e_Maharago.get()!='0':
        textreciept.insert(END,f'Maharago\t\t\t{int(e_Maharago.get())*500}\n\n')
    if e_Cambuulo.get()!='0':
        textreciept.insert(END,f'Cambuulo\t\t\t{int(e_Cambuulo.get())*3000}\n\n')
    if e_Chicken.get()!='0':
        textreciept.insert(END,f'Chicken\t\t\t{int(e_Chicken.get())*7500}\n\n')

    if e_avocados.get()!='0':
        textreciept.insert(END,f'avocados\t\t\t{int(e_avocados.get())*1000}\n\n')
    if e_Mangoes.get()!='0':
        textreciept.insert(END,f'Mangoes\t\t\t{int(e_Mangoes.get())*1000}\n\n')
    if e_Lemon.get()!='0':
        textreciept.insert(END,f'Lemon\t\t\t{int(e_Lemon.get())*1000}\n\n')
    if e_Watermelon.get()!='0':
        textreciept.insert(END,f'Watermelon\t\t\t{int(e_Watermelon.get())*1000}\n\n')
    if e_SmallWater.get()!='0':
        textreciept.insert(END,f'Small Water\t\t\t{int(e_SmallWater.get())*500}\n\n')
    if e_PigWater.get()!='0':
        textreciept.insert(END,f'Pig Water\t\t\t{int(e_PigWater.get())*1500}\n\n')
    if e_Coffee.get()!='0':
        textreciept.insert(END,f'Coffee\t\t\t{int(e_Coffee.get())*1000}\n\n')
    if e_MilkTea.get()!='0':
        textreciept.insert(END,f'Milk Tea\t\t\t{int(e_MilkTea.get())*1000}\n\n')
    if e_BlackTea.get()!='0':
        textreciept.insert(END,f'Black Tea\t\t\t{int(e_BlackTea.get())*500}\n\n')

    textreciept.insert(END, '**************************************************************\n')
    if CostOfFoodVar.get() != '0 UGX':
       textreciept.insert(END,f'Cost Of Food\t\t\t{PriceofFood}UGX\n\n')
    if CostOfFoodVar.get() != '0 UGX':
       textreciept.insert(END, f'Cost Of Drinks\t\t\t{PriceofDrinks}UGX\n\n')


    textreciept.insert(END, f'Sub Total\t\t\t{subtotalofitems}UGX\n\n')
    textreciept.insert(END, f'Service Tax\t\t\t{0}UGX\n\n')
    textreciept.insert(END, f'Total Cost\t\t\t{subtotalofitems+0}UGX\n\n')
    textreciept.insert(END, '**************************************************************\n')






def totalCost():
    global PriceofFood,PriceofDrinks,subtotalofitems
    item1=int(e_Chapati.get())
    item2=int(e_fish.get())
    item3=int(e_canjerosomali.get())
    item4=int(e_Bariis.get())
    item5=int(e_Baasto.get())
    item6=int(e_Liver.get())
    item7=int(e_Baastomakrooni.get())
    item8=int(e_Maharago.get())
    item9=int(e_Cambuulo.get())
    item10=int(e_Chicken.get())


    item11=int(e_avocados.get())
    item12=int(e_Mangoes.get())
    item13=int(e_Lemon.get())
    item14=int(e_Watermelon.get())
    item15=int(e_SmallWater.get())
    item16=int(e_PigWater.get())
    item17=int(e_Coffee.get())
    item18=int(e_MilkTea.get())
    item19=int(e_BlackTea.get())

    PriceofFood=((item1 * 1000) + (item2 * 5000) + (item3 * 500) + (item4 * 3000) + (item5*3000) + (item6 * 4000) + (item7 * 3000) \
                 +(item8 * 500)+(item9 * 3000) + (item10 * 7500))

    PriceofDrinks=((item11 * 1000)+(item12 * 1000) + (item13 * 1000) + (item14 * 1000) + (item15*500) + (item16 * 1500) + (item17 * 1000) \
                 +(item18 * 1000)+(item19 * 500))
    CostOfFoodVar.set(str(PriceofFood)+ ' UGX')
    CostOfDrinksVar.set(str(PriceofDrinks)+ ' UGX')

    subtotalofitems=PriceofFood+PriceofDrinks
    subtotalVar.set(str(subtotalofitems)+' UGX')

    serviceTaxVar.set(' 0 UGX')

    totalCost=subtotalofitems+0
    totalCostVar.set(str(totalCost)+' UGX')

def Chapati():
    if Var1.get()==1:
     textchapati.config(state=NORMAL)
     textchapati.delete(0,END)
     textchapati.focus()
    else:
     textchapati.config(state=DISABLED)
     e_Chapati.set('0')


def Fish():
    if Var2.get() ==1:
        textfish.config(state=NORMAL)
        textfish.delete(0, END)
        textfish.focus()
    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')


def canjerosomali():
    if Var3.get()==1:
     textcanjerosomali.config(state=NORMAL)
     textcanjerosomali.delete(0,END)
     textcanjerosomali.focus()
    else:
     textcanjerosomali().config(state=DISABLED)
     e_canjerosomali.set('0')

def Bariis():
    if Var4.get() == 1:
        textBariis.config(state=NORMAL)
        textBariis.delete(0, END)
        textBariis.focus()
    else:
        textBariis.config(state=DISABLED)
        e_Bariis.set('0')

def Baasto():
    if Var5.get() == 1:
        textBaasto.config(state=NORMAL)
        textBaasto.delete(0, END)
        textBaasto.focus()
    else:
        textBaasto.config(state=DISABLED)
        e_Baasto.set('0')


def Liver():
    if Var6.get() == 1:
        textLiver.config(state=NORMAL)
        textLiver.delete(0, END)
        textLiver.focus()
    else:
        textLiver.config(state=DISABLED)
        e_Liver.set('0')

def Baastomakrooni():
    if Var7.get() == 1:
        textBaastomakrooni.config(state=NORMAL)
        textBaastomakrooni.delete(0, END)
        textBaastomakrooni.focus()
    else:
        textBaastomakrooni.config(state=DISABLED)
        e_Baastomakrooni.set('0')

def Maharago():
    if Var8.get() == 1:
        textMaharago.config(state=NORMAL)
        textMaharago.delete(0, END)
        textMaharago.focus()
    else:
        textMaharago.config(state=DISABLED)
        e_Maharago.set('0')

def Cambuulo():
    if Var9.get() == 1:
        textCambuulo.config(state=NORMAL)
        textCambuulo.delete(0, END)
        textCambuulo.focus()
    else:
        textCambuulo.config(state=DISABLED)
        e_Cambuulo.set('0')

def Chicken():
    if Var10.get() == 1:
        textChicken.config(state=NORMAL)
        textChicken.delete(0, END)
        textChicken.focus()
    else:
        textChicken.config(state=DISABLED)
        e_Chicken.set('0')

def avocados():
    if Var11.get() == 1:
        textavocados.config(state=NORMAL)
        textavocados.delete(0, END)
        textavocados.focus()
    else:
        textavocados.config(state=DISABLED)
        e_avocados.set('0')

def Mangoes():
    if Var12.get() == 1:
        textMangoes.config(state=NORMAL)
        textMangoes.delete(0, END)
        textMangoes.focus()
    else:
        textMangoes.config(state=DISABLED)
        e_Mangoes.set('0')

def Lemon():
    if Var13.get() == 1:
        textLemon.config(state=NORMAL)
        textLemon.delete(0, END)
        textLemon.focus()
    else:
        textLemon.config(state=DISABLED)
        e_Lemon.set('0')

def Watermelon():
    if Var14.get() == 1:
        textWatermelon.config(state=NORMAL)
        textWatermelon.delete(0, END)
        textWatermelon.focus()
    else:
        textWatermelon.config(state=DISABLED)
        e_Watermelon.set('0')

def SmallWater():
    if Var15.get() == 1:
        textSmallwater.config(state=NORMAL)
        textSmallwater.delete(0, END)
        textSmallwater.focus()
    else:
        textSmallwater.config(state=DISABLED)
        e_SmallWater.set('0')

def PigWater():
    if Var16.get() == 1:
        textPigWater.config(state=NORMAL)
        textPigWater.delete(0, END)
        textPigWater.focus()
    else:
        textPigWater.config(state=DISABLED)
        e_PigWater.set('0')

def Coffee():
    if Var17.get() == 1:
        textCoffee.config(state=NORMAL)
        textCoffee.delete(0, END)
        textCoffee.focus()
    else:
        textCoffee.config(state=DISABLED)
        e_Coffee.set('0')

def MilkTea():
    if Var18.get() == 1:
        textMilkTea.config(state=NORMAL)
        textMilkTea.delete(0, END)
        textMilkTea.focus()
    else:
        textMilkTea.config(state=DISABLED)
        e_MilkTea.set('0')

def BlackTea():
    if Var19.get() == 1:
        textBlackTea.config(state=NORMAL)
        textBlackTea.delete(0, END)
        textBlackTea.focus()
    else:
        textBlackTea.config(state=DISABLED)
        e_BlackTea.set('0')


root =Tk()
root.title("Restaurant Management System")
root.configure(bg='Green4')

topFrame=Frame(root,bd=10,relief=RIDGE,bg='Green4')
topFrame.pack(side=TOP)
LabelTitle=Label(topFrame,text='Hiil Cafe Restaurant Management',font=('arial',30,'bold'),fg='yellow',bd=9,bg='Green4',width=51)
LabelTitle.grid(row=0,column=0)

#frames

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='Yellow4')
menuFrame.pack(side=LEFT)
costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='Blue4',pady=10)
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='Food',font=('arial',19,'bold'),bd=10,relief=RIDGE,bg='Green4',)
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text='drinks',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='Blue4')
drinksFrame.pack(side=LEFT)
cakesFrame=LabelFrame(menuFrame,text='cakes',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='Green4')
cakesFrame.pack(side=LEFT)
rightFrame=Frame(root,bd=15,relief=RIDGE,bg='Green4')
rightFrame.pack(side=RIGHT)
calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='Blue4')
calculatorFrame.pack()

receiptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='yellow4')
receiptFrame.pack()
buttonFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='yellow4')
buttonFrame.pack()

#variable

Var1=IntVar()
Var2=IntVar()
Var3=IntVar()
Var4=IntVar()
Var5=IntVar()
Var6=IntVar()
Var7=IntVar()
Var8=IntVar()
Var9=IntVar()
Var10=IntVar()
Var11=IntVar()
Var12=IntVar()
Var13=IntVar()
Var14=IntVar()
Var15=IntVar()
Var16=IntVar()
Var17=IntVar()
Var18=IntVar()
Var19=IntVar()
Var20=IntVar()




e_Chapati=StringVar()
e_fish=StringVar()
e_canjerosomali = StringVar()
e_Bariis = StringVar()
e_Baasto = StringVar()
e_Liver = StringVar()
e_Baastomakrooni = StringVar()
e_Cambuulo = StringVar()
e_Maharago = StringVar()
e_Chicken = StringVar()



e_avocados=StringVar()
e_Mangoes=StringVar()
e_Lemon=StringVar()
e_Watermelon=StringVar()
e_SmallWater=StringVar()
e_PigWater=StringVar()
e_Coffee=StringVar()
e_MilkTea=StringVar()
e_BlackTea=StringVar()


CostOfFoodVar=StringVar()
CostOfDrinksVar=StringVar()
subtotalVar=StringVar()
serviceTaxVar=StringVar()
totalCostVar=StringVar()

e_Chapati.set('0')
e_fish.set('0')
e_canjerosomali.set('0')
e_Bariis.set('0')
e_Baasto.set('0')
e_Liver.set('0')
e_Baastomakrooni.set('0')
e_Maharago.set('0')
e_Cambuulo.set('0')
e_Chicken.set('0')

e_avocados.set('0')
e_Mangoes.set('0')
e_Lemon.set('0')
e_Watermelon.set('0')
e_SmallWater.set('0')
e_PigWater.set('0')
e_Coffee.set('0')
e_MilkTea.set('0')
e_BlackTea.set('0')







##FOOD

chapati=Checkbutton(foodFrame,text='Chapati',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=Var1,command=Chapati)
chapati.grid(row=1,column=0,sticky=W)
fish=Checkbutton(foodFrame,text='fish',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=Var2,command=Fish)
fish.grid(row=2,column=0,sticky=W)
Canjerosomali=Checkbutton(foodFrame,text='Canjerosomali',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=Var3,command=canjerosomali)
Canjerosomali.grid(row=3,column=0,sticky=W)
Bariis=Checkbutton(foodFrame,text='Bariis',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=Var4,command=Bariis)
Bariis.grid(row=4,column=0,sticky=W)
Baasto=Checkbutton(foodFrame,text='Baasto',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=Var5,command=Baasto)
Baasto.grid(row=5,column=0,sticky=W)
Liver=Checkbutton(foodFrame,text='Liver',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=Var6,command=Liver)
Liver.grid(row=6,column=0,sticky=W)
Baastomakrooni=Checkbutton(foodFrame,text='Baastomakrooni',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=Var7,command=Baastomakrooni)
Baastomakrooni.grid(row=7,column=0,sticky=W)
Maharago=Checkbutton(foodFrame,text='Maharago',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=Var8,command=Maharago)
Maharago.grid(row=8,column=0,sticky=W)
Cambuulo=Checkbutton(foodFrame,text='Cambuulo',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=Var9,command=Cambuulo)
Cambuulo.grid(row=9,column=0,sticky=W)
Chicken=Checkbutton(foodFrame,text='Chicken',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=Var10,command=Chicken)
Chicken.grid(row=10,column=0,sticky=W)

#Entry Fields for Food Items

textchapati=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Chapati)
textchapati.grid(row=1,column=1)
textfish=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fish)
textfish.grid(row=2,column=1)
textcanjerosomali=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_canjerosomali)
textcanjerosomali.grid(row=3,column=1)
textBariis=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Bariis)
textBariis.grid(row=4,column=1)
textBaasto=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Baasto)
textBaasto.grid(row=5,column=1)
textLiver=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Liver)
textLiver.grid(row=6,column=1)
textBaastomakrooni=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Baastomakrooni)
textBaastomakrooni.grid(row=7,column=1)
textMaharago=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Maharago)
textMaharago.grid(row=8,column=1)
textCambuulo=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Cambuulo)
textCambuulo.grid(row=9,column=1)
textChicken=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Chicken)
textChicken.grid(row=10,column=1)

#Drinks

avocados=Checkbutton(drinksFrame,text='avocados',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=Var11,command=avocados)
avocados.grid(row=0,column=0,sticky=W)
mangoes=Checkbutton(drinksFrame,text='mangoes',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=Var12,command=Mangoes)
mangoes.grid(row=1,column=0,sticky=W)
lemon=Checkbutton(drinksFrame,text='lemon',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=Var13,command=Lemon)
lemon.grid(row=2,column=0,sticky=W)
watermelon=Checkbutton(drinksFrame,text='watermelon',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=Var14,command=Watermelon)
watermelon.grid(row=3,column=0,sticky=W)
SmallWater=Checkbutton(drinksFrame,text='Small Water',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=Var15,command=SmallWater)
SmallWater.grid(row=4,column=0,sticky=W)
PigWater=Checkbutton(drinksFrame,text='PigWater',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=Var16,command=PigWater)
PigWater.grid(row=5,column=0,sticky=W)
Coffee=Checkbutton(drinksFrame,text='Coffee',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=Var17,command=Coffee)
Coffee.grid(row=6,column=0,sticky=W)
MilkTea=Checkbutton(drinksFrame,text='Milk Tea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=Var18,command=MilkTea)
MilkTea.grid(row=7,column=0,sticky=W)
BlackTea=Checkbutton(drinksFrame,text='Black Tea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=Var19,command=BlackTea)
BlackTea.grid(row=8,column=0,sticky=W)


#Entry Field for drinks Items

textavocados=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_avocados)
textavocados.grid(row=0,column=1)
textMangoes=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Mangoes)
textMangoes.grid(row=1,column=1)
textLemon=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Lemon)
textLemon.grid(row=2,column=1)
textWatermelon=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Watermelon)
textWatermelon.grid(row=3,column=1)
textSmallwater=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_SmallWater)
textSmallwater.grid(row=4,column=1)
textPigWater=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_PigWater)
textPigWater.grid(row=5,column=1)
textCoffee=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Coffee)
textCoffee.grid(row=6,column=1)
textMilkTea=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_MilkTea)
textMilkTea.grid(row=7,column=1)
textBlackTea=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_BlackTea)
textBlackTea.grid(row=8,column=1)

#Costlabels & entry fields

labelcostofFood=Label(costFrame,text='Cost of Foods',font=('arial',16,'bold'),bg='green4',fg='White')
labelcostofFood.grid(row=0,column=0)

textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=CostOfFoodVar)
textCostofFood.grid(row=0,column=1,padx=4)
labelcostofDrinks=Label(costFrame,text='Cost of Drinks',font=('arial',16,'bold'),bg='green4',fg='White')
labelcostofDrinks.grid(row=1,column=0)

textCostofDrinks=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=CostOfDrinksVar)
textCostofDrinks.grid(row=1,column=1,padx=4)

labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg='green4',fg='White')
labelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalVar)
textSubTotal.grid(row=0,column=3,padx=4)

labelServiceTax=Label(costFrame,text='Service  Tax',font=('arial',16,'bold'),bg='green4',fg='White')
labelServiceTax.grid(row=1,column=2)
textServiceTax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=serviceTaxVar)
textServiceTax.grid(row=1,column=3,padx=4)

labelTotalCost=Label(costFrame,text='TotalCost',font=('arial',16,'bold'),bg='green4',fg='White')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalCostVar)
textTotalCost.grid(row=2,column=3,padx=4)

#Buttons

buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='blue4',bd=3,padx=5,command=totalCost)
buttonTotal.grid(row=0,column=0)
buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='green4',bd=3,padx=5,command=receipt)
buttonReceipt.grid(row=0,column=1)
buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=Save)
buttonSave.grid(row=0,column=2)
buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='yellow4',bd=3,padx=5,command=send)
buttonSend.grid(row=0,column=3)
buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='yellow4',bd=3,padx=5)
buttonReset.grid(row=0,column=4)
buttonPrint=Button(buttonFrame,text='Print',font=('arial',14,'bold'),fg='white',bg='green4',bd=3,padx=5)
buttonPrint.grid(row=0,column=5)
#textarea for receipt
textreciept=Text(receiptFrame,font=('arial',12,'bold'),width=42,height=14)
textreciept.grid(row=0,column=0)

#calculator

operator='' #7+9
def buttonClick(numbers): #9
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def Clear():
    global operator
    operator=''
    calculatorField.delete(0,END)


def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''

calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='yellow',bg='green4',bd=6,width=6,command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)
button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='yellow',bg='green4',bd=6,width=6,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)
button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='yellow',bg='green4',bd=6,width=6,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)
buttonplus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='yellow',bg='green4',bd=6,width=6,command=lambda:buttonClick('+'))
buttonplus.grid(row=1,column=3)
button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='yellow',bg='green4',bd=6,width=6,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)
button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)
button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)
buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='yellow',bg='green4',bd=6,width=6,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)
button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='yellow',bg='blue4',bd=6,width=6,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)
button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)
button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)
buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='yellow',bg='blue4',bd=6,width=6,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)
buttonAns=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='green4',bd=6,width=6,command=answer)
buttonAns.grid(row=4,column=0)
buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='yellow',bg='yellow4',bd=6,width=6,command=Clear)
buttonClear.grid(row=4,column=1)
button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='yellow',bg='blue4',bd=6,width=6,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)
buttonDiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='yellow',bg='green4',bd=6,width=6,command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)
















root.mainloop()