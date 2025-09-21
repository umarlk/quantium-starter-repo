import pandas
from dash import Dash, dcc, html, Input, Output

PATH = "./output.csv"
COLORS = {
    "primary": "#FEDBFF",
    "secondary": "#D598EB",
    "font": "#522A61"
}


from plotly.express import line


data = pandas.read_csv(PATH)
data = data.sort_values(by="date")

dash_app = Dash(__name__)

def generate_figure(chart_data):
    line_chart = line(chart_data, x="date", y="sales", title="Sales of Pink Morsel")
    line_chart.update_layout(plot_bgcolor=COLORS["secondary"], paper_bgcolor=COLORS["primary"], font_color=COLORS["font"])
    return line_chart

visualisation = dcc.Graph(id="visualisation", figure=generate_figure(data))

header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        "background-color": COLORS["secondary"],
        "color": COLORS["font"],
        "border-radius": "20px"
    }
)


region_picker = dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    "north",
    id="region_picker",
    inline=True
)

region_picker_wrapper = html.Div(
    [
        region_picker
    ],
    style={
        "font-size": "150%"
    }
)


@dash_app.callback(
    Output(visualisation, "figure"),
    Input(region_picker, "value")
)

def update_graph(region):
    if region == "all":
        trimmed_data = data
    else:
        trimmed_data = data[data["region"] == region]
    
    figure = generate_figure(trimmed_data)
    return figure


dash_app.layout = html.Div([header, visualisation, region_picker_wrapper], style={"textAlign": "center", "background-color": COLORS["primary"], "border-radius": "20px"})


if __name__ == '__main__':
    dash_app.run()
