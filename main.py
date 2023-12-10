from flet import *
import flet as ft
from useraction_table import create_table
import sqlite3

conn=sqlite3.connect('db/dbcad.db', check_same_thread=False)

def main(page:Page):
    create_table()
    page.scroll = 'auto'

    def showinput(e):
        inputcon.offset=transform.Offset(0,0)
        page.update()

    def hidecon(e):
        inputcon.offset=transform.Offset(0,0)
        page.update()

    def savedata(e):
        try:
            c=conn.cursor()
            c.execute('''INSERT INTO users (
                name,age,contact,email,address,gender) VALUES (?,?,?,?,?,?,)''',(
                name.value,
                age.value,
                contact.value,
                email.value,
                address.value,
                gender.value)
            )
            conn.commit()
            print('success')
        except Exception as e:
            print(e)

            inputcon.offset=transform.Offset(2,0)

            page.snack_bar  = SnackBar(
                Text('success Input'),
                bgcolor='green'
            )
            page.snack_bar.open=True
            page.update()


    name = TextField(label='name')
    age = TextField(label='age')
    contact = TextField(label='contact')
    email = TextField(label='email')
    address = TextField(label='address')
    gender = RadioGroup(content=Column([
        Radio(value='Masculino', label='man'),
        Radio(value='Feminino', label='woman')
    ]))

    inputcon = Card(
        offset=transform.Offset(2,0),
        animate_offset=animation.Animation(600,curve='easyIn'),
        elevation=30,
        content=Container([
            Row([
                Text('add dados',size=20,weight='bold'),
                IconButton(icon='Sair',icon_size=30, on_click=hidecon),
                name,
                age, 
                contact,
                gender, 
                email, 
                address,
                FilledButton('Salvar dados', on_click=savedata)
            ])
        ])
    )
    page.add(
        Column([
            Text('Cadastro de Usuários', size=30, weight='bold'),
            ElevatedButton('Cadastrar', on_click=showinput)
        ])
    )

ft.app(target=main)