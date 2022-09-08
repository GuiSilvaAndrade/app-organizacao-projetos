# App para organização de projetos

De acordo com o escopo da empresa, o ciclo de um projeto tem a seguinte estrutura:

    * Definição do traçado do projeto no Google Earth (.kmz)
    * Desenvolvimento do projeto no ambiente do AutoCAD (.dwg), com uso da base CAD atual da cidade (.dwg)
    * Preenchimento do formulário com dados do projeto (.xlsx)

Dessa forma, o app possui duas funções:

    Uma função para quem cria os traçados do projeto:

        1) Criar uma pasta com o mesmo nome do traçado do projeto 
           e mover o arquivo para dentro dessa pasta.

    E outra função para quem desenvolve os projetos:

        2) A mesma função anterior, além disso, copiar para dentro 
           da pasta o arquivo de desenvolvimento do projeto e 
           arquivo de formulário e renomeá-los com o mesmo nome do 
           traçado do projeto, mas com as respectivas extensões.
        
Apesar do código parecer simples, o ganho de produtividade foi enorme. 

Para fins de teste, utilizou-se o app para a execução das funções em 
1.000 arquivos e o tempo de resposta foi inferior a 10 segundos. 
Estima-se que o ganho de tempo é de aproximadamente 500 vezes,
quando comparado a execução manual.