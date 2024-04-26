from threading import Thread

invoice_amount = [1000]
class BankAccount(Thread):

    def deposit_task():
        for _ in range(5):
            deposit = 100
            invoice_amount.append(deposit)
            print(f'Deposited {deposit}, new balance is {sum(invoice_amount)}')
    def withdraw_task():
        for _ in range(5):
            withdraw = -150
            invoice_amount.append(withdraw)
            print(f'Deposited {withdraw}, new balance is {sum(invoice_amount)}')


    deposit_thread = Thread(target=deposit_task)
    withdraw_thread = Thread(target=withdraw_task)

    deposit_thread.start()
    withdraw_thread.start()

    deposit_thread.join()
    withdraw_thread.join()
print(len(invoice_amount))
print(invoice_amount)