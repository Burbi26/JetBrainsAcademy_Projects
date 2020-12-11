import random
import sqlite3
connect = sqlite3.connect("card.s3db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS card (
id INTEGER,
number TEXT,
pin TEXT,
balance INTEGER DEFAULT 0
);""")
connect.commit()


class CreditCard:
    def createAccount(self):
        cardNumberTemp = random.randint(000000000, 999999999)
        cardNumberTemp = (4000000000000000 + cardNumberTemp * 10)
        verifyNum = cardNumberTemp // 10
        verifySum = 0
        while verifyNum != 0:
            if (verifyNum % 10) * 2 >= 10:
                verifySum += (verifyNum % 10) * 2 - 9
            else:
                verifySum += (verifyNum % 10) * 2
            verifyNum = verifyNum // 10
            verifySum += verifyNum % 10
            verifyNum = verifyNum // 10
        checkSum = (verifySum * 9) % 10
        cardNumberTemp = cardNumberTemp + checkSum
        cardNumberTemp = str(cardNumberTemp)
        cardPinTemp = str()
        for _ in range(4):
            cardPinTemp += str(random.randint(0, 9))
        print("\nYour card has been created")
        print("Your card number:")
        print(cardNumberTemp)
        print("Your card PIN:")
        print(cardPinTemp)
        cursor.execute("SELECT * FROM card;")
        if len(cursor.fetchall()) == 0:
            id = 1
        else:
            cursor.execute("SELECT * FROM card;")
            id = len(cursor.fetchall()) + 1
        cursor.execute("INSERT INTO card (id, number, pin) VALUES(?,?,?)", (id, cardNumberTemp, cardPinTemp))
        connect.commit()

    def logInAccount(self):
        print("\nEnter your card number:")
        self.loginCard = input()
        cursor.execute(f"SELECT * FROM card WHERE number={self.loginCard}")
        if bool(cursor.fetchone()) is not False:
            print("Enter your PIN:")
            self.loginPin = input()
            cursor.execute(f"SELECT * FROM card WHERE number={self.loginCard}")
            verPin = cursor.fetchone()[2]
            if self.loginPin == verPin:
                print("You have successfully logged in!\n")
                return 2
            else:
                print("Wrong card number or PIN!\n")
                return 1
        else:
            print("Wrong card number or PIN!\n")
            return 1

    def Balance(self):
        cursor.execute(f"SELECT * FROM card WHERE number={self.loginCard} AND pin={self.loginPin}")
        print("Balance: {}\n".format(cursor.fetchone()[3]))

    def logOutAccount(self):
        print("You have successfully logged out!")
        print()
        return 1

    def addIncome(self):
        print("Enter income:")
        income = int(input())
        cursor.execute(f"SELECT * FROM card WHERE number={self.loginCard} AND pin={self.loginPin}")
        id = cursor.fetchone()[0]
        cursor.execute(f"SELECT * FROM card WHERE number={self.loginCard} AND pin={self.loginPin}")
        cardNumberTemp = cursor.fetchone()[1]
        cursor.execute(f"SELECT * FROM card WHERE number={self.loginCard} AND pin={self.loginPin}")
        cardPinTemp = cursor.fetchone()[2]
        cursor.execute(f"SELECT * FROM card WHERE number={self.loginCard} AND pin={self.loginPin}")
        income = income + cursor.fetchone()[3]
        cursor.execute(f"DELETE FROM card WHERE number={self.loginCard} AND pin={self.loginPin}")
        cursor.execute("INSERT INTO card (id, number, pin, balance) VALUES(?,?,?,?)", (id, cardNumberTemp, cardPinTemp, income))
        print("Income was added!\n")
        connect.commit()

    def doTransfer(self):
        print("Transfer")
        print("Enter card number:")
        transferCard = input()
        cursor.execute(f"SELECT * FROM card WHERE number={transferCard}")
        verifySum = 0
        cardDigit = int(transferCard) % 10
        checkCard = int(transferCard) // 10
        while checkCard != 0:
            if (checkCard % 10) * 2 >= 10:
                verifySum += (checkCard % 10) * 2 - 9
            else:
                verifySum += (checkCard % 10) * 2
            checkCard = checkCard // 10
            verifySum += checkCard % 10
            checkCard = checkCard // 10
        checkDigit = (verifySum * 9) % 10
        if checkDigit == cardDigit:
            if bool(cursor.fetchone()) is not False:
                if transferCard == self.loginCard:
                    print("You can't transfer money to the same account!\n")
                else:
                    print("Enter how much money you want to transfer:")
                    cursor.execute(f"SELECT * FROM card WHERE number={self.loginCard} AND pin={self.loginPin}")
                    acBalance = cursor.fetchone()[3]
                    transferBalance = int(input())
                    if acBalance < transferBalance:
                        print("Not enough money!\n")
                    else:
                        cursor.execute(f"SELECT * FROM card WHERE number={self.loginCard} AND pin={self.loginPin}")
                        idS = cursor.fetchone()[0]
                        cursor.execute(f"SELECT * FROM card WHERE number={self.loginCard} AND pin={self.loginPin}")
                        cardNumberTempS = cursor.fetchone()[1]
                        cursor.execute(f"SELECT * FROM card WHERE number={self.loginCard} AND pin={self.loginPin}")
                        cardPinTempS = cursor.fetchone()[2]
                        incomeS = acBalance - transferBalance
                        cursor.execute(f"DELETE FROM card WHERE number={self.loginCard} AND pin={self.loginPin}")
                        cursor.execute("INSERT INTO card (id, number, pin, balance) VALUES(?,?,?,?)", (idS, cardNumberTempS, cardPinTempS, incomeS))
                        cursor.execute(f"SELECT * FROM card WHERE number={self.loginCard} AND pin={self.loginPin}")
                        connect.commit()
                        idT = cursor.fetchone()[0]
                        cursor.execute(f"SELECT * FROM card WHERE number={transferCard}")
                        cardNumberTempT = cursor.fetchone()[1]
                        cardPinTempT = transferCard
                        cursor.execute(f"SELECT * FROM card WHERE number={transferCard}")
                        incomeT = transferBalance + cursor.fetchone()[3]
                        cursor.execute(f"DELETE FROM card WHERE number={transferCard}")
                        cursor.execute("INSERT INTO card (id, number, pin, balance) VALUES(?,?,?,?)", (idT, cardNumberTempT, cardPinTempT, incomeT))
                        print()
                        connect.commit()
            else:
                print("Such a card does not exist.")
        else:
            print("Probably you made mistake in card number. Please try again!")

    def closeAccount(self):
            cursor.execute(f"DELETE FROM card WHERE number={self.loginCard} AND pin={self.loginPin}")
            print("The account has been closed!")
            connect.commit()
            return 1


mainActivity = 1
creditCard = CreditCard()
while mainActivity != 0:
    print("1. Create an account\n2. Log into account\n0. Exit")
    mainActivity = int(input())
    if mainActivity == 1:
        creditCard.createAccount()
        print()
    elif mainActivity == 2:
        mainActivity = creditCard.logInAccount()
        while mainActivity == 2:
            print("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit")
            accountActivity = int(input())
            print()
            if accountActivity == 1:
                creditCard.Balance()
            elif accountActivity == 2:
                creditCard.addIncome()
            elif accountActivity == 3:
                creditCard.doTransfer()
            elif accountActivity == 4:
                mainActivity = creditCard.closeAccount()
            elif accountActivity == 5:
                mainActivity = creditCard.logOutAccount()
            elif accountActivity == 0:
                mainActivity = 0
connect.close()
