from tkinter import *
from tkinter import messagebox
from customtkinter import *
import json
import os
from werkzeug.security import generate_password_hash, check_password_hash


ingredients = {}
counter = 0


def validate_int_input(value):
    try:
        value = float(value)
        return True
    except ValueError:
        messagebox.showerror("Błąd", "Wprowadź poprawną liczbę.")
        return False


def validate_input(value):
    if len(value) > 0:
        return True
    else:
        messagebox.showerror("Błąd", "Musisz wprowadzić dane.")
        return False


def app_quit():
    menu.quit()


def updating_password(old_var, new_var, new_var_again):
    old_pass = old_var.get()
    new_pass = new_var.get()
    new_pass_again = new_var_again.get()

    if new_pass == new_pass_again:

        with open("password.txt", "r") as file:
            password = file.read()

        if check_password_hash(password, old_pass):
            hash_password = generate_password_hash(
                new_pass,
                method='pbkdf2:sha256',
                salt_length=8
            )
            with open("password.txt", "w") as file:
                file.write(hash_password)

    changing_password_frame.pack_forget()
    def_menu()


def check_password(input_var, administrator):

    input_password = input_var.get()

    with open("password.txt", "r") as file:
        password = file.read()

    if check_password_hash(password, input_password):
        if administrator:
            password_admin.pack_forget()
            admin_menu()
        else:
            password_frame.pack_forget()
            add_products()
    else:
        if administrator:
            password_admin.pack_forget()
            def_menu()
        else:
            password_frame.pack_forget()
            def_menu()


def load_ingredients():
    if os.path.exists('ingredients.json'):
        with open('ingredients.json', 'r') as file:
            return json.load(file)
    else:
        ingredients = {}
        with open('ingredients.json', 'w') as file:
            json.dump(ingredients, file)
        return ingredients


def save_ingredients():
    with open('ingredients.json', 'w') as file:
        json.dump(ingredients, file)


def editing_product(product_choice):

    def saving():
        global ingredients

        changing_frame.pack_forget()
        saving_bool = None

        for i in range(len(edit_ingredients)):
            entry_name = edit_ingredients[i]
            entry = entry_vars[i].get()
            if validate_int_input(entry):
                ingredients[product_choice][entry_name] = entry
                saving_bool = True
            else:
                saving_bool = False

        if saving_bool:
            save_ingredients()

        def_menu()

    def changing():

        add_products_frame.pack_forget()

        global entry_names_vars, entry_vars, changing_frame

        entry_names_vars = []
        entry_vars = []

        changing_frame = Frame(master=window)
        changing_frame.pack(fill=BOTH, expand=True)

        for n in range(len(edit_ingredients)):
            label_name = Label(changing_frame, text=edit_ingredients[n])
            label_name.place(relx=0.1, rely=(n/13 + 0.175), anchor=W)

            entry_var = StringVar()
            entry_vars.append(entry_var)
            entry = Entry(changing_frame, textvariable=entry_var)
            entry.insert(0, edit_weight[n])
            entry.place(relx=0.5, rely=(n/13 + 0.175), anchor=W)

        button = Button(changing_frame, text="Dalej", command=saving)
        button.place(relx=0.5,  rely=0.9, anchor=CENTER)

    ingredients = load_ingredients()

    edit_ingredients = []
    edit_weight = []
    for product, ingr in ingredients.items():
        if product == product_choice:
            for ing, weight in ingredients[product].items():
                edit_ingredients.append(ing)
                edit_weight.append(weight)
    changing()


def deleting_product(product_choice):

    delete_products_frame.pack_forget()

    global ingredients

    ingredients = load_ingredients()

    if product_choice in ingredients:
        del ingredients[product_choice]

    save_ingredients()
    def_menu()


def adding_product():

    global add_products, password_frame

    def saving_product():
        adding_ingredients_frame.pack_forget()
        saving = None
        for i in range(int(ingr)):
            ingredient_value = ingredient_vars[i].get()
            quantity_value = quantity_vars[i].get()
            if validate_int_input(quantity_value) and validate_input(ingredient_value):
                ingredients[name][ingredient_value] = quantity_value
                saving = True
            else:
                saving = False
                add_products()
                break

        if saving:
            save_ingredients()
            def_menu()

    def adding_ingredients(name_var, ingr_var):
        add_products_frame.pack_forget()

        global ingr, ingredient_vars, quantity_vars, name, adding_ingredients_frame, password_frame

        name = name_var.get()
        ingr = ingr_var.get()

        if validate_int_input(ingr) and validate_input(name):

            if name not in ingredients:
                ingredients[name] = {}

            ingredient_vars = []
            quantity_vars = []

            adding_ingredients_frame = Frame(master=window)
            adding_ingredients_frame.pack(fill=BOTH, expand=True)

            ingredient_label = Label(adding_ingredients_frame, text="Składniki:")
            ingredient_label.place(relx=0.1, rely=0.1, anchor=W)

            quantity_label = Label(adding_ingredients_frame, text="Ilość:")
            quantity_label.place(relx=0.5, rely=0.1, anchor=W)

            for i in range(int(ingr)):
                ingredient_var = StringVar()
                ingredient_vars.append(ingredient_var)
                ingredient_input = Entry(adding_ingredients_frame, textvariable=ingredient_var)
                ingredient_input.place(relx=0.1, rely=(i/13 + 0.175), anchor=W)

                quantity_var = StringVar()
                quantity_vars.append(quantity_var)
                quantity_input = Entry(adding_ingredients_frame, textvariable=quantity_var)
                quantity_input.place(relx=0.5, rely=(i/13 + 0.175), anchor=W)

            next_button = Button(adding_ingredients_frame, text="Dalej", command=saving_product)
            next_button.place(relx=0.5, rely=0.9, anchor=CENTER)

        else:
            add_products()

    menu.pack_forget()

    password_frame = Frame(master=window)
    password_frame.pack(fill=BOTH, expand=True)

    pass_label = Label(password_frame, text="Podaj hasło: ")
    pass_label.place(relx=0.5, rely=0.3, anchor=CENTER)
    pass_var = StringVar()
    pass_input = Entry(password_frame, textvariable=pass_var, show="*")
    pass_input.place(relx=0.5, rely=0.4, anchor=CENTER)
    pass_button = Button(password_frame, text="Dalej", command=lambda: check_password(pass_var, administrator=False))
    pass_button.place(relx=0.5, rely=0.5, anchor=CENTER)

    def back_adding():
        add_products_frame.pack_forget()
        def_menu()

    def add_products():

        global ingredients, add_products_frame

        add_products_frame = Frame(master=window)
        add_products_frame.pack(fill=BOTH, expand=True)

        ingredients = load_ingredients()

        name_label = Label(add_products_frame, text="Podaj nazwę produktu:")
        name_label.place(relx=0.5, rely=0.25, anchor=CENTER)

        name_var = StringVar()
        name_input = Entry(add_products_frame, textvariable=name_var)
        name_input.place(relx=0.5, rely=0.32, anchor=CENTER)

        ingr_label = Label(add_products_frame, text="Podaj ilość składników:")
        ingr_label.place(relx=0.5, rely=0.42, anchor=CENTER)

        ingr_var = StringVar()
        ingr_input = Entry(add_products_frame, textvariable=ingr_var)
        ingr_input.place(relx=0.5, rely=0.49, anchor=CENTER)

        name_button = Button(add_products_frame, text="Dalej",
                                              command=lambda: adding_ingredients(name_var, ingr_var))
        name_button.place(relx=0.5, rely=0.59, anchor=CENTER)

        back_button = Button(add_products_frame, text='Cofnij', command=back_adding)
        back_button.place(relx=0.5, rely=0.69, anchor=CENTER)


def making_product():

    print_ingredients = []
    print_weight = []
    global index
    index = 0

    def printing():
        global index
        if index >= len(print_ingredients):
            printing_frame.destroy()
            return def_menu()
        label.configure(text=f"{print_ingredients[index]}: {print_weight[index]}g")
        index += 1

    def next_ingredient():
        printing()

    def back_ingredient():
        global index
        if index > 1:
            index -= 2
            printing()

    def counting(name, weight_var):

        global ingredients, counting_frame, printing_frame,label

        weight_input_frame.pack_forget()

        input_weight = weight_var.get()
        if validate_int_input(input_weight):

            for ingredient in ingredients.values():
                for ingr, weight in ingredient.items():
                    if ingr != "weight":
                        result = float((float(weight) * float(input_weight))/100)
                        rounded_result = round(result, 2)
                        ingredient[ingr] = rounded_result

            printing_frame = Frame(master=window)
            printing_frame.pack(fill=BOTH, expand=True)

            label = Label(printing_frame, text="", font=("Helvetica", 20))
            label.place(relx=0.5, rely=0.5, anchor=CENTER)

            next_button = Button(printing_frame,  text='Dalej', command=next_ingredient)
            next_button.place(relx=0.5, rely=0.7, anchor=CENTER)

            back_button = Button(printing_frame, text="Cofnij", command=back_ingredient)
            back_button.place(relx=0.5, rely=0.8, anchor=CENTER)

            for product, ingr in ingredients.items():
                if product == name:
                    for ing, weight in ingredients[product].items():
                            print_ingredients.append(ing)
                            print_weight.append(weight)
            printing()
        else:
            making_product()

    def back_making_product():
        weight_input_frame.pack_forget()
        making_product()

    def back_to_menu():
        making_products_frame.pack_forget()
        def_menu()

    def weight_input(name):
        making_products_frame.pack_forget()

        global weight_input_frame

        weight_input_frame = Frame(master=window)
        weight_input_frame.pack(fill=BOTH, expand=True)

        weight_label = Label(weight_input_frame, text="Wprowadź ilość:")
        weight_label.place(relx=0.5, rely=0.3, anchor=CENTER)

        weight_var = StringVar()
        weight_input = Entry(weight_input_frame, textvariable=weight_var)
        weight_input.place(relx=0.5, rely=0.4, anchor=CENTER)

        next_button = Button(weight_input_frame, text="Dalej",
                                              command=lambda: counting(name, weight_var))
        next_button.place(relx=0.5, rely=0.5, anchor=CENTER)

        back_button = Button(weight_input_frame, text="Cofnij", command=back_making_product)
        back_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    menu.pack_forget()

    global ingredients

    making_products_frame = Frame(master=window)
    making_products_frame.pack(fill=BOTH, expand=True)

    ingredients = load_ingredients()

    i = 0
    if len(ingredients) > 11:
        for i, product in enumerate(ingredients):
            product_button = Button(making_products_frame, text=product,
                                                     command=lambda prod=product: weight_input(prod))
            if i < 11:
                product_button.place(relx=0.3, rely=(i / 13 + 0.1), width=100, anchor=CENTER)
            else:
                product_button.place(relx=0.7, rely=((i / 13 + 0.1)-(1/13)*11), width=100, anchor=CENTER)

    else:
        for i, product in enumerate(ingredients):
            product_button = Button(making_products_frame, text=product,
                                                     command=lambda prod=product: weight_input(prod))
            product_button.place(relx=0.5, rely=(i/13 + 0.1), width=100, anchor=CENTER)

    back_button = Button(making_products_frame, text="Cofnij", command=back_to_menu)
    back_button.place(relx=0.5, rely=0.95, anchor=CENTER)

def admin():

    global admin_menu, password_admin
    menu.pack_forget()

    password_admin = Frame(master=window)
    password_admin.pack(fill=BOTH, expand=True)

    pass_label = Label(password_admin, text="Podaj hasło: ")
    pass_label.place(relx=0.5, rely=0.3, anchor=CENTER)

    pass_var = StringVar()
    pass_input = Entry(password_admin, textvariable=pass_var, show="*")
    pass_input.place(relx=0.5, rely=0.4, anchor=CENTER)

    pass_button = Button(password_admin, text="Dalej",
                                          command=lambda: check_password(pass_var, administrator=True))
    pass_button.place(relx=0.5, rely=0.5, anchor=CENTER)

    def admin_menu():


        def back_menu():
            admin_menu_frame.destroy()
            def_menu()

        def back_password():
            changing_password_frame.pack_forget()
            admin()

        def change_password():

            global changing_password_frame

            admin_menu_frame.pack_forget()

            changing_password_frame = Frame(master=window)
            changing_password_frame.pack(fill=BOTH, expand=True)

            old_label = Label(changing_password_frame, text="Wpisz stare hasło: ")
            old_label.place(relx=0.5, rely=0.3, anchor=E)

            old_var = StringVar()
            old_entry = Entry(changing_password_frame, textvariable=old_var, show="*")
            old_entry.place(relx=0.5, rely=0.3, anchor=W)

            new_label = Label(changing_password_frame, text="Wpisz nowe hasło: ")
            new_label.place(relx=0.5, rely=0.4, anchor=E)

            new_var = StringVar()
            new_entry = Entry(changing_password_frame, textvariable=new_var, show="*")
            new_entry.place(relx=0.5, rely=0.4, anchor=W)

            new_label_again = Label(changing_password_frame, text="Wpisz ponownie nowe hasło: ")
            new_label_again.place(relx=0.5, rely=0.5, anchor=E)

            new_var_again = StringVar()
            new_entry_again = Entry(changing_password_frame, textvariable=new_var_again, show="*")
            new_entry_again.place(relx=0.5, rely=0.5, anchor=W)

            continue_button = Button(changing_password_frame, text="Dalej",
                                                      command=lambda: updating_password(old_var, new_var,
                                                                                        new_var_again))
            continue_button.place(relx=0.5, rely=0.6, anchor=CENTER)

            back_button = Button(changing_password_frame, text="Cofnij", command=back_password)
            back_button.place(relx=0.5, rely=0.7, anchor=CENTER)

        def back_edit():
            add_products_frame.pack_forget()
            admin()

        def edit_products():
            admin_menu_frame.pack_forget()

            global ingredients, add_products_frame

            add_products_frame = Frame(master=window)
            add_products_frame.pack(fill=BOTH, expand=True)

            ingredients = load_ingredients()

            i = 0
            if len(ingredients) > 11:
                for i, product in enumerate(ingredients):
                    product_button = Button(add_products_frame, text=product,
                                            command=lambda prod=product: editing_product(prod))
                    if i < 11:
                        product_button.place(relx=0.3, rely=(i / 13 + 0.1), width=100, anchor=CENTER)
                    else:
                        product_button.place(relx=0.7, rely=((i / 13 + 0.1)-(1/13)*11), width=100, anchor=CENTER)

            else:
                for i, product in enumerate(ingredients):
                    product_button = Button(add_products_frame, text=product, command=lambda prod=product: editing_product(prod))
                    product_button.place(relx=0.5, rely=(i/13 + 0.1), width=100, anchor=CENTER)

            back_button = Button(add_products_frame, text="Cofnij", command=back_edit)
            back_button.place(relx=0.5, rely=0.95, anchor=CENTER)

        def back_delete():
            delete_products_frame.pack_forget()
            admin()

        def delete_products():
            admin_menu_frame.pack_forget()

            global ingredients, delete_products_frame

            delete_products_frame = Frame(master=window)
            delete_products_frame.pack(fill=BOTH, expand=True)

            ingredients = load_ingredients()

            i = 0
            if len(ingredients) > 11:
                for i, product in enumerate(ingredients):
                    delete_button = Button(delete_products_frame, text=product, command=lambda prod=product:  deleting_product(prod))
                    if i < 11:
                        delete_button.place(relx=0.3, rely=(i / 13 + 0.1), width=100, anchor=CENTER)
                    else:
                        delete_button.place(relx=0.7, rely=((i / 13 + 0.1)-(1/13)*11), width=100, anchor=CENTER)

            else:
                for i, product in enumerate(ingredients):
                    delete_button = Button(delete_products_frame, text=product,
                                           command=lambda prod=product: deleting_product(prod))
                    delete_button.place(relx=0.5, rely=(i/13 + 0.1), width=100, anchor=CENTER)

            back_button = Button(delete_products_frame, text='Cofnij', command=back_delete)
            back_button.place(relx=0.5, rely=0.95, anchor=CENTER)

        menu.pack_forget()

        admin_menu_frame = Frame(master=window)
        admin_menu_frame.pack(fill=BOTH, expand=True)

        password_button = Button(admin_menu_frame, text="Zmień hasło", width=18,
                                                  command=change_password)
        password_button.place(relx=0.5, rely=0.3, anchor=CENTER)

        edit_button = Button(admin_menu_frame, text="Edytuj produkty", width=18,
                                              command=edit_products)
        edit_button.place(relx=0.5, rely=0.4, anchor=CENTER)

        delete_button = Button(admin_menu_frame, text="Usuń produkty", width=18,
                                                command=delete_products)
        delete_button.place(relx=0.5, rely=0.5, anchor=CENTER)

        exit_button = Button(admin_menu_frame, text="Wróć", width=18, command=back_menu)
        exit_button.place(relx=0.5, rely=0.6, anchor=CENTER)


def def_menu():
    global menu

    menu = Frame(master=window)
    menu.pack(fill=BOTH, expand=True)

    title_label = Label(menu, text="Piekarnia", font=("Helvetica", 20))
    title_label.place(relx=0.5, rely=0.1, anchor=CENTER)

    add_button = Button(menu, text="Dodaj nowy produkt", width=18, command=adding_product)
    add_button.place(relx=0.5, rely=0.3, anchor=CENTER)

    bake_button = Button(menu, text="Piecz", width=18, command=making_product)
    bake_button.place(relx=0.5, rely=0.45, anchor=CENTER)

    admin_button = Button(menu, text="ADMIN", width=18, command=admin)
    admin_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    quit_button = Button(menu, text="Wyjdź", width=18, command=app_quit)
    quit_button.place(relx=0.5, rely=0.75, anchor=CENTER)


def main():
    global window

    window = Tk()
    window.title("Piekarnia")
    window.geometry('400x400')
    def_menu()
    window.mainloop()


main()
