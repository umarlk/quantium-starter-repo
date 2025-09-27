from visualiser import dash_app

def header(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#header", timeout=10)

def visualisation(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#visualisation", timeout=10)

def region_picker(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#region_picker", timeout=10)
