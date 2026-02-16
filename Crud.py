#Estruturas de dados

usuarios = [
    {
        "id": 1,
        "nome": "Erik",
        "email": "erik@email.com",
        "senha": "123456"
    }
]


# Create
# Regras de negócio:
    #email -> não pode repetir
    #senha -> precisa ter pelo menos 6 caracteres
    #id -> deve ser único
    

def criar_usuario(usuarios, nome, email, senha):

    # validar senha
    if len(senha) < 6:
        return "Erro: senha muito curta"

    # validar email duplicado
    for usuario in usuarios:
        if usuario["email"] == email:
            return "Erro: email já existe"

    # gerar id
    novo_id = len(usuarios) + 1

    novo_usuario = {
        "id": novo_id,
        "nome": nome,
        "email": email,
        "senha": senha
    }

    usuarios.append(novo_usuario)

    return "Usuário criado com sucesso"

# Read - Listar usuários

def listar_usuarios(usuarios):

    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado")
        return

    for usuario in usuarios:
        print(f"""
ID: {usuario["id"]}
Nome: {usuario["nome"]}
Email: {usuario["email"]}
""")

# Update - Atualizar usuário

def atualizar_usuario(usuarios, id, novo_nome):

    for usuario in usuarios:

        if usuario["id"] == id:
            usuario["nome"] = novo_nome
        return "Usuário não encontrado"
    
# Delete - Deletar usuário

def deletar_usuario(usuarios, id):

    for usuario in usuarios:

        if usuario["id"] == id:
            usuarios.remove(usuario)
            return "Usuário deletado"
        
    return "Usuário não encontrado"

# TESTE

print(criar_usuario(usuarios, "Erik", "erik@email.com", "123456"))

listar_usuarios(usuarios)

print(atualizar_usuario(usuarios, 1, "Erik Santos"))

listar_usuarios(usuarios)

print(deletar_usuario(usuarios, 1))

listar_usuarios(usuarios)