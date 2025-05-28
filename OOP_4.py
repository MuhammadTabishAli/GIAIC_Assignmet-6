class Bank:
    bank_name = "Default Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show_bank(self):
        print(f"Bank Name: {self.bank_name}")

acc1 = Bank()
acc2 = Bank()

acc1.show_bank()
acc2.show_bank()

Bank.change_bank_name("UBL Bank")

acc1.show_bank()
acc2.show_bank()