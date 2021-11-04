from config import *


class Plano(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome
        }

class Carro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(254))
    modelo = db.Column(db.String(254))
    placa = db.Column(db.String(7))
    ano = db.Column(db.String(254))
    # clienteId = db.Column(db.Integer, db.ForeignKey(Cliente.id), nullable=False) 
    # cliente = db.relationship("Cliente")

    def json(self):
        return {
            "id": self.id,
            "marca": self.marca,
            "modelo": self.modelo,
            "placa": self.placa,
            "ano": self.ano,
            # "clienteId": self.clienteId,
            # "cliente": self.cliente.json()
        }

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    telefone = db.Column(db.String(254))
    endereco = db.Column(db.String(254))
    planoId = db.Column(db.Integer, db.ForeignKey(Plano.id), nullable=True) 
    plano = db.relationship("Plano")

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "telefone": self.telefone,
            "endereco": self.endereco,
            "planoid": self.planoId,
            "plano": self.plano.json()
        }


# pra mostrar de modo entendivel no print
    def __str__(self):
        return str(self.id)+"- "+ self.marca + ", " +\
            self.modelo + ", " + self.placa+ ", " + self.ano

# teste com valores fixos    
if __name__ == "__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    #criar e adicionar carros
    carro = Carro(marca = "Chevrolet", modelo = "Corsa", placa = "1234567", ano = "2006")
    db.session.add(carro)
    carro1 = Carro(marca = "Volkswagen", modelo = "Parati", placa = "INT9070", ano = "2006")
    db.session.add(carro1)
    carro2 = Carro(marca = "Ford", modelo = "Focus", placa = "SST5819", ano = "2018")
    db.session.add(carro2)
    carro3 = Carro(marca = "Fiat", modelo = "Uno", placa = "IRS4B90", ano = "2012")
    db.session.add(carro3)

    plano = Plano(nome = "Troca de oleo")
    db.session.add(plano)

    #enviar modificações ativas na sessão pro bd
    db.session.commit()

    print("carros cadastrados no NOVO banco de dados:")
    for carro in db.session.query(Carro).all():
        print(carro.json())

    print("planos cadastrados no NOVO banco de dados:")
    for plano in db.session.query(Plano).all():
        print(plano.json())
