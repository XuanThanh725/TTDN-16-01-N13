<h2 align="center">
    <a href="https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin">
    🎓 Faculty of Information Technology (DaiNam University)
    </a>
</h2>
<h2 align="center">
    PLATFORM ERP
</h2>
<div align="center">
    <p align="center">
        <img src="docs/logo/aiotlab_logo.png" alt="AIoTLab Logo" width="170"/>
        <img src="docs/logo/fitdnu_logo.png" alt="AIoTLab Logo" width="180"/>
        <img src="docs/logo/dnu_logo.png" alt="DaiNam University Logo" width="200"/>
    </p>

[![AIoTLab](https://img.shields.io/badge/AIoTLab-green?style=for-the-badge)](https://www.facebook.com/DNUAIoTLab)
[![Faculty of Information Technology](https://img.shields.io/badge/Faculty%20of%20Information%20Technology-blue?style=for-the-badge)](https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin)
[![DaiNam University](https://img.shields.io/badge/DaiNam%20University-orange?style=for-the-badge)](https://dainam.edu.vn)

</div>

## 📖 1. Giới thiệu
Platform ERP được áp dụng vào học phần Thực tập doanh nghiệp dựa trên mã nguồn mở Odoo. 

## 🔧 2. Các công nghệ được sử dụng
<div align="center">

### Hệ điều hành
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)
### Công nghệ chính
[![Odoo](https://img.shields.io/badge/Odoo-714B67?style=for-the-badge&logo=odoo&logoColor=white)](https://www.odoo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![XML](https://img.shields.io/badge/XML-FF6600?style=for-the-badge&logo=codeforces&logoColor=white)](https://www.w3.org/XML/)
### Cơ sở dữ liệu
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
</div>

## 🚀 3. Các project đã thực hiện dựa trên Platform

Một số project sinh viên đã thực hiện:
- #### [Khoá 15](./docs/projects/K15/README.md)
- #### [Khoá 16]() 
## ⚙️ 4. Cài đặt

### 4.1. Cài đặt công cụ, môi trường và các thư viện cần thiết

#### 4.1.1. Tải project.
```
git clone https://gitlab.com/anhlta/odoo-fitdnu.git
```
#### 4.1.2. Cài đặt các thư viện cần thiết
Người sử dụng thực thi các lệnh sau đề cài đặt các thư viện cần thiết

```
sudo apt-get install libxml2-dev libxslt-dev libldap2-dev libsasl2-dev libssl-dev python3.10-distutils python3.10-dev build-essential libssl-dev libffi-dev zlib1g-dev python3.10-venv libpq-dev
```
#### 4.1.3. Khởi tạo môi trường ảo.
- Khởi tạo môi trường ảo
```
python3.10 -m venv ./venv
```
- Thay đổi trình thông dịch sang môi trường ảo
```
source venv/bin/activate
```
- Chạy requirements.txt để cài đặt tiếp các thư viện được yêu cầu
```
pip3 install -r requirements.txt
```
### 4.2. Setup database

Khởi tạo database trên docker bằng việc thực thi file dockercompose.yml.
```
sudo docker-compose up -d
```
### 4.3. Setup tham số chạy cho hệ thống
Tạo tệp **odoo.conf** có nội dung như sau:
```
[options]
addons_path = addons
db_host = localhost
db_password = odoo
db_user = odoo
db_port = 5431
xmlrpc_port = 8069
```
Có thể kế thừa từ file **odoo.conf.template**
### 4.4. Chạy hệ thống và cài đặt các ứng dụng cần thiết
Lệnh chạy
```
python3 odoo-bin.py -c odoo.conf -u all
```
Người sử dụng truy cập theo đường dẫn _http://localhost:8069/_ để đăng nhập vào hệ thống.

## 🖼️ 5. Demo sản phẩm Platform ERP

> Phần này minh hoạ các chức năng tiêu biểu của hệ thống Platform ERP được xây dựng dựa trên mã nguồn mở Odoo và triển khai phục vụ học phần Thực tập doanh nghiệp tại Khoa Công nghệ Thông tin – Đại học Đại Nam.

<div align="center">

### 🔹 Hình 5.1: Demo phân hệ CRM – Quản lý cơ hội kinh doanh
<img src="docs/logo/cntt1.png" alt="CRM Pipeline Demo" width="900"/>

</div>

**Công dụng:**
- Quản lý pipeline bán hàng theo các giai đoạn (New, Qualified, Proposition, Won).
- Theo dõi và đánh giá cơ hội kinh doanh, giá trị hợp đồng.
- Hỗ trợ mô phỏng quy trình bán hàng thực tế trong doanh nghiệp.

**Nguồn:** Ảnh chụp màn hình hệ thống Platform ERP (Odoo) do nhóm thực hiện.

---

<div align="center">

### 🔹 Hình 5.2: Demo phân hệ Nhân sự – Quản lý nhân viên
<img src="docs/logo/cntt2.png" alt="Employees Management Demo" width="900"/>

</div>

**Công dụng:**
- Quản lý thông tin nhân viên, phòng ban và vị trí công việc.
- Hỗ trợ phân loại và quản trị nguồn nhân lực trong doanh nghiệp.
- Phục vụ bài toán quản lý nhân sự trong hệ thống ERP.

**Nguồn:** Ảnh chụp màn hình hệ thống Platform ERP (Odoo) do nhóm thực hiện.

---

<div align="center">

### 🔹 Hình 5.3: Demo phân hệ CRM Follow-up – Theo dõi hoạt động chăm sóc khách hàng
<img src="docs/logo/cntt3.png" alt="CRM Follow-up Demo" width="650"/>

</div>

**Công dụng:**
- Theo dõi các hoạt động chăm sóc khách hàng như Email, Gọi điện, Họp.
- Nhắc việc và quản lý tiến độ xử lý công việc liên quan đến khách hàng.
- Nâng cao hiệu quả chăm sóc khách hàng và khả năng chuyển đổi cơ hội.

**Nguồn:** Ảnh chụp màn hình hệ thống Platform ERP (Odoo) do nhóm thực hiện.



    
