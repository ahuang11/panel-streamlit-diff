import panel as pn
pn.extension()

def callback(_):
    counter.value = str(int(counter.value) + 1)

button = pn.widgets.Button(name="Click me!")
counter = pn.widgets.StaticText(name="Clicks", value="0")

# add interactivity
button.on_click(callback=callback)

column = pn.Column(button, counter)
column.servable()