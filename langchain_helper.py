from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def suggest_pet_name(animal,body_color):
    llm=OpenAI(temperature=0.6)

    prompt_template=PromptTemplate(
        input_variables=['animal','body_color'],
        template="I have a {body_color} {animal} and I want a creative name for it. Suggest me five creative names for my {animal}"
    )
    llm_name_chain=LLMChain(llm=llm,prompt=prompt_template)

    response=llm_name_chain({'animal':animal,'body_color':body_color})



   
    return response


if __name__=="__main__":
    print(suggest_pet_name('cat','white'))

