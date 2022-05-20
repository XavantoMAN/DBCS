import csv


def create_table(tablename, fieldnames):
    header = fieldnames.split(', ')
    with open(tablename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(header)


def select_tb(tablename, cond):
    data = []
    with open(tablename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
        if cond == '':
            for row in reader:
                data.append(row)
        else:
            condition = cond.split('=')
            #print(condition[0])
            #print(condition[1])
            count = 0
            for row in reader:
                #print('row:' + str(row))
                for i in row:
                    #print('el:' + str(i))
                    if i == condition[0]:
                        a = count
                        data.append(row)
                        #print('count:',a)
                        break;
                    count += 1
                if row[a] == condition[1]:
                    data.append(row)
                    
    return data


def add_row(tablename, row):
    row = row.split(', ')
    with open(tablename, 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(row)


def delete_row_id(tablename, id):
    data = []
    with open(tablename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
        for row in reader:
            if row[0] != str(id):
                data.append(row)

    with open(tablename, 'w', newline='') as csvfile:    
        for row in data:  
            writerf = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writerf.writerow(row)


def update_row_by_id(tablename, new_data):
    new_data = new_data.split(', ')
    data = []
    with open(tablename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)
        for row in reader:
            if row[0] == new_data[0]:
                data.append(new_data)
            else:
                data.append(row)
    
    with open(tablename, 'w', newline='') as csvfile:    
        for row in data:  
            writerf = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writerf.writerow(row)
