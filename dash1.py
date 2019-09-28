import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
	html.H1("Hello Dash!!",
		style={
            'textAlign': 'center',
            'color': colors['text']}
            ),
	html.Div('DASh --- whatever'),

	dcc.Graph(
		id = 'samplegraph',
		figure = {

			'data' : [
			{'x' : [5,6,7], 'y': [12,15,18], 'type' : 'bar', 'name': 'FF' },
			{'x' : [8,9,10,7.5], 'y': [12,15,9.5,18], 'type' : 'bar', 'name': 'SF' }


			],

			'layout' : {

				'title' : 'Simple work'

			}

		}
		)


	])

if __name__ == '__main__':
	app.run_server(port =4050)
