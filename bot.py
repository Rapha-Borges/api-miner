


#   Lista os blocos minerados pela Flexpool utilizando a própria API do site:   #
#                                                                               #
#      Campo "filtro" determina o valor minimo para filtro                   #


import requests

filtro = 2

requisicao = requests.get("https://api.flexpool.io/v2/pool/blocks?coin=eth&page=0")
dic_requisicao = requisicao.json()

for val in dic_requisicao['result']['data']:
    numero = (val['number'])
    recompensa = (val['reward'])/1000000000000000000
    recompensaadicional = (val['mevReward'])/100000000000000000
    
    if recompensa > filtro:
        print ('\n🎉 [NEW ETH BLOCK] Mined # {}\n'.format(numero))
        print ('🤑 Reward:  {:.6}'.format(recompensa))
        print ('💰 MEV:     {:.4}\n'.format(recompensaadicional))
        print ('-----------------------------------')
        

#   Lista os blocos minerados pela Flexpool utilizando a API da etherscan:    #
#                                                                             #
#       Campo "filtro" determina o valor minimo para filtro                #
#                                                                             #
#       Campo "api_key" recebe a chave de api gerada no site da etherscan     #


import requests

api_key = ''
filtro = 2

requisicao = requests.get("https://api.etherscan.io/api?module=account&action=getminedblocks&address=0x7F101fE45e6649A6fB8F3F8B43ed03D353f2B90c&blocktype=blocks&page=1&offset=10&apikey={}".format(api_key))
dic_requisicao = requisicao.json()

for val in dic_requisicao['result']:
    numero = (val['blockNumber'])
    recompensa = int((val['blockReward']))/1000000000000000000
    
    if recompensa > filtro:
        print('\n🎉 [NEW ETH BLOCK] Mined # {}\n'.format(numero))
        print ('🤑 Reward:  {:.6}\n'.format(recompensa))
        print ('-----------------------------------')

