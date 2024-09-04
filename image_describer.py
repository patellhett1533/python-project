import ollama

print("====== Image Describer ======")
res = ollama.chat(
    model='llava:13b',
    messages=[
        {'role': "user",
         'images': ["./het.jpg"],
         "content": "describe the image"}
    ])

print(res['message']['content'])
print("===============End==================")
