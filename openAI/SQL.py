import openai
import os
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text

os.environ["GUY_OPENAI_KEYS"]='sk-'
openai.api_key=os.getenv("GUY_OPENAI_KEYS")
df=pd.read_csv("sales_data_sample.csv")
##
# test data file be read
# print(df)
# print(df.groupby("QTR_ID").sum()['SALES'])
##

##
# create TEMP DB in RAM
#PUSH Pandas DF -> TEMP DB
#SQL query on TEMP DB

temp_db = create_engine('sqlite:///:memory:',echo=True)
data = df.to_sql(name='Sales', con=temp_db)

with temp_db.connect() as conn:
    # makes the connection
    #run code indentation/block
    result = conn.execute(text("SELECT SUM(SALES) from Sales"))
    # auto close connection
print(result.all())

def create_table_definition(df):
    prompt = """### sqlite SQL table, with it properties:
    #
    # Sales({})
    #
    """.format(",".join(str(col) for col in df.columns))
    return prompt
print(create_table_definition(df))

def prompt_input():
    nlp_text=input("Enter the info you want: ")
    return nlp_text

def combin_prompts(df,query_prompt):
    definition = create_table_definition(df)
    query_init_string = f"### A query to answer: {query_prompt}\nSELECT"
    return definition+query_init_string
nlp_text=prompt_input()
print(combin_prompts(df,nlp_text))

response = openai.Completion.create(
        model='text-davinci-003',
        prompt = combin_prompts(df,nlp_text),
        max_tokens=150,
        top_p =1.0,
        frequency_penalty=0,
        presence_penalty=0,
        stop=['#',';']
)
print(response['choices'][0]['text'])
def handle_response(response):
    query = response['choices'][0]['text']
    if query.startswith(" "):
        query = "SELECT"+query
    return query
print(handle_response(response))

with temp_db.connect() as conn:
    result=conn.execute(text(handle_response(response)))
print(result.all())
