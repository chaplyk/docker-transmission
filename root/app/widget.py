from transmission_rpc import Client
from flask import Flask, request

app = Flask(__name__)
client = Client(username='username', password='password')

@app.route('/transmission_widget')
def index():
    return '''<form action="" method="post">
            <p><input type="text" id="name" name="name" placeholder="Name" required></p>
            <p><input type="text" id="magnet" name="magnet" placeholder="Magnet URL" required></p>
            <p><select name="type" id="type">
                <option value="movies">Movie</option>
                <option value="shows">TV Show</option>
            </select></p>
            <p><input type="submit" name="submit" value="Start Download"/></p>
            </form>'''


@app.route('/transmission_widget', methods=['POST'])
def post_abc():
    magnet_url=request.form['magnet']
    download_path='/downloads/' + request.form['type'] + '/' + request.form['name']
    try:
        add_torrent=client.add_torrent(magnet_url, download_dir=download_path)
        return '''<p>Torrent added</p>'''
    except Exception as e:
        print(e)
        return '''Error occured'''

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True, port=5141, host='0.0.0.0')
