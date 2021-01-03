# -*- coding: utf-8 -*-
import csv
import sys
#Criar Cliente
def R(Dict_Pass, Dict_Client):
    
    #Introduzir o NIF do cliente
    nif = int(input("Introduza o NIF: "))

    #Valida se o NIF já existe no dicionário
    for client in Dict_Client:
        if client["NIF"] == nif:
            
            print("Este cliente já se encontra registado")
            
            #Termina o programa caso um cliente com o mesmo NIF seja encontrado
            sys.exit() 

    #Input dos restantes valores
    name = input("Introduza o nome do Cliente: ")
    age = int(input("Introduza a idade do Cliente: "))
    balance = int(input("introduza do saldo do Cliente: "))
    title = "N/A"    
    
    #Valida se o Cliente já possui passe
    choice = True
    choice = input("Já possui passe?: ")
    if choice == "s": #Caso que sim, qual o tipo de passe
        Chosen_Pass = True
        while Chosen_Pass:
            print("""
                  Indique qual o seu passe:
                    1 - Normal
                    2 - Social B
                    3 - Social A
                    4 - Sub 23
                """)
                          
            Chosen_Pass = input("Indique qual dos passes possui: ")
            
            if Chosen_Pass  == "1":
                rank = "Normal"
            elif Chosen_Pass == "2":
                rank = "Social B"
            elif Chosen_Pass == "3":
                rank = "Social A"
            elif Chosen_Pass == "4":
                rank = "Sub 23"
            else:
                print("Escolha inválida")
                
            expiration_date = int(input("Indique a validade do passe(Ano):"))
            Chosen_Pass = False
    
    #Caso que não, atribui N/A ao escalão e á validade
    elif choice == "n":
        rank = "N/A"
        expiration_date = "N/A"

    else:
        print("Escolha uma opção correcta(s/n)")

    
    #Cria um novo dicionário
    new_Client = {}

    #Atribui ao novo dicionário
    new_Client["NIF"] = nif
    new_Client["Nome"] = name
    new_Client["Idade"] = age
    new_Client["Saldo"] = balance
    new_Client["Escalao"] = rank
    new_Client["Validade"] = expiration_date
    new_Client["Titulo"] = title

    #Junta ao dicionário Dict_Client
    Dict_Client.append(new_Client)

    print("Cliente com o NIF %d adicionado" % nif)

#Adquirir titulo
def EP(Dict_Pass, Dict_Client):

   
    nif = int(input("Introduza o NIF do cliente: "))
    
    
    for client in Dict_Client:
        if client["NIF"] == nif:
            
            #Isto evita fazer for loops sempre que precisamos dos dados do Cliente
            i = Dict_Client.index(client)
            
            print("Cliente Validado")

            
            Rank = Dict_Client[i]["Escalao"]
            Client_Age = Dict_Client[i]["Idade"]
                                  
            menu = True
            while menu:
                
                print("""
                      1 - Metropolitano
                      2 - Municipal
                      3 - -12
                      4 - +65
                      5 - Voltar ao menu principal
                      """)
                      
                      
                menu = input("Selecione a opção: ")
                
 #A ideia nas proiximas linhas de código é:

#Valida se o Saldo é superior ou igual ao valor do titulo que está adquirir
 #if Dict_Client[i]["Saldo"] >= Dict_Pass[0]["Normal"]:
  
#Desconta o valor ao cliente     
#Dict_Client[i]["Saldo"] = Dict_Client[i]["Saldo"] - Dict_Pass[0]["Normal"]

#Atribui o titulo ao cliente
#Dict_Client[i]["Titulo"] = Dict_Pass[0]["Pass"]
                
                #Metropolitano
                if menu == "1":
                    
                    if Rank == "Normal":
                        if Dict_Client[i]["Saldo"] >= Dict_Pass[0]["Normal"]:
                            Dict_Client[i]["Saldo"] = Dict_Client[i]["Saldo"] - Dict_Pass[0]["Normal"]
                            Dict_Client[i]["Titulo"] = Dict_Pass[0]["Pass"]
                            print("Titulo Atribuido")
                            
                        else:
                            print("Saldo insuficiente")
                            
                    if Rank == "Social B":
                        if Dict_Client[i]["Saldo"] >= Dict_Pass[0]["Social B"]:
                            Dict_Client[i]["Saldo"] = Dict_Client[i]["Saldo"] - Dict_Pass[0]["Social B"]
                            Dict_Client[i]["Titulo"] = Dict_Pass[0]["Pass"]
                            print("Titulo Atribuido")
                            
                    
                    #Social A
                    if Rank == "Social A":
                        if Dict_Client[i]["Saldo"] >= Dict_Pass[0]["Social A"]:
                            Dict_Client[i]["Saldo"] = Dict_Client[i]["Saldo"] - Dict_Pass[0]["Social A"]
                            Dict_Client[i]["Titulo"] = Dict_Pass[0]["Pass"]
                            print("Titulo Atribuido")
                            
                        else:
                            print("Saldo Insuficiente")
                      
                        #Sub 23
                    if Rank == "Sub 23":
                        if Dict_Client[i]["Saldo"] >= Dict_Pass[0]["Sub 23"]:
                            Dict_Client[i]["Saldo"] = Dict_Client[i]["Saldo"] - Dict_Pass[0]["Sub 23"]
                            Dict_Client[i]["Titulo"] = Dict_Pass[0]["Pass"]
                            print("Titulo Atribuido")
                            
                        else:
                            print("Saldo Insuficiente")
                
                #Municipal
                if menu == "2":
                
                                  
                    if Rank == "Normal":
                        if Dict_Client[i]["Saldo"] >= Dict_Pass[1]["Normal"]:
                            Dict_Client[i]["Saldo"] = Dict_Client[i]["Saldo"] - Dict_Pass[1]["Normal"]
                            Dict_Client[i]["Titulo"] = Dict_Pass[1]["Pass"]
                            print("Titulo Atribuido")
                            
                        else:
                            print("Saldo insuficiente")
                    
                        #Social B
                    if Rank == "Social B":
                        if Dict_Client[i]["Saldo"] >= Dict_Pass[1]["Social B"]:
                            Dict_Client[i]["Saldo"] = Dict_Client[i]["Saldo"] - Dict_Pass[1]["Social B"]
                            Dict_Client[i]["Titulo"] = Dict_Pass[1]["Pass"]
                            print("Titulo Atribuido")
                            print(Dict_Client[i])
                        else:
                            print("Saldo insuficiente")
                            
                        #Social A
                    if Rank == "Social A":
                        if Dict_Client[i]["Saldo"] >= Dict_Pass[1]["Social A"]:
                            Dict_Client[i]["Saldo"] = Dict_Client[i]["Saldo"] - Dict_Pass[1]["Social A"]
                            Dict_Client[i]["Titulo"] = Dict_Pass[1]["Pass"]
                            print("Titulo Atribuido")
                            
                        else:
                            print("Saldo Insuficiente")
                      
                        #Sub 23
                    if Rank == "Sub 23":
                        if Dict_Client[i]["Saldo"] >= Dict_Pass[1]["Sub 23"]:
                            Dict_Client[i]["Saldo"] = Dict_Client[i]["Saldo"] - Dict_Pass[1]["Sub 23"]
                            Dict_Client[i]["Titulo"] = Dict_Pass[1]["Pass"]
                            print("Titulo Atribuido")
                            
                        else:
                            print("Saldo insuficiente")
                            
                            
                ##+12
                if menu == "3":    
                    
                    
                    if Client_Age >= 12:
                        print("Não apresenta os requisitos necessários para adquirir este passe")
                    
                    
                    else:    
                        Dict_Client[i]["Titulo"] = Dict_Pass[2]["Pass"]
                        print("Titulo Atribuido")
                        
                        
                        
                #+65
                if menu == "4":    
                    
                    
                    if Client_Age <= 65:
                        print("Não apresenta os requisitos necessários para adquirir este passe")
                    
                    
                    else:    
                        #Descontar do Saldo
                        #Normal
                        if Rank == "Normal":
                            if Dict_Client[i]["Saldo"] >= Dict_Pass[3]["Normal"]:
                                Dict_Client[i]["Saldo"] = Dict_Client[i]["Saldo"]- Dict_Pass[3]["Normal"]
                                Dict_Client[i]["Titulo"] = Dict_Pass[3]["Pass"]
                                print("Titulo Atribuido")
                                
                            else:
                                print("Saldo insuficiente")
                    
                        #Social B
                        if Rank == "Social B":
                            if Dict_Client[i]["Saldo"] >= Dict_Pass[3]["Social B"]:
                                Dict_Client[i]["Saldo"] = Dict_Client[i]["Saldo"] - Dict_Pass[3]["Social B"]
                                Dict_Client[i]["Titulo"] = Dict_Pass[3]["Pass"]
                                print("Titulo Atribuido")
                                
                            else:
                                print("Saldo insuficiente")
                            
                        #Social A
                        if Rank == "Social A":
                            if Dict_Client[i]["Saldo"] >= Dict_Pass[3]["Social A"]:
                                Dict_Client[i]["Saldo"] = Dict_Client[i]["Saldo"] - Dict_Pass[3]["Social A"]
                                Dict_Client[i]["Titulo"] = Dict_Pass[3]["Pass"]
                                print("Titulo Atribuido")
                            
                            else:
                                print("Saldo Insuficiente")  

                    
    else:
         print("Cliente não se encontra registado, por favor registe antes de adquirir um titulo")                           
  
#Verificar validade do passe
def CV(Dict_Client):
    
    anoActual = 2021
    
    nif = int(input("Introduza o NIF do cliente: "))
    
    for client in Dict_Client:
        if (client["NIF"] == nif):
            
            i = Dict_Client.index(client)
            
            if anoActual > Dict_Client[i]["Validade"]:
                print("Data de validade expirada")
                break
                
            else:
                print("Está dentro da validade")
                break
    else:
        print("Cliente não se encontra registado, por favor registe antes de efectuar esta operação")

#Guardar dicionário de clientes em um ficheiro CSV
def G(Dict_Client):

    Colunas = ["NIF", "Nome", "Idade", "Saldo", "Escalao", "Validade", "Titulo"]
    
    filename="Clientes.csv"

    with open(filename, 'w') as csvfile: 
        
        writer = csv.DictWriter(csvfile, fieldnames = Colunas) 
        
        writer.writeheader() 
        
        writer.writerows(Dict_Client) 
        
    print("Ficheiro guardado")

#Ler Ficheiro de clientes
def L():
    filename="Clientes.csv"
    
    with open(filename, 'r') as data: 
      
        for line in csv.DictReader(data): 
            print(line)  

#Main
def main():
    
    Dict_Pass = [
    
        {
            "Pass": "Metropolitano", 
            "Validade espacial": "AML", 
            "Validade Temporal": "Mensal", 
            "Normal": 40.0, 
            "Social B": 30.0, 
            "Social A": 20.0, 
            "Sub 23": 16.0
        },
    
        {
            "Pass": "Municipal", 
            "Validade espacial": "Lisboa ou Amadora ou Odivelas", 
            "Validade Temporal": "Mensal", 
            "Normal": 30.0, 
            "Social B": 22.5, 
            "Social A": 15.0, 
            "Sub 23": 12.0
         },
        
        {
            "Pass": "-12", 
            "Validade espacial": "AML", 
            "Validade Temporal": "Mensal", 
            "Normal": 0.0, 
            "Social B": 0.0, 
            "Social A": 0.0,
            "Sub 23": 0.0,
         },
            
        {
            "Pass": "+65", 
            "Validade espacial": "AML", 
            "Validade Temporal": "Mensal", 
            "Normal": 20.0, 
            "Social B": 20.0,
            "Social A": 20.0, 
            "Sub 23":  20.0,
         }, 
        ]

    Dict_Client = [
    
        {
            "NIF": 1, 
            "Nome": "Ruben", 
            "Idade": 70, 
            "Saldo": 100.0, 
            "Escalao": "Normal", 
            "Validade": 2020, 
            "Titulo": "N/A"
         },
    
        {
            "NIF": 2, 
            "Nome": "Patricia", 
            "Idade": 10, 
            "Saldo": 100.0, 
            "Escalao": "Social B", 
            "Validade": 2022, 
            "Titulo": "N/A"
         },
    
        {
            "NIF": 3, 
            "Nome": "Carla", 
            "Idade": 30, 
            "Saldo": 100.0, 
            "Escalao": "Social A", 
            "Validade": 2022, 
            "Titulo": "N/A"
         },
    
        {
            "NIF": 4, 
            "Nome": "Andre", 
            "Idade": 20, 
            "Saldo": 100.0, 
            "Escalao": "Sub 23", 
            "Validade": 2022, 
            "Titulo": "N/A"
         }
        ]
    
    
    menu = True
    while menu:
        print("""
              1 - Criar Cliente
              2 - Adquirir Passe
              3 - Consultar Validade do Passe
              4 - Guardar Base de Dados
              5 - Ler Base de Dados
              6 - Sair do programa
              """)
              
        menu = input("Selecione a opção: ")
        
        if menu == "1":     
            R(Dict_Pass, Dict_Client)
        elif menu == "2":   
            EP(Dict_Pass, Dict_Client)
        elif menu == "3":   
            CV(Dict_Pass, Dict_Client)
        elif menu == "4":   
            G(Dict_Client)
        elif menu == "5":   
            L()
        elif menu == "6":   
            menu = None # Sair do Programa            
        else:           # Para o Programa não crashar
            print("Opção inválida") 

main()