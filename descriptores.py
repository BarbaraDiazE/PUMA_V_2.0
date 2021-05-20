#importar librerias
import pandas as pd
import numpy as  np

#importar libreria rdkit y funciones
from rdkit import Chem
from rdkit import Chem
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import Draw, Descriptors

#definir df
Data = pd.read_csv("/Users/eurijuarez/Desktop/Alexis/Quimiotecas_Enfocadas/APEXBT_DiscoveryProbe-Epigenetics-Compound_Library_CURADA.csv")

#definir columna 
smiles = list(Data["NEW_SMILES"])
ID = list(Data["ID"])

#definir una lista vacia llamada sm
sm  = list()
#la funcion append guarda resultados de la funcion Chem.MolFromSmiles en la lista sm
for i in smiles:
    sm.append(Chem.MolFromSmiles(i))   

#definir listas
HBA = list()
HBD = list()
RB = list()
LogP = list()
TPSA = list()
MW = list()

#Calcular propidades
for i in sm:
    HBA.append(Descriptors.NumHAcceptors(i))
    HBD.append(Descriptors.NumHDonors(i))
    RB.append(Descriptors.NumRotatableBonds(i))
    LogP.append(Descriptors.MolLogP(i))
    TPSA.append(Descriptors.TPSA(i))
    MW.append(Descriptors.MolWt(i))
    
columns = ["ID","NEW_SMILES", "HBA", "HBD", "RB", "LogP", "TPSA", "MW"]
data = [ID,smiles, HBA, HBD, RB, LogP, TPSA, MW]
data = np.transpose(data, axes=None)

#Hacer un data frame con los smiles y las propiedades
Database = pd.DataFrame(
            data = data,
            columns = columns)
Database["Library"] = "APEXBIO"

#Guardar el resultado en un archivo .csv
Database.to_csv("/Users/eurijuarez/Desktop/Alexis/descriptores/APEXBIO_descriptores.csv", encoding="utf-8", index=True)