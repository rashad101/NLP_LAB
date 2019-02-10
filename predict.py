from seq2seq_model import RD
from utils.lcquad import LCQUaDDataSet


def main():
    model = RD()
    model.load_glove_model('./embedding')
    model.load_model(model_dir_path='./models')
    data_set = LCQUaDDataSet(data_path='data/LCQuAD/dev-v1.1.json')
    size = data_set.size()
    count = 0
    ok = 0
    while count<size:
        p,q,a = data_set.get_data(count)
        pa = model.reply(p,q)
        if count%1000==0:
            print(count, " done")
        if pa==a:
            ok+=1
        count+=1


    print("OK",ok)
    print("count",count)

    for i in range(10):
        paragraph, question, actual_answer = data_set.get_data(i)
        predicted_answer = model.reply(paragraph, question)

        print('question: ', question)
        print('List of relations: ', paragraph)
        print({'predicted_relation': predicted_answer, 'actual_relation': actual_answer})


if __name__ == '__main__':
    main()
