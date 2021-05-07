import shelve
import os

DIR = os.path.dirname(os.path.realpath(__file__))
db = shelve.open(f'{DIR}/contatos.db')


class Contato:
    def __init__(self, nome, telefone, email, blog):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.blog = blog

    def salvar(self):
        novo_contato_id = self.email
        db[novo_contato_id] = {
            "nome": self.nome,
            "telefone": self.telefone,
            "email": self.email,
            "blog": self.blog,
            "contato_id": novo_contato_id
        }
        return novo_contato_id

    def pega_novo_id(self):
        id_inteiro = []
        for i in db.keys():
            id_inteiro.append(int(i))
        return str(max(id_inteiro) + 1)

    @classmethod
    def pesquisar_nome(cls, nome):
        encontrados = []
        for c in db:
            if db[c]['nome'].find(nome) >= 0:
                encontrados.append(db[c])
        return encontrados

    @classmethod
    def remover(cls, contato_id):
        del db[contato_id]
        return True

    @classmethod
    def atualizar(cls, contato_id, contato):
        db[contato_id] = contato
        return True

    @classmethod
    def pesquisar(cls, contato_id):
        try:
            return db[contato_id]
        except IndexError:
            return {}

    @classmethod
    def tudo(cls):
        return dict(db)

