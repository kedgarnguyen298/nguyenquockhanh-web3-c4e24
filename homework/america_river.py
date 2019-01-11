import mlab
from models.river_model import River

mlab.connect()

america_river = River.objects(continent__exact='S. America', length__lt=1000)

for river in america_river:
    print(river.name)