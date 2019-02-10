from matplotlib import pyplot as plt


def create_history_plot_acc(history, model_name, metrics=None):
    plt.title('Accuracy (Relation Detector)')
    if metrics is None:
        metrics = {'acc', 'loss'}
    if 'acc' in metrics:
        plt.plot(history.history['acc'], color='g', label='Train Accuracy')
        plt.plot(history.history['val_acc'], color='b', label='Validation Accuracy')
    plt.legend(loc='best')

    plt.tight_layout()

def create_history_plot_loss(history, model_name, metrics=None):
    plt.title('Loss (Relation Detector)')
    if metrics is None:
        metrics = {'acc', 'loss'}
    if 'loss' in metrics:
        plt.plot(history.history['loss'], color='r', label='Train Loss')
        plt.plot(history.history['val_loss'], color='m', label='Validation Loss')
    plt.legend(loc='best')

    plt.tight_layout()


def plot_loss(history,model_name,metrics):
    create_history_plot_loss(history,model_name,metrics)
    plt.savefig("img/loss.jpg")
    plt.show()


def plot_and_save_history(history, model_name, file_path, metrics=None):
    if metrics is None:
        metrics = {'acc', 'loss'}
    create_history_plot_acc(history, model_name, metrics)
    plt.savefig("img/acc.jpg")
    plt.show()
    plot_loss(history,model_name,metrics=None)

