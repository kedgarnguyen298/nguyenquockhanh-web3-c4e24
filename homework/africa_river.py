import mlab
from models.river_model import River

mlab.connect()

africa_river = River.objects(continent__exact='Africa')

for river in africa_river:
    print(river.name)


