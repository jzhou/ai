#!/usr/bin/python 

import pandas

def panda_load_csv():
    #filename = 'pima-indians-diabetes.data.csv'
    filename = './idt_atm.csv/1atm.csv'
    colnames = ['T', 'rT', 'tor', 'e1', 'e2']
    data = pandas.read_csv(filename,names=colnames)
    print(data.shape)
    training_result = data[['rT','tor']]
    print(training_result.shape)
    print(training_result)
    #Note that in this example we explicitly specify the names of each attribute to the DataFrame. Running the example displays the shape of the data:


def url_load_csv():
    # Load CSV using Pandas from URL
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
    names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
    data = pandas.read_csv(url, names=names)
    print(data.shape)

if __name__=="__main__":
    url_load_csv()
    panda_load_csv()
