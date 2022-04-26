from dash import Dash, html, Input

app = Dash(__name__)

app.layout = html.Div(style={'backgroundColor': '#85799F'}, children=[
    html.Nav(children=[
        html.Nav(children='Get Your Best Reward!',
                 style={
                     'textAlign': 'center',
                     'color': 'white',
                     'float': 'left',
                     'font-size': '50px',
                     'padding': '200px',
                     'font-family': '-apple-system,system-ui,"Segoe UI",Roboto,"Helvetica Neue",Ubuntu,sans-serif',
                     '-webkit-text-stroke': '3px black',
                     'font-weight': 'bold'

                 }
                 ),
        html.Nav(children='You Give Us Data We Find Your Reward',
                 style={
                     'textAlign': 'center',
                     'color': 'white',
                     'font-size': '50px',
                     'background-image': 'url(https://images.pexels.com/photos/2786933/pexels-photo-2786933.jpeg?auto'
                                         '=compress&cs=tinysrgb&w=1260&h=750&dpr=1)',
                     'background-size': '100%',
                     'padding': '200px',
                     'font-family': '-apple-system,system-ui,"Segoe UI",Roboto,"Helvetica Neue",Ubuntu,sans-serif'

                 }
                 )]),

    html.Div(
        children='''FindYourReward is a tool which enables users to input their sales data, define KPIs and recieve 
        analysis on best reward-giving advertisement. '''
        , style={
            'textAlign': 'left',
            'color': 'black',
            'border': '7px solid blue',
            'border-style': 'inset',
            'padding': '50px',
            'margin': '20px',
            'width': 300,
            'font-family': '-apple-system,system-ui,"Segoe UI",Roboto,"Helvetica Neue",Ubuntu,sans-serif',
            'font-size': '20px',
            'margin-left': '4%',
            'margin-top': '2.4%',
            'display': 'inline-flex'}),

    html.A(
        href="https://media-exp1.licdn.com/dms/image/C4E03AQFO8pbKx2E8kA/profile-displayphoto-shrink_200_200/0"
             "/1625566409743?e=1652918400&v=beta&t=H8CKBf6uDoTSmNdq3uoK79X8bdEF_Vt6R8d7jZMfsMU",
        target='_blank',
        children='Want to know how the algorithm works?',
        style={
            'textAlign': 'left',
            'color': 'black',
            'border': '5px solid blue',
            'border-style': 'dashed solid',
            'padding': '40px',
            'margin': '20px',
            'width': 270,
            'margin-left': '50%',
            'margin-top': '1%'

        }
    ),
    html.Button('INPUT YOUR DATA!', id='submit-val', n_clicks=0,
                style={
                    'appearance': 'button',
                    'backface-visibility': 'hidden',
                    'background-color': '#405cf5',
                    'border-radius': '6px',
                    'border-width': '0',
                    'box-shadow': 'rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, '
                                  '0, .07) 0 1px 1px 0',
                    'box-sizing': 'border-box',
                    'color': '#fff',
                    'cursor': 'pointer',
                    'font-family': '-apple-system,system-ui,"Segoe UI",Roboto,"Helvetica Neue",Ubuntu,sans-serif',
                    'font-size': '150%',
                    'height': '44px',
                    'line-height': 1.15,
                    'margin': '12px',
                    'outline': 'none',
                    'overflow': 'hidden',
                    'padding': '30px',
                    'position': 'relative',
                    'text-align': 'center',
                    'text-transform': 'none',
                    'user-select': 'none',
                    '-webkit-user-select': 'none',
                    'touch-action': 'manipulation',
                    'width': '20%',
                    'left': '40%',
                    'margin-top': '-5%'
                }),

    html.Button('View On Generated Data', id='submit-val1', n_clicks=0,
                style={

                    'appearance': 'button',
                    'align-items': 'center',
                    'background-color': '#0A66C2',
                    'border': 0,
                    'border-radius': '100px',
                    'box-sizing': 'border-box',
                    'color': '#ffffff',
                    'cursor': 'pointer',
                    'display': 'inline-flex',
                    'font-family': '-apple-system,system-ui,"Segoe UI",Roboto,"Helvetica Neue",Ubuntu,sans-serif',
                    'font-size': '16px',
                    'font-weight': 600,
                    'justify-content': 'center',
                    'line-height': '20px',
                    'max-width': '480px',
                    'min-height': '40px',
                    'min-width': '0px',
                    'overflow': 'hidden',
                    'padding': '10px',
                    'padding-left': '20px',
                    'adding-right': '20px',
                    'text-align': 'center',
                    'touch-action': 'manipulation',
                    'transition': 'background-color 0.167s cubic-bezier(0.4, 0, 0.2, 1) 0s, box-shadow 0.167s '
                                  'cubic-bezier(0.4, 0, 0.2, 1) 0s, color 0.167s cubic-bezier(0.4, 0, 0.2, 1) 0s',
                    'user-select': 'none',
                    '-webkit-user-select': 'none',
                    'vertical-align': 'middle',
                    'width': '15%',
                    'margin-left': '78.5%',
                    'margin-top': '-3.5%'
                })

])


@app.callback(
    Input('submit-val', 'n_clicks')
)
def update_output(n_clicks):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        n_clicks
    )


if __name__ == '__main__':
    app.run_server(debug=False)
