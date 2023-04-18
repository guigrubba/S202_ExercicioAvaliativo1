from bson.objectid import ObjectId

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, motorista):
        try:
            corridas = []
            for corrida in motorista.corridas:
                corridas.append({
                    "nota": corrida.nota,
                    "distancia": corrida.distancia,
                    "passageiro": {
                        "nome": corrida.passageiro.nome,
                        "documento": corrida.passageiro.documento
                    }
                })
            res = self.db.collection.insert_one({
                "corridas": corridas, 
                "nota": motorista.nota
            })
            print(f"Motorista created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Um erro ocorreu criando um motorista: {e}")
            return None
        

    def read_motorista_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Motorista achado: {res}")
            return res
        except Exception as e:
            print(f"Um erro ocorreu: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deleted: {res.deleted_count} documento deletado")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return None
