# Simple CLI & Web Calculator

## คำอธิบาย
โปรแกรมสำหรับการคำนวณทางคณิตศาสตร์เบื้องต้น รองรับตัวดำเนินการ `+`, `-`, `*`, `/`, `**` ในรูปแบบ `num1 operator num2` เช่น `1 + 2`  

โปรแกรมสามารถใช้งานได้ทั้งแบบ CLI (ใน terminal) และแบบเว็บ (GUI) ผ่าน Flask

---

## วิธีติดตั้งและรัน

1. **ดาวน์โหลดโปรเจกต์**
   - โหลดโค้ดจาก GitHub ลงเครื่องของคุณ

2. **ติดตั้ง dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **รันโปรแกรมแบบ CLI**
   ```bash
   python src/main.py
   ```
   - จะมีข้อความแสดงใน terminal
   - ผู้ใช้สามารถกรอกคำสั่ง เช่น `calculate`, `history`, `clear history`, หรือ `quit`

4. **รันโปรแกรมแบบเว็บ (GUI)**
   ```bash
   python src/app.py
   ```
   - จะปรากฏข้อความใน terminal เช่น:
     ```
     * Serving Flask app 'app'
     * Debug mode: on
     WARNING: This is a development server. Do not use it in production deployment.
     * Running on all addresses (0.0.0.0)
     * Running on http://127.0.0.1:5000
     ```
   - เปิดลิงก์ `http://127.0.0.1:5000` ในเว็บบราวเซอร์
   - กด `CTRL+C` ใน terminal เมื่อต้องการปิดโปรแกรม

5. **รันโปรแกรมด้วย Docker**
   - สร้าง image:
     ```bash
     docker build -t simple-calculator .
     ```
   - รัน container:
     ```bash
     docker run -p 5000:5000 simple-calculator
     ```
   - เปิดลิงก์ `http://127.0.0.1:5000` ในเว็บบราวเซอร์

---

## วิธีใช้งาน

### CLI (main.py)
- รัน `main.py` จะปรากฏข้อความใน terminal
- ผู้ใช้กรอกคำสั่ง:
  - `calculate` → ทำการคำนวณ
  - `history` → แสดงประวัติการคำนวณ
  - `clear history` → ล้างประวัติ
  - `quit` → ออกจากโปรแกรม

### เว็บ (app.py)
- รัน `app.py` แล้วเปิดลิงก์ในเว็บบราวเซอร์
- หน้า Calculator:
  - กรอกโจทย์คำนวณ เช่น `5 + 3`
  - กดปุ่ม `คำนวณ` เพื่อดูผลลัพธ์
- หน้า History:
  - แสดงประวัติการคำนวณทั้งหมด
  - ปุ่ม `Clear History` ลบประวัติทั้งหมด

---

## โครงสร้างโปรเจกต์ (สำคัญ)
```
Sample-calculator/
├─ planning/
│   ├─ flow.md
│   ├─ planning_week 1.md
│   ├─ planning_week 2.md
│   ├─ planning_week 3.md
│   ├─ planning_week 4.md
│   ├─ READMEoid.md
│   └─ วิธีการยิงapiเบื้องต้น.md
├─ src/
│  ├─ templates/
│  ├─ app.py
│  ├─ main.py
│  └─ history.json
├─ static/
├─ Dockerfile
├─ README.md
└─ requirements.txt
```

---

## หมายเหตุ
- ระบบเว็บนี้เป็น **development server** สำหรับทดลองเท่านั้น
- ไม่แนะนำให้ใช้งานใน production โดยตรง
- การรันผ่าน Docker ช่วยให้ตั้งค่าและรันโปรแกรมง่ายขึ้น

# Dependencies

- Python >= 3.13

- Flask

- ติดตั้งด้วย:

- pip install -r requirements.txt




# Flow การทำงานของโปรเจกต์ Simple CLI & Web Calculator

## 1. เริ่มต้นโปรเจกต์

* ผู้ใช้ดาวน์โหลดโค้ดจาก GitHub
* ติดตั้ง dependencies ผ่าน `pip install -r requirements.txt`
* มีตัวเลือกให้รันโปรแกรมแบบ CLI (main.py) หรือแบบเว็บ (app.py)

## 2. การทำงานแบบ CLI (main.py)

1. ผู้ใช้รัน `main.py`
2. โปรแกรมแสดงข้อความต้อนรับ และแจ้งคำสั่งที่รองรับ: `calculate`, `history`, `clear history`, `quit`
3. ผู้ใช้เลือกคำสั่ง:

   * `calculate` → โปรแกรมเรียกฟังก์ชัน `get_numbers_and_operator()`

     * ผู้ใช้กรอกโจทย์ เช่น `5 + 3`
     * โปรแกรมแยกตัวเลขและ operator
     * เลือกฟังก์ชันคำนวณ (`add_numbers`, `subtract_numbers`, etc.)
     * แสดงผลลัพธ์ใน terminal
     * บันทึกประวัติลง `history.json`
   * `history` → โหลดประวัติจาก `history.json` และแสดง
   * `clear history` → ลบประวัติและไฟล์ `history.json`
   * `quit` → ออกจากโปรแกรม

## 3. การทำงานแบบเว็บ (app.py)

1. ผู้ใช้รัน `app.py`
2. Flask server เริ่มต้นที่ `0.0.0.0:5000`
3. หน้าเว็บหลัก

   * `/` หรือ `/c` → หน้า Calculator

     * ผู้ใช้กรอกโจทย์ เช่น `5 + 3` ในฟอร์ม POST
     * Flask เรียก `get_numbers_and_operator_butnoprint()` จาก main.py
     * ตรวจสอบความถูกต้องของตัวเลขและ operator
     * เรียกฟังก์ชันคำนวณตาม operator
     * แสดงผลลัพธ์บนหน้าเว็บ
     * บันทึกประวัติลง `history.json`
   * `/h` → หน้า History

     * โหลดประวัติจาก `history.json`
     * แสดงเป็นตาราง
     * มีปุ่ม `Clear History` → ส่ง DELETE request ไป `/historyTest`

## 4. API Endpoints (สำหรับการทำงานแบบโปรแกรมอื่น/JavaScript)

* `POST /CalculateTest` → คำนวณเลขจาก JSON payload `{num1, num2, operator}`

  * ส่งผลลัพธ์เป็น JSON
  * บันทึก history
* `GET /historyTest` → ส่ง JSON ของประวัติทั้งหมด
* `DELETE /historyTest` → ล้างประวัติ

## 5. การทำงานกับ Docker

1. Build image: `docker build -t simple-calculator .`
2. Run container: `docker run -p 5000:5000 simple-calculator`
3. เข้าหน้าเว็บผ่าน `http://127.0.0.1:5000`

## 6. โฟลว์โดยสรุป (ภาพรวม)

```
[User] --> (CLI main.py) --> Input Command --> Calculation/History/Clear/Quit
                  --> Save/Load history.json --> Output Result

[User] --> (Web app.py) --> Browser Requests --> Flask Routes
                  --> Validate Input --> Call main.py functions
                  --> Save/Load history.json --> Return HTML/JSON Response

Docker --> Run app.py --> Access via Browser --> Same Flow as Web
```

* ฟังก์ชันคำนวณทั้งหมดถูกเรียกจาก main.py
* ประวัติการคำนวณเก็บใน `history.json`
* หน้าเว็บใช้ Jinja2 templates:


