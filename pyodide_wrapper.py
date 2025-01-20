import pyodide
import openai

async def initialize_pyodide():
    await pyodide.loadPackage('openai')

def call_openai_method(method_name, *args, **kwargs):
    method = getattr(openai, method_name)
    return method(*args, **kwargs)
