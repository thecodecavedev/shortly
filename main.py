from flask import Flask,render_template,request,redirect, jsonify
import json, random, os, sqlite3

app = Flask(__name__)

connect = sqlite3.connect('database.db')
connect.execute('''
    CREATE TABLE IF NOT EXISTS URLS(
    id TEXT NOT NULL,
    shortly TEXT NOT NULL,
    url TEXT NOT NULL
    )        
    ''')

def shorten_link(url_: str, server_url: str)->str:
    id = random.randint(1000000,9999999)
    short_url = f"{server_url}short.ly/{id}"
    
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO URLS (id,shortly,url) VALUES (?,?,?)",(str(id),short_url,url_))
        conn.commit()
                      
    return short_url

def get_original_url(id: int)-> str:
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT url FROM URLS WHERE id=?",(str(id),))
        data = cursor.fetchone()
        print(data[0])
        url = data[0]
        
    return url
        

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/shorten', methods=["POST"])
def shorten():
    url = request.form.get("url")
    server_url = request.host_url
    shortly_link = shorten_link(url_=url,server_url=server_url)
    
    return jsonify(status = "success",message = shortly_link)

@app.route('/short.ly/<int:url_id>')
def shortly(url_id):
    url = get_original_url(url_id)
    if url == None:
        return render_template("404.html")
    else:
        return redirect(url)

if __name__ == "__main__":
    app.run(debug=True)
