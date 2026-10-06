```python
from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def home():
    return "Server pengolahan data aktif"


@app.route("/hitung")
def hitung():

    panjang = float(os.environ.get("PANJANG", 10))
    lebar = float(os.environ.get("LEBAR", 5))

    # Rumus luas persegi panjang
    luas = panjang * lebar

    return jsonify({
        "panjang": panjang,
        "lebar": lebar,
        "luas": luas
    })


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 10000))

    app.run(
        host="0.0.0.0",
        port=port
    )
```
