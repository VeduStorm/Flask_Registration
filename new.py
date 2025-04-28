from  flask import Flask, render_template, request

web = Flask(__name__)
@web.route('/')
@web.route('/register')

def reigster():
    return render_template('register.html')

@web.route('/confirmation', methods=['POST', 'GET'])
def confirmation():
    if request.method == 'POST':
        n = request.form.get('name')
        n2 = request.form.get('email')
        n3 = request.form.get('contact')
        n4 = request.form.get('addy')
        n5 = request.form.get('gender')
        return render_template('confirm.html', name=n, email=n2, contact=n3, addy=n4, gender=n5)


if __name__ == '__main__':
    web.run(debug=True)

