charSpe = False 
Liste_char = ["!","°","?","&","@","#","%"]

def test(mdp):
    sécurité = True
    
    if len(mdp) < 8:
        print("Le mot de passe est trop court.")
        sécurité = False
        
    if not any(c.isdigit() for c in mdp):
        print("Le mot de passe ne contient pas de chiffres.")
        sécurité = False
        
    if not any(c.isupper() for c in mdp):
        print("Le mot de passe ne contient pas de majuscules.")
        sécurité = False
        
    if not any(char in Liste_char for char in mdp):
        print("Le mot de passe ne contient pas de caractères spéciaux.")
        sécurité = False
    
    return sécurité

mdp = input("Entrer un nouveau mot de passe : ")

while not test(mdp):
    print("Le mot de passe n'est pas sécurisé.")
    mdp = input("Entrer un nouveau mot de passe : ")

print("Le mot de passe est sécurisé.")