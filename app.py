from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    # GET FORM DATA
    age = int(request.form['age'])

    pain = int(request.form['pain'])

    breath = int(request.form['breath'])

    hr = int(request.form['hr'])

    # BLOOD PRESSURE
    bp_value = request.form.get('bp')

    # IF USER DOESN'T KNOW BP
    if bp_value is None or bp_value == "":
        bp = 120

    else:
        bp = int(bp_value)

    score = 0

    # AGE LOGIC
    if age > 50:
        score += 20

    # BP LOGIC
    if bp > 140:
        score += 25

    # HEART RATE LOGIC
    if hr > 110:
        score += 20

    # CHEST PAIN LOGIC
    if pain == 2:
        score += 25

    # BREATHING PROBLEM
    if breath == 1:
        score += 15

    # FINAL RESULT
    if score < 30:

        result = "🟢 LOW RISK"

    elif score < 60:

        result = "🟡 MEDIUM RISK"

    else:

        result = "🔴 HIGH RISK"

    # BP STATUS
    if bp < 90:

        bp_status = "Low BP"

    elif bp <= 120:

        bp_status = "Normal BP"

    elif bp <= 140:

        bp_status = "High BP"

    else:

        bp_status = "Danger BP"

    # SEND DATA TO HTML
    return render_template(
        'index.html',
        prediction=result,
        bpm=hr,
        bp=bp_status
    )


if __name__ == "__main__":

    app.run(debug=False)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)