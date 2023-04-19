def moyenne():
    note_oral_fr = cursor.execute("SELECT note_oral_fr FROM eleves")*5
    note_ecrit_fr = cursor.execute("SELECT note_ecrit_fr FROM eleves")*5
    note_spe_1 = cursor.execute("SELECT note_spe_1 FROM eleves")*16
    note_spe_2 = cursor.execute("SELECT note_spe_2 FROM eleves")*16
    note_grand_oral = cursor.execute("SELECT note_grand_oral FROM eleves")*10
    note_philosophie = cursor.execute("SELECT note_philosophie FROM eleves")*8