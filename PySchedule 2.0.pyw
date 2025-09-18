from datetime import datetime as dtime
import tkinter as tk


def apply_icon(w):
    try:
        icon = tk.PhotoImage(data=icondata)
        w.iconphoto(True, icon)
    except Exception as e:
        print("Could not load icon due to:\n  ", e)


icondata = '''
iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAQAAADZc7J/AAAAIGNIUk0AAHomAACAhAAA+gAAAIDo
AAB1MAAA6mAAADqYAAAXcJy6UTwAAAACYktHRAD/h4/MvwAAAAd0SU1FB+gECxEcLjMHi1sAAAOD
SURBVEjHtZVdaFtlGMd/SSfKhlBWsy3R2VRtp2wsmTO9G2YM7IUFz4XTMb1oCxPUbQ1sF6IXaWCC
+HEj1FGnJiCCbsjKBtLtYmsZ2AlV06LYerEeYrd+bIGk9GNLzvs+XuRNemITFcT3wOE95/D7Px/n
eZ4X/uPy1H5thbEI0QiCRufUuB68nP6XAq/HZnsJbmEnPgRBmGOCWbStEiOpfxCwoiQJ7qeTZkAA
MfcbnOcSytbdo8N1Baw+4u304EPIMskdAITNtNGEME8/11CJsb6aAlaSrh46ESa5wJT5LGgUmlZe
4EngHB+jU+nuMtXgsh47RgfLDPAtWcBTwRWKBa4yzW5CbGMk7PMsDFcJWFGSPXQwTX/FNi68dGX4
kSeIsInvo00jWRvAaxxIttPJMin+cOFu2MHB4Xc+YomX2IdOlkAvgBUj2IPwxV9w7cIVRVZZ4Rfe
RYihgi1dax707sfHJD/XxYsss8gqPk4wzE/4eR4VNwJWmGAnwgWDb+cQ91fhKyxyF8VrfM0mNJ8i
HEYFA+GSB9YWmskyZaxbPMcp9pi4C+RZQbGHizzLcd5GMcYt2vCjrZJAaCcwWXF+gCEe4gQneYAC
eYps5X0+5DQv8oMJbQzYiwrBBqCxVHnl2JdIcZ03aOcM35FHOMJXvEPelJRCcxPBj240AmLqXqPR
OGgmOMJBXuUgMMXL/GbA8l2XurSURGFjBS/9MAdFgdN8A8DVdbgyDaaADaBzS0hV1TkollEMoFjk
yyp8zQNBlwXmgM0u2GGVAoo8H7gg9y4AZNA58IIan0Boc+FFVmtA7l0EYRQ9Dl7Qg7PcoIlWgzvc
rdRhbfwZAvxKBj0IXric1vZ5BMs0TJF765JWvTuK8DnaLqRNL6jEJeZ5iqcpUuSesa3r+HGACDOc
RRKVZhpJKbsfeJPtFCnWtFt+3sF7QBxtOynXPNDd1zjHRnp5FKem22v4g3zGELq7aiLN2H7P9eg2
IkSxseuk7wCf8DBneQudkHUDnnByt5yRvOTkihySx6VFmuURCchW8UmTdMhFmZM5OSUN4knWGeu7
+lR8HzH8CLcY46ap+QARAggzxBlCJ6SPemtHtHX6MTkmo5KVrNyR23JbFmRB5uWKvCL3ScO0J/q3
JxNAS5eKq6CfvfhNzWcYJYO2JeGsi7zO4RoIa0uFdKNJYE6P68FCmv9j/QnF7l1pUPLv7AAAACV0
RVh0ZGF0ZTpjcmVhdGUAMjAyNC0wNC0xMVQxNzoyODo0NiswMDowMNzGhxkAAAAldEVYdGRhdGU6
bW9kaWZ5ADIwMjQtMDQtMTFUMTc6Mjg6NDYrMDA6MDCtmz+lAAAAKHRFWHRkYXRlOnRpbWVzdGFt
cAAyMDI0LTA0LTExVDE3OjI4OjQ2KzAwOjAw+o4eegAAAABJRU5ErkJggg==
'''
weekday = dtime.weekday(dtime.today())
if weekday == 0:
    weekday = "Mon"
elif weekday == 1:
    weekday = "Tue"
elif weekday == 2:
    weekday = "Wed"
elif weekday == 3:
    weekday = "Thu"
elif weekday == 4:
    weekday = "Fri"
elif weekday == 5:
    weekday = "Sat"
else:
    weekday = "Sun"
if weekday == "Wed":
    # Setting variables up
    currentTime = -1
    currentHour = -1
    currentMin = -1
    currentMinUnderTen = -1
    minFormTime = -1
    currentDate = str(
        str(dtime.today().month) + "/" + str(dtime.today().day) + "/" + str(dtime.today().year)[slice(2, 4)])

    # Setting tkinter up
    ##tk window
    root = tk.Tk()
    root.geometry("150x100")
    root.title("School Schedule")
    root.attributes('-topmost', True)
    apply_icon(root)
    ##widgets
    dateLabel = tk.Label(text="Today is " + str(weekday) + ", " + currentDate + ".")
    time = tk.Label(text=str("The time is: " + str(currentHour) + ":" + str(currentMin)))
    schoolPeriod = tk.Label(text="It is __st/nd/th period.")
    timeLeftPeriod = tk.Label(text="There are __ minute(s) left.")


    # Functions
    def get_time():
        global currentTime, currentHour, currentMin, minFormTime
        currentTime = dtime.now()
        currentHour = currentTime.hour
        currentMin = currentTime.minute
        minFormTime = str(int(currentHour) * 60 + int(currentMin))
        print(str(currentHour) + ":" + str(currentMin))
        print(minFormTime)


    def get_period():
        if int(minFormTime) < 440:
            schoolPeriod.config(text="School hasn't started yet.")
            timeLeftPeriod.config(text=str("School starts in " + str(440 - int(minFormTime)) + " minutes."))
        elif int(minFormTime) <= 484:
            schoolPeriod.config(text="It is First Period.")
            timeLeftPeriod.config(text=str("Class ends in " + str(484 - int(minFormTime)) + " minutes."))
        elif int(minFormTime) <= 530:
            schoolPeriod.config(text="It is Second Period.")
            timeLeftPeriod.config(text=str("Class ends in " + str(530 - int(minFormTime)) + " minutes."))
        elif int(minFormTime) <= 576:
            schoolPeriod.config(text="It is Third Period.")
            timeLeftPeriod.config(text=str("Class ends in " + str(576 - int(minFormTime)) + " minutes."))
        elif int(minFormTime) <= 622:
            schoolPeriod.config(text="It is Fourth Period.")
            timeLeftPeriod.config(text=str("Class ends in " + str(622 - int(minFormTime)) + " minutes."))
        elif int(minFormTime) <= 652:
            schoolPeriod.config(text="It is A Lunch.")
            timeLeftPeriod.config(text=str("Lunch ends in " + str(652 - int(minFormTime)) + " minutes."))
        elif int(minFormTime) <= 698:
            schoolPeriod.config(text="It is Fifth Period.")
            timeLeftPeriod.config(text=str("Class ends in " + str(698 - int(minFormTime)) + " minutes."))
        elif int(minFormTime) <= 744:
            schoolPeriod.config(text="It is Sixth Period.")
            timeLeftPeriod.config(text=str("Class ends in " + str(744 - int(minFormTime)) + " minutes."))
        elif int(minFormTime) <= 790:
            schoolPeriod.config(text="It is Seventh Period.")
            timeLeftPeriod.config(text=str("School ends in " + str(790 - int(minFormTime)) + " minutes."))
        else:
            schoolPeriod.config(text="School is out.")


    def update_time():
        global currentTime, currentHour, currentMin, minFormTime, currentMinUnderTen
        currentTime = dtime.now()
        currentHour = currentTime.hour
        currentMin = currentTime.minute
        minFormTime = str(int(currentHour) * 60 + int(currentMin))
        if currentMin < 10:
            currentMinUnderTen = str("0" + str(currentMin))
        else:
            currentMinUnderTen = currentMin
        print("Time Updated")
        get_period()
        if currentHour > 12:
            time.config(text=str("It is " + str(int(currentHour) - 12) + ":" + str(currentMinUnderTen) + " P.M."))
        else:
            time.config(text=str("It is " + str(currentHour) + ":" + str(currentMinUnderTen) + " A.M."))
        root.after(1000, update_time)


    # Calling functions
    get_time()
    update_time()
    get_period()
    # Widget packing
    dateLabel.pack()
    time.pack()
    schoolPeriod.pack()
    timeLeftPeriod.pack()
    root.mainloop()
else:
    # Setting variables up
    currentTime = -1
    currentHour = -1
    currentMin = -1
    currentMinUnderTen = -1
    minFormTime = -1
    currentDate = str(
        str(dtime.today().month) + "/" + str(dtime.today().day) + "/" + str(dtime.today().year)[slice(2, 4)])
    # Setting tkinter up
    ##tk window
    root = tk.Tk()
    root.geometry("150x100")
    root.title("School Schedule")
    root.attributes('-topmost', True)
    apply_icon(root)
    ##widgets
    dateLabel = tk.Label(text="Today is " + str(weekday) + ", " + currentDate + ".")
    time = tk.Label(text=str("The time is: " + str(currentHour) + ":" + str(currentMin)))
    schoolPeriod = tk.Label(text="It is __st/nd/th period.")
    timeLeftPeriod = tk.Label(text="There are __ minute(s) left.")


    # Functions

    def get_time():
        global currentTime, currentHour, currentMin, minFormTime
        currentTime = dtime.now()
        currentHour = currentTime.hour
        currentMin = currentTime.minute
        minFormTime = str(int(currentHour) * 60 + int(currentMin))
        print(str(currentHour) + ":" + str(currentMin))
        print(minFormTime)


    def get_period():
        if int(minFormTime) < 440:
            schoolPeriod.config(text="School hasn't started yet.")
            timeLeftPeriod.config(text=str("School starts in " + str(440 - int(minFormTime)) + " minutes."))
        elif int(minFormTime) <= 494:
            schoolPeriod.config(text="It is First Period.")
            timeLeftPeriod.config(text=str("Class ends in " + str(494 - int(minFormTime)) + " minutes."))
        elif int(minFormTime) <= 550:
            schoolPeriod.config(text="It is Second Period.")
            timeLeftPeriod.config(text=str("Class ends in " + str(550 - int(minFormTime)) + " minutes."))
        elif int(minFormTime) <= 606:
            schoolPeriod.config(text="It is Third Period.")
            timeLeftPeriod.config(text=str("Class ends in " + str(606 - int(minFormTime)) + " minutes."))
        elif int(minFormTime) <= 662:
            schoolPeriod.config(text="It is Fourth Period.")
            timeLeftPeriod.config(text=str("Class ends in " + str(662 - int(minFormTime)) + " minutes."))
        elif int(minFormTime) <= 692:
            schoolPeriod.config(text="It is A Lunch.")
            timeLeftPeriod.config(text=str("Lunch ends in " + str(692 - int(minFormTime)) + " minutes."))
        elif int(minFormTime) <= 748:
            schoolPeriod.config(text="It is Fifth Period.")
            timeLeftPeriod.config(text=str("Class ends in " + str(748 - int(minFormTime)) + " minutes."))
        elif int(minFormTime) <= 804:
            schoolPeriod.config(text="It is Sixth Period.")
            timeLeftPeriod.config(text=str("Class ends in " + str(804 - int(minFormTime)) + " minutes."))
        elif int(minFormTime) <= 860:
            schoolPeriod.config(text="It is Seventh Period.")
            timeLeftPeriod.config(text=str("School ends in " + str(860 - int(minFormTime)) + " minutes."))
        else:
            schoolPeriod.config(text="School is out.")


    def update_time():
        global currentTime, currentHour, currentMin, minFormTime, currentMinUnderTen
        currentTime = dtime.now()
        currentHour = currentTime.hour
        currentMin = currentTime.minute
        minFormTime = str(int(currentHour) * 60 + int(currentMin))
        if currentMin < 10:
            currentMinUnderTen = str("0" + str(currentMin))
        else:
            currentMinUnderTen = currentMin
        print("Time Updated")
        get_period()
        if currentHour > 12:
            time.config(text=str("It is " + str(int(currentHour) - 12) + ":" + str(currentMinUnderTen) + " P.M."))
        else:
            time.config(text=str("It is " + str(currentHour) + ":" + str(currentMinUnderTen) + " A.M."))
        root.after(1000, update_time)


    # Calling functions
    get_time()
    update_time()
    get_period()
    # Widget packing
    dateLabel.pack()
    time.pack()
    schoolPeriod.pack()
    timeLeftPeriod.pack()
    root.mainloop()
