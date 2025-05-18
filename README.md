# Dự án Dịch thuật Anh-Việt với mBART-Large-50 (Opus100)

Dự án này fine-tune mô hình `facebook/mbart-large-50` cho tác vụ dịch máy từ tiếng Anh sang tiếng Việt sử dụng một phần của bộ dữ liệu Opus100.

## Giới thiệu

Mục tiêu là xây dựng một mô hình dịch thuật có khả năng chuyển ngữ các câu từ tiếng Anh sang tiếng Việt. Dự án sử dụng thư viện Transformers của Hugging Face để tải mô hình tiền huấn luyện, xử lý dữ liệu và thực hiện quá trình fine-tuning.

## Mô hình

* **Mô hình cơ sở:** `facebook/mbart-large-50`
* **Bộ dữ liệu:** Một tập con của `opus100` (cặp ngôn ngữ Anh-Việt), bao gồm 10,000 mẫu cho tập huấn luyện và 1,000 mẫu cho tập đánh giá sau khi lọc.
* **Fine-tuning:** Mô hình được fine-tune cho tác vụ dịch máy Anh-Việt.

### Tình huống Huấn luyện và Hạn chế
Do hạn chế về tài nguyên tính toán (ví dụ: khi sử dụng Google Colab phiên bản miễn phí), mô hình chỉ được huấn luyện trong **1 epoch**. Điều này có nghĩa là hiệu suất của mô hình có thể chưa đạt mức tối ưu và có thể cần được huấn luyện thêm để cải thiện chất lượng bản dịch. Các kỹ thuật như `fp16`, `gradient_accumulation_steps` và `gradient_checkpointing` đã được sử dụng để tối ưu hóa việc sử dụng bộ nhớ trong quá trình huấn luyện.

## Cài đặt và Thiết lập

1.  **Cài đặt thư viện cần thiết:**
    ```bash
    pip install torch datasets transformers sentencepiece accelerate
    ```
    *(Lưu ý: `accelerate` được khuyên dùng cho `Trainer` và `fp16`)*

2.  **Tải mô hình đã fine-tune:**
    Mô hình đã được fine-tune có thể được tải về từ Google Drive:
    [Link tải mô hình](https://drive.google.com/drive/folders/1dJAaIPvjHNiEcdeDLa7ytnT3a6bR81WR?usp=sharing)

    Sau khi tải về, giải nén (nếu cần) và đặt các tệp của mô hình vào thư mục:
    `models/translation_model_fast/`
    Thư mục này nên chứa các tệp như `pytorch_model.bin`, `config.json`, `tokenizer_config.json`, v.v.

## Chi tiết Huấn luyện (Tóm tắt)

Quá trình huấn luyện bao gồm các bước chính sau:

1.  **Tải và chuẩn bị dữ liệu:**
    * Sử dụng bộ dữ liệu `opus100` (en-vi) từ Hugging Face Datasets.
    * Chọn một tập con gồm 10,000 mẫu huấn luyện và 1,000 mẫu đánh giá.
    * Lọc các mẫu không hợp lệ (ví dụ: câu trống, quá dài, hoặc sai định dạng). Giới hạn độ dài câu là 500 ký tự.

2.  **Tokenizer và Mô hình:**
    * Sử dụng `AutoTokenizer` và `AutoModelForSeq2SeqLM` để tải tokenizer và mô hình `facebook/mbart-large-50`.
    * Cấu hình tokenizer cho ngôn ngữ nguồn (`en_XX`) và ngôn ngữ đích (`vi_VN`).
    * Thêm tiền tố `"translate English to Vietnamese: "` vào đầu mỗi câu nguồn để hướng dẫn mô hình thực hiện tác vụ dịch.

3.  **Token hóa dữ liệu:**
    * Các câu trong tập huấn luyện và tập đánh giá được token hóa bằng tokenizer đã tải.

4.  **Thiết lập tham số huấn luyện (`TrainingArguments`):**
    * `output_dir`: './translation_model_fast'
    * `num_train_epochs`: 1 (Do hạn chế tài nguyên)
    * `learning_rate`: 2e-5
    * `per_device_train_batch_size`: 4
    * `per_device_eval_batch_size`: 8
    * `gradient_accumulation_steps`: 4 (Mô phỏng batch size lớn hơn: 4x4=16)
    * `fp16`: True (Sử dụng mixed precision để tăng tốc và giảm bộ nhớ)
    * `gradient_checkpointing`: True (Tiết kiệm bộ nhớ)
    * `eval_strategy` và `save_strategy`: 'epoch'

5.  **Huấn luyện:**
    * Sử dụng lớp `Trainer` của Transformers cùng với `DataCollatorForSeq2Seq` để thực hiện quá trình fine-tuning.

## Ví dụ Kết quả Dịch (Test)

<p align="center">
  <img src="https://github.com/HitDrama/EN-VI-Translation-mBART-Large-50-Opus100/blob/main/static/img-train/img-test.png" alt="Ví dụ kết quả dịch" width="600"/>
</p>



## Những hạn chế

* Như đã đề cập, mô hình chỉ được huấn luyện trong 1 epoch do giới hạn tài nguyên. Chất lượng bản dịch có thể được cải thiện đáng kể nếu huấn luyện thêm nhiều epochs, trên một tập dữ liệu lớn hơn và đa dạng hơn.
* Chất lượng dịch có thể không đồng đều cho các loại câu hoặc lĩnh vực khác nhau.

## Nhà phát triển

* Đặng Tố Nhân 

---

