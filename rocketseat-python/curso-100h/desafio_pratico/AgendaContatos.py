from os import system
from time import sleep

def loading(text):

    for letter in text:
        print(letter, end="", flush=True)
        sleep(0.5)
    print()

def unknown_command(style):

    match style:
        case 1:
            print("\n[?] Unknown command. Returning to the Menu [?]")
        case 2:
            print("\n[?] Unknown command. Try again [?]")
        case _:
            print("\n(⌐■_■) This is a bug")

    loading('\n...')
    system('cls')

def title_screen():
    print("   _____            _             _           ".center(64))
    print("  / ____|          | |           | |      _   ".center(64))
    print(" | |     ___  _ __ | |_ __ _  ___| |_   _| |_ ".center(64))
    print(" | |    / _ \\| '_ \\| __/ _` |/ __| __| |_   _|".center(64))
    print(" | |___| (_) | | | | || (_| | (__| |_    |_|  ".center(64))
    print("  \\_____\\___/|_| |_|\\__\\__,_|\\___|\\__|        ".center(64))

    print("\n>>> Welcome to Contact+! Let's go to the menu!")


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
    print("\n"+">>> Contact List <<<".center(64))
    print("-"*64)

    for i, contact in enumerate(contacts, start=1):
        fav = "⭐" if contact["fav"] else " "
        ctt_name = contact['name']
        ctt_mobile = contact['mobile']
        ctt_email = contact['email']

        print(f"{i}. [{fav}] {ctt_name} ∗ {ctt_mobile} ∗ {ctt_email}\n"+"-"*64)

def see_fav_contacts(contacts):
    print("\n"+">>> Favorite Contacts <<<".center(64))
    print("-"*64)

    has_favorites = False

    for i, contact in enumerate(contacts, start=1):
        if contact["fav"]:
            has_favorites = True
            print(f"{i}. [⭐] {contact['name']} ∗ {contact['mobile']} ∗ {contact['email']}") # É para mostrar o index original mesmo. Isso é proposital. Posso mudar e criar uma lista apenas para os favoritos.
            print("-" * 64)

    if not has_favorites:
        print("No favorite contacts found.")
        print("-" * 64) 
            

# Terceira função - Editar contatos

def edit_contact(contacts, ctt_index):
    if not ctt_index.isdigit():
        print("Invalid contact ID. Try again.")
        return
    
    index_adjusted = int(ctt_index) - 1

    if index_adjusted < 0 or index_adjusted >= len(contacts):
        print("Index out of range. Try again.")
        return

    contact = contacts[index_adjusted]
    ctt_name = contact["name"]
    ctt_mobile = contact["mobile"]
    ctt_email = contact["email"]

        
    print("\n"+" EDITING A CONTACT ".center(64, '-')+"\n")
    print(f">>> What would you like to edit in '{ctt_name}'s contact?\n")

    print(f"1. [☻ ] {ctt_name}")
    print(f"2. [☎ ] {ctt_mobile}")
    print(f"3. [✉ ] {ctt_email}")
    
    if contacts[index_adjusted]["fav"] == True: 
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
            loading('\n...')
            system('cls')

        case "2":
            ctt_new_mobile = input("\n[new mobile] ").replace("-", "").replace(")", "").replace("(", "").replace(" ", "")
            contacts[index_adjusted]["mobile"] = ctt_new_mobile
            print('\n'+'-'*64)
            print(f"✓ Mobile successfully updated to '{ctt_new_mobile}' ✓".center(64))
            print("-"*64)
            loading('\n...')
            system('cls')

        case "3":
            ctt_new_email = input("\n[new email] ").lower()
            contacts[index_adjusted]["email"] = ctt_new_email
            print('\n'+'-'*64)
            print(f"✓ E-mail successfully updated to '{ctt_new_email}' ✓".center(64))
            print("-"*64)
            loading('\n...')
            system('cls')

        case "4":
            if contacts[index_adjusted]["fav"] == False:
                contacts[index_adjusted]["fav"] = True
                print('\n'+'-'*64)
                print(f"✓ '{ctt_name}' was successfully marked as favorite ✓".center(64))
                print("-"*64)
            else:
                contacts[index_adjusted]["fav"] = False
                print('\n'+'-'*64)
                print(f"✓ '{ctt_name}' was successfully removed from favorites ✓".center(64))
                print("-"*64)
            loading('\n...')
            system('cls')
        case _:
            unknown_command(1)
    return


# Quarta função - Deletar contatos

def delete_ctt(contacts, ctt_index):
    
    if not ctt_index.isdigit():
        print("Invalid contact ID. Try again.")
        return
    
    index_adjusted = int(ctt_index) - 1

    if index_adjusted < 0 or index_adjusted >= len(contacts):
        print("Index out of range. Try again.")
        return

    ctt_name = contacts[index_adjusted]["name"]
    contacts.pop(index_adjusted)

    print('\n'+'-'*64)
    print(f"✓ '{ctt_name}' was removed from your contact list ✓".center(64))
    print("-"*64)
    
    loading('\n...')
    system('cls')


contacts = []

while True:
    title_screen()  
    print("\n"+"="*29+" MENU "+"="*29)
    print("[1] Add contact")
    print("[2] View contact list")       # Inclui ver lista de favoritos
    print("[3] Edit existing contact")   # Inclui marcar como favorito
    print("[4] Delete a contact") 
    print("[5] Exit") 
    print("="*64)

    opt = input("[option] ")

    match opt:
        case "1":
            print("\n"+" CREATING A CONTACT ".center(64, '-')+"\n")
            ctt_name = input("[☻] ")
            ctt_mobile = input("[☎ ] ").replace("-", "").replace(")", "").replace("(", "").replace(" ", "") # futuramente adicionar uma função para formatar todos os números de uma forma bonita.

            ctt_email = input("[✉ ] ").lower() 

            add_contact(contacts, ctt_name, ctt_mobile, ctt_email)
        
        case "2":
            print("\n[1] See Favorites\n[2] See all contacts\n[3] << Back")
            opt_3 = input("[option] ")

            match opt_3:
                case "1":
                    see_fav_contacts(contacts)
                case "2":
                    see_contacts(contacts)
                case "3":
                    loading('\n...')
                    system('cls')
                    continue
                case _:
                    unknown_command(1)
                    continue

            print("[1] ← Back")
            print("[2] Edit contact")

            opt_2 = input("\n[option] ")

            match opt_2:
                case '1':
                    loading('\n...')
                    system('cls')

                case '2':
                    print("\n>>> Which contact do you want to edit?")
                    ctt_index = input("[id] ")
                    edit_contact(contacts, ctt_index)

                case _:
                    unknown_command(1)

        case "3":

            if len(contacts) == 0:
                print("[X] Add contacts first [X]")
                loading("\n...")
            
            else:
                see_contacts(contacts)
                print("\n>>> Which contact do you want to edit?")
                ctt_index = input("[id] ")
                edit_contact(contacts, ctt_index)

        case "4":
            if len(contacts) == 0:
                print("[X] Add contacts first [X]")
                loading("\n...")
            
            else:
                see_contacts(contacts)
                print("\n>>> Which contact do you want to delete?")
                ctt_index = input("[id] ")
                delete_ctt(contacts, ctt_index)

        case "5":
            break

        case _:
            unknown_command(1)