import Order_Class

order = []
new_data_list = []

def cleaning_file():
    with open('warehouse_data_final_exam_Python.txt') as data:
        for i in data:
            i = i.split()
            if i:
                i = [str(x) for x in i]
                new_data_list.append(i)
      
def creating_orders(data_list):
    for x in data_list:
        a,b,c,d,e,f = zip(x)
        order.append(Order_Class.Order(*a,*b,*c,*d,*e,*f))
    
def print_list(order):
     for i in order:
        print(i)

cleaning_file()
new_data_list.sort(key = lambda x:(x[3],-int(x[4]),x[5]))
creating_orders(new_data_list)
print_list(order)
