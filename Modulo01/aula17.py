nivel = int(input("Digite o seu nível de experiência profissional entre (1 ate 10):"))

if(nivel < 1):
    mensagem = "Você nunca trabalhou na vida"
if(nivel >= 1 <= 3):
    mensagem = "Você foi apenas jovem aprendiz"
if(nivel >= 4 < 6):
    mensagem = "Você já trabalhou alguns anos"
if(nivel >= 6 < 9):
    mensagem = "Você é um bom profissional"
if(nivel == 10):
    mensagem = "Você está perto de se aposentar"


print(mensagem)