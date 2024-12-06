Feature: Formulário de Contato

  Scenario: Cadastrar produto
     Given Entro na Página de cadastro de produto
      When faço login
      And Efetuo login
      And clico em adicionar
      And preencho os dados do produto
      And faço o upload da imagem "C:\Users\User\Desktop\Captura de tela 2024-12-03 193307.png"
      And salvo os dados
