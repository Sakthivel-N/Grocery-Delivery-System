import mysql.connector
import time

mydb = mysql.connector.connect(host="localhost", user="root", password="123456", database="food_delivery")
mycursor = mydb.cursor()

class Reg_user:
    def newuser(self):
        username = input("Enter your name :")
        password = input("Enter your password :")
        mail = input("Enter your mail :")
        phone = input("Enter your Phone number :")
        address = input("Enter your address :")
        activecount = wallet = '0'
        mycursor.execute(
            "insert into userdetails(userid,username,password,mail,phone,address,activecount,wallet) values(NULL,%s,%s,%s,%s,%s,%s,%s)",
            (username, password, mail, phone, address, activecount, wallet,))
        mydb.commit()
        print("Registration success !!")
class Admin_view:
    def admin(self):
        def show_fb():
            mycursor.execute("select username,feedback from feedbackdetails")
            d = mycursor.fetchall()
            if d:
                print("Feedbacks are:-")
                print()
                for i in range(len(d)):
                    print("User is : %s" % d[i][0])
                    print("Feedback is : %s" % d[i][1])
                    print()
            else:
                print("No Feedback here")
        def give_offer(self):
            mycursor.execute("select fooditems,offers from stock where  quantity > 70 ")
            d = mycursor.fetchall()
            if d:

                off_rate = int(input("how much give you offer :  "))
                for i in range(len(d)):
                    fooditems = d[i][0]
                    mycursor.execute("update stock SET offers =%s WHERE fooditems like %s", (off_rate, fooditems,))
                    mydb.commit()
            print("offers updated success")
        def display_orders():
            mycursor.execute("select * from orderdetails")
            data = mycursor.fetchall()
            if data:
                for row in range(len(data)):
                    print("Name :%s" % data[row][1], end="       ")
                    print("Foodname :%s" % data[row][2], end="        ")
                    print("Cost:%s" % data[row][3])

            else:
                print("No Records found!")
        def ord_failed():
            mycursor.execute("select username,totalcost from orderdetails where delivery_status like 'Not Delivered'")
            d = mycursor.fetchall()
            if d:
                print()
                print("Give refund for failed orders")
                print()
                for row in range(len(d)):
                    username = d[row][0]
                    totalcost = float(d[row][1])

                    mycursor.execute("select wallet from userdetails where username like %s", (username,))
                    d1 = mycursor.fetchone()
                    wallet = totalcost + float(d1[0])
                    mycursor.execute("update userdetails SET wallet=%s WHERE username like %s",
                                     (str(wallet), username,))
                    mydb.commit()
                    print(
                        "The Refund Rs.{} given to {} and Now he have Rs.{} in wallet".format(totalcost, username,
                                                                                              wallet))
                mycursor.execute("DELETE FROM orderdetails WHERE delivery_status like 'Not Delivered'")
                mydb.commit()
            else:
                print()
                print("There is Nothing Failed orders")
                print()
        def display_food():
            mycursor.execute("select fooditems,price from stock")
            data = mycursor.fetchall()
            for row in range(len(data)):
                print("Foodname :%s" % data[row][0], end=" ")
                print("Cost:%s" % data[row][1])
                print()
        def display_all():
            mycursor.execute("select * from userdetails")
            data = mycursor.fetchall()
            for row in range(len(data)):
                print("User_Id :%s" % data[row][0])
                print("Name:%s" % data[row][1])
                print("Password :%s" % data[row][2])
                print("Mail :%s" % data[row][3])
                print("Phone :%s" % data[row][4])
                print("Address :%s" % data[row][5])
                print("Wallet : Rs. :%s" % data[row][7])
                print("Activeuserlevel :%s" % data[row][6])
                print()
            return 1
        def display_user(username):
            mycursor.execute("select * from userdetails where username like %s", (username,))
            data = mycursor.fetchall()
            print("User_Id :%s" % data[0][0])
            print("Name:%s" % data[0][1])
            for row in range(len(data)):
                print("Password :%s" % data[row][2])
                print("Mail :%s" % data[row][3])
                print("Phone :%s" % data[row][4])
                print("Address :%s" % data[row][5])
                print("Activeuserlevel :%s" % data[row][6])
                print()
            return 1
        print(
            "1.Display the particular user details" + '\n' + "2.Display all the records" + '\n' + "3.Display food table" + '\n' + "4.Display order details" + '\n' + "5.Check Failed orders for refund" + '\n' + "6.Give offers for nonrated items" + '\n' + "7.Show Users Feedback")
        print("Enter your option :")
        option = int(input())
        if option == 1:
            username = input("Enter the username: ")

            display_user(username)
        elif option == 2:

            display_all()
        elif option == 3:

            display_food()
        elif option == 4:

            display_orders()
        elif option == 5:
            print("check refund for failed orders")

            ord_failed()
        elif option == 6:
            print("The offers allocated for nonrated items")

            give_offer()
        elif option == 7:

            show_fb()
            print()
        else:
            print("Invalid option Please choose correct option!")
class validuser:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def validate_login(self):
        mycursor.execute("select * from userdetails where username like %s", (self.username,))
        data = mycursor.fetchall()
        if data:
            name = data[0][1]
            passw = data[0][2]
            if name == self.username and passw == self.password:
                return 1
        return 0
class userview:
    def __init__(self,username):
        self.username=username

    def user(self):
        def decision():
            print("1.continue with order" + '\n' + "2.cancel order")
            val_inp = int(input("select : "))
            a = 0
            if (val_inp == 1):
                a = 1
                return a
            elif (val_inp == 2):

                return a
            else:
                print("try agin,!")
                decision()
        def payment_orderr(wallet):
            print("Choose payment for Rs. {}".format(wallet))
            print("1. Online mode" + '\n' + "2. Offline mode")
            op_trans = int(input())
            if (op_trans == 1):
                a = input("enter card number")
                b = input("enter exp_date/month")
                c = input("enter cvv number")
                if (a, b, c is True):
                    print("payment received from online mode")
                    return 1
                else:
                    print("try again transaction process")
                    payment_orderr(wallet)

            elif (op_trans == 2):
                print("payment received from offline mode")
                return 1
            else:
                print("wrong option , try agin payment")
                payment_orderr(wallet)


        def payment_order(totalcost, wallet):
            print("Choose payment for Rs. {}".format(totalcost))
            print("1. Online mode" + '\n' + "2. Offline mode" + '\n' + "3. From Wallet :Rs. %s" % wallet)

            op_trans = int(input())
            if (op_trans == 1):
                a = input("enter card number")
                b = input("enter exp_date/month")
                c = input("enter cvv number")
                if (a, b, c is True):
                    print("payment received from online mode")
                    return 1
                else:
                    print("try again transaction process")
                    payment_order(totalcost, wallet)

            elif (op_trans == 2):
                print("payment received from offline mode")
                return 1
            elif (op_trans == 3):
                if (totalcost - wallet <= 0):
                    print("payment received from Wallet")
                    wal = wallet - totalcost
                    mycursor.execute("update userdetails SET wallet=%s WHERE username like %s", (str(wal), self.username,))
                    mydb.commit()
                    return 1
                elif (totalcost - wallet > 0):
                    wal = totalcost - wallet

                    mycursor.execute("update userdetails SET wallet= '0' WHERE username like %s", (self.username,))
                    mydb.commit()
                    wallet = wal
                    s = payment_orderr(wallet)


            else:
                print("wrong option , try agin payment")
                payment_order(totalcost, wallet)

        def feedb(find_id):
            print("Give your feedback here")
            s = input()
            if s:
                mycursor.execute("insert into feedbackdetails(fb_id,username,feedback) values(%s,%s,%s)",
                                 (find_id,self. username, s,))
                mydb.commit()
                print("Thank You ")
                return 1
            else:
                print("plz give your feedback")
                feedb(find_id)
        def order(address,wallet):
            global totalcost
            global st
            global act
            global itemlist
            global countlist
            totalcost = 0
            st = ""
            itemlist = []
            countlist = []
            print()
            print("Veg Category")
            print("1:Idly Rs.10" + '\n' + "2:Dosa Rs.20")
            print()
            print("Non Veg Category")
            print("3:Meal Rs.30" + '\n' + "4:Biriyani Rs.40" + '\n' + "5:Parotta Rs.50")
            print()
            d = {1: "Idly", 2: "Dosa", 3: "Meal", 4: "Biriyani", 5: "Parotta"}
            print("No of food would like to buy :")
            c_i = int(input())
            for i in range(c_i):
                option = int(input("select your food " + str(i + 1) + "  : "))
                if option >= 1 and option <= 5:
                    food = d[option]
                    itemlist.append(food)
                    mycursor.execute("select price from stock where fooditems like %s", (food,))
                    data = mycursor.fetchone()
                    ct = int(data[0])
                    mycursor.execute("select offers from stock where fooditems like %s", (food,))
                    data1 = mycursor.fetchone()
                    cost = ct - ((int(data1[0]) / 100) * ct)
                    print("Enter the count of order :")
                    count = int(input())
                    countlist.append(count)

                    st += food + "-" + str(count) + ","
                    totalcost += cost * count

                else:
                    print("Invalid option")
                    return 0

            mycursor.execute("select activecount from userdetails where username like %s", (self.username,))
            data4 = mycursor.fetchone()
            if (int(data4[0]) >= 5):
                totalcost -= ((5 / 100) * totalcost)

            if (totalcost < 200):
                act = int(data4[0]) + 0
            elif (totalcost >= 200):
                act = int(data4[0]) + 1

            if (int(data4[0]) >= 5):
                totalcost -= ((5 / 100) * totalcost)

            s = payment_order(totalcost, wallet)

            print("Name :%s" % username)
            print("Food Ordered :%s" % st)
            print("Address :%s" % address)
            print("Total Cost :%s" % totalcost)

            return 1



        def displayprev():
            mycursor.execute("select * from orderdetails where username like %s", (self.username,))
            data = mycursor.fetchall()
            if data:
                print("Name :%s" % data[0][1])
                for row in range(len(data)):
                    print("Food Ordered :%s" % data[row][2])
                    print("Total Cost :%s" % data[row][3])
            else:
                print("No Records found!")
            return 1

        def add_wallet(wallet):
            print("Wallet has Rs. %s" % wallet)
            ad_value = int(input("how much you want add"))
            wallet += ad_value
            s = payment_orderr(wallet)
            mycursor.execute("update userdetails SET wallet=%s WHERE username like %s", (str(wallet), self.username,))
            mydb.commit()
            print("the RS:{} has been credited and  now your wallet has :{}".format(ad_value, wallet))
        def orderplaced():
            s=decision()
            if (s == 0):
                print("Order failed !!")
                mycursor.execute("update userdetails SET wallet=%s WHERE username like %s", (totalcost, self.username,))
                mydb.commit()
                print("Your amount Rs. %s wiil be refunded with a minute" % totalcost)
                mycursor.execute(
                    "insert into orderdetails(ord_id,username,foodordered,totalcost,delivery_status) values (NULL,%s,%s,%s,%s)",
                    (self.username, st, totalcost, 'Refunded',))
                mydb.commit()
            else:
                for x, y in zip(itemlist, countlist):
                    food = x

                    mycursor.execute("select quantity,ratedfood from stock where fooditems like %s", (food,))
                    data2 = mycursor.fetchall()

                    rf = int(data2[0][1]) + 1
                    qu = int(data2[0][0]) - y
                    mycursor.execute("update stock SET quantity=%s WHERE fooditems like %s", (str(qu), food,))
                    mydb.commit()
                    mycursor.execute("update stock SET ratedfood=%s WHERE fooditems like %s", (str(rf), food,))
                    mydb.commit()

                mycursor.execute(
                    "insert into orderdetails(ord_id,username,foodordered,totalcost,delivery_status) values (NULL,%s,%s,%s,%s)",
                    (self.username, st, totalcost, 'Not Delivered',))
                mydb.commit()
                print("Order Success")
                print('Wait for few seconds for setting up delivery')

                time.sleep(5)
                mycursor.execute("update userdetails SET activecount=%s WHERE username like %s",
                                 (str(act), self.username,))
                mydb.commit()
                print("delivery starts, it will delivered within 30 mins")

                mycursor.execute("select * from orderdetails where username like %s", (self.username,))
                d = mycursor.fetchall()
                find_id = d[len(d) - 1][0]

                mycursor.execute("update orderdetails SET delivery_status='deivered' WHERE ord_id like  %s",
                                 (find_id,))
                mydb.commit()
                feedb(find_id)


        print("1:Order food ")
        print("2:Display my previous orders")
        print("3.show wallet amount")
        print("4.add wallet amount")
        option = int(input("Enter your option :"))

        mycursor.execute("select address,wallet from userdetails where username like %s", (self.username,))
        d = mycursor.fetchall()
        address = d[0][0]
        wallet = float(d[0][1])

        if option == 1:
            if order(address, wallet):
                orderplaced()

        elif option == 2:
            displayprev()
        elif option == 3:
            print("your wallet amount is : %2d " % wallet)
        elif option == 4:
            add_wallet(wallet)
        else:
            print("Invalid option Please enter valid option")

if __name__ == '__main__':

    print("welcome to Foodparadise !!")
    destination = input("Are you a user or admin or newuser?" + '\n' + " Type your destination :")
    destination = destination.lower()

    if destination == "user":
        username = input("Enter your name :")
        password = input("Enter your password :")
        obj=validuser(username,password)
        if obj.validate_login():
            obj1=userview(username)
            obj1.user()
        else:
            print("User does not exist")

    elif destination == "admin":
        obj=Admin_view()
        obj.admin()
    elif destination == "newuser":
        obj=Reg_user()
        obj.newuser()
    else:
        print("choose the correct option")
