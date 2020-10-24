import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('C:\\Users\\eric-\\Downloads\\Eric Rodrigues de Carvalho - dados - Eric Rodrigues de Carvalho - dados.csv', index_col = 0)
df.columns = ['Municípios', 'Matrículas', 'Docentes', 'Estabelecimentos', 'Escolarização', 'Anos iniciais', 'Anos finais']
dp = pd.DataFrame(df)
dp = dp.loc[:, ['Municípios','Anos iniciais', 'Anos finais']]
print (dp.describe())
print(dp.groupby(['Anos iniciais'])['Anos iniciais'].count())
frequenciaI = dp.groupby(['Anos iniciais'])['Anos iniciais'].count()
print(dp.groupby(['Anos iniciais'])['Anos iniciais'].count()*100/78)
print(dp.groupby(['Anos finais'])['Anos finais'].count())
frequenciaF = dp.groupby(['Anos finais'])['Anos finais'].count()
print(dp.groupby(['Anos finais'])['Anos finais'].count()*100/78)
dp.plot(x = 'Municípios', y = ['Anos iniciais','Anos finais'], kind = 'bar')
plt.legend(loc='center right', bbox_to_anchor=(1, 1.05))
plt.ylabel('Anos')
plt.xlabel('Municípios')
plt.subplots_adjust(left=0.03, bottom=0.28, right=0.99, top=0.93, wspace=None, hspace=None)
plt.show()
frequenciaI.plot (x = 'Notas do IDEB para anos iniciais', y = 'Frequência', kind = 'bar')
plt.show()
frequenciaF.plot (x = 'Notas do IDEB para anos finais', y = 'Frequência', kind = 'bar')
plt.show()
