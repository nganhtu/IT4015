# Bài tập lập trình 4: sử dụng mã khối

## Đề tài

Cài đặt 2 sơ đồ mã khóa và giải mã:

1. AES với CBC mode sử dụng PKCS#7 padding.
2. AES với Counter mode.

Cả 2 sơ đồ đều dùng IV ngẫu nhiên 16-byte.

## Công nghệ sử dụng

Chương trình sử dụng ngôn ngữ lập trình Python và thư viện `random`.

## Mô tả chương trình

Thư mục gồm 4 chương trình:

### Mã hóa AES với CBC mode

enc_cbc.py nhận đầu vào từ 2 tập tin:

-   ptbin.txt chứa mã nhị phân là biểu diễn ASCII mở rộng của bản rõ (có thể sinh mã nhị phân tại [đây](https://codebeautify.org/string-binary-converter)).

-   key.txt chứa khóa 128-bit biểu diễn dưới dạng thập lục phân.

và trả về kết quả là những thông số được in ra ở console.

### Mã hóa AES với CTR mode

enc_ctr.py nhận đầu vào từ 2 tập tin:

-   ptbin.txt chứa mã nhị phân là biểu diễn ASCII mở rộng của bản rõ (có thể sinh mã nhị phân tại [đây](https://codebeautify.org/string-binary-converter)).

-   key.txt chứa khóa 128-bit biểu diễn dưới dạng thập lục phân.

và trả về kết quả là những thông số được in ra ở console.

### Giải mã AES với CBC mode

dec_cbc.py nhận đầu vào từ 2 tập tin:

-   ctbin.txt chứa mã nhị phân là biểu diễn ASCII mở rộng của bản mã.

-   key.txt chứa khóa 128-bit biểu diễn dưới dạng thập lục phân.

-   IV.txt là giá trị IV dưới dạng 128-bit nhị phân tương ứng với bản mã.

và trả về kết quả là những thông số được in ra ở console (có thể dịch kết quả từ dạng mã nhị phân ra chuỗi ký tự tại [đây](https://codebeautify.org/binary-string-converter)).

### Giải mã AES với CTR mode

dec_cbc.py nhận đầu vào từ 2 tập tin:

-   ctbin.txt chứa mã nhị phân là biểu diễn ASCII mở rộng của bản mã.

-   key.txt chứa khóa 128-bit biểu diễn dưới dạng thập lục phân.

-   nonce.txt là giá trị nonce dưới dạng 64-bit nhị phân tương ứng với bản mã.

và trả về kết quả là những thông số được in ra ở console (có thể dịch kết quả từ dạng mã nhị phân ra chuỗi ký tự tại [đây](https://codebeautify.org/binary-string-converter)).

**Lưu ý:** trước khi sử dụng chương trình, cần phải thay đổi đường dẫn của các tập tin trong hàm `main` đúng với đường dẫn lưu trên máy.

## Đánh giá hiệu năng chương trình

Tạm thời em chưa cài đặt được thư viện `pycrypto` ạ :v
