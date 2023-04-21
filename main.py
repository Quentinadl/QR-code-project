import qrcode
from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image
import webbrowser

def generate_qr_code():
    link = input("Entrez le lien que vous souhaitez associer au QR code : ")
    version = int(input("Entrez la version du QR code (entre 1 et 40) : "))
    box_size = int(input("Entrez la taille des boîtes en pixels : "))
    border = int(input("Entrez la largeur de la bordure en modules : "))
    fill_color = input("Entrez la couleur de remplissage (ex: black, blue, #ffffff) : ")
    back_color = input("Entrez la couleur de fond (ex: white, red, #000000) : ")
    
    qr = qrcode.QRCode(version=version, box_size=box_size, border=border)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    filename = input("Entrez le nom du fichier de sortie (avec l'extension .png ou .jpg) : ")
    img.save(filename)
    print(f"Le QR code a été généré et enregistré sous le nom {filename}.")

def read_qr_code():
    filename = input("Entrez le nom du fichier contenant le QR code à lire : ")
    img = Image.open(filename)
    data = decode(img, symbols=[ZBarSymbol.QRCODE])
    if len(data) > 0:
        link = data[0].data.decode('utf-8')
        print(f"Le QR code lu correspond au lien suivant : {link}.")
        webbrowser.open(link)
    else:
        print("Le fichier ne contient pas de QR code.")

def modify_qr_code():
    filename = input("Entrez le nom du fichier contenant le QR code à modifier : ")
    img = Image.open(filename)
    data = decode(img, symbols=[ZBarSymbol.QRCODE])
    if len(data) > 0:
        old_link = data[0].data.decode('utf-8')
        print(f"Lien actuel associé au QR code : {old_link}.")
        new_link = input("Entrez le nouveau lien que vous souhaitez associer au QR code : ")
        qr = qrcode.QRCode(version=None, box_size=10, border=5)
        qr.add_data(new_link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        print(f"Le lien associé au QR code a été modifié pour : {new_link}.")
    else:
        print("Le fichier ne contient pas de QR code.")

while True:
    print("\nQue souhaitez-vous faire ?")
    print("1 - Générer un QR code")
    print("2 - Lire un QR code")
    print("3 - Modifier un QR code")
    print("0 - Quitter")
    
    choice = int(input("Entrez votre choix : "))
    
    if choice == 1:
        generate_qr_code()
    elif choice == 2:
        read_qr_code()
    elif choice == 3:
        modify_qr_code()
    elif choice == 0:
        break
    else:
        print("Choix invalide. Veuillez entrer un choix valide.")
