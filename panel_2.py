import panel as pn
pn.extension()

package = pn.widgets.Select(
    name="Package", options=["Panel", "Streamlit"]
)
column = pn.Column(package)

# set package value
package.value = "Streamlit"

# get package value
column.append(f"Selected package: {package.value}")

column.servable()