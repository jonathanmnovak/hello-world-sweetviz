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

The code will output the report to `./tutorial/output/titanic_report.html`

###Resources
* [Powerful EDA (Exploratory Data Analysis) in just two lines of code using Sweetviz](https://towardsdatascience.com/powerful-eda-exploratory-data-analysis-in-just-two-lines-of-code-using-sweetviz-6c943d32f34)
* [Know your data much faster with the new Sweetviz Python library](https://www.kdnuggets.com/2021/03/know-your-data-much-faster-sweetviz-python-library.html)