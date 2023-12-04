import openai
import os
os.environ["GUY_OPENAI_KEYS"]='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'
openai.api_key=os.getenv("GUY_OPENAI_KEYS")
prompt = "Give me details about the technology startup called Jinghang"
def create_test_prompt(topic,num_questions,num_possibale_answers):
    prompt=f"Create a multiple choice quiz on the topic of {topic} consisting of {num_questions} questions. "\
            +f"Each question should have {num_possibale_answers} options. "\
            +f"Also include the correct answer for each question using the starting string 'Correct Answer:' "
    return  prompt
print (create_test_prompt('Chinese History',4,4))
response = openai.Completion.create(
            model = 'text-curie-001',#text-curie-001,text-davinci-003,text-ada-001,text-babbage-001
            prompt=create_test_prompt('Chinese History',4,4),
            max_tokens=256,
            temperature=0.5
    )
print(response)
print(response['choices'][0]['text'])