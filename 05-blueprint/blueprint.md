# Blueprint Visual — Dahara Yoga e Constelação Familiar

Este documento mapeia a estrutura visual e de seções detalhada com base nos arquivos de referência e estilos globais identificados na pasta `/04-referencia-visual/`. Este é um site **One Page** moderno, com transições suaves, alta legibilidade e elementos de design premium.

---

## 1. Estilo Visual Identificado (Design System)

### Paleta de Cores
*   **Fundo Principal (Light Mode):** `#faf3ee` (Creme Suave / Nude Quente)
*   **Fundo Escuro / Overlays (Dark Sections):** `#2a1238` (Roxo Profundo)
*   **Cor de Destaque Primária (Botões e Links principais):** `#3a1c48` (Roxo Escuro Profundo)
*   **Cor de Hover Primária:** `#5a3068` (Roxo Médio)
*   **Cor de Destaque Secundária / Accent 1:** `#ab7e44` (Dourado Elegante)
*   **Cor de Destaque Terciária / Accent 2:** `#c9a46c` (Dourado Claro / Champagne)
*   **Cor de Fundo Secundária (Seções de Destaque):** `#f3e4d8` (Creme Rosado)
*   **Texto Principal:** `#3d2e34` (Marrom Escuro Quente)
*   **Títulos:** `#2e1a35` (Roxo Título)
*   **Linhas / Divisores:** `#e0c9b5` (Dourado/Nude Sutil)

### Tipografia
*   **Títulos (H1, H2, H3, H4, H5, H6):** `Outfit` ou `Be Vietnam Pro` (Sans-serif moderno, geométrico e com excelente peso visual).
    *   **Pesos:** 600 (Semibold) ou 700 (Bold)
    *   **Espaçamento:** Letter-spacing negativo de `-1px` para H1 e `-0.5px` para H2 para um visual editorial premium.
*   **Texto Corrido & Elementos Menores:** `Inter` (Sans-serif geométrico de alta legibilidade).
    *   **Peso:** 400 (Regular)
    *   **Line-height:** `1.4em` a `1.5em` para leitura confortável.

### Espaçamento entre Seções
*   **Desktop:** `7em` de preenchimento vertical (Padding Top/Bottom).
*   **Tablet:** `5em` a `3em` de preenchimento vertical.
*   **Mobile:** `2em` a `1em` de preenchimento vertical.

### Estilo de Elementos
*   **Botões / CTAs:** Estilo cápsula (`border-radius: 21px` ou superior), com borda sutil de `1px` sólida e transição suave de cor no hover.
*   **Campos de Formulário:** Arredondados com `border-radius: 30px` e borda sutil.
*   **Cards:** Bordas arredondadas suaves (`border-radius: 15px`), sombras extremamente suaves (`box-shadow: 0 0 60px rgba(0, 0, 0, 0.1)`) para dar efeito de flutuação tridimensional.
*   **Imagens:** Cantos arredondados (`border-radius: 15px` ou superior). Na seção Hero, as imagens de background possuem um overlay escuro gradiente (`#080C14` a `#080C141A`) com ângulo de 135 graus para garantir alto contraste com o texto em branco.

---

## 2. Estrutura do HEADER (Cabeçalho)

O cabeçalho é dividido em duas barras horizontais integradas:

### 1) Barra de Acessos Superior (Top Bar)
*   **Fundo:** Cor primária `#3a1c48` (Roxo Escuro Profundo)
*   **Elementos à Esquerda:** Lista de ícones inline contendo o telefone de contato `(19) 98138-1560` e horário de funcionamento, na cor branca/cinza claro `#F0F0F0`.
*   **Elementos à Direita:** Ícones sociais circulares (Instagram, Facebook).
*   **Responsividade:** Oculta em dispositivos móveis (Mobile).

### 2) Barra Principal de Navegação
*   **Fundo:** `#faf3ee` (translúcido/vidro com desfoque creme quente).
*   **Elemento Esquerdo:** Logo da empresa (Dahara) alinhado à esquerda (altura de 49px no desktop, 35px no mobile).
*   **Elemento Central/Direito:** Menu de navegação horizontal (`nav-menu`) com link direto para as âncoras da página One Page: Início, Benefícios, Serviços, Para Quem, Como Funciona, Diferenciais, Depoimentos, FAQ, Contato.
*   **Elemento Extremo Direito:** Botão de ação (CTA) para agendamento direto ("Falar no WhatsApp"), estilizado com cantos arredondados.
*   **Comportamento Mobile:** O botão de ação é ocultado no mobile. Surge um botão de menu hambúrguer (`ti-menu`) que se transforma em botão de fechar (`ti-close`) ao ser clicado, abrindo um menu dropdown limpo com os mesmos links de âncoras.

---

## 3. Ordem Exata das Seções (De cima para baixo)

### Seção 1: HERO
*   **Tipo:** Hero Section com fundo de mídia dinâmico e overlay gradiente.
*   **Estrutura:**
    *   Fundo com slideshow de imagens de alta resolução que transitam de forma suave (efeito Ken Burns ativado).
    *   Overlay gradiente roxo profundo (`#2a1238`) de 135 graus para legibilidade do texto.
    *   Coluna de conteúdo alinhada à esquerda (ocupando 50% da largura da tela).
    *   Título Principal H1 (Tipografia `Outfit` de 48px a 61px).
    *   Subtítulo/Texto descritivo em branco.
    *   Dois botões de CTA lado a lado (Primário: Botão preenchido "Agendar pelo WhatsApp"; Secundário: Botão vazado/borda "Conhecer os Serviços").

### Seção 2: BARRA DE AGENDAMENTO / CREDIBILIDADE (Floating Card)
*   **Tipo:** Seção flutuante e sobreposta que transiciona entre a Hero e a seção posterior.
*   **Estrutura:**
    *   Um grande card centralizado flutuando com margem superior negativa (`margin-top: -6em`), cantos arredondados (`border-radius: 15px`), fundo branco e sombra suave e profunda (`box-shadow: 0 0 60px rgba(0, 0, 0, 0.1)`).
    *   **Coluna Esquerda (35%):** Fundo com imagem e overlay gradiente de menta/sage. Contém dois blocos de ícones (Phone e Email/WhatsApp) para atendimento imediato.
    *   **Coluna Direita (65%):** Um formulário de agendamento online rápido com campos de texto de largura parcial (Nome, Telefone, Serviço, Data, Hora) e um botão de envio arredondado "Agendar Agora".

### Seção 3: SOBRE NÓS (Who We Are)
*   **Tipo:** Estrutura mista de duas colunas (Conteúdo e Mídia).
*   **Estrutura:**
    *   **Coluna Esquerda (55%):** Textos institucionais e missão. Contém um H6 de categoria ("Sobre Nós"), um H2 ("Quem Somos"), um parágrafo descritivo largo, um divisor sutil e dois blocos de ícones ilustrando a essência da marca.
    *   **Coluna Direita (45%):** Imagem institucional de alta qualidade com cantos arredondados (`border-radius: 15px`) acompanhada de um contador estatístico ("15+ anos de experiência", etc.).

### Seção 4: LOGOS DE CONFIANÇA (Trusted By)
*   **Tipo:** Grid horizontal simples / Carrossel sutil.
*   **Estrutura:**
    *   Uma linha de logos de marcas parceiras ou representadas, em tons de cinza claro/esmaecido para não competir visualmente com o conteúdo principal.

### Seção 5: BENEFÍCIOS (Our Value)
*   **Tipo:** Grid de Destaques / Seção institucional com aspas/depoimento flutuante.
*   **Estrutura:**
    *   Título de seção "Benefícios" com subtítulo H2 explicativo.
    *   Layout de duas colunas:
        *   **Lado Esquerdo:** Lista de benefícios marcados com ícones personalizados.
        *   **Lado Direito:** Uma caixa de destaque flutuante que exibe um depoimento forte ou uma frase de impacto inspiradora integrada ao design, cercada de aspas estilizadas.

### Seção 6: SERVIÇOS (Our Services)
*   **Tipo:** Grid de Cards de Serviços.
*   **Estrutura:**
    *   H6 pequeno de categoria ("Nossos Serviços") + H2 grande de destaque.
    *   Grid responsivo de 3 colunas (totalizando 6 cards de serviços):
        *   Cada card possui borda sutil, fundo branco, cantos arredondados, ícone ilustrativo no topo (de estilo minimalista em tons de verde-água/sage), título do serviço H3, parágrafo explicativo curto e um link de CTA inline ("Quero saber mais").

### Seção 7: COMO FUNCIONA (How it Works)
*   **Tipo:** Linha de Processo Passo a Passo.
*   **Estrutura:**
    *   H6 de categoria ("Passo a Passo") + H2 ("Como Funciona").
    *   Layout horizontal de 4 a 5 colunas representando as etapas consecutivas (1, 2, 3, 4).
    *   Cada passo contém um número grande em tom pastel (ex: "01"), título curto da etapa e descrição simplificada.

### Seção 8: DIFERENCIAIS (Why Choose Us)
*   **Tipo:** Banner misto com Imagem de Destaque de um lado e Blocos de Ícones de outro.
*   **Estrutura:**
    *   H6 de categoria + H2 de impacto.
    *   Coluna de imagem de grande impacto visual que retrata a harmonia do espaço físico.
    *   Coluna adjacente com uma lista de diferenciais representados por ícones minimalistas de alta resolução e textos de apoio.

### Seção 9: DEPOIMENTOS (Testimonials)
*   **Tipo:** Carrossel horizontal de depoimentos.
*   **Estrutura:**
    *   Título da seção com foco na prova social.
    *   Carrossel deslizante composto por cards de depoimentos, com estrelas de avaliação, mensagem de agradecimento, nome do cliente e sua respectiva localização/cidade.

### Seção 10: ÁREA DE ATUAÇÃO E LOCALIZAÇÃO (Map Section)
*   **Tipo:** Estrutura de dois blocos (Contato/Endereço + Mapa Incorporado).
*   **Estrutura:**
    *   **Bloco Esquerdo:** Caixa com as informações de endereço físico, horários e telefones destacados de forma organizada e elegante com ícones funcionais.
    *   **Bloco Direito:** Mapa do Google Maps integrado de ponta a ponta (full-width ou em card correspondente) mostrando a exata localização de forma dinâmica.

### Seção 11: PERGUNTAS FREQUENTES (FAQ)
*   **Tipo:** Accordion (Sanfona de Dúvidas).
*   **Estrutura:**
    *   Título e pequeno texto convidando o usuário a tirar suas dúvidas.
    *   Lista vertical de perguntas e respostas que abrem e fecham de forma interativa através de efeito de sanfona (Accordion) suave, mantendo o visual limpo.

### Seção 12: CTA DE LEALDADE / FINAL (Newsletter/Loyalty Program)
*   **Tipo:** Seção final de grande impacto (Call to Action).
*   **Estrutura:**
    *   Fundo em cor contrastante escura ou com overlay gradiente.
    *   H2 centralizado de convite à ação ("Agende sua aula experimental").
    *   Um formulário rápido ou um botão grande e destacado para ação direta no WhatsApp.

---

## 4. Estrutura do FOOTER (Rodapé)

O rodapé encerra a navegação com uma divisão limpa de duas seções principais:

### 1) Área Principal de Links e Informações (3 ou 4 Colunas)
*   **Fundo:** `#faf3ee` ou `#f3e4d8` (cor coordenada com o estilo geral creme).
*   **Coluna 1 (30%):** Logo estilizada, breve texto de apresentação/propósito da empresa e os links das redes sociais (ícones circulares).
*   **Coluna 2 (20%):** Links rápidos de navegação interna (Início, Benefícios, Serviços, Contato).
*   **Coluna 3 (20%):** Informações de endereço físico, email de suporte e telefone em formato de lista de ícones.
*   **Coluna 4 (30%):** Formulário simples de Newsletter contendo campo de input para e-mail com bordas arredondadas e botão de envio integrado.

### 2) Barra de Copyright & Políticas (Bottom Footer)
*   **Fundo:** Cor de destaque secundária `#ab7e44` (Dourado Elegante) com opacidade suave e borda superior fina para separação.
*   **Lado Esquerdo:** Texto de Copyright oficial ("© 2026 Dahara Yoga e Constelação Familiar. Todos os direitos reservados. Desenvolvido por Axtra Venture").
*   **Lado Direito:** Links de rodapé horizontais para Termos de Serviço e Políticas de Privacidade.
