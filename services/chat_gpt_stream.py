import openai
import os

OPENAI_KEY = os.getenv('OPENAI_KEY')


class ChatGPT():
    def __init__(self):
        openai.api_key = OPENAI_KEY
        
    def perguntar(self, pergunta:str):
        
        print('Analisando...')
        
        try:
            # Use the GPT-3 to extract the keywords
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=pergunta,
                max_tokens=512,
                n=1,
                temperature=0.5,
                stream=True,
                stop=None
            )
            
            return response
        
        except Exception as e:
            print(f'Error: {e}')
            return 'Desculpe, algo de errado aconteceu, verifique os logs para mais detalhes.'

