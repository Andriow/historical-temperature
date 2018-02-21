#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
BRAZILIAN METAR CODES FROM http://servicos.cptec.inpe.br/XML/
'''

def get_airport_list():
    airports = []
    airport = {}
    airport['sigla'] = 'SBTK'
    airport['aeroporto'] = 'Tarauacá'
    airport['estado'] = 'AC'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBRB'
    airport['aeroporto'] = 'Presidente Médici'
    airport['estado'] = 'AC'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBCZ'
    airport['aeroporto'] = 'Internacional'
    airport['estado'] = 'AC'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBMO'
    airport['aeroporto'] = 'Zumbi dos Palmares'
    airport['estado'] = 'AL'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBEG'
    airport['aeroporto'] = 'Eduardo Gomes'
    airport['estado'] = 'AM'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBMN'
    airport['aeroporto'] = 'Ponta Pelada'
    airport['estado'] = 'AM'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBMY'
    airport['aeroporto'] = 'Manicoré'
    airport['estado'] = 'AM'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBTT'
    airport['aeroporto'] = 'Tabatinga'
    airport['estado'] = 'AM'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBYA'
    airport['aeroporto'] = 'Iuaretê'
    airport['estado'] = 'AM'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBUA'
    airport['aeroporto'] = 'São Gabriel da Cachoeira'
    airport['estado'] = 'AM'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBTF'
    airport['aeroporto'] = 'Tefé'
    airport['estado'] = 'AM'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBAM'
    airport['aeroporto'] = 'Amapá'
    airport['estado'] = 'AP'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBMQ'
    airport['aeroporto'] = 'Internacional'
    airport['estado'] = 'AP'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBOI'
    airport['aeroporto'] = 'Oiapoque'
    airport['estado'] = 'AP'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBLP'
    airport['aeroporto'] = 'Bom Jesus da Lapa'
    airport['estado'] = 'BA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBCV'
    airport['aeroporto'] = 'Caravelas'
    airport['estado'] = 'BA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBIL'
    airport['aeroporto'] = 'Jorge Amado'
    airport['estado'] = 'BA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBLE'
    airport['aeroporto'] = 'Chapada Diamantina'
    airport['estado'] = 'BA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBUF'
    airport['aeroporto'] = 'Paulo Afonso'
    airport['estado'] = 'BA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBPS'
    airport['aeroporto'] = 'Porto Seguro'
    airport['estado'] = 'BA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBSV'
    airport['aeroporto'] = 'Dep. Luís Eduardo Magalhães'
    airport['estado'] = 'BA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBQV'
    airport['aeroporto'] = 'Vitória da Conquista'
    airport['estado'] = 'BA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBFZ'
    airport['aeroporto'] = 'Pinto Martins'
    airport['estado'] = 'CE'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBJU'
    airport['aeroporto'] = 'Cariri'
    airport['estado'] = 'CE'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBBR'
    airport['aeroporto'] = 'Juscelino Kubitschek'
    airport['estado'] = 'DF'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBVT'
    airport['aeroporto'] = 'Eurico Aguiar Salles'
    airport['estado'] = 'ES'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBAN'
    airport['aeroporto'] = 'Anápolis'
    airport['estado'] = 'GO'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBGO'
    airport['aeroporto'] = 'Santa Genoveva'
    airport['estado'] = 'GO'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBCI'
    airport['aeroporto'] = 'Carolina'
    airport['estado'] = 'MA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBIZ'
    airport['aeroporto'] = 'Imperatriz'
    airport['estado'] = 'MA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBSL'
    airport['aeroporto'] = 'Mar. Cunha Machado'
    airport['estado'] = 'MA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBAX'
    airport['aeroporto'] = 'Araxá'
    airport['estado'] = 'MG'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBPR'
    airport['aeroporto'] = 'Carlos Prates'
    airport['estado'] = 'MG'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBBQ'
    airport['aeroporto'] = 'Barbacena'
    airport['estado'] = 'MG'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBBH'
    airport['aeroporto'] = 'Pampulha'
    airport['estado'] = 'MG'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBCF'
    airport['aeroporto'] = 'Tancredo Neves'
    airport['estado'] = 'MG'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBPC'
    airport['aeroporto'] = 'Poços de Caldas'
    airport['estado'] = 'MG'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBUR'
    airport['aeroporto'] = 'Uberaba'
    airport['estado'] = 'MG'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBUL'
    airport['aeroporto'] = 'Uberlândia'
    airport['estado'] = 'MG'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBIP'
    airport['aeroporto'] = 'Ipatinga'
    airport['estado'] = 'MG'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBJF'
    airport['aeroporto'] = 'Francisco de Assis'
    airport['estado'] = 'MG'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBMK'
    airport['aeroporto'] = 'Montes Claros'
    airport['estado'] = 'MG'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBVG'
    airport['aeroporto'] = 'Varginha'
    airport['estado'] = 'MG'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBGV'
    airport['aeroporto'] = 'Gov. Valadares'
    airport['estado'] = 'MG'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBCG'
    airport['aeroporto'] = 'Internacional'
    airport['estado'] = 'MS'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBCR'
    airport['aeroporto'] = 'Corumbá'
    airport['estado'] = 'MS'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBPP'
    airport['aeroporto'] = 'Internacional'
    airport['estado'] = 'MS'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBAT'
    airport['aeroporto'] = 'Alta Floresta'
    airport['estado'] = 'MT'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBBW'
    airport['aeroporto'] = 'Barra do Garças'
    airport['estado'] = 'MT'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBCY'
    airport['aeroporto'] = 'Marechal Rondon'
    airport['estado'] = 'MT'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBHT'
    airport['aeroporto'] = 'Altamira'
    airport['estado'] = 'PA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBBE'
    airport['aeroporto'] = 'Val-de-Cans'
    airport['estado'] = 'PA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBIH'
    airport['aeroporto'] = 'Itaituba'
    airport['estado'] = 'PA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBEK'
    airport['aeroporto'] = 'Jacareacanga'
    airport['estado'] = 'PA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBMA'
    airport['aeroporto'] = 'Marabá'
    airport['estado'] = 'PA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBCC'
    airport['aeroporto'] = 'Cachimbó'
    airport['estado'] = 'PA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBTB'
    airport['aeroporto'] = 'Trombetas'
    airport['estado'] = 'PA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBCJ'
    airport['aeroporto'] = 'Carajás'
    airport['estado'] = 'PA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBSN'
    airport['aeroporto'] = 'Santarém'
    airport['estado'] = 'PA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBTU'
    airport['aeroporto'] = 'Tucuruí'
    airport['estado'] = 'PA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBAA'
    airport['aeroporto'] = 'Conceição do Araguaia'
    airport['estado'] = 'PA'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBKG'
    airport['aeroporto'] = 'Pres. João Suassuna'
    airport['estado'] = 'PB'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBJP'
    airport['aeroporto'] = 'Pres. Castro Pinto'
    airport['estado'] = 'PB'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBFN'
    airport['aeroporto'] = 'Fernando de Noronha'
    airport['estado'] = 'PE'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBRF'
    airport['aeroporto'] = 'Guararapes'
    airport['estado'] = 'PE'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBPL'
    airport['aeroporto'] = 'Sen. Nilo Coelho'
    airport['estado'] = 'PE'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBPB'
    airport['aeroporto'] = 'Dr. João Silva Filho'
    airport['estado'] = 'PI'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBTE'
    airport['aeroporto'] = 'Sen. Petrônio Portella'
    airport['estado'] = 'PI'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBLO'
    airport['aeroporto'] = 'Londrina'
    airport['estado'] = 'PR'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBFI'
    airport['aeroporto'] = 'Cataratas'
    airport['estado'] = 'PR'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBBI'
    airport['aeroporto'] = 'Bacacheri'
    airport['estado'] = 'PR'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBCT'
    airport['aeroporto'] = 'Afonso Pena'
    airport['estado'] = 'PR'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBMG'
    airport['aeroporto'] = 'Silvio Name Junior'
    airport['estado'] = 'PR'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBCB'
    airport['aeroporto'] = 'Cabo Frio'
    airport['estado'] = 'RJ'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBAF'
    airport['aeroporto'] = 'Afonsos'
    airport['estado'] = 'RJ'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBGL'
    airport['aeroporto'] = 'Galeão'
    airport['estado'] = 'RJ'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBJR'
    airport['aeroporto'] = 'Jacarepaguá'
    airport['estado'] = 'RJ'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBRJ'
    airport['aeroporto'] = 'Santos Dumont'
    airport['estado'] = 'RJ'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBSC'
    airport['aeroporto'] = 'Santa Cruz'
    airport['estado'] = 'RJ'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBME'
    airport['aeroporto'] = 'Macaé'
    airport['estado'] = 'RJ'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBES'
    airport['aeroporto'] = 'S. Pedro da Aldeia'
    airport['estado'] = 'RJ'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBCP'
    airport['aeroporto'] = 'Bartolomeu Lysandro'
    airport['estado'] = 'RJ'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBMS'
    airport['aeroporto'] = 'Dix-Sept Rosado'
    airport['estado'] = 'RN'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBNT'
    airport['aeroporto'] = 'Augusto Severo'
    airport['estado'] = 'RN'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBGM'
    airport['aeroporto'] = 'Guajará Mirim'
    airport['estado'] = 'RO'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBVH'
    airport['aeroporto'] = 'Brigadeiro Camarão'
    airport['estado'] = 'RO'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBPV'
    airport['aeroporto'] = 'Gov. Jorge Teixeira de Oliveira'
    airport['estado'] = 'RO'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBBV'
    airport['aeroporto'] = 'Boa Vista'
    airport['estado'] = 'RR'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBBG'
    airport['aeroporto'] = 'Bagé'
    airport['estado'] = 'RS'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBSM'
    airport['aeroporto'] = 'Santa Maria'
    airport['estado'] = 'RS'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBPA'
    airport['aeroporto'] = 'Salgado Filho'
    airport['estado'] = 'RS'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBPK'
    airport['aeroporto'] = 'Pelotas'
    airport['estado'] = 'RS'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBCO'
    airport['aeroporto'] = 'Canoas'
    airport['estado'] = 'RS'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBUG'
    airport['aeroporto'] = 'Rubem Berta'
    airport['estado'] = 'RS'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBCH'
    airport['aeroporto'] = 'Chapecó'
    airport['estado'] = 'SC'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBCM'
    airport['aeroporto'] = 'Forquilinha'
    airport['estado'] = 'SC'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBFL'
    airport['aeroporto'] = 'Hercílio Luz'
    airport['estado'] = 'SC'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBJV'
    airport['aeroporto'] = 'Lauro Carneiro de Loyola'
    airport['estado'] = 'SC'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBNF'
    airport['aeroporto'] = 'Min. Victor Konder'
    airport['estado'] = 'SC'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBAR'
    airport['aeroporto'] = 'Santa Maria'
    airport['estado'] = 'SE'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBAU'
    airport['aeroporto'] = 'Araçatuba'
    airport['estado'] = 'SP'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBBU'
    airport['aeroporto'] = 'Bauru'
    airport['estado'] = 'SP'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBKP'
    airport['aeroporto'] = 'Viracopos'
    airport['estado'] = 'SP'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBDN'
    airport['aeroporto'] = 'Pres. Prudente'
    airport['estado'] = 'SP'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBRP'
    airport['aeroporto'] = 'Leite Lopes'
    airport['estado'] = 'SP'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBSR'
    airport['aeroporto'] = 'S. J. do Rio Preto'
    airport['estado'] = 'SP'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBYS'
    airport['aeroporto'] = 'Fontenelle'
    airport['estado'] = 'SP'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBST'
    airport['aeroporto'] = 'Base Aérea'
    airport['estado'] = 'SP'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBGP'
    airport['aeroporto'] = 'Gavião Peixoto'
    airport['estado'] = 'SP'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBGW'
    airport['aeroporto'] = 'Guaratinguetá'
    airport['estado'] = 'SP'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBGR'
    airport['aeroporto'] = 'Guarulhos'
    airport['estado'] = 'SP'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBSJ'
    airport['aeroporto'] = 'São J. dos Campos'
    airport['estado'] = 'SP'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBMT'
    airport['aeroporto'] = 'Campo de Marte'
    airport['estado'] = 'SP'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBSP'
    airport['aeroporto'] = 'Congonhas'
    airport['estado'] = 'SP'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBTA'
    airport['aeroporto'] = 'Taubaté'
    airport['estado'] = 'SP'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBPJ'
    airport['aeroporto'] = 'Palmas'
    airport['estado'] = 'TO'
    airports.append(airport)
    airport = {}
    airport['sigla'] = 'SBPN'
    airport['aeroporto'] = 'Porto Nacional'
    airport['estado'] = 'TO'
    airports.append(airport)
    return airports