import pandas as pd
import numpy as np
import datetime
from datetime import date, timedelta
import os
from NOTIWEB.script_NOTICOVID import NOTICOVID_2022
from SISCOVID.script_SISCOVID import SISCOVID_2022
from NETLAB.script_NETLAB import NETLAB_2021 #descomentar si se utilizará netlab

def consolidar():
	#1. ###########LLAMANDO LA FUNCION DE NETLAB
	nlab= NETLAB_2021()# COMENTAR SEGUN SEA EL CASO DEL ARCHIVO 

	#2. ###########LLAMANDO LA FUNCION DE NOTIWEB
	nt = NOTICOVID_2022()
	nt_pcr=nt
	nt_pcr_mask=nt['Tipo de Prueba']=='Px PCR'
	nt_pcr=nt_pcr[nt_pcr_mask]

	nt_ant=nt
	nt_ant_mask=nt['Tipo de Prueba']=='Px Antígeno'
	nt_ant=nt_ant[nt_ant_mask]
	
	nt_rap=nt
	nt_rap_mask=nt['Tipo de Prueba']=='Px Rápida'
	nt_rap=nt_rap[nt_rap_mask]
  
	#3. ##########LLAMANDO A LA FUNCION SISCOVID###############
	si = SISCOVID_2022()

	sis_ant=si
	sis_ant_mask=si['Tipo de Prueba']=='Px Antígeno'
	sis_ant=sis_ant[sis_ant_mask]

	sis_rap=si
	sis_rap_mask=si['Tipo de Prueba']=='Px Rápida'
	sis_rap=sis_rap[sis_rap_mask]

	###################UNIR TODOS LOS FRAMES SEPARADOS################
	union=[nlab,nt_pcr,nt_ant,sis_ant,nt_rap,sis_rap] #agregar nlab al principio nlab,
	
	df_final = pd.concat(union)
	
	#ordena por ResultadoFinal y elimina los duplicados por Dni_Final
	df_final=df_final.sort_values('ResultadoFinal',ascending=False)
	df_final=df_final.drop_duplicates(subset=['Dni_Final'])

	df_final.to_excel('CONSOLIDADO_SIS_NOTI_NET.xlsx')
	#return(df_final)
consolidar()

