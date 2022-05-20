import os
import sys
import dbcs


def create_query(tb_name, data):
    tableName = table_name(tb_name)
    dbcs.create_table(tableName, data)


def select_query(tb_name, cond):
    tableName = table_name(tb_name)
    return dbcs.select_tb(tableName, cond)


def update_query(tb_name, data):
    tableName = table_name(tb_name)
    dbcs.update_row_by_id(tableName, data)


def delete_query(tb_name, cond):
    tableName = table_name(tb_name)
    dbcs.delete_row_id(tableName, cond)


def insert_query(tb_name, data):
    tableName = table_name(tb_name)
    dbcs.add_row(tableName, data)


def table_name(name):
    return os.path.join('DataBase', name + '.csv')


def query(query):
    if query.upper() == 'EXIT':
        print('----See you next time !----')
        sys.exit()
    try:
        command = query.split('=>')
        tb_name = command[1].split(';')
    except:
        if query.upper() == 'HELP':
            print('HELP:\nSELECT=>tb;cond\nCREATE=>tb;d1, d2 .. dn\nUPDATE=>tb;id\nDELETE=>tb;id\nINSERT=>tb;d1, d2 .. dn')
        else:
            print(f'"{query}" не является встроенной коммандой !\nКоманда "HELP" для помощи')
    if command[0].upper() == 'SELECT':
        return select_query(tb_name[0],tb_name[1])
    elif command[0].upper() == 'CREATE':
        create_query(tb_name[0], tb_name[1])
    elif command[0].upper() == 'UPDATE':
        update_query(tb_name[0], tb_name[1])
    elif command[0].upper() == 'DELETE':
        delete_query(tb_name[0], tb_name[1])
    elif command[0].upper() == 'INSERT':
        insert_query(tb_name[0], tb_name[1])
    
         
