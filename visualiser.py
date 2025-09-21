import pandas
from dash import Dash, dcc, html

PATH = "./output.csv"

from plotly.express import line


data = pandas.read_csv(PATH)
data = data.sort_values(by="date")

dash_app = Dash(__name__)

line_chart = line(data, x="date", y="sales", title="Sales of Pink Morsel")
visualisation = dcc.Graph(id="visualisation", figure=line_chart)

header = html.H1("Pink Morsel sales visualiser", id="header")

dash_app.layout = html.Div([header, visualisation])

if __name__ == '__main__':
    dash_app.run()
