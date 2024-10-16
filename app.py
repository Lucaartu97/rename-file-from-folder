import os

def rename_files_in_directory(directory, old_word, new_word):
    # Cambia la directory a quella specificata
    os.chdir(directory)
    
    # Itera attraverso tutti i file nella directory
    for filename in os.listdir(directory):
        # Controlla se la parola da sostituire è nel nome del file
        if old_word in filename:
            # Crea il nuovo nome sostituendo la parola
            new_filename = filename.replace(old_word, new_word)
            # Rinomina il file
            os.rename(filename, new_filename)
            print(f'Rinominato: {filename} -> {new_filename}')

# Esempio di utilizzo
directory_path = '/percorso/della/cartella'  # Sostituisci con il percorso della tua cartella
old_word = 'old word'  # La parola da sostituire
new_word = 'new word'  # La nuova parola

rename_files_in_directory(directory_path, old_word, new_word)
