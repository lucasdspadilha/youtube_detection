Youtube Detection

ALunos: Julio Schendroski, Lucas Padilha, Pollyana Keller, Rayana Silva, Vitorio Serafini.

Sobre o Projeto

Este projeto tem como objetivo identificar o botão "Pular Anúncio" na plataforma YouTube para facilitar a usabilidade do usuário, sem burlar as regras de uso do sistema. A solução utiliza técnicas de visão computacional para automatizar o clique no botão, tornando a experiência mais fluida.

Tecnologias Utilizadas

YOLOv5: Algoritmo de detecção de objetos usado para identificar elementos como youtube_ad e youtube_skip_button nas imagens.

Python: Linguagem principal para desenvolvimento do modelo e scripts auxiliares.

Label Studio: Ferramenta para anotação do dataset.

PyTorch: Biblioteca utilizada para o treinamento do modelo.

Dataset

Classes

youtube_ad: Identificação de anúncios do YouTube.

youtube_skip_button: Identificação do botão "Pular Anúncio".

Origem

Todas as imagens foram capturadas pelo grupo, garantindo originalidade.

Inclui variações de imagens de diferentes anúncios.

Estrutura

Divisão em conjuntos de treino, validação e teste para garantir a qualidade e robustez do modelo.

Pipeline de Treinamento

Preparação do Dataset:

Anotação das imagens utilizando o Label Studio.

Divisão do dataset em treino, validação e teste.

Configuração do Modelo:

Definição dos hiperparâmetros, como taxa de aprendizado e número de épocas.

Configuração do modelo YOLOv5 para treinamento.

Treinamento:

Treinamento utilizando PyTorch, ajustando parâmetros para maximizar a precisão e minimizar o custo computacional.

Desafios

Qualidade do Dataset:

Garantir diversidade e representatividade para melhorar a precisão do modelo.

Eficiência Computacional:

Ajustar o modelo para obter maior precisão sem aumentar significativamente o custo computacional.

Lições Aprendidas

A importância de um dataset diversificado para treinar modelos de visão computacional.

A necessidade de validação constante para garantir resultados confiáveis.

Como a visão computacional pode ser aplicada de forma criativa para resolver problemas do cotidiano e melhorar a experiência do usuário
