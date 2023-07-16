import os
import sys

common = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.path.pardir, "common")
)
if common not in sys.path:
    sys.path.insert(0, common)

# import kicad_sym 
import sys

# Create an IC that has 4 pins and is a rectangel
# R = AHK?
# Val = 100nF
from kicad_sym import Circle, KicadLibrary, KicadSymbol, Pin, Rectangle

# the libname of the file and the symbol needs to be the same
libname = "demo"
file_name = "demo"
new_symbol = KicadSymbol("a_new_part", libname, filename=file_name)
lib = KicadLibrary(libname + ".kicad_sym")
lib.symbols.append(new_symbol)


# TODO properties
new_symbol.add_default_properties()
ref = new_symbol.get_property("Reference")
ref.value = "F"
ref.posx = 0
ref.posy = 2.54 * 3.25  # 325 mil
val = new_symbol.get_property("Value")
val.posy = 2.54 * 2.5


new_symbol.pins.append(
    Pin(number="1", name="GND", etype="passive", posx=-7.62, posy=2.54, length=5.08)
)
new_symbol.pins.append(
    Pin(number="2", name="PA2", etype="passive", posx=-5.08, posy=-2.54)
)


new_symbol.rectangles.append(Rectangle(2.54, -5.08, -2.54, 5.08, stroke_width=0.254))
new_symbol.arcs.append(Circle(2.54, 0, 5.08, fill_type="outline"))


lib.write()