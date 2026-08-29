
from flask import Flask, render_template, request

from src.pipelines.predict_pipeline import CustomData, predict_pipeline


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():

    # GET request -> show prediction form
    if request.method == "GET":
        return render_template("home.html", result=None)


    # POST request -> get form data
    data = CustomData(
        gender=request.form.get("gender"),
        race_ethnicity=request.form.get("race_ethnicity"),
        parental_level_of_education=request.form.get(
            "parental_level_of_education"
        ),
        lunch=request.form.get("lunch"),
        test_preparation_course=request.form.get(
            "test_preparation_course"
        ),
        reading_score=int(request.form.get("reading_score")),
        writing_score=int(request.form.get("writing_score"))
    )


    # Convert input into DataFrame
    pred_df = data.get_data_as_dataframe()

    print(pred_df)


    # Load model and make prediction
    prediction_pipeline = predict_pipeline()

    result = prediction_pipeline.predict(pred_df)


    # Send prediction to HTML
    return render_template("home.html",result=result[0])



if __name__ == "__main__":
    app.run(debug=True)
