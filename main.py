from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

status_data = {
    "user_id": "",
    "amount": "",
    "status": "idle",
    "msg": "أدخل البيانات واضغط على زر شحن الآن"
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html dir="rtl">
<head>
    <title>نظام شحن العملات الاحترافي</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: Arial, sans-serif; background-color: #0f172a; color: white; text-align: center; padding: 20px; }
        .card { background-color: #1e293b; padding: 25px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); max-width: 400px; margin: 0 auto; border: 1px solid #334155; }
        h1 { color: #38bdf8; font-size: 22px; margin-bottom: 20px; }
        .form-group { text-align: right; margin-bottom: 15px; }
        label { display: block; font-size: 14px; margin-bottom: 5px; color: #94a3b8; }
        input, select { width: 100%; padding: 12px; border-radius: 8px; border: 1px solid #475569; background-color: #0f172a; color: white; font-size: 16px; box-sizing: border-box; text-align: center; }
        input:focus { border-color: #38bdf8; outline: none; }
        .btn { display: block; width: 100%; background-color: #38bdf8; color: #0f172a; border: none; padding: 14px; margin-top: 20px; border-radius: 8px; font-size: 16px; cursor: pointer; font-weight: bold; transition: 0.3s; }
        .btn:hover { background-color: #0ea5e9; }
        .status-box { background-color: #0f172a; padding: 15px; border-radius: 10px; margin-top: 20px; border: 1px solid #334155; }
        .success { color: #4ade80; font-weight: bold; }
    </style>
</head>
<body>

    <div class="card">
        <h1>💎 لوحة تحكم شحن العملات 💎</h1>
        
        <form action="/send_charge" method="POST">
            <div class="form-group">
                <label>معرّف الحساب (ID):</label>
                <input type="text" name="user_id" placeholder="أدخل الـ ID هنا" required>
            </div>
            
            <div class="form-group">
                <label>كمية العملات المطلوبة:</label>
                <select name="amount">
                    <option value="1000">1,000 عملة رقمية</option>
                    <option value="5000">5,000 عملة رقمية</option>
                    <option value="10000">10,000 عملة رقمية</option>
                    <option value="50000">50,000 عملة رقمية</option>
                </select>
            </div>
            
            <button type="submit" class="btn">🚀 إرسال الشحن الآن</button>
        </form>

        {% if data.status != 'idle' %}
        <div class="status-box">
            <h3>📊 حالة العملية الحالية:</h3>
            <p class="success">🎯 الحساب المستهدف: {{ data.user_id }}</p>
            <p class="success">💰 الكمية المرسلة: {{ data.amount }} عملة</p>
            <p class="success">✨ النتيجة: {{ data.msg }}</p>
        </div>
        {% endif %}
    </div>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, data=status_data)

@app.route('/send_charge', methods=['POST'])
def send_charge():
    status_data["user_id"] = request.form.get("user_id")
    status_data["amount"] = request.form.get("amount")
    status_data["status"] = "success"
    status_data["msg"] = "تم الاتصال بالخادم الافتراضي وضخ العملات بنجاح للمعرف المخزن!"
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
