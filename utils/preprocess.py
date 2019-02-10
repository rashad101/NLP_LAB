import json


wrf = open("data/LCQuAD/ER_n_relList_v3.json")
data = json.load(wrf)
wrf.close()


data  = data[0]


def ans_start_idx(context,ans):
    idx = 0
    for j in context.split(" "):
        if j == ans:
            break
        else:
            idx += (1 + len(j))
    return idx


def build_squad_like_data(data):
    train_list = []
    dev_list = []
    n_traintest = 24945
    count = 0
    print("Total data: "+str(len(data)))
    for d in data:
        if count%2000==0:
            print("Processed "+str(count)+" data !")
        title = "qa"+str(count)
        context = ' '.join(rel for rel in d["list_of_relations"])
        paragraph = [
            {
                "context": context,
                "qas":[
                    {
                        "answers":[
                            {
                                "answer_start": ans_start_idx(context,d["predicate"]),
                                "text": d["predicate"]
                            }
                            ],
                        "question": d["question"],
                        "id": "id"+str(count),
                        "is_impossible": False
                    }
                ]
            }
        ]
        qa_dict = {
            "title":title,
            "paragraphs": paragraph
        }
        if count<n_traintest:
            train_list.append(qa_dict)
        else:
            dev_list.append(qa_dict)
        count+=1


    info = {"data":train_list}
    write_to_file = open("data/LCQuAD/train-v1.1.json","w")
    json.dump(info,write_to_file,indent=4)
    write_to_file.close()

    info = {"data":dev_list}
    write_to_file = open("data/LCQuAD/dev-v1.1.json","w")
    json.dump(info,write_to_file,indent=4)
    write_to_file.close()


    print("DONE Preprocessing")




if __name__ == '__main__':
    build_squad_like_data(data)




