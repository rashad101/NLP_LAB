# Relation Linker
Implementation of Relation Linker that detects correct relation from a set of relations, for a given question. 


## Data
All the data generated in different steps can be found and downloaded from the following link:
[Download Link](https://www.dropbox.com/sh/wj8iojvn493d233/AAA0tA1qrOv2r9K3B8GKqeWoa?dl=0)

## Installation
For installing the program first clone the github repository by running the following repository
```
git clone https://github.com/rashad101/NLP_LAB.git
cd NLP_LAB
```
All the requried datasets are already there for running the program.
### Pre-processing

```
python utils/preprocess.py
```
After pre-processing the data two file will be generated inside 'data/LCQuAD' directory: [train-v1.1.json](https://github.com/rashad101/NLP_LAB/blob/master/data/LCQuAD/train-v1.1.json), [dev-v1.1.json](https://github.com/rashad101/NLP_LAB/blob/master/data/LCQuAD/dev-v1.1.json)
```
train-v1.1.json
├── "data"
   └── [i]
       ├── "paragraphs"
           └── [j]
               ├── "context": "list of space separated candidate relations"
               └── "qas"
                   └── [k]
                       ├── "answers"
                       │   └── [l]
                       │       ├── "answer_start": N
                       │       └── "text": "correct relation"
                       ├── "id": "question id"
                       └── "question": "question"
```

### Train
For training the program run the following command, here 60 is the number of ephos and 256 is the batch size
```
python train.py 60 256
```
Running this program randomly divide the data into train and test set into a ratio of 80/20

## Performance
![alt text](https://github.com/rashad101/NLP_LAB/blob/master/img/acc.jpg)
![alt_text](https://github.com/rashad101/NLP_LAB/blob/master/img/loss.jpg)
