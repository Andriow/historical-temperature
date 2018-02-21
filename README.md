# historical-temperature
Armazena em um banco de dados informações históricas de clima e temperatura atualizadas com granularidade diária para as cidades que contém aeroportos com informações de METAR, de forma gratuíta.

Para os aeroportos brasileiros a relação de código de METAR pode ser encontrada na página do INPE. em: http://servicos.cptec.inpe.br/XML/

A extração de dados é realizada através da consulta histórica WEB do site https://www.wunderground.com, por exemplo: https://www.wunderground.com/history/airport/SBBI/2018/1/5/DailyHistory.html

# Configuração do banco de dados
A configuraço do banco de dados se dá através da função configure_engine().
```Python
DB_TYPE = 'mysql'
DB_DRIV = 'pymysql'
DB_USER = 'DBUSER'
DB_PASS = 'PASSWORD'
DB_HOST = 'IP'
DB_NAME = 'DBNAME'
```
E se necessário, pode-se utilizar a função create_table() para criar a tabela, se ela não existir.

# Como testar
Para teste da extraço de dados, foi crida a função test(), que recebe como parâmetros o código do aerporto e a data e imprime na tela o dataframe do pandas com as informaçes lidas do HTML.

Por exemplo:
```Python
test('SBCG',2017,10,2)
```

# Como utilizar
Para utilização é apenas chamar a função run com os parâmetros de data de início e data de fim.

Por exemplo:
```Python
start_date = date(2018, 1, 1)
end_date = date(2018, 2, 1) 
run(start_date, end_date)
```
Levando em consideraço que o data de fim não é inclusivo, então o range gerado, no exemplo, fica entre 01/01/2018 até 31/01/2018.

As saídas são os dados inseridos no banco de dados definido na parte de configurações, e um json impresso no terminal contendo a contagem de quantos dias não foram possíveis recuperar dados para cada aeroporto.
