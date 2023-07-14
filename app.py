from flask import Flask, Response
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route('/getname/<value>', methods=['GET'])
def GetCompanyName(value):
    try:
        template = """You are a naming consultant for new companies. What is a good name for a company that makes {question}?"""
        prompt = PromptTemplate(template=template, input_variables=["question"])
        bot = ChatOpenAI(temperature=1.0, model_name="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY)
        chain = LLMChain(prompt=prompt, llm=bot)
        response = f"ChatGPT Answer: {chain.run(question=value)}"
        return Response(response, status=200, mimetype='text/plain')
    except ValueError:
        return Response("Invalid input", status=400, mimetype='text/plain')

if __name__ == '__main__':
    app.run()
