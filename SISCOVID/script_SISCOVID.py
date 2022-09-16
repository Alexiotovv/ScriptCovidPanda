import pandas as pd
import numpy as np
import datetime
from datetime import date, timedelta
import os
##no olvidar instalar openpy

#####################ABRIR SISCOVID_2020##########################################


def SISCOVID_2022():
	###Contamos cuantos archivos hay en el directorio para realizar el for
	#files_count = 0
	#for path in pathlib.Path("DATASOURCE").iterdir():
    #if path.is_file():
    #    files_count += 1
    ########################################################################

	current_dir = os.path.dirname(os.path.realpath(__file__)) 
	###########################ABRIR ARCHIVOS 2022 PARA UNIR############
	ene_2022=os.path.join(current_dir, "DATASOURCE/ENERO-2022.xlsx")
	feb_2022=os.path.join(current_dir, "DATASOURCE/FEBRERO-2022.xlsx")
	mar_2022=os.path.join(current_dir, "DATASOURCE/MARZO-2022.xlsx")
	abr_2022=os.path.join(current_dir, "DATASOURCE/ABRIL-2022.xlsx")
	may_2022=os.path.join(current_dir, "DATASOURCE/MAYO-2022.xlsx")
	jun_2022=os.path.join(current_dir, "DATASOURCE/JUNIO-2022.xlsx")
	jul_2022=os.path.join(current_dir, "DATASOURCE/JULIO-2022.xlsx")
	ago_2022=os.path.join(current_dir, "DATASOURCE/AGOSTO-2022.xlsx")
	set_2022=os.path.join(current_dir, "DATASOURCE/SETIEMBRE-2022.xlsx")
	#oct_2022=os.path.join(current_dir, "DATASOURCE/OCTUBRE-2022.xlsx")
	#nov_2022=os.path.join(current_dir, "DATASOURCE/NOVIEMBRE-2022.xlsx")
	#dic_2022=os.path.join(current_dir, "DATASOURCE/DICIEMBRE-2022.xlsx")


	#LEER ARCHIVOS 2022
	file1=pd.read_excel(ene_2022)
	file2=pd.read_excel(feb_2022)
	file3=pd.read_excel(mar_2022)
	file4=pd.read_excel(abr_2022)
	file5=pd.read_excel(may_2022)
	file6=pd.read_excel(jun_2022)
	file7=pd.read_excel(jul_2022)
	file8=pd.read_excel(ago_2022)
	file9=pd.read_excel(set_2022)
	#file10=pd.read_excel(oct_2022)
	#file11=pd.read_excel(nov_2022)
	#file12=pd.read_excel(dic_2022)
	#CONVERTIR EN DATAFRAME
	df1=pd.DataFrame(file1)
	df2=pd.DataFrame(file2)
	df3=pd.DataFrame(file3)
	df4=pd.DataFrame(file4)
	df5=pd.DataFrame(file5)
	df6=pd.DataFrame(file6)
	df7=pd.DataFrame(file7)
	df8=pd.DataFrame(file8)
	df9=pd.DataFrame(file9)
	#df10=pd.DataFrame(file10)
	#df11=pd.DataFrame(file11)
	#df12=pd.DataFrame(file12)
	#df13=pd.DataFrame(file13)
	#df14=pd.DataFrame(file14)
	#CAMBIAR EL NOMBRE DE LA COLUMNA(ÍNDICE 79) Resultado A Resultado.1 
	
	#df1.columns.values[85]="Resultado_1"
	#df2.columns.values[85]="Resultado_1"
	#df3.columns.values[85]="Resultado_1"
	#df4.columns.values[85]="Resultado_1"
	#df5.columns.values[85]="Resultado_1"
	#df6.columns.values[85]="Resultado_1"
	
	#df7.columns.values[85]="Resultado_1"
	#df8.columns.values[85]="Resultado_1"
	#df9.columns.values[85]="Resultado_1"
	#df10.columns.values[85]="Resultado_1"
	#df11.columns.values[85]="Resultado_1"
	#df12.columns.values[85]="Resultado_1"
	

	union_df_2022= [df1,df2,df3,df4,df5,df6,df7,df8,df9]#,,df7,df8,df9,df10,df11,df12,agregar los df que correspondan c/mes

	df_2022=pd.concat(union_df_2022)

	df_2022=df_2022.loc[:,['Nro Documento','nombres','Apellido Paterno','Apellido Materno','comun_sexo_paciente','Edad','Provincia','Distrito','Tipo de Prueba','Fecha Ejecucion Prueba','Resultado','Usuario','Fecha_inicio_sintomas','cod_establecimiento_ejecuta','Establecimiento_Ejecuta','Direccion','Etnia','Personal Salud']]
	df_2022['NombreCompleto']=df_2022['nombres']+" "+df_2022['Apellido Paterno']+" " + df_2022['Apellido Materno']

	#union=[df_2020,df_2022]
	#df_2022=pd.concat(union)
	df_2022['comun_sexo_paciente']=df_2022['comun_sexo_paciente'].replace(['FEMENINO','MASCULINO'],['F','M'])

	df_2022.insert(1,"Nro",0,allow_duplicates=True)
	df_2022.insert(9,"ResultadoFinal","",allow_duplicates=True)
	df_2022.insert(10,"Fuente","SISCOVID",allow_duplicates=True)

	df_2022.insert(8,"Semana","",allow_duplicates=True)
	df_2022.insert(9,"AÑO","",allow_duplicates=True)
	df_2022.insert(10,"MES","",allow_duplicates=True)
	df_2022.insert(11,"DIA","",allow_duplicates=True)
	df_2022.insert(12,"Ultimos 07 Dias","0",allow_duplicates=True)
	df_2022.insert(13,"Dias Transcurridos","",allow_duplicates=True)
	df_2022.insert(14,"Estado Actual","",allow_duplicates=True)
	df_2022.insert(15,"Fallecido","",allow_duplicates=True)

	df_2022.insert(1,"Dni_Final","",allow_duplicates=True)
	df_2022.insert(5,"Etapa de Vida","",allow_duplicates=True)

	df_2022["ResultadoFinal"]=["IgG" if str(r)=='IgG Reactivo' else r for r in df_2022['Resultado']]
	df_2022["ResultadoFinal"]=['POSITIVO' if str(r).find('IgM')!= -1 or str(r)=='Reactivo' else r for r in df_2022['ResultadoFinal']]
	df_2022["ResultadoFinal"]=[r if str(r)=='POSITIVO' or str(r)=='IgG' else 'NEGATIVO' for r in df_2022['ResultadoFinal']]

	df_2022["Dni_Final"]=["00000000"+ str(r) for r in df_2022['Nro Documento']]
	df_2022["Dni_Final"]=[str(r)[-8:] for r in df_2022['Dni_Final']]
	df_2022["Tipo de Prueba"]=["Px Antígeno" if str(r).find('Antígeno')!= -1 else "Px Rápida" for r in df_2022['Tipo de Prueba']]

	df_2022["Dni_Final"]=df_2022['Dni_Final'].str.replace('nan','00000000')

	df_2022["Distrito"]=df_2022['Distrito'].str.upper()
	df_2022["Provincia"]=df_2022['Provincia'].str.upper()

	df_2022["Distrito"]=df_2022['Distrito'].str.replace('Á','A')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('É','E')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('Í','I')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('Ó','O')

	df_2022["Provincia"]=df_2022['Provincia'].str.replace('Ó','O')
	###############################

	#Create a List of our conditions
	conditionsp=[
	(df_2022['Distrito']=='BALSAPUERTO'),
	(df_2022['Distrito']=='JEBEROS'),
	(df_2022['Distrito']=='LAGUNAS'),
	(df_2022['Distrito']=='SANTA CRUZ'),
	(df_2022['Distrito']=='TENIENTE CESAR LOPEZ ROJAS'),
	(df_2022['Distrito']=='YURIMAGUAS'),
	(df_2022['Distrito']=='ANDOAS'),
	(df_2022['Distrito']=='BARRANCA'),
	(df_2022['Distrito']=='CAHUAPANAS'),
	(df_2022['Distrito']=='MANSERICHE'),
	(df_2022['Distrito']=='MORONA'),
	(df_2022['Distrito']=='PASTAZA'),
	(df_2022['Distrito']=='NAUTA'),
	(df_2022['Distrito']=='PARINARI'),
	(df_2022['Distrito']=='TIGRE'),
	(df_2022['Distrito']=='TROMPETEROS'),
	(df_2022['Distrito']=='URARINAS'),
	(df_2022['Distrito']=='ALTO NANAY'),
	(df_2022['Distrito']=='BELEN'),
	(df_2022['Distrito']=='INDIANA'),
	(df_2022['Distrito']=='IQUITOS'),
	(df_2022['Distrito']=='FERNANDO LORES'),
	(df_2022['Distrito']=='LAS AMAZONAS'),
	(df_2022['Distrito']=='MAZAN'),
	(df_2022['Distrito']=='NAPO'),
	(df_2022['Distrito']=='PUNCHANA'),
	(df_2022['Distrito']=='TORRES CAUSANA'),
	(df_2022['Distrito']=='SAN JUAN BAUTISTA'),
	(df_2022['Distrito']=='PEBAS'),
	(df_2022['Distrito']=='RAMON CASTILLA'),
	(df_2022['Distrito']=='SAN PABLO'),
	(df_2022['Distrito']=='YAVARI'),
	(df_2022['Distrito']=='ALTO TAPICHE'),
	(df_2022['Distrito']=='CAPELO'),
	(df_2022['Distrito']=='EMILIO SAN MARTIN'),
	(df_2022['Distrito']=='JENARO HERRERA'),
	(df_2022['Distrito']=='MAQUIA'),
	(df_2022['Distrito']=='PUINAHUA'),
	(df_2022['Distrito']=='REQUENA'),
	(df_2022['Distrito']=='SAQUENA'),
	(df_2022['Distrito']=='SOPLIN'),
	(df_2022['Distrito']=='TAPICHE'),
	(df_2022['Distrito']=='YAQUERANA'),
	(df_2022['Distrito']=='CONTAMANA'),
	(df_2022['Distrito']=='INAHUAYA'),
	(df_2022['Distrito']=='PADRE MARQUEZ'),
	(df_2022['Distrito']=='PAMPA HERMOSA'),
	(df_2022['Distrito']=='SARAYACU'),
	(df_2022['Distrito']=='VARGAS GUERRA'),
	(df_2022['Distrito']=='PUTUMAYO'),
	(df_2022['Distrito']=='ROSA PANDURO'),
	(df_2022['Distrito']=='TENIENTE MANUEL CLAVERO'),
	(df_2022['Distrito']=='YAGUAS'),
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
	df_2022["Provincia"]=np.select(conditionsp,valuesp)

	#############
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('BALSAPUERTO','160202 - BALSAPUERTO')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('JEBEROS','160205 - JEBEROS')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('LAGUNAS','160206 - LAGUNAS')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('SANTA CRUZ','160210 - SANTA CRUZ')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('TENIENTE CESAR LOPEZ ROJAS','160211 - TENIENTE CESAR LOPEZ ROJAS')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('YURIMAGUAS','160201 - YURIMAGUAS')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('ANDOAS','160706 - ANDOAS')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('BARRANCA','160701 - BARRANCA')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('CAHUAPANAS','160702 - CAHUAPANAS')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('MANSERICHE','160703 - MANSERICHE')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('MORONA','160704 - MORONA')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('PASTAZA','160705 - PASTAZA')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('NAUTA','160301 - NAUTA')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('PARINARI','160302 - PARINARI')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('TIGRE','160303 - TIGRE')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('TROMPETEROS','160304 - TROMPETEROS')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('URARINAS','160305 - URARINAS')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('ALTO NANAY','160102 - ALTO NANAY')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('BELEN','160112 - BELEN')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('INDIANA','160104 - INDIANA')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('IQUITOS','160101 - IQUITOS')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('FERNANDO LORES','160103 - FERNANDO LORES')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('LAS AMAZONAS','160105 - LAS AMAZONAS')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('MAZAN','160106 - MAZAN')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('NAPO','160107 - NAPO')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('PUNCHANA','160108 - PUNCHANA')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('TORRES CAUSANA','160110 - TORRES CAUSANA')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('SAN JUAN BAUTISTA','160113 - SAN JUAN BAUTISTA')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('PEBAS','160402 - PEBAS')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('RAMON CASTILLA','160401 - RAMON CASTILLA')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('SAN PABLO','160404 - SAN PABLO')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('YAVARI','160403 - YAVARI')
	df_2022['Distrito']=['160509 - TAPICHE' if str(r)=='TAPICHE' else r for r in df_2022['Distrito']]
	#df_2022["Distrito"]=df_2022['Distrito'].str.replace('TAPICHE','160509 - TAPICHE')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('CAPELO','160503 - CAPELO')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('EMILIO SAN MARTIN','160504 - EMILIO SAN MARTIN')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('JENARO HERRERA','160510 - JENARO HERRERA')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('MAQUIA','160505 - MAQUIA')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('PUINAHUA','160506 - PUINAHUA')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('REQUENA','160501 - REQUENA')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('SAQUENA','160507 - SAQUENA')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('SOPLIN','160508 - SOPLIN')
	df_2022['Distrito']=['160502 - ALTO TAPICHE' if str(r)=='ALTO TAPICHE' else r for r in df_2022['Distrito']]
	#df_2022["Distrito"]=df_2022['Distrito'].str.replace('ALTO TAPICHE','160502 - ALTO TAPICHE')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('YAQUERANA','160511 - YAQUERANA')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('CONTAMANA','160601 - CONTAMANA')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('INAHUAYA','160602 - INAHUAYA')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('PADRE MARQUEZ','160603 - PADRE MARQUEZ')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('PAMPA HERMOSA','160604 - PAMPA HERMOSA')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('SARAYACU','160605 - SARAYACU')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('VARGAS GUERRA','160606 - VARGAS GUERRA')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('PUTUMAYO','160801 - PUTUMAYO')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('ROSA PANDURO','160802 - ROSA PANDURO')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('TENIENTE MANUEL CLAVERO','160803 - TENIENTE MANUEL CLAVERO')
	df_2022["Distrito"]=df_2022['Distrito'].str.replace('YAGUAS','160804 - YAGUAS')

	#Create a List of our conditions
	conditions=[
		(df_2022['Edad']<12),
		(df_2022['Edad']<18),
		(df_2022['Edad']<30),
		(df_2022['Edad']<60),
		(df_2022['Edad']<200),
	]
	#Create a List values of each conditions
	values =['Niño','Adolescente','Joven','Adulto','Adulto Mayor']
	df_2022["Etapa de Vida"]=np.select(conditions,values)

	#df_2022["Fecha Registro Prueba"]=[str(r)[:-9] for r in df_2022['Fecha Registro Prueba']]
	df_2022["Fecha Ejecucion Prueba"]=pd.to_datetime(df_2022['Fecha Ejecucion Prueba'])
	df_2022["Semana"]=df_2022['Fecha Ejecucion Prueba'].dt.isocalendar().week
	df_2022["AÑO"]=df_2022['Fecha Ejecucion Prueba'].dt.year
	df_2022["MES"]=df_2022['Fecha Ejecucion Prueba'].dt.month
	df_2022["DIA"]=df_2022['Fecha Ejecucion Prueba'].dt.day

	td=timedelta(0)#EL NUMERO ES LA DIFERENCIA DE DIAS 
	today = pd.datetime.now() - td 
	df_2022["Dias Transcurridos"]=(today - df_2022["Fecha Ejecucion Prueba"]).dt.days

	conditionnro=[
	(df_2022['Tipo de Prueba']=='Px PCR'),
	(df_2022['Tipo de Prueba']=='Px Antígeno'),
	(df_2022['Tipo de Prueba']=='Px Rápida')
	]
	valuesnro=[
	1,
	2,
	3
	]

	df_2022["Nro"]=np.select(conditionnro,valuesnro)

	##################datos en Estado Actual################33
	condition=[
	(df_2022['Dias Transcurridos'] < 15) & 
	(df_2022['ResultadoFinal'] == 'POSITIVO'),
	(df_2022['Dias Transcurridos'] > 14) & 
	(df_2022['ResultadoFinal'] == 'POSITIVO')|
	(df_2022['ResultadoFinal'] == 'IgG'),
	(df_2022['ResultadoFinal'] == 'NEGATIVO')
	]
	values=['AISLAMIENTO DOMICILIARIO','ALTAS CLÍNICAS Y HOSPITALARIAS','NEGATIVO']


	df_2022['Estado Actual']=np.select(condition,values)
	######################################################
	#df_2022['Estado Actual']=['ALTAS CLÍNICAS Y HOSPITALARIAS' if str(r)=='' or str(r)=='0'  else r for r in df_2022['Estado Actual']]
	#df_2022['Estado Actual']=df_2022['Estado Actual'].str.replace(str(''),'ALTAS CLÍNICAS Y  HOSPITALARIAS')

	df_2022['Fallecido']='NO'
	df_2022= df_2022.loc[:,['Nro','Tipo de Prueba','Dni_Final',
	'NombreCompleto','comun_sexo_paciente','Edad',
	'Etapa de Vida','Distrito','Provincia',
	'Fecha_inicio_sintomas',
	'Fecha Ejecucion Prueba','Semana','AÑO','MES','DIA',
	'Ultimos 07 Dias','Dias Transcurridos','Estado Actual',
	'Fallecido','Resultado','ResultadoFinal','Fuente','Usuario',
	'Etnia','cod_establecimiento_ejecuta','Establecimiento_Ejecuta','Direccion','Personal Salud']]
	df_2022=df_2022.sort_values(by='Nro',ascending=True)
	#df_2022.to_excel("RESULT/SISCOVID_2022.xlsx")#SE PUSO DESDE SISCOVID porque es llamado por otro script que esta en otra ruta
	return(df_2022)

SISCOVID_2022()