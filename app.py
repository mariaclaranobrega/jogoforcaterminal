from random import choice

animais = ["cachorro","gato","cavalo","papagaio","zebra","girafa","boi","ovelha","borboleta","elefante","cobra"]
frutas = ["banana","goiaba","morango","amora","framboesa","uva","laranja"]
cores = ["azul","amarelo","branco","preto","rosa","roxo","verde","laranja"]
acertos = 0

while True:
    print("JOGO DA FORCA\nEscolha um tema:\nDigite 1 para ANIMAIS\nDigite 2 para FRUTAS\nDigite 3 para CORES\nDigite 0 para SAIR DO JOGO")
    escolha = input('')
    tentativas =[]
    chances = 0
    
    if escolha == "0":
        break
    elif escolha == "1":
        palavra=choice(animais)
        print("Categoria: Animais")
        
        while chances<=3:
            for letra in palavra:
                if letra in tentativas:
                    print(letra,end=" ")
                else:
                    print("_",end=" ")
            palpite = str(input('Digite uma letra: ')).lower()
            
            if palpite in tentativas:
                print("Você já tentou esta letra, tente outra!")
                chances+=1

            tentativas.append(palpite)

            if palpite in palavra:
                print("Acertou!")
            else:
                print("Incorreto!")
                chances+=1

            for letra in set(palavra):
                if letra in set(tentativas):
                    if len(set(tentativas))>=len(set(palavra)):
                        if set(tentativas).issuperset(set(palavra)):
                            chances=5

        if set(palavra).issubset(set(tentativas)):
            print(f"{palavra}\nParabéns, você conseguiu adivinhar a palavra!")
            break
        else:
            print("GAME OVER")
            break

    elif escolha == "2":
        palavra=choice(frutas)
        print("Categoria: Frutas")
        
        while chances<=3:
            for letra in palavra:
                if letra in tentativas:
                    print(letra,end=" ")
                else:
                    print("_",end=" ")
            palpite = str(input('Digite uma letra: ')).lower()
            
            if palpite in tentativas:
                print("Você já tentou esta letra, tente outra!")
                chances+=1
                continue

            tentativas.append(palpite)

            if palpite in palavra:
                print("Acertou!")
               
            else:
                print("Incorreto!")
                chances+=1

            for letra in set(palavra):
                if letra in set(tentativas):
                    if len(set(tentativas))>=len(set(palavra)):
                        if set(tentativas).issuperset(set(palavra)):
                            chances=5

        if set(palavra).issubset(set(tentativas)):
            print(f"{palavra}\nParabéns, você conseguiu adivinhar a palavra!")
            break
        else:
            print("GAME OVER")
            break

    elif escolha == "3":
        palavra=choice(cores)
        print("Categoria: Cores")
        
        while chances<=3:
            for letra in palavra:
                if letra in tentativas:
                    print(letra,end=" ")
                else:
                    print("_",end=" ")
            palpite = str(input('Digite uma letra: ')).lower()
            
            if palpite in tentativas:
                print("Você já tentou esta letra, tente outra!")
                chances+=1
                continue
            
            tentativas.append(palpite)
            
            if palpite in palavra:
                print("Acertou!")
              
            else:
                print("Incorreto!")
                chances+=1

            for letra in set(palavra):
                if letra in set(tentativas):
                    if len(set(tentativas))>=len(set(palavra)):
                        if set(tentativas).issuperset(set(palavra)):
                            chances=5

        if set(palavra).issubset(set(tentativas)):
            print(f"{palavra}\nParabéns, você conseguiu adivinhar a palavra!")
            break
        else:
            print("GAME OVER")
            break

    else:
        print("Opção inválida, escolha uma das opções abaixo:")


