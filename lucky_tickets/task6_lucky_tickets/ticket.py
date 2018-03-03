def tickets_list():
    max_ticket_number = 1000000
    tickets_list = []
    for j in range(max_ticket_number):
        j = str(j)
        if len(j) <= 6:
            j = ('0' * (6 - len(j)) + j)
            tickets_list.append(j)
    return tickets_list


def lucky_Moskow_tickets(tickets_list):
    Moskow_tickets = 0
    for j in tickets_list:
        sum1 = int(j[0]) + int(j[1]) + int(j[2])
        sum2 = int(j[3]) + int(j[4]) + int(j[5])
        if sum1 == sum2:
            Moskow_tickets += 1
    return Moskow_tickets


def lucky_Piter_tickets(tickets_list):
    Piter_tickets = 0
    for j in tickets_list:
        sum1 = int(j[0]) + int(j[2]) + int(j[4])
        sum2 = int(j[1]) + int(j[3]) + int(j[5])
        if sum1 == sum2:
            Piter_tickets += 1
    return Piter_tickets
