# 🔀 Guia Prático: Fork, Google Colab e Pull Request (Turma SIS_4AN262)

Para mantermos nosso repositório oficial organizado e simularmos um fluxo de trabalho real (muito usado no mercado), nós utilizaremos o modelo de **Fork e Pull Request (PR)** para a entrega das atividades. 

Abaixo, você encontra o passo a passo de como copiar o repositório da disciplina, salvar seus exercícios direto do Colab e enviar para avaliação da professora.

---

## Passo 1: Realizando o Fork do Repositório
O *Fork* cria uma cópia exata do repositório oficial na sua própria conta do GitHub. É nesse seu espaço pessoal que você vai salvar seus arquivos iniciais antes de enviar.

1. Acesse a página do repositório oficial da disciplina no GitHub.
2. No canto superior direito da tela, clique no botão **Fork**.
3. Na tela seguinte, mantenha as configurações padrão e clique em **Create fork**.
4. Pronto! Agora você tem uma cópia do repositório no seu perfil (ex: `seu-usuario/python_sis_26_2`).

---

## Passo 2: Salvando o Arquivo via Google Colab no SEU Fork
Agora que você tem o seu próprio repositório, os exercícios feitos no Google Colab serão salvos lá, respeitando as regras de governança da disciplina.

1. No menu superior do Google Colab, clique em **Arquivo** > **Salvar uma cópia no GitHub**.
2. Autorize o Colab a acessar seu GitHub, caso seja o seu primeiro acesso.
3. No campo de seleção de repositório, escolha **o seu fork** (ex: `seu-usuario/python_sis_26_2`) e **NÃO** o repositório oficial da professora.
4. No campo **Caminho do arquivo (File path)**, adicione a pasta da aula antes do nome do arquivo, respeitando o padrão PEP 8 (`snake_case` - letras minúsculas separadas por underline).
   * **Correto:** `aula_02/nome_sobrenome_aula02.ipynb`
   * **Incorreto:** `MeuArquivo Aula2.ipynb` ou salvando direto na raiz sem a pasta da aula.
5. Escreva uma **Mensagem de Commit** clara e descritiva. 
   * *Prefira:* `feat: adiciona declaração de variáveis e inputs da aula 02`.
   * *Evite:* `salvando código` ou `atualização`.
6. Clique em **OK / Salvar**.

---

## Passo 3: Criando o Pull Request (PR)
O Pull Request é o seu "pedido oficial de entrega" para que a professora puxe o código que está no seu Fork para o repositório principal da turma.

1. Acesse o **seu repositório (Fork)** no GitHub (`seu-usuario/python_sis_26_2`).
2. Você verá uma notificação informando que o seu repositório tem commits à frente do original. Clique em **Contribute** (Contribuir) e depois em **Open pull request**.
3. O GitHub vai comparar as alterações. Verifique visualmente se o caminho do seu arquivo está correto (dentro da pasta da aula correspondente).
4. Clique no botão verde **Create pull request**.
5. No título, coloque um resumo claro (ex: *Entrega Aula 02 - Nome Sobrenome*). Na descrição, você pode adicionar comentários adicionais ou dúvidas sobre a atividade para a professora ler.
6. Clique novamente em **Create pull request** para finalizar o envio.

---
### 📅 Lembrete de Datas de Entrega:
* **1º Bimestre:** Os exercícios devem ser entregues até o dia **30/09/2026**.
* **2º Bimestre:** Os exercícios devem ser entregues até o dia **25/11/2026**.

⚠️ **Dificuldades?** Caso tenha problemas para inserir seu arquivo no repositório seguindo este fluxo, solicite ajuda durante a aula ou envie o material por e-mail para `taciany.lima@santacruz.br` até a data prevista do respectivo bimestre.
