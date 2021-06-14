
from flask import Flask, request
import statistics

app = Flask(__name__)


@app.route('/average', methods=['GET'])
def average():
    bar = request.args.to_dict()
    print(bar)
    s = bar['X']
    p = s.split(",")
    sum = 0
    for x in p :
        if x.find('.') == -1 :
            sum = sum + int(x)
        else :
            sum = sum +float(x)
    d = sum/len(p)
    return str(d)

@app.route('/mean', methods=['GET'])
def mean():
    bar = request.args.to_dict()
    print(bar)
    s = bar['X']
    p = s.split(",")
    sum = 0
    for x in p :
        if x.find('.') == -1 :
            sum = sum + int(x)
        else :
            sum = sum +float(x)
    d = sum/len(p)
    return str(d)



@app.route('/median', methods=['GET'])
def median():
    bar = request.args.to_dict()
    print(bar)
    s = bar['X']
    p = s.split(",")

    i = 0
    for x in p :
        if x.find('.') == -1 :
            p[i] = int(x)
        else :
            p[i] = float(x)
        i = i+1
    d = statistics.median(p)
    return str(d)

@app.route('/max_', methods=['GET'])
def max_():
    bar = request.args.to_dict()
    print(bar)
    s = bar['X']
    p = s.split(",")

    i = 0
    for x in p :
        if x.find('.') == -1 :
            p[i] = int(x)
        else :
            p[i] = float(x)
        i = i+1
    d = max(p)
    return str(d)

@app.route('/min_', methods=['GET'])
def min_():
    bar = request.args.to_dict()
    print(bar)
    s = bar['X']
    p = s.split(",")

    i = 0
    for x in p :
        if x.find('.') == -1 :
            p[i] = int(x)
        else :
            p[i] = float(x)
        i = i+1
    d = min(p)
    return str(d)



@app.route('/add', methods=['GET'])
def add():
    bar = request.args.to_dict()
    print(bar)
    s = bar['X']
    p = s.split(",")
    sum = 0
    for x in p :
        if x.find('.') == -1 :
            sum = sum + int(x)
        else :
            sum = sum +float(x)

    return str(sum)




@app.route('/mul', methods=['GET'])
def mul():
    bar = request.args.to_dict()
    print(bar)
    s = bar['X']
    p = s.split(",")
    sum = 1
    for x in p :
        if x.find('.') == -1 :
            sum = sum * int(x)
        else :
            sum = sum *float(x)

    return str(sum)


@app.route('/sub', methods=['GET'])
def sub():
    bar = request.args.to_dict()
    print(bar)
    s = bar['X']
    p = s.split(",")

    if (len(p)==2) :
        l = []
        for x in p :
            if x.find('.') == -1 :
                l.append(int(x))
            else :
                l.append(float(x))
        return str(l[0]-l[1])
    else :
        return str("give 2 numbers as input")


@app.route('/div', methods=['GET'])
def div():
    bar = request.args.to_dict()
    print(bar)
    s = bar['X']
    p = s.split(",")

    if (len(p)==2) :
        l = []
        for x in p :
            if x.find('.') == -1 :
                l.append(int(x))
            else :
                l.append(float(x))
        return str(l[0]/l[1])
    else :
        return str("give 2 numbers as input")


if __name__ == '__main__':
    app.run(port = 80 ,debug=True)
