import pandas as pd
import numpy as np
import datetime
from datetime import date, timedelta

import os

def NETLAB_2021():
	current_dir = os.path.dirname(os.path.realpath(__file__))
	#MOLECULAR PCR
	###################################################################################
	objxls=os.path.join(current_dir, "DATASOURCE/NETLAB-2022.xlsx")    #lee ruta del archivo
	obj=pd.read_excel(objxls)#lee el archivo excel
	df=pd.DataFrame(obj)#le pone en dataframe
	#df_union=[df]
	#df=pd.concat(df_union)
	df_nl=df
	df_nl["Nombre de Examen"]=['SI' if str(r).find('SARS')!= -1 else r for r in df['Nombre de Examen']]
	
	df_nl_mask=df_nl['Nombre de Examen']=='SI'
	df_nl=df_nl[df_nl_mask]

	df=df_nl

	df= df.loc[:,['Documento Identidad',
	'Paciente','Genero','Edad',
	'Distrito EE.SS Origen','Provincia EE.SS Origen',
	'Fecha Colección',
	'Resultado',
	'Direccion de Paciente']]

	df['Genero']=df['Genero'].replace(['Femenino','Masculino'],['F','M'])

	df["Resultado"]=["NEGATIVO" if str(r).find('NEGATIVO')!= -1 else r for r in df['Resultado']]
	df["Resultado"]=["POSITIVO" if str(r).find('POSITIVO')!= -1 else r for r in df['Resultado']]
	df["Resultado"]=[r if str(r).find('POSITIVO')!= -1 or str(r).find('NEGATIVO')!= -1 else 'NO_RESULT' for r in df['Resultado']]
	df_mask=df['Resultado']!='NO_RESULT'
	df=df[df_mask]

	df['ResultadoFinal']=df['Resultado']

	df['Documento Identidad']=[str(r[6:15]) for r in df['Documento Identidad']]

	#AgregandoCampos conforme se va definiendo
	df['Nro']=1
	df['Tipo de Prueba']='Px PCR'
	df['ResultadoFinal']=df['Resultado']
	df['Fuente']='NETLAB'
	
	df['Fecha Colección']=pd.to_datetime(df['Fecha Colección'])#convertimos campo a tipo fecha
	#df['Fecha Colección']=df['Fecha Colección'].dt.strftime('%d/%m/%Y')#damos formato dia/mes/año x k estaba mes/dia/año
	#df['Fecha Colección']=pd.to_datetime(df['Fecha Colección'], infer_datetime_format=True)#volvemos a aplicar formato fecha
	
	df['Semana']=df['Fecha Colección'].dt.isocalendar().week
	df['AÑO']=df['Fecha Colección'].dt.year
	df['MES']=df['Fecha Colección'].dt.month
	df['DIA']=df['Fecha Colección'].dt.day

	df['Ultimos 07 Dias']='0'
	###############################################################
	td=timedelta(0)#EL NUMERO ES LA DIFERENCIA DE DIAS 
	today = pd.datetime.now() - td
	df['Dias Transcurridos']=(today - df['Fecha Colección']).dt.days
	###############################################################
	condition=[
	(df['Dias Transcurridos'] < 15) &
	(df['ResultadoFinal'] == 'POSITIVO'),
	(df['Dias Transcurridos'] > 14) &
	(df['ResultadoFinal'] == 'POSITIVO')|
	(df['ResultadoFinal'] == 'IgG'),
	(df['ResultadoFinal'] == 'NEGATIVO')
	]
	values=['AISLAMIENTO DOMICILIARIO','ALTAS CLÍNICAS Y HOSPITALARIAS','NEGATIVO']
	df['Estado Actual']=np.select(condition,values)
	df['Fallecido']='NO'
	df['Usuario']=''
	df['Etnia']=''
	df['Personal Salud']=''
	df['cod_establecimiento_ejecuta']=''
	df['Establecimiento_Ejecuta']=''
	#################################################3
	conditions=[
		(df['Edad']<12),
		(df['Edad']<18),
		(df['Edad']<30),
		(df['Edad']<60),
		(df['Edad']<200),
	]
	#Create a List values of each conditions
	values =['Niño','Adolescente','Joven','Adulto','Adulto Mayor']
	df["Etapa de Vida"]=np.select(conditions,values)

	df['Fecha Inicio Sintomas de la Ficha Paciente']=''

	df=df.rename(columns={'Documento Identidad':'Dni_Final','Paciente':'NombreCompleto',
		'Genero':'comun_sexo_paciente','Distrito EE.SS Origen':'Distrito',
		'Provincia EE.SS Origen':'Provincia','Fecha Colección':'Fecha Ejecucion Prueba',
		'Direccion de Paciente':'Direccion'})
	
	df["Provincia"]=df['Provincia'].str.replace('MARISCAL RAMON CASTILLA','RAMON CASTILLA')#CORRIGE MARISCAL RAMON CASTILLA A RAMON CASTILLA

	df["Distrito"]=df['Distrito'].str.replace('BALSAPUERTO','160202 - BALSAPUERTO')
	df["Distrito"]=df['Distrito'].str.replace('JEBEROS','160205 - JEBEROS')
	df["Distrito"]=df['Distrito'].str.replace('LAGUNAS','160206 - LAGUNAS')
	df["Distrito"]=df['Distrito'].str.replace('SANTA CRUZ','160210 - SANTA CRUZ')
	df["Distrito"]=df['Distrito'].str.replace('TENIENTE CESAR LOPEZ ROJAS','160211 - TENIENTE CESAR LOPEZ ROJAS')
	df["Distrito"]=df['Distrito'].str.replace('YURIMAGUAS','160201 - YURIMAGUAS')
	df["Distrito"]=df['Distrito'].str.replace('ANDOAS','160706 - ANDOAS')
	df["Distrito"]=df['Distrito'].str.replace('BARRANCA','160701 - BARRANCA')
	df["Distrito"]=df['Distrito'].str.replace('CAHUAPANAS','160702 - CAHUAPANAS')
	df["Distrito"]=df['Distrito'].str.replace('MANSERICHE','160703 - MANSERICHE')
	df["Distrito"]=df['Distrito'].str.replace('MORONA','160704 - MORONA')
	df["Distrito"]=df['Distrito'].str.replace('PASTAZA','160705 - PASTAZA')
	df["Distrito"]=df['Distrito'].str.replace('NAUTA','160301 - NAUTA')
	df["Distrito"]=df['Distrito'].str.replace('PARINARI','160302 - PARINARI')
	df["Distrito"]=df['Distrito'].str.replace('TIGRE','160303 - TIGRE')
	df["Distrito"]=df['Distrito'].str.replace('TROMPETEROS','160304 - TROMPETEROS')
	df["Distrito"]=df['Distrito'].str.replace('URARINAS','160305 - URARINAS')
	df["Distrito"]=df['Distrito'].str.replace('ALTO NANAY','160102 - ALTO NANAY')
	df["Distrito"]=df['Distrito'].str.replace('BELEN','160112 - BELEN')
	df["Distrito"]=df['Distrito'].str.replace('INDIANA','160104 - INDIANA')
	df["Distrito"]=df['Distrito'].str.replace('IQUITOS','160101 - IQUITOS')
	df["Distrito"]=df['Distrito'].str.replace('FERNANDO LORES','160103 - FERNANDO LORES')
	df["Distrito"]=df['Distrito'].str.replace('LAS AMAZONAS','160105 - LAS AMAZONAS')
	df["Distrito"]=df['Distrito'].str.replace('MAZAN','160106 - MAZAN')
	df["Distrito"]=df['Distrito'].str.replace('NAPO','160107 - NAPO')
	df["Distrito"]=df['Distrito'].str.replace('PUNCHANA','160108 - PUNCHANA')
	df["Distrito"]=df['Distrito'].str.replace('TORRES CAUSANA','160110 - TORRES CAUSANA')
	df["Distrito"]=df['Distrito'].str.replace('SAN JUAN BAUTISTA','160113 - SAN JUAN BAUTISTA')
	df["Distrito"]=df['Distrito'].str.replace('PEBAS','160402 - PEBAS')
	#df["Distrito"]=df['Distrito'].str.replace('MARISCAL','')
	df["Distrito"]=df['Distrito'].str.replace('RAMON CASTILLA','160401 - RAMON CASTILLA')
	df["Distrito"]=df['Distrito'].str.replace('SAN PABLO','160404 - SAN PABLO')
	df["Distrito"]=df['Distrito'].str.replace('YAVARI','160403 - YAVARI')
	df['Distrito']=['160509 - TAPICHE' if str(r)=='TAPICHE' else r for r in df['Distrito']]
	#df["Distrito"]=df['Distrito'].str.replace('TAPICHE','160509 - TAPICHE')
	df["Distrito"]=df['Distrito'].str.replace('CAPELO','160503 - CAPELO')
	df["Distrito"]=df['Distrito'].str.replace('EMILIO SAN MARTIN','160504 - EMILIO SAN MARTIN')
	df["Distrito"]=df['Distrito'].str.replace('JENARO HERRERA','160510 - JENARO HERRERA')
	df["Distrito"]=df['Distrito'].str.replace('MAQUIA','160505 - MAQUIA')
	df["Distrito"]=df['Distrito'].str.replace('PUINAHUA','160506 - PUINAHUA')
	df["Distrito"]=df['Distrito'].str.replace('REQUENA','160501 - REQUENA')
	df["Distrito"]=df['Distrito'].str.replace('SAQUENA','160507 - SAQUENA')
	df["Distrito"]=df['Distrito'].str.replace('SOPLIN','160508 - SOPLIN')
	df['Distrito']=['160502 - ALTO TAPICHE' if str(r)=='ALTO TAPICHE' else r for r in df['Distrito']]
	#df["Distrito"]=df['Distrito'].str.replace('ALTO TAPICHE','160502 - ALTO TAPICHE')
	df["Distrito"]=df['Distrito'].str.replace('YAQUERANA','160511 - YAQUERANA')
	df["Distrito"]=df['Distrito'].str.replace('CONTAMANA','160601 - CONTAMANA')
	df["Distrito"]=df['Distrito'].str.replace('INAHUAYA','160602 - INAHUAYA')
	df["Distrito"]=df['Distrito'].str.replace('PADRE MARQUEZ','160603 - PADRE MARQUEZ')
	df["Distrito"]=df['Distrito'].str.replace('PAMPA HERMOSA','160604 - PAMPA HERMOSA')
	df["Distrito"]=df['Distrito'].str.replace('SARAYACU','160605 - SARAYACU')
	df["Distrito"]=df['Distrito'].str.replace('VARGAS GUERRA','160606 - VARGAS GUERRA')
	df["Distrito"]=df['Distrito'].str.replace('PUTUMAYO','160801 - PUTUMAYO')
	df["Distrito"]=df['Distrito'].str.replace('ROSA PANDURO','160802 - ROSA PANDURO')
	df["Distrito"]=df['Distrito'].str.replace('TENIENTE MANUEL CLAVERO','160803 - TENIENTE MANUEL CLAVERO')
	df["Distrito"]=df['Distrito'].str.replace('YAGUAS','160804 - YAGUAS')


	df= df.loc[:,['Nro','Tipo de Prueba','Dni_Final',
	'NombreCompleto','comun_sexo_paciente','Edad',
	'Etapa de Vida','Distrito','Provincia',
	'Fecha Inicio Sintomas de la Ficha Paciente',
	'Fecha Ejecucion Prueba','Semana','AÑO','MES','DIA',
	'Ultimos 07 Dias','Dias Transcurridos','Estado Actual',
	'Fallecido','Resultado','ResultadoFinal','Fuente','Usuario',
	'Etnia','cod_establecimiento_ejecuta','Establecimiento_Ejecuta','Direccion','Personal Salud']]
	#df.to_excel('RESULT/TEST_NETLAB.xlsx')
	return(df)
NETLAB_2021()