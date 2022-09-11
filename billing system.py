from tkinter import *
import math, random, os
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = '#993366'
        title = Label(self.root, text="BILL PAYMENT  ", bd=15, bg=bg_color, fg="white",
                      font=("times new roman", 30, "bold"), pady=2).pack(fill=X)
        # ================Variables===========================
        # ================Cosemetics==========================

        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gel = IntVar()
        self.lotion = IntVar()

        # ================Grocery==========================

        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        # ================Cold Drinks==========================

        self.maaza = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumbsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        # ================Total Product Price & Tax variables==========================

        self.cosemtic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosemetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        # ================Cutomers==================================

        self.c_name = StringVar()
        self.c_phone = StringVar()

        self.bill_no = StringVar()
        x = random.randint(1000, 9999)

        self.bill_no.set(str(x))

        self.search_bill = StringVar()

        # ============================================================
        self.paytm = IntVar()
        self.cash = IntVar()
        self.cre_deb = IntVar()

        # =============Customer Details Frame
        F1 = LabelFrame(self.root, bd=8, text="Customer Details", font=("times new roman", 15, "bold"), fg="gold",
                        bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="White", font=("times new roman", 18, "bold")).grid(
            row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                             column=1,
                                                                                                             pady=5,
                                                                                                             padx=10)

        cphn_lbl = Label(F1, text="Contact No", bg=bg_color, fg="White", font=("times new roman", 18, "bold")).grid(
            row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                             column=3,
                                                                                                             pady=5,
                                                                                                             padx=10)

        c_bill_lbl = Label(F1, text="Item Search", bg=bg_color, fg="White", font=("times new roman", 18, "bold")).grid(
            row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font="arial 12").grid(row=0,
                                                                                                           column=6,
                                                                                                           padx=6,
                                                                                                           pady=10)

        # ===================Cosemetics Frame==========

        F2 = LabelFrame(self.root, bd=8, text="Cosemetics", font=("times new roman", 15, "bold"), fg="gold",
                        bg=bg_color)
        F2.place(x=5, y=180, width=320, height=380)

        bath_lbl = Label(F2, text="Bath Soap", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(F2, width=5, textvariable=self.soap, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        Face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Face_cream_txt = Entry(F2, width=5, textvariable=self.face_cream, font=("times new roman", 16, "bold"), bd=5,
                               relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        Fcae_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Face_w_txt = Entry(F2, width=5, textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        Hair_s_lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Hair_s_txt = Entry(F2, width=5, textvariable=self.spray, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        Hair_g_lbl = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Hair_g_txt = Entry(F2, width=5, textvariable=self.gel, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        Body_lbl = Label(F2, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_color,
                         fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        Body_txt = Entry(F2, width=5, textvariable=self.lotion, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ===================Grocery Frame==========

        F3 = LabelFrame(self.root, bd=8, text="Groceries", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F3.place(x=335, y=180, width=315, height=380)



        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        g1_txt = Entry(F3, width=5, textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        g2_lbl = Label(F3, text="Food Oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=5, textvariable=self.food_oil, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        g3_lbl = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        g3_txt = Entry(F3, width=5, textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        g4_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        g4_txt = Entry(F3, width=5, textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        g5_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        g5_txt = Entry(F3, width=5, textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        g6_lbl = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        g6_txt = Entry(F3, width=5, textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ===================Cold Drink Frame==========

        F4 = LabelFrame(self.root, bd=8, text="Cold Drinks", font=("times new roman", 15, "bold"), fg="gold",
                        bg=bg_color)
        F4.place(x=660, y=180, width=315, height=380)
        c1_lbl = Label(F4, text="Mazza", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        c1_txt = Entry(F4, width=5, textvariable=self.maaza, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        c2_lbl = Label(F4, text="Coca Cola", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=5, textvariable=self.cock, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        c3_lbl = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=5, textvariable=self.frooti, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        c4_lbl = Label(F4, text="Thumbs Up", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        c4_txt = Entry(F4, width=5, textvariable=self.thumbsup, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        c5_lbl = Label(F4, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        c5_txt = Entry(F4, width=5, textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        c6_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        c6_txt = Entry(F4, width=5, textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ===============Bill Area=============
        F5 = Frame(self.root, bd=8, relief=GROOVE)
        F5.place(x=990, y=179, width=370, height=380)

        bill_title = Label(F5, text="BILL AREA", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ==============Button Frame=============

        F6 = LabelFrame(self.root, bd=8, text="BILL MENU", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)
        m1_lbl = Label(F6, text="Total Cosemetics Price", bg=bg_color, fg="white",
                       font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.cosemtic_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", bg=bg_color, fg="white",
                       font=("times new roman", 15, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drink Price", bg=bg_color, fg="white",
                       font=("times new roman", 15, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drink_price, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl = Label(F6, text="Cosemetics Tax", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18, textvariable=self.cosemetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="Grocery Tax", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="Cold Drink Tax", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18, textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=2, column=3, padx=10, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=740, width=590, height=102)

        total_btn = Button(btn_F, text="Total", command=self.total, bg="cadetblue", fg="white", pady=15, bd=4, width=6,
                           font="arial 14 bold").grid(row=0, column=0, padx=4, pady=5)
        Payment_btn = Button(btn_F, text="Payment Mode", command=self.paym, bg="cadetblue", fg="white", pady=15, bd=4,
                             width=13, font="arial 14 bold").grid(row=0, column=1, padx=4, pady=4)
        GBill_btn = Button(btn_F, text="Generate Bill", command=self.bill_area, bg="cadetblue", fg="white", pady=15,
                           bd=4, width=10, font="arial 14 bold").grid(row=0, column=2, padx=4, pady=5)
        Clear_btn = Button(btn_F, text="Clear", command=self.clear_data, bg="cadetblue", fg="white", pady=15, bd=4,
                           width=6, font="arial 14 bold").grid(row=0, column=3, padx=4, pady=5)
        Exit_btn = Button(btn_F, text="Exit", command=self.Exit_app, bg="cadetblue", fg="white", pady=15, bd=4,
                          width=6, font="arial 14 bold").grid(row=0, column=4, padx=4, pady=5)
        self.welcome_bill()

    # =============functions for working=============================
    def total(self):
        self.c_s_p = self.soap.get() * 40
        self.c_fc_p = self.face_cream.get() * 120
        self.c_fw_p = self.face_wash.get() * 60
        self.c_hs_p = self.spray.get() * 180
        self.c_hg_p = self.gel.get() * 140
        self.c_bl_p = self.lotion.get() * 180
        self.total_cosemetic_price = float(
            self.c_s_p +
            self.c_fc_p +
            self.c_fw_p +
            self.c_hs_p +
            self.c_hg_p +
            self.c_bl_p
        )
        self.cosemtic_price.set("Rs. " + str(self.total_cosemetic_price))
        self.c_tax = round((self.total_cosemetic_price * 0.05), 2)
        self.cosemetic_tax.set("Rs. " + str(self.c_tax))

        self.g_r_p = self.rice.get() * 40
        self.g_f_p = self.food_oil.get() * 120
        self.g_d_p = self.daal.get() * 60
        self.g_w_p = self.wheat.get() * 180
        self.g_s_p = self.sugar.get() * 140
        self.g_t_p = self.tea.get() * 180

        self.total_grocery_price = float(
            self.g_r_p +
            self.g_f_p +
            self.g_d_p +
            self.g_w_p +
            self.g_s_p +
            self.g_t_p
        )
        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price * 0.1), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.d_m_p = self.maaza.get() * 60
        self.d_c_p = self.cock.get() * 60
        self.d_f_p = self.frooti.get() * 50
        self.d_t_p = self.thumbsup.get() * 45
        self.d_l_p = self.limca.get() * 40
        self.d_s_p = self.sprite.get() * 60
        self.total_drinks_price = float(
            self.d_m_p +
            self.d_c_p +
            self.d_f_p +
            self.d_t_p +
            self.d_l_p +
            self.d_s_p
        )
        self.cold_drink_price.set("Rs. " + str(self.total_drinks_price))
        self.d_tax = round((self.total_drinks_price * 0.05), 2)
        self.cold_drink_tax.set("Rs. " + str(self.d_tax))

        self.Total_bill = float(
            self.total_cosemetic_price +
            self.total_grocery_price +
            self.total_drinks_price +
            self.c_tax +
            self.g_tax +
            self.d_tax
        )

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t Welcome to Grocery Shop \n")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n ========================================")
        self.txtarea.insert(END, f"\n Products\t\tQTY\tPrice")
        self.txtarea.insert(END, f"\n ========================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer Details are must")
        elif self.cosemtic_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drink_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
            # ========Cosemetics==========
            if self.soap.get() != 0:
                self.txtarea.insert(END, f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")

            if self.face_cream.get() != 0:
                self.txtarea.insert(END, f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")

            if self.face_wash.get() != 0:
                self.txtarea.insert(END, f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")

            if self.spray.get() != 0:
                self.txtarea.insert(END, f"\n Hair Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")

            if self.gel.get() != 0:
                self.txtarea.insert(END, f"\n Hair Gel\t\t{self.gel.get()}\t\t{self.c_hg_p}")

            if self.lotion.get() != 0:
                self.txtarea.insert(END, f"\n Body Lotion\t\t{self.lotion.get()}\t\t{self.c_bl_p}")

            # ========Grocery==========
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")

            if self.food_oil.get() != 0:
                self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")

            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")

            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")

            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")

            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")

            # ========Cold Drinks==========
            if self.maaza.get() != 0:
                self.txtarea.insert(END, f"\n Maaza\t\t{self.maaza.get()}\t\t{self.d_m_p}")

            if self.cock.get() != 0:
                self.txtarea.insert(END, f"\n Coca Cola\t\t{self.cock.get()}\t\t{self.d_c_p}")

            if self.frooti.get() != 0:
                self.txtarea.insert(END, f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")

            if self.thumbsup.get() != 0:
                self.txtarea.insert(END, f"\n Thumbs Up\t\t{self.thumbsup.get()}\t\t{self.d_t_p}")

            if self.limca.get() != 0:
                self.txtarea.insert(END, f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")

            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")

            self.txtarea.insert(END, f"\n ------------------------------------")
            if self.cosemetic_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cosemetic Tax\t\t{self.cosemetic_tax.get()}")
            if self.grocery_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Grocery Tax\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cold Drink Tax\t\t{self.cold_drink_tax.get()}")

            if self.paytm.get() == 1:
                self.txtarea.insert(END, "\n")
                self.txtarea.insert(END, "\n PAYMENT - PayTM")
                self.txtarea.insert(END, "\n")
            if self.cash.get() == 1:
                self.txtarea.insert(END, "\n")
                self.txtarea.insert(END, "\n PAYMENT - Cash")
                self.txtarea.insert(END, "\n")
            if self.cre_deb.get() == 1:
                self.txtarea.insert(END, "\n")
                self.txtarea.insert(END, "\n PAYMENT - credit/debit card")
                self.txtarea.insert(END, "\n")

            self.txtarea.insert(END, f"\n Total Bill : \t\t Rs. {self.Total_bill}")
            self.txtarea.insert(END, f"\n ------------------------------------")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Saving Bill.....", "Do You Want Save your Bill")

        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("Bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saving.....",
                                f"{self.c_name.get()} Your Bill No : {self.bill_no.get()}  Successfully Saved please see the Bills folder on bill directory to see your Bills")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"Bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill Number ..Please Enter Valid Bill Number")

    def clear_data(self):
        op = messagebox.askyesno("Clearing...", "Do You Really Want to Clear All data")
        if op > 0:
            # ================Cosemetics==========================

            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gel.set(0)
            self.lotion.set(0)

            # ================Grocery==========================

            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            # ================Cold Drinks==========================

            self.maaza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            # ================Total Product Price & Tax variables==========================

            self.cosemtic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosemetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            # ================Cutomers==================================

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)

            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op = messagebox.askyesno("Exit", "Do You Really Want to Exit")
        if op > 0:
            self.root.destroy()

    def paym(self):
        p = pay(self)


def toggle(var):
    var.set(not var.get())


class pay():
    def __init__(self, parentSelf):
        self.root = Tk()
        self.root.geometry("500x300")
        self.parent = parentSelf
        self.root.title("Mode of payment")

        self.paytm = IntVar()
        self.cash = IntVar()
        self.cre_deb = IntVar()
        self.mop = Label(self.root, text="Select the mode of payment", font=('times new roman', 18, 'bold'), fg='brown',
                         bg='light green')
        self.paytm_button = Checkbutton(self.root, text="PayTM", offvalue=0, onvalue=1, font=('Verdana', 15, 'bold'),
                                        fg='blue', bg='light green', command=lambda: toggle(self.paytm))
        self.cash_button = Checkbutton(self.root, text="Cash", offvalue=0, onvalue=1, font=('Verdana', 15, 'bold'),
                                       fg='blue', bg='light green',  command=lambda: toggle(self.cash))
        self.cre_deb_button = Checkbutton(self.root, text="Credit/Debit card", offvalue=0, onvalue=1,
                                          font=('Verdana', 15, 'bold'), fg='blue', bg='light green',
                                          command=lambda: toggle(self.cre_deb))
        self.done = Button(self.root, text="Done", command=self.close, font=('times new roman', 15, 'bold'),
                           bg='light blue', fg='white', relief=GROOVE, width=6)

        self.create_elements()
        self.root.mainloop()

    def create_elements(self):
        self.mop.place(x=50, y=50)
        self.paytm_button.place(x=50, y=80)
        self.cash_button.place(x=50, y=110)
        self.cre_deb_button.place(x=50, y=140)
        self.done.place(x=100, y=190)

    def close(self):
        self.parent.paytm = self.paytm
        self.parent.cash = self.cash
        self.parent.cre_deb = self.cre_deb
        self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()
