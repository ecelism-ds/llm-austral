replacements = {
    "HARRY": "ROBERTO", "POTTER": "GONZALES", "Harry": "Roberto", "Potter": "Gonzales",
    "Hermione": "Carolina", "Granger": "Fernandez", "HERMIONE": "CAROLINA", "GRANGER": "FERNANDEZ",
    "Ron": "Diego", "Weasley": "Lopez", "RON": "DIEGO", "WEASLEY": "LOPEZ",
    "Albus": "Alfonso", "Dumbledore": "Dominguez", "ALBUS": "ALFONSO", "DUMBLEDORE": "DOMINGUEZ",
    "Sirius": "Gustavo", "Black": "Martinez", "SIRIUS": "GUSTAVO", "BLACK": "MARTINEZ",
    "Severus": "Carlos", "Snape": "Peralta", "SEVERUS": "CARLOS", "SNAPE": "PERALTA",
    "Rubeus": "Matias", "Hagrid": "Villalba", "RUBEUS": "MATIAS", "HAGRID": "VILLALBA",
    "Draco": "Javier", "Malfoy": "Sosa", "DRACO": "JAVIER", "MALFOY": "SOSA",
    "Minerva": "Elena", "McGonagall": "Romero", "MINERVA": "ELENA", "MCGONAGALL": "ROMERO",
    "Voldemort": "Salvador", "VOLDEMORT": "SALVADOR",
    "Tom": "Oscar", "Riddle": "Castillo", "TOM": "OSCAR", "RIDDLE": "CASTILLO",
    "Lily": "Sofia", "James": "Ricardo", "LILY": "SOFIA", "JAMES": "RICARDO",
    "Remus": "Pedro", "Lupin": "Cardozo", "REMUS": "PEDRO", "LUPIN": "CARDOZO",
    "Bellatrix": "Miranda", "Lestrange": "Gimenez", "BELLATRIX": "MIRANDA", "LESTRANGE": "GIMENEZ",
    "Lucius": "Mariano", "LUCIUS": "MARIANO",
    "Narcissa": "Julia", "NARCISSA": "JULIA",
    "Neville": "Mauricio", "Longbottom": "Silva", "NEVILLE": "MAURICIO", "LONGBOTTOM": "SILVA",
    "Ginny": "Martina", "GINNY": "MARTINA",
    "Fred": "Pablo", "George": "Luis", "FRED": "PABLO", "GEORGE": "LUIS",
    "Percy": "Miguel", "PERCY": "MIGUEL",
    "Arthur": "Raul", "Molly": "Alicia", "ARTHUR": "RAUL", "MOLLY": "ALICIA",
    "Fleur": "Camila", "Delacour": "Saenz", "FLEUR": "CAMILA", "DELACOUR": "SAENZ",
    "Cedric": "Nicolas", "Diggory": "Ortega", "CEDRIC": "NICOLAS", "DIGGORY": "ORTEGA",
    "Cho": "Paula", "Chang": "Mejia", "CHO": "PAULA", "CHANG": "MEJIA",
    "Luna": "Gabriela", "Lovegood": "Ortiz", "LUNA": "GABRIELA", "LOVEGOOD": "ORTIZ",
    "Nymphadora": "Viviana", "Tonks": "Perez", "NYMPHADORA": "VIVIANA", "TONKS": "PEREZ",
    "Kingsley": "Hector", "Shacklebolt": "Maldonado", "KINGSLEY": "HECTOR", "SHACKLEBOLT": "MALDONADO",
    "Horace": "Eduardo", "Slughorn": "Ramirez", "HORACE": "EDUARDO", "SLUGHORN": "RAMIREZ",
    "Igor": "Ramon", "Karkaroff": "Morales", "IGOR": "RAMON", "KARKAROFF": "MORALES",
    "Gellert": "Alberto", "Grindelwald": "Guzman", "GELLERT": "ALBERTO", "GRINDELWALD": "GUZMAN",
    "Moody": "Acosta", "MOODY": "ACOSTA",
    "Pettigrew": "Salazar", "Peter": "Gonzalo", "PETTIGREW": "SALAZAR", "PETER": "GONZALO",
    "Dudley": "Leonardo", "Dursley": "Carrizo", "DUDLEY": "LEONARDO", "DURSLEY": "CARRIZO",
    "Vernon": "Francisco", "Petunia": "Beatriz", "VERNON": "FRANCISCO", "PETUNIA": "BEATRIZ"
}

def replace_names_in_directory(dir_path, replacements):
    """
    Replaces occurrences of specified strings in all .txt files in a directory
    and saves the modified files in a new directory with "_modified" appended to the original path.

    Parameters:
    - dir_path (str): Path to the directory containing .txt files.
    - replacements (dict): Dictionary of names to replace in the format {'Original Name': 'New Name'}.
    """
    modified_dir_path = dir_path + "_modified"
    os.makedirs(modified_dir_path, exist_ok=True)

    for filename in os.listdir(dir_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(dir_path, filename)

            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            for old_name, new_name in replacements.items():
                content = content.replace(old_name, new_name)

            modified_file_path = os.path.join(modified_dir_path, filename)
            with open(modified_file_path, 'w', encoding='utf-8') as modified_file:
                modified_file.write(content)

            print(f"Processed and saved: {modified_file_path}")

if __name__ == "__main__":
    replace_names_in_directory('../../data/practica_rag/harry_potter_books/')
    