# Saya Abighail Shafira Ihsani mengerjakan evaluasi TP3 dalam mata kuliah Desain dan Pemrograman Beriorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikan. Aamiin. */
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from Guest import Guest
from PIL import ImageTk, Image
import random
import sys

root = Tk()
root.geometry("900x700+0+0")
root.title("The Phoenix Hotel")
root.config(bg="cadet blue")
root.resizable(False, False)
root.iconbitmap('hotelku/building.ico')

bg_color = "cadet blue"
font_lbl = ("times new roman", 12, "bold")
font_input = ("times new roman", 12)

list_data = []
filename = ""
image = ""

#=========================================Guest Data==========================================
Frame1 = LabelFrame(root, padx=15, pady=15, text="Guest Data", bg=bg_color, relief=RIDGE)
Frame1.place(x=20, y=40, height="185", width="450")

#guest name
guest_name = StringVar()
lblName = Label(Frame1, text="Name", fg="black", bg=bg_color, font=font_lbl).grid(row=0, column=0, padx=15 ,pady=5, sticky="w")
entryName = Entry(Frame1, font=font_input, textvariable=guest_name ,bd=5, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10, sticky="w", ipadx=30)

#guest number
guest_number = StringVar()
lblNoTlp = Label(Frame1, text="Phone Number", fg="black", bg=bg_color, font=font_lbl).grid(row=1, column=0, padx=15 ,pady=5, sticky="w")
entryNoTlp = Entry(Frame1, font=font_input, textvariable=guest_number, bd=5, relief=SUNKEN).grid(row=1, column=1, pady=5, padx=10, sticky="w", ipadx=30)

#total guest
total_guest = StringVar()
lblJmlOrg = Label(Frame1, text="Total Guest", fg="black", bg=bg_color, font=font_lbl).grid(row=2, column=0, padx=15 ,pady=5, sticky="w")
entryJmlOrg = Entry(Frame1, font=font_input, textvariable=total_guest ,bd=5, relief=SUNKEN).grid(row=2, column=1, pady=5, padx=10, sticky="w", ipadx=30)

#=======================================Detail Room Data======================================
Frame2 = LabelFrame(root, bg=bg_color, padx=15, pady=15, relief=RIDGE, text="Detail Room")
Frame2.place(x=20, y=230, height="145", width="450")

#dropdown menu for selection room
lblJenisKamar = Label(Frame2, text="Room Type", fg="black", bg=bg_color, font=font_lbl).grid(row=0, column=0, padx=15 ,pady=5, sticky="w")
options = [
    "Standard",
    "Single",
    "Twin",
    "Connecting",
    "Superior",
    "Deluxe",
    "Junior Suite",
    "Suite",
    "Presidential"
]
room_type = StringVar()
room_type.set(options[0])
dropdown = OptionMenu(Frame2, room_type, *options)
dropdown.grid(row=0, column=1, pady=5, padx=10, sticky="w")

#room number
room_number = StringVar()
room_number.set(random.randint(1,500))
lblNoKamar = Label(Frame2, text="Room Number", fg="black", bg=bg_color, font=font_lbl).grid(row=1, column=0, padx=15 ,pady=5, sticky="w")
entryNoKamar = Entry(Frame2, font=font_input, textvariable=room_number ,bd=5, relief=SUNKEN, state=DISABLED).grid(row=1, column=1, pady=5, padx=10, sticky="w", ipadx=30)

#==============================Additional Facilities==============================
Frame3 = LabelFrame(root, bg=bg_color, padx=15, pady=15, relief=RIDGE, text="Additional Facilities")
Frame3.place(x=20, y=380, height="180", width="450")

#check box for additional facilities
lblDish = Label(Frame3, text="Dish", fg="black", bg=bg_color, font=font_lbl, width=4).grid(row=0, column=0,pady=5, padx=13,sticky="w")
additional_dish = ("Breakfast", "Lunch", "Dinner")
selected_dish = dict()
for i, ds in enumerate(additional_dish):
    selected_dish[ds] = BooleanVar()
    cb = Checkbutton(
        Frame3,
        text=ds,
        onvalue=True,
        offvalue=False,
        variable=selected_dish[ds]
    )
    cb.grid(row=0, column=i + 1, padx=5, sticky="e")

#radio button for extra bed facilities
lblExtraBed = Label(Frame3, text="Extra Bed", fg="black", bg=bg_color, font=font_lbl).grid(row=1, column=0, padx=15 ,pady=5, sticky="w")
additional_bed = StringVar()
Radiobutton(Frame3, text="Yes", variable=additional_bed, value="Yes").grid(row=1, column=1, sticky="w", padx=37)
Radiobutton(Frame3, text="No", variable=additional_bed, value="No").grid(row=1, column=2, sticky="w")
additional_bed.set("No")

#room price
room_price = StringVar()
room_price.set("0")
lblHarga = Label(Frame3, text="Price" ,fg="black", bg=bg_color, font=font_lbl).grid(row=2, column=0, padx=15 ,pady=5, sticky="w")
entryHarga = Entry(Frame3, font=font_input, textvariable=room_price ,bd=5, relief=SUNKEN, state=DISABLED).grid(row=2, column=1, columnspan=3, pady=5, padx=37, sticky="w")

#button total price
b_hitung = Button(Frame3, text="Total", command=lambda: total_price(), bd=5, relief=GROOVE)
b_hitung.grid(row=2, column=3, pady=5, padx=5, sticky="e")

#fungsi untuk menghitung total price
def total_price():
    if(room_type.get() == options[0]):
        room_price.set("350.000")
    elif(room_type.get() == options[1]):
        room_price.set("400.000")
    elif(room_type.get() == options[2]):
        room_price.set("500.000")
    elif(room_type.get() == options[3]):
        room_price.set("600.000")
    elif(room_type.get() == options[4]):
        room_price.set("900.000")
    elif(room_type.get() == options[5]):
        room_price.set("1.300.000")
    elif(room_type.get() == options[6]):
        room_price.set("2.000.000")
    elif(room_type.get() == options[7]):
        room_price.set("2.100.000")
    elif(room_type.get() == options[8]):
        room_price.set("2.200.000")
    else:
        room_price.set("0")

#======================================================================================
Frame4 = Frame(root, bg=bg_color, padx=15, pady=15)
Frame4.place(x=20, y=570, height="100", width="450")

#button reset form
b_reset = Button(Frame4, text="RESET", command=lambda: resetForm(), bd=7, relief=GROOVE)
b_reset.grid(row=0, pady=5, ipadx=185, sticky="w")

#fungsi untuk reset input pada form
def resetForm():
    guest_name.set("")
    guest_number.set("")
    total_guest.set("")
    room_type.set(options[0])
    room_number.set(random.randint(1,500))
    for i in selected_dish:
        selected_dish[i].set(False)
    additional_bed.set("No")
    room_price.set("0")
    filename = None
    image = None
    lbl_img.configure(image="")

#button submit
b_submit = Button(Frame4, text="SUBMIT", command=lambda: submit_window(), bd=7, relief=GROOVE)
b_submit.grid(row=1, pady=5, ipadx=180, sticky="w")

#fungsi ketika button submit di clicked
def submit_window():
    if((guest_name.get() == "") or (guest_number.get() == "") or (total_guest.get() == "") or (room_type.get() == "") or (not bool(selected_dish)) or (additional_bed.get() == "")):
        #show message
        messagebox.showwarning("Incomplete Data Input","Please enter all required fields")
        pass
    else:
        #insert new data
        list_data.append(Guest(guest_name.get(), guest_number.get(), total_guest.get(), room_type.get(), room_number.get(), ({i: selected_dish[i].get() for i in selected_dish}), additional_bed.get(), "Rp " + room_price.get(), filename, image))
        #reset form
        resetForm()
        #show message
        messagebox.showinfo("Data Added", "The data has been added")

#======================================================================================
title = Label(root, text="The Phoenix Hotel", font=("Arial", 30, "bold"), bg=bg_color)
title.place(x=530, y=60)

subtitle = Label(root, text="Sistem pendataan tamu hotel", font=("times new roman", 15), bg=bg_color)
subtitle.place(x=535, y=110)

Frame3 = Frame(root, bg=bg_color ,padx=15, pady=15)
Frame3.place(x=530, y=160, height="170", width="350")

#button see data
b_lihatData = Button(Frame3, text="SEE ALL SUBMISSIONS", command=lambda: AllData(), bd=7, relief=GROOVE, width=43)
b_lihatData.grid(row=0, column=0, pady=10)

#fungsi untuk menampilkan seluruh data
def AllData():
    root = Tk()
    root.title("The Phoenix Hotel")
    root.config(bg=bg_color)
    root.resizable(False, False)
    root.iconbitmap('hotelku/building.ico')
    
    mainTable = Frame(root, bg=bg_color, padx=20, pady=20)
    mainTable.pack(expand="yes")

    #column
    lb_hd_Name = Label(mainTable, text="Name", borderwidth=1, relief="solid")
    lb_hd_Name.grid(row=0, column=0, rowspan=2, sticky="news", ipadx=10)
    lb_hd_PhoneNumber = Label(mainTable, text="Phone Number",borderwidth=1, relief="solid")
    lb_hd_PhoneNumber.grid(row=0, column=1, rowspan=2, sticky="news", ipadx=10)
    lb_hd_TotalGuest = Label(mainTable, text="Total Guest", borderwidth=1, relief="solid")
    lb_hd_TotalGuest.grid(row=0, column=2, rowspan=2, sticky="news", ipadx=10)
    lb_hd_RoomType = Label(mainTable, text="Room Type", borderwidth=1, relief="solid")
    lb_hd_RoomType.grid(row=0, column=3, rowspan=2, sticky="news", ipadx=10)
    lb_hd_RoomNumber = Label(mainTable, text="Room Number", borderwidth=1, relief="solid")
    lb_hd_RoomNumber.grid(row=0, column=4, rowspan=2, sticky="news", ipadx=10)
    lb_hd_Dish = Label(mainTable, text="Additional Dish", borderwidth=1, relief="solid")
    lb_hd_Dish.grid(row=0, column=5, columnspan=len(additional_dish), sticky="news", ipadx=5)
    for j, ds in enumerate(additional_dish):
        lb_cb = Label(mainTable, text=ds, borderwidth=1, relief="solid")
        lb_cb.grid(row=1, column=5+j, sticky="news", ipadx=5)
    lb_hd_Bed = Label(mainTable, text="Extra Bed", borderwidth=1, relief="solid")
    lb_hd_Bed.grid(row=0, column=8, rowspan=2,sticky="news", ipadx=10)
    lb_hd_RoomPrice = Label(mainTable, text="Room Price", borderwidth=1, relief="solid")
    lb_hd_RoomPrice.grid(row=0, column=9, rowspan=2,sticky="news", ipadx=10)
    lb_hd_Image = Label(mainTable, text="Image", borderwidth=1, relief="solid")
    lb_hd_Image.grid(row=0, column=10, rowspan=2,sticky="news", ipadx=10)

    #body
    for i, lists_data in enumerate(list_data):
        lb_cb_Name = Label(mainTable, text=lists_data.guest_name, borderwidth=1, relief="solid")
        lb_cb_Name.grid(row=i+2, column=0, sticky="nesw", ipadx=5)
        lb_cb_PhoneNumber = Label(mainTable, text=lists_data.guest_number,borderwidth=1, relief="solid")
        lb_cb_PhoneNumber.grid(row=i+2, column=1, sticky="nesw", ipadx=5)
        lb_cb_TotalGuest = Label(mainTable, text=lists_data.total_guest,borderwidth=1, relief="solid")
        lb_cb_TotalGuest.grid(row=i+2, column=2, sticky="nesw", ipadx=5)
        lb_cb_RoomType = Label(mainTable, text=lists_data.room_type, borderwidth=1, relief="solid")
        lb_cb_RoomType.grid(row=i+2, column=3, sticky="nesw", ipadx=5)
        lb_cb_RoomNumber = Label(mainTable, text=lists_data.room_number, borderwidth=1, relief="solid")
        lb_cb_RoomNumber.grid(row=i+2, column=4, sticky="nesw", ipadx=5)
        for j, ds in enumerate(lists_data.additional_dish):
            lb_cb_Dish = Label(mainTable, text=str(lists_data.additional_dish[ds]), borderwidth=1, relief="solid")
            lb_cb_Dish.grid(row=i+2, column=5+j, sticky="nesw", ipadx=5)
        lb_cb_Bed = Label(mainTable, text=lists_data.additional_bed, borderwidth=1, relief="solid")
        lb_cb_Bed.grid(row=i+2, column=8, sticky="nesw", ipadx=5)
        lb_cb_RoomPrice = Label(mainTable, text=lists_data.room_price, borderwidth=1, relief="solid")
        lb_cb_RoomPrice.grid(row=i+2, column=9, sticky="nesw", ipadx=5)
        lb_cb_Image = Label(mainTable, image=lists_data.image, borderwidth=1, relief="solid")
        lb_cb_Image.grid(row=i+2, column=10, sticky="nesw")
        b_cb_Image = Button(lb_cb_Image, text="Open", height=1, width=5, padx=6, command=lambda: viewImage(), bd=5, relief=GROOVE).grid(row=i+2, column=10)
    
    #button back
    b_back = Button(mainTable, text="Back", command=root.destroy, relief=GROOVE, bd=5)
    b_back.grid(row=3+len(list_data), column=0, columnspan=8+len(additional_dish), pady=15)

#======================================================================================
#button clear data
b_hapusData = Button(Frame3, text="CLEAR SUBMISSIONS", command=lambda: clearData(), bd=7, relief=GROOVE, width=43)
b_hapusData.grid(row=1, column=0, pady=10)

#fungsi untuk menghapus semua data pada program
def clearData():
    iClear = messagebox.askyesno("The Phoenix Hotel" ,"Are you sure you want to delete all the data?" + "\n\n" + "WARNING: This action will delete all data in the table")
    if iClear > 0:
        #clear the data list
        list_data.clear()
        messagebox.showinfo("The Phoenix Hotel","All the data has been successfully deleted")
        return

#button about
b_about = Button(Frame3, text="ABOUT", command=lambda: about_window(), bd=7, relief=GROOVE, width=43)
b_about.grid(row=3, column=0, pady=10)

#fungsi untuk menampilkan deskripsi dari program
def about_window():
    top = Toplevel()
    top.title("About")
    top.iconbitmap('hotelku/building.ico')
    top.geometry("743x330+0+0")
    top.config(bg="cadet blue")
    top.resizable(False, False)

    d_frame = LabelFrame(top, padx=15, pady=15, bg=bg_color, relief=GROOVE, bd=5)
    d_frame.place(x=20, y=80, height="180", width="700")

    title = Label(top, text="Sistem Pendataan Tamu The Phoenix Hotel", font=("Arial", 20, "bold"), bg=bg_color)
    title.place(x=20, y=30)
      
    d_about = Label(d_frame, font=("times new roman", 13), text="Sistem pendataan tamu the phoenix hotel ini merupakan sistem untuk input data-data pada tamu hotel sehingga dapat membantu dan memudahkan pegawai khususnya bagian front office dalam pelayanan kepada tamu hotel, serta dapat mempermudah dalam pendataan administrasi terkait kegiatan reservasi kamar pada the phoenix hotel.", bg=bg_color, justify=LEFT, wraplength=650).grid(row=0, column=0, sticky="w")
    d_about = Label(d_frame, font=("times new roman", 13), text="\n\n" + "By Abighail Shafira Ihsani", anchor="w", bg=bg_color).grid(row=1, column=0, sticky="w")

    b_back = Button(top, text="Back", command=top.destroy, relief=GROOVE, bd=5)
    b_back.place(x=20,y=270)

#=====================================Image Viewer=====================================
Frame6 = LabelFrame(root, bg=bg_color, padx=15, pady=15, relief=RIDGE, text="Open Image")
Frame6.place(x=530, y=380, height="180", width="350")

frame_img = Frame(Frame6, height=115, width=230)
frame_img.pack(side="left", padx=10)
frame_img.pack_propagate(0)

lbl_img = Label(frame_img)
lbl_img.pack(fill="both", expand="yes")

b_openImg = Button(Frame6, text="Browse..", relief=GROOVE, bd=5, command=lambda:getImage())
b_openImg.place(x=250, y=7)

#fungsi untuk mengambil gambar
def getImage():
    global filename
    filename = filedialog.askopenfilename(initialdir="~", title="Select a Photo", filetypes=(("Images", "*.jpg* *.jpeg* *.png*"), ("all files", "*.*")))

    img = Image.open(filename)
    render = ImageTk.PhotoImage(img.resize((400, 200), Image.ANTIALIAS))
    lbl_img.configure(image=render)
    lbl_img.image = render
    image = ImageTk.PhotoImage(img)
    img.close()

#fungsi untuk menampilkan gambar
def viewImage():
    top = Toplevel()
    top.title("Image Viewer")
    top.iconbitmap('hotelku/building.ico')

    canvas = Canvas(top, width = 300, height = 300)  
    canvas.grid(columnspan=3)
    if(filename != "") :
        img = Image.open(filename)
        img = ImageTk.PhotoImage(img.resize((400, 200), Image.ANTIALIAS))
        lbl_image = Label(canvas, image=img)
        lbl_image.image = img
        lbl_image.grid(column=1, row=0)
#======================================================================================
Frame5 = Frame(root, bg=bg_color, padx=15, pady=15)
Frame5.place(x=530, y=619, height="100", width="350")

#button exit
b_exit = Button(Frame5, text="EXIT", command=lambda: exit_window(), bd=7, relief=GROOVE, width=43)
b_exit.grid(row=0, column=0, sticky="w")

#fungsi untuk keluar dari program
def exit_window():
    iExit = messagebox.askyesno("The Phoenix Hotel" ,"Do you want to exit?")
    if iExit > 0:
        root.destroy()
        return

root.mainloop()