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

    print('-'*64)
    print(f"✓ Contact of '{ctt_name}' was successfully added ✓".center(64))
    print('-'*64)

    return






contacts = []
title_screen()

while True:
    print("\n"+"-"*29+" MENU "+"-"*29)
    print("[1] Add contact")
    print("[2] See contacts list")       # Inclui ver lista de favoritos
    print("[3] Edit existing contact")   # Inclui marcar como favorito
    print("[4] Delete/Block a contact") 
    print("="*64)

    opt = input("[option] ")

    match opt:
        case "1":
            print("\nLet's add a Contact!\n")
            ctt_name = input("[☻] ")
            ctt_mobile = input("[☎ ] ")
            ctt_email = input("[✉ ] ")

            add_contact(contacts, ctt_name, ctt_mobile, ctt_email)
        
        case "2":
            print("")
        case "3":
            print("")
        case "4":
            print("")
        case _:
            print("Unknown command. Try again")

    
