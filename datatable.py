from flet import *
import sqlite3

conn=sqlite3.connect('db/dbcad.db', check_same_thread=False)

tb=DataTable(
    columns=[
        DataColumn(Text('Ação')),
        DataColumn(Text('Nome')),
        DataColumn(Text('Idade')),
        DataColumn(Text('Contato')),
        DataColumn(Text('Email')),
        DataColumn(Text('Endereço')),
        DataColumn(Text('Sexo')),
    ],
    rows=[]
)

def showdelete(e):
    try:
        myid = int(e.control.data)
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE id=?",(myid,))
        conn.commit()
        tb.rows.clear()
        calldb()
        tb.update()

    except Exception as erro:
        print(erro)

id_edit = Text()
name_edit = TextField(label='Nome')
age_edit = TextField(label='Idade')
contact_edit = TextField(label='Contato')
gender_edit = RadioGroup(content=Column([
    Radio(value='Masculino', label='Masculino'),
    Radio(value='Feminino', label='Feminino')
]))
email_edit = TextField(label='Email')
address_edit = TextField(label='Endereço')

def hidedlg(e):
    dlg.visible=False
    dlg.update()

def updateandsave(e):
    try:
        myid = id_edit.value
        c=conn.cursor()
        c.execute(
            """UPDATE users SET name=?, contact=?,
            age=?, gender=?, email=?, address=?
            WHERE id=?""", (name_edit.value, contact_edit.value, 
            age_edit.value, gender_edit.value, email_edit.value, address_edit.value, myid)
        )
        conn.commit()
        print('Editados com sucesso')
        tb.rows.clear()
        calldb()
        dlg.visible=False
        dlg.update()
        tb.update()

    except Exception as erro:
        print('o erro está aqui', erro)

dlg = Container(
    bgcolor='green200',
    padding=10,
    content=Column([
        Row([
            Text(
                'Editar dados',
                size=20,
                weight='bold'
            ),
            IconButton(
                icon='close', 
                on_click=hidedlg
            )], alignment='spaceBetween'),
        name_edit,
        age_edit,
        contact_edit,
        Text('Selecione o sexo', size=20,weight='bold'),
        gender_edit,
        email_edit,
        address_edit,
        ElevatedButton(
            'Atualizar',
            on_click=updateandsave
        ),
    ])
)

def showedit(e):
    data_edit = e.control.data
    id_edit.value = data_edit['id']
    name_edit.value = data_edit['name']
    age_edit.value = data_edit['age']
    contact_edit.value = data_edit['contact']
    gender_edit.value = data_edit['gender']
    email_edit.value = data_edit['email']
    address_edit.value = data_edit['address']

    dlg.visible=True
    dlg.update()

def calldb():
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    print(users)

    if not users == '':
        keys= ['id', 'name', 'contact', 'age', 'gender', 'email', 'address']
        result = [dict(zip(keys, values)) for values in users]
        for x in result:
            tb.rows.append(
                DataRow(
                    cells=[
                        DataCell(
                            Row([
                                IconButton(
                                    icon='create',
                                    icon_color='blue',
                                    data=x,
                                    on_click=showedit
                                ),
                                IconButton(
                                    icon='delete',
                                    icon_color='red',
                                    data=x['id'],
                                    on_click=showdelete
                                ),
                            ])
                        ),
                        DataCell(Text(x['name'])),
                        DataCell(Text(x['age'])),
                        DataCell(Text(x['contact'])),
                        DataCell(Text(x['email'])),
                        DataCell(Text(x['address'])),
                        DataCell(Text(x['gender'])),
                    ],
                ),
            )

calldb()
dlg.visible=False

mytable = Column([
    dlg,
    Row([tb],scroll='always')
])