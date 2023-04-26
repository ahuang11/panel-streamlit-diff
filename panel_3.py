import panel as pn
pn.extension()

def callback(clicks):
    return pn.widgets.StaticText(name="Clicks", value=str(clicks))

button = pn.widgets.Button(name="Click me!")
counter = pn.bind(callback, clicks=button.param.clicks)

pn.Column(button, counter).servable()