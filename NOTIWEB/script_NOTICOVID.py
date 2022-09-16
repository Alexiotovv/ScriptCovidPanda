import pandas as pd
import numpy as np
import datetime
from datetime import date, timedelta
import os
def NOTICOVID_2022():
	
	current_dir = os.path.dirname(os.path.realpath(__file__))
	#MOLECULAR PCR
	###################################################################################
	#objxls1=os.path.join(current_dir, "DATASOURCE/NOTIWEB-2021.xlsx")#lee ruta del file NOTIWEB-2021
	objxls2=os.path.join(current_dir, "DATASOURCE/NOTIWEB-2022.xlsx")#lee ruta del file NOTIWEB-2022
	
	#obj1=pd.read_excel(objxls1)#lee el archivo excel1
	obj2=pd.read_excel(objxls2)#lee el archivo excel2

	#df1=pd.DataFrame(obj1)#le pone en dataframe
	df2=pd.DataFrame(obj2)
	union_df1_df2=[df2]# df1, une los 2 archivos 2021-2022
	df=pd.concat(union_df1_df2)#concatena la union de 2021-2022

	df=df.loc[:,['id','numdoc','apenom','sexo','edad','distrito','provincia','prueba','fecha_mue','resultado','usuario_reg','pueblo_etnico','ipress','ipress_hos','nombre_via','otros_sintomas','trabajador_salud']]
	df['sexo']=df['sexo'].replace(['FEMENINO','MASCULINO'],['F','M'])

	df.insert(1,"Nro",0,allow_duplicates=True)
	df.insert(9,"ResultadoFinal","",allow_duplicates=True)
	df.insert(2,"TIPOPRUEBA","",allow_duplicates=True)
	df.insert(10,"Fuente","NOTIWEB",allow_duplicates=True)
	df.insert(8,"Semana","",allow_duplicates=True)
	df.insert(9,"AÑO","",allow_duplicates=True)
	df.insert(10,"MES","",allow_duplicates=True)
	df.insert(10,"InicioSintomas","",allow_duplicates=True)
	df.insert(11,"DIA","",allow_duplicates=True)
	df.insert(12,"Ultimos 07 Dias","0",allow_duplicates=True)
	df.insert(13,"Dias Transcurridos","",allow_duplicates=True)
	df.insert(14,"Estado Actual","",allow_duplicates=True)
	df.insert(15,"Fallecido","",allow_duplicates=True)
	df.insert(1,"Dni_Final","",allow_duplicates=True)
	df.insert(5,"Etapa de Vida","",allow_duplicates=True)

	df["Dni_Final"]=["00000000"+ str(r) for r in df['numdoc']]
	df["Dni_Final"]=[str(r)[-8:] for r in df['Dni_Final']]
	df["Dni_Final"]=df['Dni_Final'].str.replace('nan','00000000')

	df['provincia']=['RAMON CASTILLA' if r =='MARISCAL RAMON CASTILLA' else r for r in df['provincia']]

	#Create a List of our conditions
	conditionsp=[
	(df['distrito']=='BALSAPUERTO'),
	(df['distrito']=='JEBEROS'),
	(df['distrito']=='LAGUNAS'),
	(df['distrito']=='SANTA CRUZ'),
	(df['distrito']=='TENIENTE CESAR LOPEZ ROJAS'),
	(df['distrito']=='YURIMAGUAS'),
	(df['distrito']=='ANDOAS'),
	(df['distrito']=='BARRANCA'),
	(df['distrito']=='CAHUAPANAS'),
	(df['distrito']=='MANSERICHE'),
	(df['distrito']=='MORONA'),
	(df['distrito']=='PASTAZA'),
	(df['distrito']=='NAUTA'),
	(df['distrito']=='PARINARI'),
	(df['distrito']=='TIGRE'),
	(df['distrito']=='TROMPETEROS'),
	(df['distrito']=='URARINAS'),
	(df['distrito']=='ALTO NANAY'),
	(df['distrito']=='BELEN'),
	(df['distrito']=='INDIANA'),
	(df['distrito']=='IQUITOS'),
	(df['distrito']=='FERNANDO LORES'),
	(df['distrito']=='LAS AMAZONAS'),
	(df['distrito']=='MAZAN'),
	(df['distrito']=='NAPO'),
	(df['distrito']=='PUNCHANA'),
	(df['distrito']=='TORRES CAUSANA'),
	(df['distrito']=='SAN JUAN BAUTISTA'),
	(df['distrito']=='PEBAS'),
	(df['distrito']=='RAMON CASTILLA'),
	(df['distrito']=='SAN PABLO'),
	(df['distrito']=='YAVARI'),
	(df['distrito']=='ALTO TAPICHE'),
	(df['distrito']=='CAPELO'),
	(df['distrito']=='EMILIO SAN MARTIN'),
	(df['distrito']=='JENARO HERRERA'),
	(df['distrito']=='MAQUIA'),
	(df['distrito']=='PUINAHUA'),
	(df['distrito']=='REQUENA'),
	(df['distrito']=='SAQUENA'),
	(df['distrito']=='SOPLIN'),
	(df['distrito']=='TAPICHE'),
	(df['distrito']=='YAQUERANA'),
	(df['distrito']=='CONTAMANA'),
	(df['distrito']=='INAHUAYA'),
	(df['distrito']=='PADRE MARQUEZ'),
	(df['distrito']=='PAMPA HERMOSA'),
	(df['distrito']=='SARAYACU'),
	(df['distrito']=='VARGAS GUERRA'),
	(df['distrito']=='PUTUMAYO'),
	(df['distrito']=='ROSA PANDURO'),
	(df['distrito']=='TENIENTE MANUEL CLAVERO'),
	(df['distrito']=='YAGUAS'),
	]

	valuesp=['ALTO AMAZONAS',
	'ALTO AMAZONAS',
	'ALTO AMAZONAS',
	'ALTO AMAZONAS',
	'ALTO AMAZONAS',
	'ALTO AMAZONAS',
	'DATEM DEL MARAÑON',
	'DATEM DEL MARAÑON',
	'DATEM DEL MARAÑON',
	'DATEM DEL MARAÑON',
	'DATEM DEL MARAÑON',
	'DATEM DEL MARAÑON',
	'LORETO',
	'LORETO',
	'LORETO',
	'LORETO',
	'LORETO',
	'MAYNAS',
	'MAYNAS',
	'MAYNAS',
	'MAYNAS',
	'MAYNAS',
	'MAYNAS',
	'MAYNAS',
	'MAYNAS',
	'MAYNAS',
	'MAYNAS',
	'MAYNAS',
	'RAMON CASTILLA',
	'RAMON CASTILLA',
	'RAMON CASTILLA',
	'RAMON CASTILLA',
	'REQUENA',
	'REQUENA',
	'REQUENA',
	'REQUENA',
	'REQUENA',
	'REQUENA',
	'REQUENA',
	'REQUENA',
	'REQUENA',
	'REQUENA',
	'REQUENA',
	'UCAYALI',
	'UCAYALI',
	'UCAYALI',
	'UCAYALI',
	'UCAYALI',
	'UCAYALI',
	'PUTUMAYO',
	'PUTUMAYO',
	'PUTUMAYO',
	'PUTUMAYO'
	]

	df["provincia"]=np.select(conditionsp,valuesp)
	#df["Provincia"]=df['Provincia'].str.replace('BALSAPUERTO','160202 - BALSAPUERTO')

	df["distrito"]=df['distrito'].str.replace('BALSAPUERTO','160202 - BALSAPUERTO')
	df["distrito"]=df['distrito'].str.replace('JEBEROS','160205 - JEBEROS')
	df["distrito"]=df['distrito'].str.replace('LAGUNAS','160206 - LAGUNAS')
	df["distrito"]=df['distrito'].str.replace('SANTA CRUZ','160210 - SANTA CRUZ')
	df["distrito"]=df['distrito'].str.replace('TENIENTE CESAR LOPEZ ROJAS','160211 - TENIENTE CESAR LOPEZ ROJAS')
	df["distrito"]=df['distrito'].str.replace('YURIMAGUAS','160201 - YURIMAGUAS')
	df["distrito"]=df['distrito'].str.replace('ANDOAS','160706 - ANDOAS')
	df["distrito"]=df['distrito'].str.replace('BARRANCA','160701 - BARRANCA')
	df["distrito"]=df['distrito'].str.replace('CAHUAPANAS','160702 - CAHUAPANAS')
	df["distrito"]=df['distrito'].str.replace('MANSERICHE','160703 - MANSERICHE')
	df["distrito"]=df['distrito'].str.replace('MORONA','160704 - MORONA')
	df["distrito"]=df['distrito'].str.replace('PASTAZA','160705 - PASTAZA')
	df["distrito"]=df['distrito'].str.replace('NAUTA','160301 - NAUTA')
	df["distrito"]=df['distrito'].str.replace('PARINARI','160302 - PARINARI')
	df["distrito"]=df['distrito'].str.replace('TIGRE','160303 - TIGRE')
	df["distrito"]=df['distrito'].str.replace('TROMPETEROS','160304 - TROMPETEROS')
	df["distrito"]=df['distrito'].str.replace('URARINAS','160305 - URARINAS')
	df["distrito"]=df['distrito'].str.replace('ALTO NANAY','160102 - ALTO NANAY')
	df["distrito"]=df['distrito'].str.replace('BELEN','160112 - BELEN')
	df["distrito"]=df['distrito'].str.replace('INDIANA','160104 - INDIANA')
	df["distrito"]=df['distrito'].str.replace('IQUITOS','160101 - IQUITOS')
	df["distrito"]=df['distrito'].str.replace('FERNANDO LORES','160103 - FERNANDO LORES')
	df["distrito"]=df['distrito'].str.replace('LAS AMAZONAS','160105 - LAS AMAZONAS')
	df["distrito"]=df['distrito'].str.replace('MAZAN','160106 - MAZAN')
	df["distrito"]=df['distrito'].str.replace('NAPO','160107 - NAPO')
	df["distrito"]=df['distrito'].str.replace('PUNCHANA','160108 - PUNCHANA')
	df["distrito"]=df['distrito'].str.replace('TORRES CAUSANA','160110 - TORRES CAUSANA')
	df["distrito"]=df['distrito'].str.replace('SAN JUAN BAUTISTA','160113 - SAN JUAN BAUTISTA')
	df["distrito"]=df['distrito'].str.replace('PEBAS','160402 - PEBAS')
	df["distrito"]=df['distrito'].str.replace('RAMON CASTILLA','160401 - RAMON CASTILLA')
	df["distrito"]=df['distrito'].str.replace('SAN PABLO','160404 - SAN PABLO')
	df["distrito"]=df['distrito'].str.replace('YAVARI','160403 - YAVARI')
	df['distrito']=['160509 - TAPICHE' if str(r)=='TAPICHE' else r for r in df['distrito']]
	#df["distrito"]=df['distrito'].str.replace('ALTO TAPICHE','160502 - ALTO TAPICHE')
	df["distrito"]=df['distrito'].str.replace('CAPELO','160503 - CAPELO')
	df["distrito"]=df['distrito'].str.replace('EMILIO SAN MARTIN','160504 - EMILIO SAN MARTIN')
	df["distrito"]=df['distrito'].str.replace('JENARO HERRERA','160510 - JENARO HERRERA')
	df["distrito"]=df['distrito'].str.replace('MAQUIA','160505 - MAQUIA')
	df["distrito"]=df['distrito'].str.replace('PUINAHUA','160506 - PUINAHUA')
	df["distrito"]=df['distrito'].str.replace('REQUENA','160501 - REQUENA')
	df["distrito"]=df['distrito'].str.replace('SAQUENA','160507 - SAQUENA')
	df["distrito"]=df['distrito'].str.replace('SOPLIN','160508 - SOPLIN')
	df['distrito']=['160502 - ALTO TAPICHE' if str(r)=='ALTO TAPICHE' else r for r in df['distrito']]
	#df["distrito"]=df['distrito'].str.replace('TAPICHE','160509 - TAPICHE')
	df["distrito"]=df['distrito'].str.replace('YAQUERANA','160511 - YAQUERANA')
	df["distrito"]=df['distrito'].str.replace('CONTAMANA','160601 - CONTAMANA')
	df["distrito"]=df['distrito'].str.replace('INAHUAYA','160602 - INAHUAYA')
	df["distrito"]=df['distrito'].str.replace('PADRE MARQUEZ','160603 - PADRE MARQUEZ')
	df["distrito"]=df['distrito'].str.replace('PAMPA HERMOSA','160604 - PAMPA HERMOSA')
	df["distrito"]=df['distrito'].str.replace('SARAYACU','160605 - SARAYACU')
	df["distrito"]=df['distrito'].str.replace('VARGAS GUERRA','160606 - VARGAS GUERRA')
	df["distrito"]=df['distrito'].str.replace('PUTUMAYO','160801 - PUTUMAYO')
	df["distrito"]=df['distrito'].str.replace('ROSA PANDURO','160802 - ROSA PANDURO')
	df["distrito"]=df['distrito'].str.replace('TENIENTE MANUEL CLAVERO','160803 - TENIENTE MANUEL CLAVERO')
	df["distrito"]=df['distrito'].str.replace('YAGUAS','160804 - YAGUAS')

	#Create a List of our conditions
	conditions=[
		(df['edad']<12),
		(df['edad']<18),
		(df['edad']<30),
		(df['edad']<60),
		(df['edad']<200),
	]
	#Create a List values of each conditions
	values =['Niño','Adolescente','Joven','Adulto','Adulto Mayor']
	df["Etapa de Vida"]=np.select(conditions,values)
	###############################IMPORTANTE CAMBIAR AL AÑO ACTUAL###############################
	df["fecha_mue"]=[r if str(r).find('2022')!= -1 else 'NO_FECHA' for r in df['fecha_mue']]
	df_mask1=df['fecha_mue']!='NO_FECHA'
	df=df[df_mask1]

	df["prueba"]=[r if str(r).find('PRUEBA ANTIGÉNICA')!= -1 or str(r).find('PRUEBA MOLECULAR')!= -1 or str(r).find('PRUEBA SEROLÓGICA')!= -1 else 'NO_PRUEBA' for r in df['prueba']]
	df_mask2=df['prueba']!='NO_PRUEBA'
	df=df[df_mask2]

	df["resultado"]=[r if str(r).find('POSITIVO')!= -1 or str(r).find('NEGATIVO')!= -1 or str(r).find('Ig M')!= -1 or str(r).find('IgM')!= -1 else 'NO_RESUL' for r in df['resultado']]
	df_mask3=df['resultado']!='NO_RESUL'
	df=df[df_mask3]

	########################################
	#df_2021["ResultadoFinal"]=["IgG" if str(r)=='IgG Reactivo' else r for r in df_2021['Resultado_1']]
	#df_2021["ResultadoFinal"]=['POSITIVO' if str(r).find('IgM')!= -1 or str(r)=='Reactivo' else r for r in df_2021['ResultadoFinal']]
	#df_2021["ResultadoFinal"]=[r if str(r)=='POSITIVO' or str(r)=='IgG' else 'NEGATIVO' for r in df_2021['ResultadoFinal']]
	########################################



	df["provincia"]=[r if str(r).find('MAYNAS')!= -1 or 
	str(r).find('LORETO')!= -1 or 
	str(r).find('ALTO AMAZONAS')!= -1 or 
	str(r).find('RAMON CASTILLA')!= -1 or 
	str(r).find('DATEM DEL MARAÑON')!= -1 or 
	str(r).find('UCAYALI')!= -1 or
	str(r).find('REQUENA')!= -1 or
	str(r).find('PUTUMAYO')!= -1 else 'NO_DATA' for r in df['provincia']]
	
	df_mask3=df['provincia']!='NO_DATA'
	df=df[df_mask3]

	df["fecha_mue"]=pd.to_datetime(df['fecha_mue'])
	df['fecha_mue'].dt.isocalendar().year='2021'

	df["Semana"]=df['fecha_mue'].dt.isocalendar().week
	df["AÑO"]=df['fecha_mue'].dt.year
	df["MES"]=df['fecha_mue'].dt.month
	df["DIA"]=df['fecha_mue'].dt.day

	td=timedelta(0)#EL NUMERO ES LA DIFERENCIA DE DIAS 
	today = pd.datetime.now() - td 
	df["Dias Transcurridos"]=(today - df["fecha_mue"]).dt.days

	conditionr=[
	(df['prueba']=='PRUEBA ANTIGÉNICA'),
	(df['prueba']=='PRUEBA MOLECULAR'),
	(df['prueba']=='PRUEBA SEROLÓGICA')
	]
	valuesr=[
	'Px Antígeno',
	'Px PCR',
	'Px Rápida'
	]

	df["TIPOPRUEBA"]=np.select(conditionr,valuesr)

	df['ResultadoFinal']=df['resultado']

	df= df.loc[:,['Nro','TIPOPRUEBA','Dni_Final','apenom',
	'sexo','edad','Etapa de Vida','distrito','provincia',
	'InicioSintomas','fecha_mue','Semana','AÑO','MES',
	'DIA','Ultimos 07 Dias','Dias Transcurridos','Estado Actual',
	'Fallecido','resultado','ResultadoFinal','Fuente','usuario_reg','pueblo_etnico',
	'ipress','ipress_hos','nombre_via','otros_sintomas','trabajador_salud']]

	df=df.rename(columns={'TIPOPRUEBA':'Tipo de Prueba','apenom':'NombreCompleto',
		'sexo':'comun_sexo_paciente','edad':'Edad','distrito':'Distrito','provincia':'Provincia',
		'InicioSintomas':'Fecha Inicio Sintomas de la Ficha Paciente','fecha_mue':'Fecha Ejecucion Prueba',
		'resultado':'Resultado','usuario_reg':'Usuario','pueblo_etnico':'Etnia','ipress':'cod_establecimiento_ejecuta',
		'ipress_hos':'Establecimiento_Ejecuta','nombre_via':'Direccion','trabajador_salud':'Personal Salud'})

	conditionnro=[
	(df['Tipo de Prueba']=='Px PCR'),
	(df['Tipo de Prueba']=='Px Antígeno'),
	(df['Tipo de Prueba']=='Px Rápida')
	]
	valuesnro=[
	1,
	2,
	3
	]

	df["Nro"]=np.select(conditionnro,valuesnro)
	
	##################datos en Estado Actual################33
	condition=[
	(df['Dias Transcurridos'] < 15) & 
	(df['ResultadoFinal'] == 'POSITIVO'),
	(df['Dias Transcurridos'] > 14) & 
	(df['ResultadoFinal'] == 'POSITIVO'),
	(df['ResultadoFinal'] == 'NEGATIVO')
	]
	values=['AISLAMIENTO DOMICILIARIO','ALTAS CLÍNICAS Y HOSPITALARIAS','NEGATIVO']

	df['Estado Actual']=np.select(condition,values)

	df=df.sort_values(by='Nro',ascending=True)
	#df.to_excel('DATARESULT/NOTIWEB_2021.xlsx')#no olvidar poner noticovid_2021 para correr el script general
	return(df)

NOTICOVID_2022()