from services.texto_para_fala import TextoParaFala
from services.fala_para_texto import FalaParaTexto
from services.chat_gpt_stream import ChatGPT
import asyncio
import time

tpf = TextoParaFala()
fpt = FalaParaTexto()
gpt = ChatGPT()


def main():
    
    try:
    
        pergunta = fpt.ouvir()
        t_incio = time.time()

        resposta = gpt.perguntar(pergunta)
        t_resposta = round(time.time() - t_incio)

        asyncio.run(falar_em_stream(resposta))
        t_fala = round(time.time() - t_incio, 2)
        
        print(f'\nTempo da pergunta até o gpt responder: {t_resposta}s.\nTempo da pergunta até a fala final: {t_fala}s')
        
    except Exception as e:
        print(e)


async def falar_em_stream(response):
    
    print('Respondendo...\n')
    resposta_final = ''
    frase = ''

    for event in response:
        finish_reason = event['choices'][0]['finish_reason']
        
        if not finish_reason:
            text = event['choices'][0]['text']
            
            frase += text

            if frase[-1] in ['.','?','!'] and not str(frase[-2]).isdigit():
                print(str(frase).lstrip())
                tpf.falar(frase)
                frase = ''
                
            resposta_final += text

main()