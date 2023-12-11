from flet import *
import flet as ft
from useraction_table import create_table
from datatable import mytable,tb,calldb
import sqlite3

conn=sqlite3.connect('db/dbcad.db', check_same_thread=False)

def main(page:Page):
    page.theme_mode='light'
    create_table()
    page.scroll = 'auto'

    def showinput(e):
        inputcon.offset=transform.Offset(0,0)
        page.update()

    def hidecon(e):
        inputcon.offset=transform.Offset(1,0)
        page.update()

    def savedata(e):
        try:
            c=conn.cursor()
            c.execute('''INSERT INTO users (name, age, contact, email, address, gender) VALUES (?,?,?,?,?,?)''',(
                name.value,
                age.value,
                contact.value,
                email.value,
                address.value,
                gender.value)
            )
            conn.commit()
            print('success')

            inputcon.offset=transform.Offset(2,0)

            page.snack_bar  = SnackBar(
                Text('Cadastrado com sucesso'),
                bgcolor='green'
            )
            page.snack_bar.open=True
            tb.rows.clear()
            calldb()
            tb.update()
            page.update()

        except Exception as e:
            print('entrou no def savedata(e): mas não saiu', e)

    name = TextField(label='Nome')
    age = TextField(label='Idade')
    contact = TextField(label='Contato')
    email = TextField(label='Email')
    address = TextField(label='Endereço')
    gender = RadioGroup(content=Column([
        Radio(value='Masculino', label='Masculino'),
        Radio(value='Feminino', label='Feminino')
    ]))

    inputcon = Card(
        offset=transform.Offset(2,0),
        animate_offset=animation.Animation(600,curve='easyIn'),
        elevation=30,
        content=Container(
            bgcolor='green200',
            content=Column([
                Row([
                    Text('Novo cadastro',size=20,weight='bold'),
                    IconButton(icon='close',icon_size=30, on_click=hidecon),
                ]),
                name,
                age, 
                contact,
                gender, 
                email, 
                address,
                FilledButton('Salvar dados', on_click=savedata)
            ])
        )
    )
    page.add(
        Column([
            Text('Cadastro de Usuários', size=30, weight='bold'),
            ElevatedButton('Cadastrar', on_click=showinput),
            mytable,
            inputcon
        ])
    )

ft.app(target=main)