import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('teste-tunts-320300-8f1cec10f1d6.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open_by_key('1ImBIuXKV_jgCEVrDbpRZ7vC2B0sM0btwzyBUUD7kqWo')

pagina = wks.get_worksheet(0)

#colunas matricula aluno faltas p1 p2 p3 situação nota_para_aprovação_final
#linha inicial 4
# total de aulas 60
tam_dados = len(pagina.col_values(1))
print(tam_dados)
for i in range(4,tam_dados+1):
  faltas = int(pagina.cell(i,3).value)
  faltas_per = faltas*100/60
  p1 = int(pagina.cell(i,4).value)
  p2 = int(pagina.cell(i,5).value)
  p3 = int(pagina.cell(i,6).value)
  media = round((p1+p2+p3)/3)
  print(media)
  final = ((50*2)-media)
  if( faltas_per<=25 and media>=70):
    pagina.update_cell(i,7,'APROVADO')
    pagina.update_cell(i,8,'0')
  if( faltas_per<=25 and media>=50 and media<=70):
    pagina.update_cell(i,7,'EXAME FINAL')
    pagina.update_cell(i,8,final)
  if( faltas_per<=25 and media<50):
    pagina.update_cell(i,7,'REPROVADO POR NOTA')
    pagina.update_cell(i,8,final)
  if( faltas_per> 25):
    pagina.update_cell(i,7,'REPROVADO POR FALTA')
    pagina.update_cell(i,8,final)
