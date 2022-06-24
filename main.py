from utils import Data, Say, id_to_int_iter
from load import Load
import pandas as pd
import time


import resume
import normalizar
import export
import data_quality as quality

say = Say()
load = Load(path="in")
data = Data(path="in")


if __name__ == "__main__":

    print(
        """___________ __  .__       _____          __                         __  .__                    .___                 
\_   _____//  |_|  |     /  _  \  __ ___/  |_  ____   _____ _____ _/  |_|__|____________     __| _/____             
 |    __)_\   __\  |    /  /_\  \|  |  \   __\/  _ \ /     \\__  \\   __\  \___   /\__  \   / __ |/  _ \            
 |        \|  | |  |__ /    |    \  |  /|  | (  <_> )  Y Y  \/ __ \|  | |  |/    /  / __ \_/ /_/ (  <_> )           
/_______  /|__| |____/ \____|__  /____/ |__|  \____/|__|_|  (____  /__| |__/_____ \(____  /\____ |\____/            
        \/                     \/                         \/     \/              \/     \/      \/                  
                                                                                                                    
                                                                                                                    
                                                                                                                    
                                                                                                                    
                                                                                                                    
                                                                                                                    
__________            _____                                .__        _______          __                .___       
\______   \___.__.   /     \ _____    ___________    _____ |__| ____  \      \ _____  |  | _______     __| _/____   
 |    |  _<   |  |  /  \ /  \\__  \  /  ___/\__  \  /     \|  |/  _ \ /   |   \\__  \ |  |/ /\__  \   / __ |\__  \  
 |    |   \\___  | /    Y    \/ __ \_\___ \  / __ \|  Y Y  \  (  <_> )    |    \/ __ \|    <  / __ \_/ /_/ | / __ \_
 |______  // ____| \____|__  (____  /____  >(____  /__|_|  /__|\____/\____|__  (____  /__|_ \(____  /\____ |(____  /
        \/ \/              \/     \/     \/      \/      \/                  \/     \/     \/     \/      \/     \/ """
    )

    time.sleep(1)

    # cargamos del directorio in los dataframes
    try:
        labels = data.get_labels(path="in")
        data_dict = load.load_datasets_from_csv(path="in")
    except ValueError:
        say.cow_says_error("Error al cargar base de datos")

    # convertimos las columnas fechas a objeto -> datetime
    resume.dataset_date_iter(data_dict, labels)

    time.sleep(0.5)

    # todas las columnas tipo id se convierten en entero
    data_dict = id_to_int_iter(data_dict, labels)

    time.sleep(0.5)

    # normalizar los dataframes
    data_dict = normalizar.normalizar_all(data_dict)

    time.sleep(0.5)

    # imprimos el resumen de los dataframes
    resume.resume_dataframe(data_dict, labels)

    time.sleep(0.5)

    # Report de Calidad de los datos png
    quality.visual_report_iter(data_dict, labels)

    time.sleep(0.5)

    # Report autogenerado markdown
    quality.genarator_md_iter(labels)

    time.sleep(0.5)

    # export to csv
    export.export_to_csv(data_dict, labels)
