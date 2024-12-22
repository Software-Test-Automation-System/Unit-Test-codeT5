from flask import Flask, request, jsonify
from transformers import RobertaTokenizer, T5ForConditionalGeneration

app = Flask(__name__)
model_path = "UnitTest_codeT5"
model = T5ForConditionalGeneration.from_pretrained(model_path)
tokenizer = RobertaTokenizer.from_pretrained(model_path)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    input_text = data.get("input_text", "")
    input_ids = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True).input_ids
    output_ids = model.generate(input_ids, max_length=512, num_beams=4, early_stopping=True)
    generated_output = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    return jsonify({"generated_output": generated_output})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)