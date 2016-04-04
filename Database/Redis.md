# Redis Là Gì?
I/Tổng Quan

Hiện nay có rất nhiều chương trình hỗ trợ việc lưu trữ dữ liệu: MySQL, MongoDB, Hbase, Memcached, Redis…
Nhưng để đáp ứng nhu cầu đặt ra thì Redis là một sự lựa chọn tốt.
1. Redis là gì?

Redis là một chương trình hỗ trợ lưu trữ dữ liệu dạng key/value.
Hỗ trợ các kiểu dữ liệu: Keys Strings Hashes Lists Sets Sorted Sets Pub/Sub Transactions Scripting Connection Server
2. Vì sao lại chọn Redis

* Redis hỗ trợ thêm mới, cập nhật và loại bỏ dữ liệu nhanh chóng
* Redis có những đặc điểm giống như Memcached như:
* Lưu trữ dạng key /value.
* Tất cả data được lưu trên Memory(RAM)
* Key có thể hết hạn(expire) hoặc không
* Nhanh(Fast), nhẹ nhàng(light-weight)

Redis có thêm nhiều đặc điểm, chức năng khác mang lại lợi ích khi sử dụng và triển khai
* Persistence
* Hỗ trợ nhiều Databases
* Truy vấn theo Key
* Hỗ trợ counters dữ liệu kiểu integer
* Cấu trúc dữ liệu cấp cao
* Thao tác dữ liệu chuyên biệt
* Tự động phân trang danh sách
* Nhân rộng master-slave
* Redis lấy và nạp dữ liệu trên Memory(RAM), nhưng tại một thời điểm thì dữ liệu có thể được lưu trữ trên disk(Data in memory, but saved on disk).
* Điểm khác biệt dễ nhận thấy của Redis là: Key là một string nhưng value thì không giới hạn ở một string mà có thể là List, Sets, Sorted sets, ....
Redis hỗ trợ “Multiple database” với nhiều commands để tự động remove key từ một database tới database khác.
* Mặc định thì DB 0 sẽ được lựa chọn cho mỗi lần kết nối(connection), nhưng khi sử dụng lệnh SELECT(SELECT command) thì nó có thể select/create một database khác. Thao tác MOVE(MOVE operation) có thể chuyển một item từ một DB tới DB khác một cách tự động.
* Redis rất nhanh trong các thao tác lấy và nạp dữ liệu do redis hỗ trợ nhiều lệnh mang tính chất chuyên biệt.
* Redis hỗ trợ mở rộng master-slave nếu chúng ta muốn sự an toàn hoặc mở rộng, co giãn trong việc lưu trữ data.
