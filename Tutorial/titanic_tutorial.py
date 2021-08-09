import sweetviz
import pandas as pd

data_directory = '../titanic_data'
train = pd.read_csv(f'{data_directory}/train.csv')
test = pd.read_csv(f'{data_directory}/test.csv')

report = sweetviz.compare([train, "Train"], [test, "Test"], "Survived")
report.show_html('./output/titanic_report.html')
