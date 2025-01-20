import pyodide
import js

async def initialize_pyodide():
    await pyodide.loadPackage('openai-node')
    js.openai = js.require('openai')

def create_openai_client(api_key):
    return js.openai(api_key)

async def create_completion(client, prompt):
    completion = await client.completions.create({
        'model': 'text-davinci-003',
        'prompt': prompt,
        'max_tokens': 100
    })
    return completion.choices[0].text
