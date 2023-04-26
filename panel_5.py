import panel as pn
pn.extension()
pn.config.sizing_mode = "stretch_width"

gspec = pn.GridSpec(width=800, height=600)
gspec[0, 0:3] = pn.widgets.Ace()
gspec[0, 3:4] = pn.Spacer(background="purple", margin=0)
gspec[1, 0:4] = pn.Spacer(background="red", margin=0)

check_button_group = pn.widgets.CheckButtonGroup(
    name="Check Button Group",
    options=["A", "B"],
    button_type="primary",
)

accordion = pn.Accordion(
    objects=[("A", "a"), ("B", "b")], toggle=True
)

template = pn.template.FastListTemplate(
    sidebar=["# Sidebar Column", check_button_group, accordion],
    main=[gspec],
    header=["# Header Column"],
    sidebar_width=200,
)
template.servable()
