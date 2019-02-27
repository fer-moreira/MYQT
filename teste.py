import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class BarGraph (object):
    def __init__(self,data):
        self.col = 'r'
        df_data = data
        df_names = []

        for i in df_data:
            df_names.append(i[0])

        df = pd.DataFrame(df_data)

        bar_1 = df[0]
        bar_2 = df[1]

        x_pos = np.arange(len(bar_1))

        plt.bar(x_pos, bar_2, 0.5, color=self.col)
        plt.xticks(x_pos,df_names,rotation=20,fontsize=8)

    def SetTitle (self,Title):plt.title(str(Title))
    def SetColor(self,Color):self.col = str(Color)  
    def Show (self):plt.show()
    def Close (self):plt.close(0)


data = [('French Southern territories', None), ('Cocos (Keeling) Islands', None), ('Christmas Island', None), ('Bouvet Island', None), ('Antarctica', None)]
[('Andorra', 83.5), ('Macao', 81.6), ('San Marino', 81.1), ('Japan', 80.7), ('Singapore', 80.1)]

graph = BarGraph(data)
graph.SetColor('r')
graph.SetTitle('Population By Region')
graph.Show()
