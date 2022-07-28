# Bài tập lớn: Pha I

## 1. Giới thiệu chung

Lớp Nhập môn An toàn thông tin 124190 - học kỳ 2020.2

Giảng viên: TS. Trần Vĩnh Đức

Thành viên trong nhóm:

1. Nguyễn Anh Tú - 20184000

## 2. Mô tả đề tài

Ý tưởng về bài tập lớn của em là **áp dụng phương pháp chứng minh không kiến thức để xây dựng một mô hình chữ ký điện tử**.

Trong toán học, một chứng minh là một cách trình bày thuyết phục (sử dụng những chuẩn mực đã được chấp nhận trong lĩnh vực đó) rằng một phát biểu toán học là đúng đắn. Trong số rất nhiều các phương pháp chứng minh, thuyết phục qua đối thoại là một cảm nguồn cho khái niệm chứng minh tương tác. Một loại đặc biệt của chứng minh tương tác là chứng minh không kiến thức (ZKP).

Chứng minh tương tác đã vượt ra ngoài mô hình của những chứng minh cổ điển. Nếu như chứng minh cổ điển đưa ra các lập luận logic một cách tuần tự để dẫn tới kết quả cuối cùng thì chứng minh tương tác lại là một quá trình, thông qua tương tác, thuyết phục người xác minh rằng một mệnh đề là đúng. Tinh thần của ZKP kế thừa điều đó: chứng minh một mệnh đề là đúng, mà người xác minh vẫn không biết cách chứng minh mệnh đề đó. Có một định lý về sự tồn tại ZKP cho các bài toán NP-đầy đủ rằng: bất cứ thứ gì có thể chứng minh được thì tồn tại cách chứng minh bằng ZKP.

Một ví dụ đơn giản: Alice muốn thuyết phục Bob rằng có cách phân biệt vị nước khoáng La Vie và Aquafina. Sau hàng trăm lần thử 2 loại và Alice luôn đưa ra kết quả đúng, Bob hoàn toàn bị thuyết phục rằng có cách phân biệt vị của 2 loại nước này, trong khi vẫn không thể chứng minh được với người khác.

Về mặt ứng dụng trong thực tế, ta thấy chữ ký là một ứng dụng của ZKP. Ý tưởng về chữ ký là một biểu tượng viết tay trong các văn bản để đại diện cho sự xác nhận của người sở hữu chữ ký đó. Một số nhược điểm rất dễ nhận thấy của hệ thống này là:

-   Tốn tài nguyên: thời gian chuyển văn bản trực tiếp, công sức ký tay, các khâu trung gian,...
-   Dễ giả mạo.
-   Không đảm bảo toàn vẹn nội dung văn bản.

Chữ ký điện tử khắc phục được tất cả các nhược điểm trên ở một mức độ nào đó, thể hiện được độ tin cậy và tính hiệu quả cao. Trên thực tế, chữ ký điện tử ngày càng được các quốc gia chú trọng, đưa quy tắc vào những văn bản pháp lý.

## 3. Cơ sở lý thuyết

### 3.1. Chứng minh không kiến thức

Trong lý thuyết nhóm, một nhóm cyclic là một nhóm có thể được sinh ra từ một tập hợp sinh chỉ gồm một phần tử $ g $, phần tử này được gọi là phần tử sinh của nhóm.

**Định nghĩa**. Một nhóm $G$ được gọi là nhóm cyclic nếu trong $G$ tồn tại phần tử $g$ sao cho $G = \langle g \rangle = \{ g^n | n \in \mathbb{N} \}$.

Với một nhóm cyclic hữu hạn $G$ cấp $q$ ta có $G = \{ e, g, g^2, ..., g^{q - 1} \}$, với $e = g^q = g^0$. Trên thực tế, để đảm bảo an toàn cho các hệ mã, ta phải làm việc với nhóm cyclic có bậc rất lớn ($q$ cỡ $2^{512}$). Khi đó bài toán sau được coi là rất khó giải quyết với các máy tính hiện đại: cho $g$ và một phần tử ngẫu nhiên $y \in G$, tìm $x$ thỏa mãn $y = g^x$.

Alice có thể dễ dàng sinh phần tử $y$ bằng cách chọn ngẫu nhiên $x$ và tính $y = g^x$. Tuy nhiên nếu Bob muốn tìm được $x$ cần phải giải bài toán logarit rời rạc, một bài toán hiện nay chưa có thuật toán tối ưu để giải quyết. Quá trình Alice sử dụng ZKP để chứng minh cho Bob thấy rằng mình biết $x$ như sau:

-   Alice chọn một số ngẫu nhiên $r \in [1, q]$ rồi đưa cho Bob phần tử $u = g^r$.
-   Bob chọn một số ngẫu nhiên $k \in [1, q]$ rồi đưa cho Alice.
-   Alice tính $t = (r - kx) \mod q$ rồi đưa cho Bob.
-   Bob kiểm tra và bị thuyết phục rằng Alice biết $x$ khi và chỉ khi $u = y^k g^t$.

Ý tưởng chính của thuật toán là yêu cầu Alice đưa ra một biểu diễn của $u$ theo $y$ và $g$, với số mũ của $y$ trong biểu diễn đó (là $k$) được chọn bởi Bob. Sau đây là lý giải vì sao Alice cần phải biết $x$ mới đưa ra được kết quả $t$ cho Bob và vì sao sau khi đã nhận được kết quả $t$ từ Alice, Bob vẫn không biết gì về $x$:

- Alice buộc phải biết $x$ mới đưa ra được $t$ ứng với lựa chọn ngẫu nhiên $k$ của Bob. Trước hết ta thấy với cùng một giá trị $u = g^r$, chỉ cần Alice đưa ra được 2 câu trả lời $t_1$, $t_2$ tương ứng với 2 thử thách khác nhau $k_1$, $k_2$ của Bob thì Alice phải biết $x$. Thật vậy, khi đó $k_1x + t_1 = k_2x + t_2 = r \mod q$ và khi đó giá trị $x$ được tính dễ dàng. Do đó, việc đưa ra đáp án đúng với một câu hỏi ngẫu nhiên của Bob đã thuyết phục được Bob rằng Alice có thể trả lời được bất cứ câu hỏi nào ứng với $k \in [1, q]$, và do đó phải biết $x$.
- Sau khi đối thoại với Alice, tất cả những gì Bob biết là bộ $(u, t, k)$ thỏa mãn $u = y^k g^t$. Tuy nhiên, không cần Alice thì Bob cũng có thể tự sinh bộ số này bằng cách chọn $k$ và $t$ ngẫu nhiên rồi tính $u = y^k g^t$. Phân bố của bộ $(u, t, k)$ khi đó giống với phân bố của bộ nhận được thông qua đối thoại với Alice. Vì vậy, việc đối thoại với Alice không đem lại lợi thế nào cho Bob trong việc tìm được $x$.

Như vậy, ta kết thúc được một mô hình ZKP.

### 3.2. Chữ ký điện tử

Ta bắt đầu xây dựng sơ đồ chữ ký điện tử. Mục đích của sơ đồ này là làm sao ta có thể ký trên một văn bản có nội dung được biểu diễn bởi một giá trị $m$ để không ai ngụy tạo được chữ ký, song ai cũng có thể kiểm tra tính xác thực của chữ ký.

Khác biệt cơ bản của sơ đồ này với ZKP là chữ ký điện tử không cần thông qua tương tác, còn ZKP nhất thiết cần có tương tác. Nhìn lại sơ đồ ZKP ở phần 3.1., ta nhận thấy mấu chốt là Alice chỉ được biết $k$ sau khi đã chọn $u$. Trong trường hợp ngược lại, Alice hoàn toàn có thể chọn một giá trị $t$ bất kì rồi tính $u = y^k g^t$. Do đó, trong hoàn cảnh không có tương tác, mấu chốt là phải đảm bảo $u$ được chọn trước $k$. Ý tưởng tự nhiên là giá trị $k$ phải được tính như một hàm băm của $u$:
$$k = H(m, u)$$
Việc giá trị $k$ phụ thuộc vào $m$ nhằm xác thực trạng thái của văn bản khi được ký.

Áp dụng vào sơ đồ ZKP ở phần 3.1. và thay đổi cuộc đối thoại giữa Alice và Bob bằng quá trình Alice ký lên văn bản $m$, ta có sơ đồ chữ ký điện tử sau:

- Alice chọn khóa bí mật $x$ và công bố khóa công khai $y = g^x$.
- Alice chọn ngẫu nhiên một số $r \in [1, q]$ và tính $u = g^r$.
- Alice tính $k = H(m, u)$.
- Alice tính $t = (r - kx) \mod q$ và đặt chữ ký lên văn bản $m$ là $(u, t)$.
- Bob tính $k = H(m, u)$ và kiểm tra xem $u = y^k g^t$ hay không. Nếu bằng thì chấp nhận chữ ký trên văn bản $m$, nếu không thì bác bỏ.

## 4. Phương pháp tiến hành

## 5. Kết luận

## 6. Tài liệu tham khảo

1. Boneh D., and Shoup V., "A Graduate Course in Applied Cryptography", University of Stanford, Jan. 2020.

   <URL:https://crypto.stanford.edu/~dabo/cryptobook/BonehShoup_0_5.pdf>

2. Ben-Or M., Goldreich O., Goldwasser S., Hastad J., Kilian J., Micali S., and Rogaway P.. 

   Everything Provable is Provable in Zero-Knowledge. In *Proceedings of the Advances in Cryptology - CRYPTO '88, 8th Annual International Cryptology Conference*, Santa Barbara, California, USA, August 21-25, 1988.

   pp. 37-56.

3. ciberexplosion of GeeksForGeeks, "Schnorr Digital Signature".

   <URL:https://www.geeksforgeeks.org/schnorr-digital-signature/>
