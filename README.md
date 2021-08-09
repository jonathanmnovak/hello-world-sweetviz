# hello-world-sweetviz
Repository used to explore the 
[Sweetviz](https://github.com/fbdesignpro/sweetviz) EDA Python library. I'll 
be following the tutorials in the resources section.

###Setup
This setup assumes Python 3 is installed and that you are using MacOS.

Create environment:  
`python3 -m venv sweetviz-venv`

Activate the virtual environment:  
`source sweetviz-venv/bin/activate`

To deactivate the environment:  
`deactivate`

Install dependent libraries using `pip`  
If a requirements file is provided, then you can install by running the 
following:  
`pip install -r requirements.txt` 

###Tutorials
For the 
[Titanic Tutorial](https://towardsdatascience.com/powerful-eda-exploratory-data-analysis-in-just-two-lines-of-code-using-sweetviz-6c943d32f34), run the following: 
`python3 ./tutorial/titanic_tutorial.py`

This generates a default report which runs EDA on both the training and testing
datasets and compares the two datasets

Output reports are placed in `./tutorial/output`
* Report with default configuration: `titanic_report.html`
* Report which drops the "PassengerId" and forces "Ticket" to categorical: ``
`titanic_feature_config_chg_report.html`
    **Note: You can also change the `dtype` in pd.read_csv to force a column to
    a specific datatype (sweetviz will pickup this change)

####General thoughts:
Pros 
* Comparing two datasets to see if iid is held
* Analyzing mixed variable feature relationships (i.e. comparing numerical 
features with categorical features)
* Analyzing the relationship of features with target variable

Cons
* Wide screen monitor is required to view on the outputs from the html report
* When analyzing a specific feature, the relationship with the target variable 
isn't broken down by each dataset (train and test) and instead is combined. 
This is a much needed enhancement  to see if the distributions of features and 
the target variables are consistent between training and testing.
* No tags to represent data issues. This is a nice feature in the pandas profiling
package that isn't available in sweetviz. However, the missing values percentages are 
highlighted (green, yellow, and red) to indicate whether there is an issue.

###Resources
* [Powerful EDA (Exploratory Data Analysis) in just two lines of code using Sweetviz](https://towardsdatascience.com/powerful-eda-exploratory-data-analysis-in-just-two-lines-of-code-using-sweetviz-6c943d32f34)
* [Know your data much faster with the new Sweetviz Python library](https://www.kdnuggets.com/2021/03/know-your-data-much-faster-sweetviz-python-library.html)