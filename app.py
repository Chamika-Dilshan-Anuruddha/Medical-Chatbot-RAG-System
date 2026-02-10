from flask import Flask, request, render_template
from MedicalChatbot.pipeline.predict_pipeline import CustomData, PredictPipeline
from MedicalChatbot.pipeline.stage_04_model_trainer import ModelTrainerPipeline


app = Flask(__name__)

obj = ModelTrainerPipeline()
agent,model_trainer = obj.main()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_results', methods=["POST"])
def get_rag_result():
    if request.method == "POST":
        data_obj = CustomData(request.form["query"])
        processed_data = data_obj.get_preprocessed_data()
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.get_result(processed_data,agent,model_trainer)
        return results
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)