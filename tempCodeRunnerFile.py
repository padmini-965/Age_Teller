from tkinter import *
from datetime import datetime #importing all necessary modules

#creating a function to calculate age
def calculate_age():
    birth_input =entry.get() # input for DOB

    try:
        #storing birth date and todays date
        birth_date=datetime.strptime(birth_input, "%Y-%m-%d")
        today=datetime.today()

        #finding the difference between birth date and present date
        years= today.year - birth_date.year
        months=today.month - birth_date.month
        days= today.day - birth_date.day

        #if days become negative after difference then month will be previous and days added to 30 
        if days < 0:
            months -= 1
            days +=30
        #if months become negative after difference then year will be previous year and months added to 12 
        if months < 0:
            years -=1
            months +=12

        #to display result
        result_label.config(
            text=f"You are {years} years,{months} months, and {days} days old."
        )
        #to handle invalid date format
    except:
        result_label.config(text= " invalid date Format.Use YYYY-MM-DD")
        
#window create
window=Tk()
window.title("AGE CALCULATOR")
window.geometry("500x250")
window.configure(bg="#bbe8a1")

#heading label
heading=Label(window,text="AGE CALCULATOR",font=("Arial",15,"bold"),bg="#d1e1cf");
heading.pack(pady=10)

#label to display 
label=Label(window,text="Enter your date of birth(YYYY-MM-DD):",font=("arial",15),bg="#d1e1cf")
label.pack()

#taking input  from user
entry=Entry(window,font=("Arial",12),width=20)
entry.pack(pady=5)

#button to calculate the age
btn=Button(window,text="CALCULATE AGE",font=("Arial",15),bg="#a2d5ab",command=calculate_age)
btn.pack(pady=10)

#label to display result
result_label=Label(window,text="",font="Arial",bg="#e6f9d9")
result_label.pack(pady=10)

#runs the gui loop
window.mainloop()