import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_data = [('North America', 'Aruba'), ('Asia', 'Afghanistan'), ('Africa', 'Angola'), ('North America', 'Anguilla'), ('Europe', 'Albania'), ('Europe',
          'Andorra'), ('North America', 'Netherlands Antilles'), ('Asia', 'United Arab Emirates'), ('South America', 'Argentina'), ('Asia', 'Armenia')]

df_names = []

for i in df_data:
    df_names.append(i[0])


df = pd.DataFrame(df_data)

bar_1 = df[0]
bar_2 = df[1]

x_pos = np.arange(len(bar_1))


plt.bar(x_pos, bar_2, 0.5, color='r')
plt.title("População por País")
plt.xticks(x_pos,df_names,rotation=20,fontsize=8)

plt.show()
