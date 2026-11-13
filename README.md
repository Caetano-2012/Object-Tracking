<escape><h1 align="center">🏀 Object Tracking</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
  <img src="https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge" alt="Status Badge">
</p>

<p align="center">
  <i>Rastreamento de objetos em um vídeo de basquete utilizando OpenCV.</i><br>
  <b>Autor:</b> Caetano Bordin
</p>

---

## 🧩 Sobre o Projeto

O **Object Tracking** é um projeto desenvolvido em Python com a biblioteca OpenCV, utilizando o algoritmo **CSRT (Discriminative Correlation Filter with Channel and Spatial Reliability)** para rastrear objetos em vídeos.

O programa permite selecionar manualmente uma região do vídeo, delimitando o objeto que será acompanhado. A partir dessa seleção, o algoritmo tenta identificar e acompanhar sua posição nos frames seguintes, atualizando continuamente um retângulo ao redor dele.

O projeto utiliza um vídeo de basquete como exemplo de aplicação.

## 🧰 Tecnologias Utilizadas

- **Python** — linguagem utilizada no desenvolvimento.
- **OpenCV (cv2)** — processamento de vídeo e rastreamento de objetos.
- **Time** — módulo importado para operações relacionadas ao tempo.
- **Math** — módulo importado para operações matemáticas.

### Algoritmo CSRT

O CSRT é um algoritmo de rastreamento visual que utiliza filtros de correlação para acompanhar um objeto selecionado ao longo de um vídeo.

Ele considera informações espaciais e características dos canais de imagem para melhorar a localização do objeto durante o rastreamento.

## ⚙️ Funcionalidades

- 🎞️ Carregamento do vídeo `basquete.mp4`;
- 🎯 Seleção manual do objeto que será rastreado;
- 📦 Criação de uma região delimitadora (*Bounding Box*);
- 🔍 Rastreamento utilizando o algoritmo CSRT;
- 🟩 Atualização da posição do retângulo a cada frame;
- ✅ Exibição da mensagem "Rastreando" quando o acompanhamento é bem-sucedido;
- ❌ Exibição de "Errou" quando o rastreador não consegue localizar o objeto;
- ⏹️ Interrupção do programa pela barra de espaço.

## 🔄 Como Funciona

O funcionamento do programa pode ser dividido em cinco etapas:

**1. Carregamento do vídeo**

O OpenCV abre o arquivo `basquete.mp4` e lê seu primeiro frame.

**2. Seleção do objeto**

O usuário seleciona manualmente, com o mouse, a região que deseja acompanhar.

**3. Inicialização do rastreador**

O algoritmo CSRT recebe a imagem inicial e a região selecionada para iniciar o acompanhamento.

**4. Rastreamento contínuo**

A cada novo frame, o método `tracker.update()` tenta localizar o objeto e atualizar suas coordenadas.

**5. Exibição do resultado**

Se o objeto for localizado, um retângulo verde é desenhado ao seu redor. Caso contrário, a mensagem "Errou" é exibida.

## 📚 Aprendizados

Durante o desenvolvimento, foram trabalhados conceitos importantes de visão computacional:

- Captura e processamento de vídeos;
- Rastreamento de objetos (*Object Tracking*);
- Utilização de algoritmos de rastreamento;
- Seleção de regiões de interesse (*ROI*);
- Coordenadas e dimensões de *Bounding Boxes*;
- Atualização de informações entre frames;
- Desenho de retângulos e textos em imagens;
- Verificação de sucesso e falha no rastreamento.

## 🕹️ Como Executar

1. Instale a versão do OpenCV que disponibiliza os algoritmos de tracking:

```bash
pip install opencv-contrib-python
```

2. Coloque o arquivo `basquete.mp4` na mesma pasta do programa.

3. Execute o arquivo Python:

```bash
python main.py
```

4. Quando o primeiro frame aparecer, selecione com o mouse a região do objeto que deseja rastrear e confirme a seleção.

5. Para encerrar o programa, pressione a **barra de espaço**.

## 📜 Licença

O código pode ser usado somente para **fins educacionais**.

É permitida a modificação e redistribuição, desde que os autores sejam citados e a licença original seja mantida.

O software é fornecido **"como está"**, sem garantias de qualquer tipo. Os autores não são responsáveis por danos decorrentes de seu uso.

## 👨‍💻 Autor

**Caetano Bordin**

🔗 [@Caetano-2012](https://www.github.com/Caetano-2012)

---</escape>
