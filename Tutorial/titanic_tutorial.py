import sweetviz
import pandas as pd

#Load data
data_directory = './titanic_data'
train = pd.read_csv(f'{data_directory}/train.csv')
test = pd.read_csv(f'{data_directory}/test.csv')

#Output general report
report = sweetviz.compare([train, "Train"], [test, "Test"], "Survived")
report.show_html(filepath='./tutorial/output/titanic_report.html',
                 layout='vertical')

#Ignore feature and force another feature to categorical
feature_config = sweetviz.FeatureConfig(skip="PassengerId",
                                        force_cat=["Ticket"])
report_config_chg = sweetviz.compare([train, "Train"],
                                     [test, "Test"],
                                     "Survived",
                                     feature_config)
report_config_chg.show_html(filepath='./tutorial/output/titanic_feature_config_chg_report.html',
                            layout='vertical')

#Compare sub-populations
report_sub_pop = sweetviz.compare_intra(train, train["Sex"] == 'male',
                                        ["Male", "Female"], 'Survived')
report_sub_pop.show_html(filepath='./tutorial/output/titanic_sub_pop_report.html',
                         layout='vertical')


