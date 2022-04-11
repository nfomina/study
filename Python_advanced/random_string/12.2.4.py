# номер не может начинаться с нулей;
# номер лотерейного билета должен состоять из 7 цифр;
# все 100 лотерейных билетов должны быть различными.

import random

tickets = []
while len(tickets) < 100:
    ticket = random.randint(1000000, 9999999)
    if ticket not in tickets:
        print(ticket)
        tickets.append(ticket)
