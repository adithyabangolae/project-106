import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Coffee in ml", y="sleep in hours")
        fig.show()

def getDataSource(data_path):
    sleep_in_hours = []
    coffee_in_ml = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sleep_in_hours.append(float(row["sleep in hours"]))
            coffee_in_ml.append(float(row["Coffee in ml"]))

    return {"x" : coffee_in_ml, "y": sleep_in_hours}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation:-  \n--->",correlation[0,1])

def setup():
    data_path  = "cups of coffee vs hours of sleep.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()