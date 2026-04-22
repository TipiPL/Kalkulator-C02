from flask import Flask, render_template, request

app = Flask(__name__)

def safe_float(value):
    try:
        return float(str(value).replace(",", "."))
    except:
        return 0

#  STRONA GŁÓWNA
@app.route("/")
def home():
    return render_template("home.html")

#  KALKULATOR
@app.route("/kalkulator", methods=["GET", "POST"])
def kalkulator():
    result = None
    advice = None

    if request.method == "POST":

        car = safe_float(request.form.get("car"))
        bus = safe_float(request.form.get("bus"))
        meat = safe_float(request.form.get("meat"))
        power = safe_float(request.form.get("power"))

        total = (
            car * 0.2 * 365 +
            bus * 0.05 * 365 +
            meat * 5 * 52 +
            power * 0.5 * 12
        )

        result = total

        if result < 5000:
            advice = "Świetnie  niski ślad CO₂!"
        elif result < 10000:
            advice = "Możesz jeszcze ograniczyć emisję "
        else:
            advice = " Wysoki ślad CO₂ – spróbuj zmienić nawyki"

    return render_template("calculator.html", result=result, advice=advice)


if __name__ == "__main__":
    app.run(debug=True)