import os

def create_pos_n_neg():
    for file_type in ['pos','neg']:

        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type+'/'+img+'\n'
                with open('positives.txt','a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('negatives.txt','a') as f:
                    f.write(line)

create_pos_n_neg()
