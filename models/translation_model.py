import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class Translator:
    def __init__(self,model_path="models/translation_model_fast"):
        self.device=torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_path) #tải AutoTokenizer cho mô hình
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_path).to(self.device)

    def translate_text(self,text,max_length=256):
        try:
            input_text=f"translate English to Vietnamese: {text}"
            inputs=self.tokenizer(input_text,
                            return_tensors="pt",
                            max_length=max_length,
                            truncation=True).to(self.device)
            output=self.model.generate(
                **inputs,
                max_length=max_length,
                num_beams=5,
                early_stopping=True 
            )
            return self.tokenizer.decode(output[0],skip_special_tokens=True) #giải mã output thành chuỗi
        except Exception as e:
            print(e)