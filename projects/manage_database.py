""" SQlite3 Database management app
"""
import tkinter.ttk as ttk
from tkinter import *
import sqlite3

'''
# Create a database or connect to one
conn = sqlite3.connect("address_book.db")
# Create cursor
c = conn.cursor()

# create table
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer)
        """)
        
        
# Commit changes
conn.commit()

# Close connection
conn.close()
'''


def save_update():
    """Save record update

    """
    # Crate a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET
            first_name = :first,
            last_name = :last,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode
            WHERE oid = :oid""",
              {'first': f_name_editor.get(),
               "last": l_name_editor.get(),
               "address": address_editor.get(),
               "city": city_editor.get(),
               "state": state_editor.get(),
               "zipcode": zipcode_editor.get(),
               "oid": record_id
               }

              )

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    editor.destroy()


def edit():
    """edit a record

    """
    global editor
    editor = Tk()
    editor.title("Update a record")

    # Crate a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor
    c = conn.cursor()

    record_id = delete_box.get()
    # Querry the database
    c.execute("SELECT *, oid from addresses WHERE oid=" + record_id)
    records = c.fetchall()  # / fetchmany(50) / fetchone()

    # Create global variables for texte box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # Create text box labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)

    save_btn = Button(editor, text="Save record", command=save_update)
    save_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=140)

    # Loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()


def delete():
    """delete a record

    """
    # Crate a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("DELETE FROM addresses WHERE oid=" + delete_box.get())

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()


def create_record():
    """create a new record in database

    """
    # Crate a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get(),
              }
              )

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    # Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    """select and display a record

    """
    # Crate a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor
    c = conn.cursor()

    # Querry the database
    c.execute("SELECT *, oid from addresses")
    records = c.fetchall()  # / fetchmany(50) / fetchone()

    # build string containing record informations
    print_record = ""
    for record in records:
        print_record += str(record[0]) + " " + str(record[1]) + "\t" + str(record[6]) + "\n"

    query_label = Label(root, text=print_record)
    query_label.grid(row=12, column=0, columnspa=2)

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()


# First widget: global window
root = Tk()
root.title("Title")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')

# Text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

# Create text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text="Select ID", anchor="e")
delete_box_label.grid(row=9, column=0, padx=(100, 0))

# Create Submit Button
create_record_btn = Button(root, text="Add Record to database", command=create_record)
create_record_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=108)

# Create a Query Button
querry_btn = Button(root, text="Show records", command=query)
querry_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=135)

# Create Delete button
delete_btn = Button(root, text="Delete record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=135)

# Create Delete button
edit_btn = Button(root, text="Edit record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=140)

# Loop for dynamic screen
root.mainloop()
