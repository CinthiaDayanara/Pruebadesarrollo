import openai
from pydantic import BaseModel


class Document(BaseModel):
    prompt: str = ''


def convertidor(prompt: str) -> list:
    # token personal open ai
    openai.api_key = 'sk-...3TC5'

    # token organización open ai
    openai.organization = 'org-agMAoRaagmAVX9Us55NiUmQn'

    print('[PROCESANDO INRFOTMACION]'.center(40, '-'))

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": " Eres un convertidor binario, y muestra el resultado"
                                          "E.G: 5 en binario es 101"},

            {"role": "user", "content": prompt}
        ]
    )

    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens
    print('[PROCESO PROCESO TERMINADO]'.center(40, '-'))
    return [content, total_tokens]


