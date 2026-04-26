from os import system
from time import sleep

def loading(text):

    for letter in text:
        print(letter, end="", flush=True)
        sleep(0.5)
    print()

def title_screen():
    print("   _____            _             _           ".center(64))
    print("  / ____|          | |           | |      _   ".center(64))
    print(" | |     ___  _ __ | |_ __ _  ___| |_   _| |_ ".center(64))
    print(" | |    / _ \\| '_ \\| __/ _` |/ __| __| |_   _|".center(64))
    print(" | |___| (_) | | | | || (_| | (__| |_    |_|  ".center(64))
    print("  \\_____\\___/|_| |_|\\__\\__,_|\\___|\\__|        ".center(64))

    print("\n>>> Welcome to Contact+ let's go to the Menu!")


# Primeira função - Criar um contato.

def add_contact(contacts, ctt_name, ctt_mobile, ctt_email):

    contact = {"name": ctt_name, "mobile": ctt_mobile, "email": ctt_email, "fav": False}
    contacts.append(contact)

    print('\n'+'-'*64)
    print(f"✓ Contact of '{ctt_name}' was successfully added ✓".center(64))
    print('-'*64)
    loading('\n...')
    system('cls')
    return

# Segunda função - Ver lista de contatos.

def see_contacts(contacts):
    print("\nList of Contacts")
    print("-"*64)

    for i, contact in enumerate(contacts, start=1):
        fav = "⭐" if contact["fav"] else " "
        ctt_name = contact['name']
        ctt_mobile = contact['mobile']
        ctt_email = contact['email']

        print(f"{i}. [{fav}] {ctt_name} ∗ {ctt_mobile} ∗ {ctt_email}\n"+"-"*64)

# Terceira função - Editar contatos:

def edit_contact(contacts, ctt_index):
    index_adjusted = int(ctt_index) - 1

    for i, contact in enumerate(contacts):
        if i == index_adjusted:
            ctt_name = contact['name'] 
            ctt_mobile = contact['mobile']
            ctt_email = contact['email']

    if index_adjusted >= 0 and index_adjusted < len(contacts):
        
        print("\n========== EDITING A CONTACT ==========")
        print(f">>> In '{ctt_name}'s' contact, what do you want to edit?\n")

        print(f"1. [☻ ] {ctt_name}")
        print(f"2. [☎ ] {ctt_mobile}")
        print(f"3. [✉ ] {ctt_email}")
        if contact["fav"] == True: 
            print(f"4. [⭐] Favorited") 
        else: 
            print(f"4. [  ] Favorite")

        opt = input("\n[option] ")

        match opt:
            case "1":
                ctt_new_name = input("\n[new name] ")
                contacts[index_adjusted]["name"] = ctt_new_name
                print('\n'+'-'*64)
                print(f"✓ Name successfully updated to '{ctt_new_name}' ✓".center(64))
                print("-"*64)

            case "2":
                ctt_new_mobile = input("\n[new mobile] ").replace(")", "").replace("(", "").replace(" ", "")
                contacts[index_adjusted]["mobile"] = ctt_new_mobile
                print('\n'+'-'*64)
                print(f"\n✓ Mobile successfully updated to '{ctt_new_mobile}' ✓\n".center(64))
                print("-"*64)

            case "3":
                ctt_new_email = input("\n[new email] ").lower()
                contacts[index_adjusted]["email"] = ctt_new_email
                print('\n'+'-'*64)
                print(f"\n✓ E-mail successfully updated to '{ctt_new_email}' ✓\n".center(64))
                print("-"*64)

            case "4":
                if contact[index_adjusted]["fav"] == False:
                    contact[index_adjusted]["fav"] = True
                    print('\n'+'-'*64)
                    print(f"\n✓ '{ctt_name}' was marked as 'FAVORITE' successfully ✓\n".center(64))
                    print("-"*64)
                else:
                    contact[index_adjusted]["fav"] = False
                    print('\n'+'-'*64)
                    print(f"\n✓ '{ctt_name}' was removed from 'FAVORITES' successfully ✓\n".center(64))
                    print("-"*64)

            case _:
                print("Unknown command. Returning to Menu")
     
        loading('\n...')
        system('cls')
    else: 
        print("Index out of range. Try again.")
    return







contacts = []

while True:
    title_screen()  
    print("\n"+"="*29+" MENU "+"="*29)
    print("[1] Add contact")
    print("[2] See contacts list")       # Inclui ver lista de favoritos
    print("[3] Edit existing contact")   # Inclui marcar como favorito
    print("[4] Delete/Block a contact") 
    print("="*64)

    opt = input("[option] ")

    match opt:
        case "1":
            print("\n========== CREATING A CONTACT ==========")
            print(">>> Let's add a Contact!\n")
            ctt_name = input("[☻] ")
            ctt_mobile = input("[☎ ] ").replace("-", "").replace(")", "").replace("(", "").replace(" ", "") # futuramente adicionar uma função para formatar todos os números de uma forma bonita.

            ctt_email = input("[✉ ] ").lower() 

            add_contact(contacts, ctt_name, ctt_mobile, ctt_email)
        
        case "2":
            see_contacts(contacts)
            
            print("[1] ← Back")
            print("[2] Edit contact")

            opt_2 = input("\n[option] ")

            match opt_2:
                case '1':
                    loading('\n...')
                    system('cls')

                case '2':
                    print("\nWhich contact do you want to edit?")
                    ctt_index = input("[id] ")
                    edit_contact(contacts, ctt_index)

                case _:
                    print("Unknown command. Returning to Menu")
                    loading('\n...')
                    system('cls')

        case "3":
            see_contacts(contacts)

            print("\nWhich contact do you want to edit?")
            ctt_index = input("[id] ")
            edit_contact(contacts, ctt_index)

        case "4":
            print("")
        case _:
            print("Unknown command. Try again")