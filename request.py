import requests

url = "http://localhost:8000/run_pipeline"
data_sum = {
    "name": "summarization",
    "input_data": "The COVID-19 pandemic has had a profound impact on global economies.",
    "max_length": 50,
}
data_text_gen = {
    "name": "text-generation",
    "input_data": "In the future, AI will",
    "max_length": 50,
}
data_text_clfyt = {
    "name": "text-classification",
    "input_data": "I am extremely happy today!",
    "max_length": 50,
}
data_text_clfyn = {
    "name": "text-classification",
    "input_data": "I am not extremely happy today!",
    "max_length": 50,
}
data_tsln = {
    "name": "translation",
    "input_data": "Hello, how are you?",
    "max_length": 50,
}
response_sum = requests.post(url, json=data_sum)
response_txtgen = requests.post(url, json=data_text_gen)
response_txtclfyt = requests.post(url, json=data_text_clfyt)
response_txtclfyn = requests.post(url, json=data_text_clfyn)
response_tsln = requests.post(url, json=data_tsln)
print(response_sum.json(), end="\n\n")
print(response_txtgen.json(), end="\n\n")
print(response_txtclfyt.json(), end="\n\n")
print(response_txtclfyn.json(), end="\n\n")
print(response_tsln.json())
