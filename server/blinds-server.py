from flask import app, Flask, render_template, request, safe_join, send_from_directory

app = Flask(__name__)

@app.route("/")
def control_blinds():
    return render_template("bootstrap_test.php")

#@app.route('/<any(css, img, js):folder>/<path:filename>')
#def toplevel_static(folder, filename):
#    filename = safe_join(folder, filename)
#    cache_timeout = app.get_send_file_max_age(filename)
#    return send_from_directory(app.static_folder, filename, cache_timeout=cache_timeout)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
