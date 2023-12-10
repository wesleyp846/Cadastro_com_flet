from flet import *
import flet as ft
import sqlite3

conn=sqlite3.connect('db/dbcad.db', check_same_thread=False)



tb=DataTable(
    columns=[
        DataColumn(Text('actions')),
        DataColumn(Text('name')),
        DataColumn(Text('age')),
        DataColumn(Text('contact')),
        DataColumn(Text('email')),
        DataColumn(Text('address')),
        DataColumn(Text('gender')),
    ],
    rows=[]
)

id = Text()
name_edit = TextField(label='name')
age_edit = TextField(label='age')
contact_edit = TextField(label='contact')
email_edit = TextField(label='email')
address_edit = TextField(label='address')
gender_edit = RadioGroup(content=Column([
    Radio(value='Masculino', label='man'),
    Radio(value='Feminino', label='woman')
]))



def showedit(e):
    data_edit = e.control.data
    id = data_edit['id']
    name_edit = data_edit['name']
    age_edit = data_edit['age']
    contact_edit = data_edit['contact']
    email_edit = data_edit['email']
    address_edit = data_edit['address']
    gender_edit = data_edit['gander']

def showdelete():
    pass

def calldb():
    c=conn.cursor()
    c.execute('SELECT * FROM users')
    users=c.fetchall()
    print(users)

    if not users == '':
        keys= ['id','name','contact','age','genger','email','address']

        result =[dict(zip(keys.values)) for value in users]
        for x in result:
            tb.rows.append(
                DataRow(
                    cells=[
                        DataCell(
                            Row([
                                IconButton(icon='Criar cadastro',
                                    icon_color='green',
                                    data=x['id'],
                                    on_click=showedit
                                ),
                                IconButton(icon='Deletar',
                                    icon_color='red',
                                    data=x['id'],
                                    on_click=showdelete
                                )
                            ])
                        ),
                        DataCell(Text(x['name'])),
                        DataCell(Text(x['age'])),
                        DataCell(Text(x['contact'])),
                        DataCell(Text(x['email'])),
                        DataCell(Text(x['address'])),
                        DataCell(Text(x['gender'])),
                    ]
                )
            )

calldb()

mytable=Column([
    Row([tb],scroll='always')
])