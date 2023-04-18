from database import Database
from helper.writeAJson import writeAJson
from motoristaDAO import MotoristaDAO
from cli import MotoristaCLI

db = Database(database="atlas-cluster", collection="motoristas")
motoristaDAO = MotoristaDAO(database=db)


motoristaCLI = MotoristaCLI(motoristaDAO)
motoristaCLI.run()