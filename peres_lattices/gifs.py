#This code takes images from the pyfigures folder and creates a gif from them.

import imageio as io
import os

filenames = sorted(filename for filename in os.listdir('pyfigures') if filename.startswith('peres_lattice_XY_with_field'))

with io.get_writer('peres_lattice_XY_with_field.gif', mode='I', duration=0.1) as writer:
    for filename in filenames:
        image = io.imread(os.path.join('pyfigures', filename))
        writer.append_data(image)
writer.close()