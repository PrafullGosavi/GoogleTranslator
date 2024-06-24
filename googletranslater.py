from tkinter import *  #used for creating graphical user interfaces (GUIs).
from tkinter import ttk  #this imports the themed Tkinter widgets, which provide a more modern look to your GUI components.
from googletrans import Translator,LANGUAGES  #This imports the Translator class and LANGUAGES dictionary from the googletrans library, a Python API for Google's translation service.

#translator working

#This function translates text from a source language to a destination language using the googletrans API.
def change(text="type",src="English",dest="Hindi"):
    text1  = text   #The text to be translated.
    src1 = src      #The source language.
    dest1 = dest    #The destination language.

    trans = Translator()    #trans object and call the translator class
    trans1 = trans.translate(text,src=src1,dest=dest1)  #The result of the translation operation.
    return trans1.text   #The translated text.

#get the data
#This function retrieves the source and destination languages from the combo boxes, 
#gets the text from the source text box, performs translation, and displays the translated text in the destination text box.
def data():
    s = comb_sor.get()  #s veraible is The selected source language.
    d = comb_dest.get() #d veriable is The selected destination language.
    msg = sor_txt.get(1.0,END) #The text from the source text box.
    textget =  change(text = msg,src = s,dest = d)  #this is a The translated text.
    dest_txt.delete(1.0,END)  #this is about Clears the destination text box.
    dest_txt.insert(END,textget) #Inserts the translated text into the destination text box.

    

root = Tk() # Root is The main window of the application.

root.title("Translator") #Sets the title of the window.
root.geometry("500x500") #Sets the title of the window.
root.config(bg='Black')  #Sets the background color of the window.
 
# labels
lab_txt =Label(root,text="Translator",font=("Time New Roman",40,"bold"),bg="lime") # This Creates labels to display text.
lab_txt.place(x=100,y=40,height=50,width=300)
#frame
frame = Frame(root).pack(side=BOTTOM)  #we are making frame of root objects. pack use fro placement. Creates a frame for organizing widgets.
lab_txt =Label(root,text="Enter Text Here",font=("Time New Roman",17,"bold"),fg="white",bg="black")
lab_txt.place(x=100,y=100,height=20,width=300)
#A text box for the source text.
sor_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD,bg="ivory")
sor_txt.place(x=10,y=130,height=100 ,width=480)



#combo box
list_text = list(LANGUAGES.values())  #A list of language names from LANGUAGES.
#A combo box for selecting the source language.
comb_sor = ttk.Combobox(frame,value=list_text,font=("Time New Roman",15,"bold"))  
comb_sor.place(x=10,y=250,height=40,width=150)
#setting values in the combo box
comb_sor.set("english")

#Making a button to trigger the translation process.
button_change = Button(frame,text = "Translate",font=("Time New Roman",15,"bold"),relief=RAISED,command=data,bg="aqua",fg="black") #relief give buttons in 3d
button_change.place(x=170,y=250,height=40,width=150)

#A combo box for selecting the destination language.
comb_dest = ttk.Combobox(frame,value=list_text,font=("Time New Roman",15,"bold"))
comb_dest.place(x=330,y=250,height=40,width=150)
#setting values in the combo box
comb_dest.set("english")

#A label for the destination text box.
lab_txt =Label(root,text="Translated Text",font=("Time New Roman",17,"bold"),fg="white",bg="black")
lab_txt.place(x=100,y=300,height=50,width=300)
# A text box for the translated text.
dest_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD,bg="ivory")
dest_txt.place(x=10,y=350,height=100 ,width=480)

#Starts the GUI event loop, waiting for user interaction.
root.mainloop()



