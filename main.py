from flask import Flask, request

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

@app.route('/avg', methods=['GET'])
def avg():
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

if __name__ == '__main__':
    app.run(port = 80 ,debug=True)
