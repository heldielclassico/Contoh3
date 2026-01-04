from flask import Flask, render_template

app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def home():
    # Mengarahkan ke file index.html di dalam folder templates
    return render_template('index.html')

if __name__ == '__main__':
    # Debug mode diaktifkan agar server otomatis restart saat ada perubahan kode
    app.run(debug=True, port=5000)
