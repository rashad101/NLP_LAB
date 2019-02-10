from seq2seq_model import RD
from utils.lcquad import LCQUaDDataSet


def main():
    model = RD()
    model.load_glove_model('./embedding')
    model.load_model(model_dir_path='./models')
    data_set = LCQUaDDataSet(data_path='data/LCQuAD/train-v1.1.json')
    for i in range(5):
        paragraph, question, actual_answer = data_set.get_data(i)
        predicted_answer = model.reply(paragraph, question)

        print('question: ', question)
        print('List of relations: ', paragraph)
        print({'predicted_relation': predicted_answer, 'actual_relation': actual_answer})


if __name__ == '__main__':
    main()
