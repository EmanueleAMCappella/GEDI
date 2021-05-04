import pandas as pd

# split large file number 3 in two halves
path_to_file = "C:/Users/ECappella/OneDrive - Bip/Desktop/dati/"
file_03 = "03-rinnovi_offerta.csv"

rinnovi_offerta_03 = pd.read_csv(path_to_file + file_03).sort_values(['user_id', 'dataop', 'operazione', 'codoff'])
df1 = rinnovi_offerta_03.iloc[:500000, :]
df2 = rinnovi_offerta_03.iloc[500000:, :]

df1.to_csv(path_to_file + '03-rinnovi_offerta_PART1.csv', index=False)
df2.to_csv(path_to_file + '03-rinnovi_offerta_PART2.csv', index=False)


rinnovi_offerta_03_noDup = rinnovi_offerta_03.drop_duplicates(keep='first')
rinnovi_offerta_03_noDup.shape
rinnovi_offerta_03['user_id'].nunique()
rinnovi_offerta_03['operazione'].value_counts()


# explore files
battente = pd.read_csv(path_to_file + '00-battente_clienti.csv')
battente['user_id'].nunique()
battente[battente.duplicated(keep=False)]
battente.attivo.value_counts()

attivazione_off_01 = pd.read_csv(path_to_file + '01-attivazioni_offerta.csv')

attivazione_off_dup= attivazione_off_01[attivazione_off_01.duplicated(keep=False)].sort_values(by=['user_id', 'dataop', 'operazione', 'codoff'])
attivazione_off_dup2= attivazione_off_01[attivazione_off_01.duplicated(subset=['user_id', 'dataop', 'operazione', 'codoff'], keep=False)].sort_values(by=['user_id', 'dataop', 'operazione', 'codoff'])

attivazione_off_02_noDup = attivazione_off_01.drop_duplicates(keep='first')

attivazione_off_02_noDup.shape
attivazione_off_02_noDup['user_id'].nunique()
attivazione_off_02_noDup['operazione'].value_counts()


cessazione_off_02 = pd.read_csv(path_to_file + '02-cessazioni_offerta.csv')
cessazione_off_02.rename(columns={"tipo_cessazione": "operazione"}, inplace=True)
cessazione_duplicates = cessazione_off_02[cessazione_off_02.duplicated(subset=['user_id', 'dataop', 'operazione', 'codoff'], keep=False)].sort_values(by=['user_id', 'dataop', 'operazione', 'codoff'])
cessazione_off_noDup02 = cessazione_off_02.drop_duplicates(keep='first')
cessazione_off_noDup02.shape[0] + attivazione_off_02_noDup.shape[0]
cessazione_off_noDup02['user_id'].nunique()
cessazione_off_noDup02['tipo_cessazione'].value_counts()


compensazioni_04 = pd.read_csv(path_to_file + '04-rinnovi_offerta_compensazioni.csv')
compensazioni_04_noDup = compensazioni_04.drop_duplicates(keep='first')
compensazioni_04_noDup.shape
compensazioni_04_noDup['operazione'].value_counts()


ricariche_05 = pd.read_csv(path_to_file + '05-ricariche.csv')
ricariche_05_noDup = ricariche_05.drop_duplicates(keep='first')
ricariche_05_noDup.shape
ricariche_05_noDup['operazione'].value_counts()

SOS_06 = pd.read_csv(path_to_file + '06-servizio_sos.csv')
SOS_06_noDup = SOS_06.drop_duplicates(keep='first')
SOS_06_noDup.shape
SOS_06_noDup['operazione'].value_counts()

SOS_compensazioni_07 = pd.read_csv(path_to_file + '07-servizio_sos_compensazioni.csv')
SOS_compensazioni_07_noDup = SOS_compensazioni_07.drop_duplicates(keep='first')
SOS_compensazioni_07_noDup.shape
SOS_compensazioni_07_noDup['operazione'].value_counts()

credito_08 = pd.read_csv(path_to_file + '08-balance_credito.csv')
credito_08_noDup = credito_08.drop_duplicates(keep='first')
credito_08_noDup.shape
credito_08_noDup['operazione'].value_counts()

cessazioni_09 = pd.read_csv(path_to_file + '09-cessazioni_linea.csv')
cessazioni_09_noDup = cessazioni_09.drop_duplicates(keep='first')
cessazioni_09_noDup.shape
cessazioni_09_noDup.dtypes

