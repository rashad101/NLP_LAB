from seq2seq_model import RD
from utils.lcquad import LCQUaDDataSet
from utils.plot_utils import plot_and_save_history
import numpy as np
import sys


def main():
    random_state = 42
    output_dir_path = './models'

    np.random.seed(random_state)
    data_set = LCQUaDDataSet(data_path='data/LCQuAD/train-v1.1.json')

    model = RD()
    model.load_glove_model('./embedding')


    epochs = int(sys.argv[1])
    batch_size = int(sys.argv[2])
    print("Training Program:")
    print("Epochs = ", epochs, " , Batch size = ",batch_size)

    history = model.fit(data_set, model_dir_path=output_dir_path,
                     batch_size=batch_size, epochs=epochs,
                     random_state=random_state)

    plot_and_save_history(history,"seq2seq_model","./models")

if __name__ == '__main__':
    main()
