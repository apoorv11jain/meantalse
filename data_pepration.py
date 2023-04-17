import json
import yaml

with open('depression.yml', 'r') as file:
    data = yaml.safe_load(file)
convos = data['conversations']
output =[]
for convo in convos:
    completion = ''
    for i, dialog in enumerate(convo):
        if i == 0:
            prompt = dialog
            prompt = prompt.replace("\xa0", " ")
            # print('prompt:',prompt)
        else:
            completion += " " + dialog
            completion = completion.replace("\xa0", " ")
    completion = completion.strip()
    line = {'prompt': prompt, 'completion': completion}
    # print(line)
    output.append(line)

print(output)

with open('depression.jsonl', 'w') as outfile:
    for i in output:
        json.dump(i, outfile)
        outfile.write('\n')

