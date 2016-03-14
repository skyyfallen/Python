"""
Seja o statement sobre diversidade: “The Python Software Foundation and the global Python 
community welcome and encourage participation by everyone. Our community is based on 
mutual respect, tolerance, and encouragement, and we are working to help each other live up 
to these principles. We want our community to be more diverse: whoever you are, and 
whatever your background, we welcome you.”
Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras 
“python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para 
minúsculas e de remover antes os caracteres especiais. 
"""

texto = "The Python Software Foundation and the global Python \
community welcome and encourage participation by everyone. Our community is based on \
mutual respect, tolerance, and encouragement, and we are working to help each other live up \
to these principles. We want our community to be more diverse: whoever you are, and \
whatever your background, we welcome you."

texto = texto.translate(None, ',.')
palavras = texto.split()
lista = []
selecao = []
maior_q_4 = 0

for palavra in palavras:
        p = palavra.lower()
        
        if p[0] in "python":
            lista.append(palavra);
            if(len(palavra) > 4):
                selecao.append(palavra)
                maior_q_4 += 1

print ("\n%d palavras possuem mais de 4 caracteres e uma das letras que formam a palavra 'python'." %maior_q_4)
print "\n", "-"*80, "\n"
print selecao


