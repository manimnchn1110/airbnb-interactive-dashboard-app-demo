import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app, server
import output1


tabs_styles = {
    'height': '60px',
    'fontSize': 15,
}
tab_style = {
    'borderBottom': '2px solid #d6d6d6',
    'padding': '20px',
    'fontWeight': 'bold',
}

tab_selected_style = {
    'borderTop': '2px solid #d6d6d6',
    'borderBottom': '2px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '20px'
}

app.layout = html.Div([
    # Header
    html.Div([
        html.H4(
            "Question: How to charge the host appropriate promotional fee for additional reservation coming from third-party Ads?",
            className="row gs-header gs-text-header"),
    ]),
    ##Tabs
    html.Div([
        dcc.Tabs(id="tabs",
                 style={"height": "20", "verticalAlign": "middle"},
                 children=[
                     dcc.Tab(label="Cover Page", value="cover_tab", style=tab_style, selected_style=tab_selected_style),
                     dcc.Tab(label="Input the property with visualization", value="output1", style=tab_style, selected_style=tab_selected_style),
                     dcc.Tab(label='Predict the result', value='output2', style=tab_style, selected_style=tab_selected_style),
                 ], value="leads_tab",
                 )
    ],className="row", style=tabs_styles),

    ##Style
    html.Div([
        html.Div(id="tab_content", className="row", style={"margin": "2% 2%"}),
    ], className="row",style={"margin": "0%"}
    )

],#className="row",
    #style={'textAlign': 'left'}
)


@app.callback(Output("tab_content", "children"), [Input("tabs", "value")])
def render_content(tab):
    if tab == "cover_tab":
        return html.Div([
            html.H6("Backgrounds", className="gs-header gs-text-header padded"),
            dcc.Markdown('''   
##### - In the past, hosts can publish listings with a 3% service fee per reservation without any promotional fee
##### - Lately, Airbnb has started testing an increased host fee (from 3% to 12-15%) 
##### - Additional fee is for reservations coming from external sources (like Google Ads)
##### - The hosts can choose if participate to this promotional plan'''),
            html.H6("Business Mode", className="gs-header gs-text-header padded"),
            dcc.Markdown('''
##### - Airbnb paid for ads from outside sources (like Google Ads) 
##### - Airbnb might get a advantage
##### - Airbnb charge each host separately 
##### - Different promotional plan(CPC or CPV) and different cost'''),
            html.H6("Assumption", className="gs-header gs-text-header padded"),
            dcc.Markdown('''
##### - The host promotional fee should be different each time for each listing
##### - The revenue and cost of each reservation from promotion are different
 '''),
            html.H6("Target", className="gs-header gs-text-header padded"),
            dcc.Markdown('''
##### - Help Airbnb or Host to look for appropriate promotional fee intelligently  ''')
        ])
    elif tab == "output1":
        return output1.layout1

    elif tab == "output2":
        return output1.layout2

    else:
        return html.Div([
            html.H6("Backgrounds", className="gs-header gs-text-header padded"),
            dcc.Markdown('''   
##### - In the past, hosts can publish listings with a 3% service fee per reservation without any promotional fee
##### - Lately, Airbnb has started testing an increased host fee (from 3% to 12-15%) 
##### - Additional fee is for reservations coming from external sources (like Google Ads)
##### - The hosts can choose if participate to this promotional plan'''),
            html.H6("Business Mode", className="gs-header gs-text-header padded"),
            dcc.Markdown('''
##### - Airbnb paid for ads from outside sources (like Google Ads) 
##### - Airbnb might get a advantage
##### - Airbnb charge each host separately 
##### - Different promotional plan(CPC or CPV) and different cost'''),
            html.H6("Assumption", className="gs-header gs-text-header padded"),
            dcc.Markdown('''
##### - The host promotional fee should be different each time for each listing
##### - The revenue and cost of each reservation from promotion are different
 '''),
            html.H6("Target", className="gs-header gs-text-header padded"),
            dcc.Markdown('''
##### - Help Airbnb or Host to look for appropriate promotional fee intelligently  ''')
        ])
# # # # # # # # #
# detail the way that external_css and external_js work and link to alternative method locally hosted
# # # # # # # # #


external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://codepen.io/bcd/pen/KQrXdb.css",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

if __name__ == '__main__':
    app.run_server(debug=True)
    from output1 import input_dict
    print(input_dict)