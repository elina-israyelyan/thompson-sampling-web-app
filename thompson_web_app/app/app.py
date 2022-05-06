from dash import html, Dash, dcc, Input, Output, callback, State

import dash_bootstrap_components as dbc

import base64
import pandas as pd
import io
import plotly.express as px
import pdfkit
from time import sleep

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        children=[
            html.P("You give us data, We find your reward!", className='navText'),
            html.P("FindYourReward", className='navText1'),
        ],
        # brand="FindYourReward",
        # brand_href="#",
        color="primary",
        dark=True,
        style={'padding': '4.5%'},
    ),
    html.Div(id="page-content", style={
        'background-image': 'url(https://www.xmple.com/wallpaper/blue-gradient-white-linear-1920x1080-c2-87cefa-ffffff-a-270-f-14.svg)'
    }, className='divOverlay')

])

index_page = html.Div([
    dbc.Card([
        dbc.CardBody([html.P(
            "FindYourReward is a tool which enables user to input data, define KPIs and recieve analysis on best reward-giving advertisement.",
            className="card-text")])
    ], style={"width": "30rem"}),
    dbc.Button("Input Data", id="open", outline=True, color="primary", className='inputDataButton'),
    dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("Please specify the following information")),
            dbc.InputGroup(
                [dbc.InputGroupText("Threshold*:"), dbc.Input(type='number')],
                className="mb-3",

            ),
            dbc.InputGroup(
                [dbc.InputGroupText("Cost Per Arm:"), dbc.Input(type='number'),
                 dbc.InputGroupText("$")],
                className="mb-3",

            ),
            dbc.InputGroup(
                [dbc.InputGroupText("Exploration time"), dbc.Input(type='number'),
                 dbc.InputGroupText("Sec."), ],
                className="mb-3",

            ),
            dbc.ModalBody("* is required"),

            html.Div([  # this code section taken from Dash docs https://dash.plotly.com/dash-core-components/upload
                dcc.Upload(
                    id='upload-data',
                    children=html.Div([
                        'Drag and Drop or ',
                        html.A('Select your CSV Files')
                    ]),
                    style={
                        'width': '100%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '0px'
                    },
                    # Allow multiple files to be uploaded
                    multiple=True
                ),
                html.Div(id='output-div'),
                html.Div(id='output-datatable'),
            ]),

            dbc.ModalFooter(
                dbc.Button(
                    "Close", id="close", className="ms-auto", n_clicks=0,

                )
            ),
        ],
        id="modal",
        is_open=False,
    ),

    dbc.Card([
        dbc.CardBody([
            html.P("For more information: "),
            dcc.Link(dbc.Button("Click here", outline=True, color="primary"), href="https://www.google.com",
                     target='blank'),
        ])
    ], style={"width": "25rem"}, className='inputMore'),
    dbc.Card([
        dbc.CardBody([
            html.P("View how it works on randomly generated data: "),
            dcc.Link(dbc.Button("Analyse generated data", outline=True, color="primary"), href="/vispage"),
        ])
    ], style={"width": "25rem"}, className='analyseBox'),
], className="homeCont cont"),

df = px.data.iris()  # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length"),
popover_children = "I am a poopover!"

vis_page = html.Div([

    html.Div([

        html.Div([
            dbc.Button(
                "i",
                id="hover-target",
                color="white",
                className="me-1",
                n_clicks=0,
                style={'height': '30px', 'weight': '30px', 'textAlign': 'left'}
            ),
            dbc.Popover(
                popover_children,
                target="hover-target",
                body=True,
                trigger="hover"),

            dcc.Graph(
                figure={
                    'data': [fig],
                }, className='dynGraph1',
            ),
        ]),

        html.Div([
            dbc.Button(
                "i",
                id="hover-target1",
                color="white",
                className="me-1",
                n_clicks=0

            ),
            dbc.Popover(
                popover_children,
                target="hover-target1",
                body=True,
                trigger="hover"),

            dcc.Graph(
                figure={
                    'data': [fig],
                }, className='dynGraph2'
            ),
        ]),
    ], className="graphCont"),

    dbc.Card([
        dbc.CardBody([
            html.P(
                "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."),
        ])
    ], style={"width": "25rem"}, className='analysis'),
    dbc.Button("Calculate Waste", id='open', color="primary", className='calcwasteButton'),
    dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("Header")),
            dbc.ModalBody("This is the content of the modal"),
            dbc.ModalFooter(
                dbc.Button(
                    "Close", id="close", className="ms-auto", n_clicks=0
                )
            ),
        ],
        id="modal",
        is_open=False,
    ),

    dbc.Button("Download Output", outline=False, color="primary", id="js", n_clicks=0, className='downloadButton'),
    dcc.Link(dbc.Button("Back to Home", outline=False, color="primary"), href="/homepage", className='backHome')

], className="cont", id="print"),

app.clientside_callback(
    '''
    function(n_clicks){
        if(n_clicks > 0){
            var opt = {
                margin: 1,
                filename: 'myfile.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 3},
                jsPDF: { unit: 'cm', format: 'a2', orientation: 'p' },
                pagebreak: { mode: ['avoid-all'] }
            };
            html2pdf().from(document.getElementById("print")).set(opt).toPdf().save();
        }
    }
    ''',
    Output('js', 'n_clicks'),
    Input('js', 'n_clicks'),
)

err_page = html.Div([
    html.H1('You have entered wrong page')
]),


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def displayPage(pathname):
    if pathname == '/homepage':
        return index_page
    elif pathname == '/vispage':
        return vis_page
    else:
        return err_page


@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    if 'csv' in filename:
        # Assume that the user uploaded a CSV file 
        print('There was an error processing this file.')
        df = pd.read_csv(
            io.StringIO(decoded.decode('utf-8')))
    elif 'xls' in filename:
        # Assume that the user uploaded an excel file 
        df = pd.read_excel(io.BytesIO(decoded))
    else:
        return html.Div([
            'There was an error processing this file.'
        ])
    return dcc.Link(dbc.Button("Analyse Data", outline=False, color="primary"), href="/vispage", className='adata')


@app.callback(Output('output-datatable', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children


if __name__ == '__main__':
    app.run_server(debug=False)