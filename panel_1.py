import panel as pn
pn.extension()

markdown = pn.pane.Markdown("Hello world!")
card = pn.Card(markdown, title="Expand me!")
card.servable()
