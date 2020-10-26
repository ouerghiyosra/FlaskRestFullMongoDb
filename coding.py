from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    f = open("test-data-10-exp-5.list", "r")
    text = f.read()
    #print(text)
    noms = []
    prenom=[]
    nom=''
    for i in range(0, len(text)):
        print(text[i])
        if(text[i] != ','):
            nom= nom + text[i]
            noms.append(nom);
    print(noms)


    return noms


if __name__ == '__main__':
    app.run()
