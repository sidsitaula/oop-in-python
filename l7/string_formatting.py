subtotal = 12.32
tax = subtotal * 0.07
total = subtotal + tax
print("Sub: ${0:.2f} Tax: ${1:.2f} Total: ${total:.2f}".format(
    subtotal, tax, total=total))


orders = [('burger', 2, 5),
          ('fries', 3.5, 1),
          ('cola', 1.75, 3)]
print("PRODUCT QUANTITY PRICE SUBTOTAL")
for product, price, quantity in orders:
    subtotal = price * quantity
    print("{0:10s}{1: ^9d} ${2: <8.2f}${3: >7.2f}".format(
        product, quantity, price, subtotal))
