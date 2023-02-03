from dash import (
    Dash,
    html,
    dcc
    )

import requests

import json

def create_app():

    app = Dash(__name__)

    api_url="http://localhost:5000"

    levels_endpoint = api_url+"/get_levels"

    levels = requests.post(
        url = levels_endpoint,
        headers = {'Content-Type':'application/json'}
    ).text

    levels_list = json.loads(json.dumps(json.loads(levels)))
    levels_list = [i for i in levels_list if i is not None]

    app.layout = html.Div(
        [
            html.Div(
                [
                    html.H1("Salary Guide")
                ]
                ),
            html.Div(
                [
                    dcc.Dropdown(
                    id='levels-dropdown',
                    options=levels_list
                    )
                ]
            )
        ]
    )

    return app

def main():

    app = create_app()

    app.run_server(debug=True)

if __name__=='__main__':
    main()
