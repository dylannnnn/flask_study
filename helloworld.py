from flask import Flask
import txt_dict

app = Flask(__name__)

@app.route('/')
def hello_world():
    #return 'Hello World!'
    _dict=txt_dict.load_dict_from_file('D:\\dic.txt')
    return _dict['1.1.1.0/24']

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == '__main__':
    app.debug = True
    app.run()