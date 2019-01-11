# Update, Delete
# Atomic
import mlab
from models.character import Character

mlab.connect()

character = Character.objects().with_id("5c34a4c96de92631101cd2ee")
# character.update(inc__rate=4)
# character.reload()
# print(character.rate)

character.delete()

# 1. Update
# 1.1 Read document
# 1.2 Update document

# 2. Delete
# 2.1. Read document
# 2.2. Delete document