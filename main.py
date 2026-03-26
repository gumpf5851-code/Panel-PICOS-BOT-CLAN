#مبروك لكم البوت مقدم هديه من @Picos0 🎁💝 حط بيانات حساب الضيف في سطر 262 و 263 ومبروك لكم بحبكم في الله S 1 X PICOS 🎁💝
import threading
import time
import json
import os
import html
import requests
import base64
from datetime import datetime, timedelta
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# حاول استيراد AES من Crypto أولاً
try:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad, unpad
    print("✅ تم تحميل مكتبة Crypto بنجاح")
except ImportError:
    try:
        from Cryptodome.Cipher import AES
        from Cryptodome.Util.Padding import pad, unpad
        print("✅ تم تحميل مكتبة Cryptodome بنجاح")
    except ImportError:
        print("❌ يجب تثبيت pycryptodome أولاً: pip install pycryptodome")
        exit()

try:
    from protobuf_decoder.protobuf_decoder import Parser
except ImportError:
    class Parser:
        def parse(self, data):
            return {"error": "protobuf_decoder not installed"}
    print("Warning: protobuf_decoder not available - using dummy parser")

import random
import telebot.types

def safe_story_de_json(obj):
    try:
        return telebot.types.Story(**{k: v for k, v in obj.items() if k != "chat"})
    except Exception:
        return None

telebot.types.Story.de_json = staticmethod(safe_story_de_json)

# بيانات البوت والمسؤول
BOT_TOKEN = "8525775899:AAHBTX1RROq9pfezzGcp3MxCXxJVChki6TM"
ADMIN_ID = 6997272524 # الإدمن الرئيسي فقط

# قائمة المسؤولين (الإدمن فقط)
ADMIN_IDS = [6997272524]

# ملفات البيانات
DATA_FILE = "users2.json"
GROUPS_FILE = "groups2.json"
MAINTENANCE_FILE = "maintenance2.json"

# بيانات القناة الإجبارية
SUBSCRIPTION_CHANNEL_ID = [-1003801166959]
SUBSCRIPTION_CHANNEL_LINK = "https://t.me/PICOS_BOT_CLAN"

# بيانات التشفير (من الكود الأول)
ENCRYPTION_KEY = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
ENCRYPTION_IV = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])

# بيانات الديكور
da = 'f2212101'
dec = ['80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff']
x = ['1', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71',
     '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f']

def generate_random_hex_color():
    top_colors = [
        "FF4500", "FFD700", "32CD32", "87CEEB", "9370DB",
        "FF69B4", "8A2BE2", "00BFFF", "1E90FF", "20B2AA",
        "00FA9A", "008000", "FFFF00", "FF8C00", "DC143C",
        "FF6347", "FFA07A", "FFDAB9", "CD853F", "D2691E",
        "BC8F8F", "F0E68C", "556B2F", "808000", "4682B4",
        "6A5ACD", "7B68EE", "8B4513", "C71585", "4B0082",
        "B22222", "228B22", "8B008B", "483D8B", "556B2F",
        "800000", "008080", "000080", "800080", "808080",
        "A9A9A9", "D3D3D3", "F0F0F0"
    ]
    random_color = random.choice(top_colors)
    return random_color

# وظائف التشفير من الكود الأول
def encrypt_packet(plain_text, key=ENCRYPTION_KEY, iv=ENCRYPTION_IV):
    plain_text_bytes = bytes.fromhex(plain_text)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = cipher.encrypt(pad(plain_text_bytes, AES.block_size))
    return cipher_text.hex()

def decrypt_packet(cipher_text, key=ENCRYPTION_KEY, iv=ENCRYPTION_IV):
    cipher_text_bytes = bytes.fromhex(cipher_text)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain_text = unpad(cipher.decrypt(cipher_text_bytes), AES.block_size)
    return plain_text.hex()

def dec_to_hex(ask):
    ask_result = hex(ask)
    final_result = str(ask_result)[2:]
    if len(final_result) == 1:
        final_result = "0" + final_result
        return final_result
    else:
        return final_result

class ParsedResult:
    def __init__(self, field, wire_type, data):
        self.field = field
        self.wire_type = wire_type
        self.data = data

class ParsedResultEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ParsedResult):
            return {"field": obj.field, "wire_type": obj.wire_type, "data": obj.data}
        return super().default(obj)

def bunner_():
    ra = random.randint(203, 213)
    final_num = str(ra).zfill(3)
    bunner = "902000" + final_num
    bunner = random.choice(numbers)
    return bunner

def create_varint_field(field_number, value):
    field_header = (field_number << 3) | 0
    return encode_varint(field_header) + encode_varint(value)

def create_length_delimited_field(field_number, value):
    field_header = (field_number << 3) | 2
    encoded_value = value.encode() if isinstance(value, str) else value
    return encode_varint(field_header) + encode_varint(len(encoded_value)) + encoded_value

def create_protobuf_packet(fields):
    packet = bytearray()

    for field, value in fields.items():
        if isinstance(value, dict):
            nested_packet = create_protobuf_packet(value)
            packet.extend(create_length_delimited_field(field, nested_packet))
        elif isinstance(value, int):
            packet.extend(create_varint_field(field, value))
        elif isinstance(value, str) or isinstance(value, bytes):
            packet.extend(create_length_delimited_field(field, value))

    return packet

def encode_varint(number):
    if number < 0:
        raise ValueError("Number must be non-negative")

    encoded_bytes = []
    while True:
        byte = number & 0x7F
        number >>= 7
        if number:
            byte |= 0x80
        encoded_bytes.append(byte)
        if not number:
            break
    return bytes(encoded_bytes)

numbers = [
    902000208,
    902000209,
    902000210,
    902000211
]

def Encrypt_ID(number):
    number = int(number)
    encoded_bytes = []
    while True:
        byte = number & 0x7F
        number >>= 7
        if number:
            byte |= 0x80
        encoded_bytes.append(byte)
        if not number:
            break
    return bytes(encoded_bytes).hex()

def Encrypt(number):
    number = int(number)
    encoded_bytes = []
    while True:
        byte = number & 0x7F
        number >>= 7
        if number:
            byte |= 0x80
        encoded_bytes.append(byte)
        if not number:
            break
    return bytes(encoded_bytes).hex()

def Decrypt(encoded_bytes):
    encoded_bytes = bytes.fromhex(encoded_bytes)
    number = 0
    shift = 0
    for byte in encoded_bytes:
        value = byte & 0x7F
        number |= value << shift
        shift += 7
        if not byte & 0x80:
            break
    return number

def decrypt_api(cipher_text):
    return decrypt_packet(cipher_text, ENCRYPTION_KEY, ENCRYPTION_IV)

def encrypt_api(plain_text):
    return encrypt_packet(plain_text, ENCRYPTION_KEY, ENCRYPTION_IV)

# وظائف JWT المدمجة مباشرة
def TOKEN_MAKER(OLD_ACCESS_TOKEN, NEW_ACCESS_TOKEN, OLD_OPEN_ID, NEW_OPEN_ID, uid):
    now = datetime.now()
    now = str(now)[:len(str(now)) - 7]
    data = bytes.fromhex('1a13323032352d30372d33302031313a30323a3531220966726565206669726528013a07312e3131342e32422c416e64726f6964204f5320372e312e32202f204150492d323320284e32473438382f373030323530323234294a0848616e6468656c645207416e64726f69645a045749464960c00c68840772033332307a1f41524d7637205646507633204e454f4e20564d48207c2032343635207c203480019a1b8a010f416472656e6f2028544d292036343092010d4f70656e474c20455320332e319a012b476f6f676c657c31663361643662372d636562342d343934622d383730622d623164616364373230393131a2010c3139372e312e31322e313335aa0102656eb201203939366136323964626364623339363462653662363937386635643831346462ba010134c2010848616e6468656c64ca011073616d73756e6720534d2d473935354eea014066663930633037656239383135616633306134336234613966363031393531366530653463373033623434303932353136643064656661346365663531663261f00101ca0207416e64726f6964d2020457494649ca03203734323862323533646566633136343031386336303461316562626665626466e003daa907e803899b07f003bf0ff803ae088004999b078804daa9079004999b079804daa907c80403d204262f646174612f6170702f636f6d2e6474732e667265656669726574682d312f6c69622f61726de00401ea044832303837663631633139663537663261663465376665666630623234643964397c2f646174612f6170702f636f6d2e6474732e667265656669726574682d312f626173652e61704bf00403f804018a050233329a050a32303139313138363933a80503b205094f70656e474c455332b805ff7fc00504e005dac901ea0507616e64726f6964f2055c4b71734854394748625876574c6668437950416c52526873626d43676542557562555551317375746d525536634e30524f3751453141486e496474385963784d614c575437636d4851322b7374745279377830663935542b6456593d8806019006019a060134a2060134b2061e40001147550d0c074f530b4d5c584d57416657545a065f2a091d6a0d5033')
    data = data.replace(OLD_OPEN_ID.encode(), NEW_OPEN_ID.encode())
    data = data.replace(OLD_ACCESS_TOKEN.encode(), NEW_ACCESS_TOKEN.encode())
    d = encrypt_api(data.hex())
    Final_Payload = bytes.fromhex(d)
    
   
    headers = {
        "Host": "loginbp.ggblueshark.com",
        "X-Unity-Version": "2018.4.11f1",
        "Accept": "*/*",
        "Authorization": "Bearer",
        "ReleaseVersion": "OB52",
        "X-GA": "v1 1",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": str(len(Final_Payload)),
        "User-Agent": "Free%20Fire/2019118692 CFNetwork/3826.500.111.2.2 Darwin/24.4.0",
        "Connection": "keep-alive"
    }
    
    URL = "https://loginbp.ggblueshark.com/MajorLogin"
    RESPONSE = requests.post(URL, headers=headers, data=Final_Payload, verify=False)
    
    if RESPONSE.status_code == 200:
        if len(RESPONSE.text) < 10:
            return False
        BASE64_TOKEN = RESPONSE.text[RESPONSE.text.find("eyJhbGciOiJIUzI1NiIsInN2ciI6IjEiLCJ0eXAiOiJKV1QifQ"):-1]
        second_dot_index = BASE64_TOKEN.find(".", BASE64_TOKEN.find(".") + 1)
        BASE64_TOKEN = BASE64_TOKEN[:second_dot_index + 44]
        return BASE64_TOKEN
    else:
        print(f"MajorLogin failed with status: {RESPONSE.status_code}")
        print(f"Response: {RESPONSE.text}")
        return False

def fetch_jwt_token_direct():
    """جلب التوكن مباشرة بدون استخدام API خارجي"""
    try:
        uid = "4405612936"
        password = "4FB8997618773AA104EE494C71EB7D970B528894E92D3FC70E952113EB445A0A"
        
        url = "https://100067.connect.garena.com/oauth/guest/token/grant"
        headers = {
            "Host": "100067.connect.garena.com",
            "User-Agent": "GarenaMSDK/4.0.19P4(G011A ;Android 9;en;US;)",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "close",
        }
        data = {
            "uid": f"{uid}",
            "password": f"{password}",
            "response_type": "token",
            "client_type": "2",
            "client_secret": "",
            "client_id": "100067",
        }
        
        response = requests.post(url, headers=headers, data=data)
        print(f"📩 استجابة Garena API: {response.text}")
        
        data = response.json()
        
        if "access_token" not in data or "open_id" not in data:
            print(f"❌ مفاتيح مفقودة في الاستجابة: {data}")
            return None

        NEW_ACCESS_TOKEN = data['access_token']
        NEW_OPEN_ID = data['open_id']
        OLD_ACCESS_TOKEN = "ff90c07eb9815af30a43b4a9f6019516e0e4c703b44092516d0defa4cef51f2a"
        OLD_OPEN_ID = "996a629dbcdb3964be6b6978f5d814db"
        
        token = TOKEN_MAKER(OLD_ACCESS_TOKEN, NEW_ACCESS_TOKEN, OLD_OPEN_ID, NEW_OPEN_ID, uid)
        if token:
            print(f"✅ تم توليد التوكن بنجاح: {token}")
            return token
        else:
            print("❌ فشل توليد التوكن")
            return None
            
    except Exception as e:
        print(f"⚠️ خطأ أثناء جلب التوكن مباشرة: {e}")
        return None
# وظائف API المحدثة مع الـ Headers الجديدة
def send_friend_request(player_id):
    """إرسال طلب صداقة - الإصدار المُبسط"""
    global JWT_TOKEN
    if not JWT_TOKEN:
        return "⚠️ التوكن غير متاح حاليًا أو غير صالح. يرجى محاولة التحديث يدوياً أو انتظار التحديث الدوري."
    
    enc_id = Encrypt_ID(player_id)
    payload = f"08a7c4839f1e10{enc_id}1801" 
    encrypted_payload = encrypt_api(payload)
    
    url = "https://clientbp.ggblueshark.com/RequestAddingFriend"
    headers = {
        "Authorization": f"Bearer {JWT_TOKEN}",
        "X-Unity-Version": "2018.4.11f1",
        "X-GA": "v1 1",
        "ReleaseVersion": "OB52",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Dalvik/2.1.0 (Linux; Android 9)",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    
    try:
        r = requests.post(url, headers=headers, data=bytes.fromhex(encrypted_payload), timeout=15, verify=False)
        
        if r.status_code == 200:
            # تحليل الاستجابة المبسط
            if "BR_FRIEND_NOT_SAME_REGION" in r.text:
                return "❌ لا يمكن إضافة اللاعب لأنه ليس في نفس منطقتك (السيرفر)"
            
            # إذا وصلنا هنا يعني الإضافة ناجحة
            return "✅ تم إرسال طلب الصداقة بنجاح!"
                    
        elif r.status_code == 400:
            if "BR_FRIEND_NOT_SAME_REGION" in r.text:
                return "❌ لا يمكن إضافة اللاعب لأنه ليس في نفس منطقتك (السيرفر)"
            return "❌ خطأ في الطلب - قد يكون اللاعب من منطقة مختلفة"
        elif r.status_code == 401:
            JWT_TOKEN = None
            return "❌ التوكن غير صالح أو منتهي الصلاحية. سيتم محاولة تحديثه."
        elif r.status_code == 404:
            return "❌ اللاعب غير موجود أو خطأ في الاتصال بنقطة النهاية."
        else:
            return f"❌ فشل إرسال الطلب. كود الخطأ: {r.status_code}"
            
    except Exception as e:
        return f"❌ حدث خطأ أثناء إرسال الطلب: {str(e)}"

def remove_friend(player_id):
    """حذف صديق - الإصدار المُبسط والمُحسن للتشخيص"""
    global JWT_TOKEN
    if not JWT_TOKEN:
        return "⚠️ التوكن غير متاح حاليًا أو غير صالح. يرجى محاولة التحديث يدوياً أو انتظار التحديث الدوري."
    
    enc_id = Encrypt_ID(player_id)
    # الحمولة المشتبه بها
    payload = f"08a7c4839f1e10{enc_id}1802"  
    encrypted_payload = encrypt_api(payload)
    
    url = "https://clientbp.ggblueshark.com/RemoveFriend"
    headers = {
        "Authorization": f"Bearer {JWT_TOKEN}",
        "X-Unity-Version": "2018.4.11f1",
        "X-GA": "v1 1",
        "ReleaseVersion": "OB52",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Dalvik/2.1.0 (Linux; Android 9)",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    
    try:
        r = requests.post(url, headers=headers, data=bytes.fromhex(encrypted_payload), timeout=15, verify=False)
        
        # 🚨 مخرج التشخيص الرئيسي 🚨
        if r.status_code != 200:
            print(f"DEBUG: RemoveFriend FAILED. Status={r.status_code}, Response Body={r.text}")
        
        if r.status_code == 200:
            return "✅ تم الحذف بنجاح!"
        elif r.status_code == 401:
            JWT_TOKEN = None
            return "❌ التوكن غير صالح أو منتهي الصلاحية. سيتم محاولة تحديثه."
        elif r.status_code == 400:
            # إذا كان الخطأ 400، نُعيد نص الاستجابة بالكامل إذا أمكن
            server_error = r.text.strip()
            if server_error:
                 return f"❌ فشل الحذف. كود الخطأ: 400. استجابة السيرفر: {server_error}"
            return "❌ فشل الحذف. كود الخطأ: 400 (طلب سيئ - تحقق من الحمولة Protobuf)."
        elif r.status_code == 404:
            return "❌ اللاعب غير موجود في قائمة الأصدقاء (أو خطأ اتصال)."
        else:
            return f"❌ فشل الحذف. كود الخطأ: {r.status_code}"
            
    except Exception as e:
        return f"❌ حدث خطأ أثناء الحذف: {str(e)}"

        
def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                if isinstance(data, dict):
                    return data
            except json.JSONDecodeError:
                pass
    return {}

def save_users():
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)

def load_groups():
    if os.path.exists(GROUPS_FILE):
        with open(GROUPS_FILE, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                if isinstance(data, dict):
                    return {k: v for k, v in data.items()}
            except json.JSONDecodeError:
                pass
    return {}

def save_groups():
    with open(GROUPS_FILE, "w", encoding="utf-8") as file:
        json.dump(group_activations, file, ensure_ascii=False, indent=4)

def load_maintenance_status():
    if os.path.exists(MAINTENANCE_FILE):
        with open(MAINTENANCE_FILE, "r", encoding="utf-8") as file:
            try:
                return json.load(file).get("maintenance_mode", False)
            except json.JSONDecodeError:
                pass
    return False

def save_maintenance_status(status):
    with open(MAINTENANCE_FILE, "w", encoding="utf-8") as file:
        json.dump({"maintenance_mode": status}, file)

def is_admin(message):
    """التحقق إذا كان المستخدم من المسؤولين"""
    user_id = message.from_user.id if hasattr(message, 'from_user') else message
    return user_id in ADMIN_IDS

def is_allowed_group(message):
    chat_id_str = str(message.chat.id)
    if chat_id_str in group_activations:
        expiry_timestamp = group_activations[chat_id_str]
        if expiry_timestamp > time.time():
            return True
        else:
            del group_activations[chat_id_str]
            save_groups()
            bot.send_message(message.chat.id, "⚠️ انتهت صلاحية تفعيل البوت في هذه المجموعة.\nيرجى التواصل مع [@Picos0](https://t.me/PICOS_BOT_CLAN) لإعادة التفعيل.", parse_mode="Markdown")
            return False
    else:
        bot.send_message(message.chat.id, "⚠️ البوت غير مفعل في هذه المجموعة.\nيرجى التواصل مع [@Picos0](https://t.me/PICOS_BOT_CLAN) لكي يقوم بتفعيل البوت.", parse_mode="Markdown")
        return False

def is_subscribed(message):
    try:
        status = bot.get_chat_member(SUBSCRIPTION_CHANNEL_ID, message.from_user.id).status
        return status in ['member', 'administrator', 'creator']
    except telebot.apihelper.ApiTelegramException as e:
        if "chat not found" in str(e) or "user not found" in str(e):
            print(f"Error checking subscription: {e}")
            return False
        return False

def format_remaining_time(expiry_time):
    remaining = int(expiry_time - time.time())
    if remaining <= 0:
        return "⛔ انتهت الصلاحية"

    days = remaining // 86400
    hours = (remaining % 86400) // 3600
    minutes = ((remaining % 86400) % 3600) // 60
    seconds = remaining % 60

    parts = []
    if days > 0:
        parts.append(f"{days} يوم")
    if hours > 0:
        parts.append(f"{hours} ساعة")
    if minutes > 0:
        parts.append(f"{minutes} دقيقة")
    parts.append(f"{seconds} ثانية")

    return " ".join(parts)

def fetch_jwt_token():
    """استخدام الوظيفة المدمجة مباشرة لجلب التوكن"""
    return fetch_jwt_token_direct()

def update_jwt_periodically():
    global JWT_TOKEN
    while True:
        new_token = fetch_jwt_token()
        if new_token:
            JWT_TOKEN = new_token
            print("🔄 تم تحديث التوكن بنجاح")
        else:
            print("⚠️ فشل تحديث التوكن، سيتم المحاولة لاحقاً")
        time.sleep(5 * 3600)  # تحديث كل 5 ساعات

def remove_expired_users():
    now = time.time()
    expired = [uid for uid, d in users.items() if d.get("expiry") and d["expiry"] <= now]
    for uid in expired:
        if "added_by_tele_id" in users[uid]:
            remove_friend(uid)
        del users[uid]
    save_users()

def check_expired_users():
    while True:
        remove_expired_users()
        time.sleep(60)

def reset_daily_adds():
    now = datetime.now()
    for tele_id in list(users.keys()):
        if 'last_reset_day' in users[tele_id]:
            last_reset = datetime.fromtimestamp(users[tele_id]['last_reset_day'])
            if now.date() > last_reset.date():
                users[tele_id]['adds_today'] = 0
                users[tele_id]['last_reset_day'] = now.timestamp()
    save_users()

def daily_reset_timer():
    while True:
        reset_daily_adds()
        time.sleep(3600)

def get_total_users_count():
    """الحصول على عدد المستخدمين الفعليين في القائمة (باستثناء بيانات المستخدمين العاديين)"""
    count = 0
    for uid, data in users.items():
        # نحسب فقط المستخدمين الذين لديهم بيانات كاملة (اللاعبين المضافين)
        if isinstance(data, dict) and "name" in data and "expiry" in data:
            count += 1
    return count

users = load_users()
group_activations = load_groups()
maintenance_mode = load_maintenance_status()
bot = telebot.TeleBot(BOT_TOKEN)

# جلب التوكن مباشرة بدون API
print("🔄 جاري جلب التوكن للمرة الأولى...")
for _ in range(5):
    JWT_TOKEN = fetch_jwt_token()
    if JWT_TOKEN:
        print("✅ تم جلب التوكن بنجاح!")
        break
    time.sleep(3)
else:
    print("❌ فشل جلب التوكن بعد 5 محاولات!")

if not JWT_TOKEN:
    print("⚠️ تحذير: البوت يعمل بدون توكن، قد لا تعمل بعض الوظائف!")

threading.Thread(target=update_jwt_periodically, daemon=True).start()
threading.Thread(target=check_expired_users, daemon=True).start()
threading.Thread(target=daily_reset_timer, daemon=True).start()

def get_player_info(uid):
    try:
        # استخدام API الجديد
        res = requests.get(f"https://tmk-all-info.vercel.app/info/{uid}", timeout=10)
        data = res.json()
        info = data["basicInfo"]
        name = info["nickname"]
        region = info["region"]
        level = info["level"]
        return name, region, level
    except Exception as e:
        print(f"⚠️ Error fetching info for {uid}: {e}")
        return "غير معروف", "N/A", "N/A"

def send_message_to_all_groups(message_text):
    for chat_id in list(group_activations.keys()):
        try:
            bot.send_message(chat_id, message_text, parse_mode="Markdown")
            time.sleep(1)
        except telebot.apihelper.ApiTelegramException as e:
            if "chat not found" in str(e) or "bot was kicked from the group chat" in str(e):
                print(f"⚠️ فشل إرسال رسالة إلى المجموعة {chat_id}: تم حذف المجموعة أو البوت ليس عضواً. سيتم حذفها من القائمة.")
                del group_activations[chat_id]
                save_groups()
            else:
                print(f"⚠️ فشل إرسال رسالة إلى المجموعة {chat_id}: {e}")

@bot.message_handler(func=lambda message: message.chat.type == 'private' and not is_admin(message))
def handle_private_non_admin(message):
    bot.reply_to(message, "🗿")
    return

@bot.message_handler(commands=['start', 'help'])
def handle_general_commands(message):
    if message.chat.type == 'private' and not is_admin(message):
        return

    if message.text == '/start' or message.text == '/start@BOT_Friend_Free_Firebot':
        welcome_text = """
    أهلاً بك! أنا بوت يساعد في إدارة قائمة الأصدقاء في اللعبة.

    استخدم أمر /help لعرض قائمة الأوامر المتاحة.
    """
        bot.reply_to(message, welcome_text)
    
    elif message.text == '/help' or message.text == '/help@BOT_Friend_Free_Firebot':
        help_text = """
━━━━━━━━━━━━━━━
         [⚔️ أوامر الأعضاء العاديين ⚔️]
━━━━━━━━━━━━━━━
🔹 <code>/add &lt;id&gt;</code>
    ➝ إضافة شخص لمدة يوم
        
 S 1 X   P I C O S⚡  1⃣
        
🔹 <code>/remove &lt;id&gt;</code>
    ➝ لإزالة شخص أضفته
"""

        if is_admin(message):
            help_text += """
━━━━━━━━━━━━━━━━
[  أوامر عمك P I C O S]
━━━━━━━━━━━━━━━━
🔹 <code>/add &lt;id&gt; [عدد_الأيام]</code>
    ➝ إضافة شخص مع تحديد المدة

🔹 <code>/list</code>
    ➝ عرض جميع المضافين

🔹 <code>/remove_all</code>
    ➝ حذف جميع المضافين

🔹 <code>/sid &lt;عدد_الأيام&gt;</code>
    ➝ تفعيل البوت (داخل المجموعة)

🔹 <code>/stop</code>
    ➝ إيقاف البوت (داخل المجموعة)

🔹 <code>/maintenance</code>
    ➝ تفعيل وضع الصيانة

🔹 <code>/unmaintenance</code>
    ➝إيقاف وضع الصيانة

🔹 <code>/leave_group &lt;id&gt;</code>
    ➝ الخروج من مجموعة (في الخاص)

━━━━━━━━━━━━━━━━
"""
        bot.reply_to(message, help_text, parse_mode="HTML")

@bot.message_handler(commands=['maintenance'])
def enable_maintenance_mode(message):
    if not is_admin(message):
        bot.reply_to(message, "🔒 هذا الامر مخصص فقط لي picos.")
        return

    global maintenance_mode
    if maintenance_mode:
        bot.reply_to(message, "⚠️ البوت هو بالفعل في وضع الصيانة.")
        return

    maintenance_mode = True
    save_maintenance_status(True)
    
    maintenance_message = "⚙️ تنبيه صيانة ⚙️\n\n⚠️ دخل البوت في وضع الصيانة سيتم تشغيله عند الانتهاء\n\nشكراً لتفهمكم ❤."
    bot.reply_to(message, "✅ تم تفعيل وضع الصيانة بنجاح. سيتم إرسال رسالة تنبيه لجميع المجموعات.", parse_mode="Markdown")
    send_message_to_all_groups(maintenance_message)

@bot.message_handler(commands=['unmaintenance'])
def disable_maintenance_mode(message):
    if not is_admin(message):
        bot.reply_to(message, "🔒 هذا الأمر مخصص فقط لي picos.")
        return

    global maintenance_mode
    if not maintenance_mode:
        bot.reply_to(message, "⚠️ البوت ليس في وضع الصيانة حاليًا.")
        return

    maintenance_mode = False
    save_maintenance_status(False)

    unmaintenance_message = "🎉 إشعار هام 🎉\n\n🥳 تم حل المشاكل!\nالبوت يعمل الآن بشكل كامل. شكراً على صبركم ودعمكم."
    bot.reply_to(message, "✅ تم إزالة وضع الصيانة بنجاح. سيتم إرسال رسالة لجميع المجموعات.", parse_mode="Markdown")
    send_message_to_all_groups(unmaintenance_message)

@bot.message_handler(commands=['add'])
def add_user(message):
    if message.chat.type == 'private' and not is_admin(message):
        return
    elif message.chat.type != 'private' and not is_allowed_group(message):
        return

    if maintenance_mode and not is_admin(message):
        bot.reply_to(message, "⚙️ البوت في وضع الصيانة حالياً.\nسوف يتم إعادته بعد الانتهاء من الصيانة.\nنعتذر على الازعاج.", parse_mode="Markdown")
        return

    # التحقق من الحد الأقصى للقائمة (100 حساب)
    current_count = get_total_users_count()
    if current_count >= 100:
        bot.reply_to(message, "❌ وصل البوت للحد الأقصى من الإضافات (100 حساب).\nيرجى الانتظار حتى يتم تحرير بعض المساحة.")
        return

    user_tele_id = str(message.from_user.id)
    daily_limit = 6

    if not is_admin(message):
        now = datetime.now()
        if user_tele_id not in users:
            users[user_tele_id] = {"adds_today": 0, "last_reset_day": now.timestamp()}
            save_users()
        else:
            last_reset = datetime.fromtimestamp(users[user_tele_id].get("last_reset_day", 0))
            if now.date() > last_reset.date():
                users[user_tele_id]["adds_today"] = 0
                users[user_tele_id]["last_reset_day"] = now.timestamp()
                save_users()

        if users[user_tele_id]["adds_today"] >= daily_limit:
            bot.reply_to(message, f"⚠️ عذراً يبدو انك وصلت للحد الأقصى لليوم يمكنك تفعيل (6uid ) كل يوم ❤.")
            return

    try:
        parts = message.text.split()
        if len(parts) < 2:
            bot.reply_to(message, "❌ الاستخدام: /add [id]")
            return

        game_id = parts[1]

        if not game_id.isdigit():
            bot.reply_to(message, "❌ الأيدي يجب أن يحتوي على أرقام فقط.")
            return

        # تحديد المدة بناءً على نوع المستخدم
        if is_admin(message) and len(parts) > 2:
            # للمسؤول: يأخذ عدد الأيام من الأمر
            days_str = parts[2]
            if days_str.isdigit():
                days = int(days_str)
            else:
                days = 1
        else:
            # للمستخدم العادي :يوم واحد فقط
            days = 1  # يوم = 24/24 = 1 يوم

        # التحقق أولاً إذا كان اللاعب موجودًا بالفعل
        if game_id in users:
            bot.reply_to(message, "❌ هذا اللاعب مضاف بالفعل في القائمة.")
            return

        response = send_friend_request(game_id)
        
        # التحقق من الاستجابة بدقة
        if "✅" in response:
            name, region, level = get_player_info(game_id)

            users[game_id] = {
                "name": name,
                "expiry": time.time() + days * 86400,
                "added_by_tele_id": user_tele_id,
                "added_by_tele_username": message.from_user.username or "بدون معرف",
                "added_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            if not is_admin(message):
                users[user_tele_id]["adds_today"] += 1

            save_users()
            
            # عرض المدة بناءً على نوع المستخدم
            if is_admin(message) and len(parts) > 2:
                duration_text = f"{days} يوم"
            else:
                duration_text = "يوم واحد"
            
            bot.reply_to(message, f"""
الرد من السيرفر : ✅ تم ارسال طلب صداقة للاعب
👤 الاسم: {name}
🆔 الأيدي: {game_id}
المدة: {duration_text}
يرجى قبول طلب الصداقة 🔥
""")
        else:
            # عرض رسالة الخطأ الحقيقية من السيرفر
            error_msg = f"❌ {response}"
            bot.reply_to(message, error_msg)
            
    except Exception as e:
        print(f"[ADD_ERROR] {e}")
        error_msg = f"❌ حدث خطأ: {str(e)}"
        bot.reply_to(message, error_msg)

@bot.message_handler(commands=['remove'])
def remove_user(message):
    if message.chat.type == 'private' and not is_admin(message):
        return
    if message.chat.type != 'private' and not is_allowed_group(message):
        return

    if maintenance_mode and not is_admin(message):
        bot.reply_to(message, "⚙️ البوت في وضع الصيانة حالياً.\nسوف يتم إعادته بعد الانتهاء من الصيانة.\nنعتذر على الازعاج.", parse_mode="Markdown")
        return

    try:
        parts = message.text.split()
        if len(parts) != 2:
            bot.reply_to(message, "❌ الاستخدام:\n/remove <id>")
            return

        game_id_to_remove = parts[1]
        user_tele_id = str(message.from_user.id)

        if game_id_to_remove in users:
            # التحقق من ملكية الأيدي
            if not is_admin(message) and users[game_id_to_remove].get("added_by_tele_id") != user_tele_id:
                bot.reply_to(message, "❌ غير مسموح لك بحذف هذا الأيدي. فقط الشخص الذي أضافه أو المسؤول يمكنه حذفه.")
                return

            name = users[game_id_to_remove]['name']
            response = remove_friend(game_id_to_remove)
            
            # فقط إذا كان الحذف ناجحاً، نزيل اللاعب من القائمة
            if "✅ تم الحذف بنجاح" in response:
                del users[game_id_to_remove]
                save_users()
                bot.reply_to(message, f"""الرد من السيرفر : ✅ نجح حذف الاعب
👤 الاسم: {name}""")
            else:
                # إذا فشل الحذف، نبقي اللاعب في القائمة ونخبر المستخدم
                bot.reply_to(message, f"""الرد من السيرفر : ❌ خطاء اثناء حذف الاعب
👤 الاسم: {name}
📩 الخطأ: {response}
⚠️ اللاعب ما زال في القائمة وسيتم المحاولة لاحقاً.""")
        else:
            bot.reply_to(message, "❌ عذراً عزيزي هذا الايدي غير موجود في قائمة الايديات يرجى التأكد منه او إضافة له البوت قبل الحذف.")
    except Exception as e:
        print(f"[REMOVE_ERROR] {e}")
        bot.reply_to(message, "❌ حدث خطأ، يرجى التأكد من الصيغة الصحيحة للأمر.")

@bot.message_handler(commands=['remove_all'])
def remove_all_users(message):
    if not is_admin(message):
        bot.reply_to(message, "⚠️ هذا الأمر مخصص فقط لي picos.")
        return

    if not users:
        bot.reply_to(message, "📭 لا يوجد لاعبين.")
        return

    removed = []
    failed = []
    game_ids_to_remove = [uid for uid, d in users.items() if "added_by_tele_id" in d]
    
    for uid in game_ids_to_remove:
        name = users[uid]['name']
        response = remove_friend(uid)
        
        if "✅ تم الحذف بنجاح" in response:
            del users[uid]
            removed.append(f"👤 {name} | 🆔 {uid} ➜ ✅ تم الحذف")
        else:
            failed.append(f"👤 {name} | 🆔 {uid} ➜ ❌ فشل: {response}")
        
        time.sleep(1)
    
    save_users()

    reply_text = f"📊 تقرير الحذف:\n\n"
    if removed:
        reply_text += f"✅ تم حذف {len(removed)} لاعب:\n" + "\n".join(removed) + "\n\n"
    if failed:
        reply_text += f"❌ فشل حذف {len(failed)} لاعب:\n" + "\n".join(failed)

    if len(reply_text) > 4000:
        for i in range(0, len(reply_text), 4000):
            bot.send_message(message.chat.id, reply_text[i:i + 4000])
    else:
        bot.reply_to(message, reply_text)

@bot.message_handler(commands=['list'])
def list_users(message):
    if message.chat.type != 'private' or not is_admin(message):
        bot.reply_to(message, "⚠️ هذا الامر يخص الادمن فقط.")
        return

    if maintenance_mode and not is_admin(message):
        bot.reply_to(message, "⚙️ البوت في وضع الصيانة حالياً.\nسوف يتم إعادته بعد الانتهاء من الصيانة.\nنعتذر على الازعاج.", parse_mode="Markdown")
        return

    # التحقق من وجود بيانات المستخدمين
    if not users:
        bot.reply_to(message, "📌لا يوجد ايا لاعبين بعد في القائمة !")
        return
    
    # تصفية فقط المستخدمين الذين لديهم بيانات كاملة
    game_friends = {}
    for uid, data in users.items():
        if isinstance(data, dict) and "name" in data and "expiry" in data:
            game_friends[uid] = data
    
    if not game_friends:
        bot.reply_to(message, "📌 لا يوجد ايا لاعبين بعد في القائمة !")
        return
    
    # عرض عدد الحسابات الحالي
    total_count = get_total_users_count()
    text = f"📋 قائمة اللاعبين المضافين ({total_count}/100):\n\n"
    
    for uid, data in game_friends.items():
        try:
            name = html.unescape(data['name'])
            remaining = format_remaining_time(data['expiry'])
            added_by = data.get('added_by_tele_id', 'غير معروف')
            added_username = data.get('added_by_tele_username', 'بدون معرف')
            added_date = data.get('added_date', 'غير معروف')
            
            text += f"👤 {name}\n🆔 {uid}\n⏳ {remaining}\n👤 المضيف: {added_by} (@{added_username})\n📅 تاريخ الإضافة: {added_date}\n───────────────────\n"
        except (KeyError, TypeError):
            continue
    
    if len(text) > 4000:
        # تقسيم الرسالة إذا كانت طويلة
        chunks = [text[i:i+4000] for i in range(0, len(text), 4000)]
        for chunk in chunks:
            bot.send_message(message.chat.id, chunk)
            time.sleep(1)
    else:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['sid'])
def activate_group(message):
    if not is_admin(message):
        bot.reply_to(message, "⚠️ هذا الأمر مخصص فقط لي @Picos0.")
        return

    if message.chat.type == 'private':
        bot.reply_to(message, "❌ لا يمكن تفعيل البوت في الدردشة الخاصة، يرجى استخدام هذا الأمر في المجموعة.")
        return
    
    if maintenance_mode:
        bot.reply_to(message, "⚙️ البوت في وضع الصيانة حالياً.\nسوف يتم إعادته بعد الانتهاء من الصيانة.\nنعتذر على الازعاج.", parse_mode="Markdown")
        return
    
    try:
        parts = message.text.split()
        if len(parts) != 2:
            bot.reply_to(message, "❌ الاستخدام: /sid <عدد الأيام>")
            return

        days_str = parts[1]
        days = int(days_str)
        chat_id = message.chat.id

        expiry_date = datetime.now() + timedelta(days=days)
        group_activations[str(chat_id)] = expiry_date.timestamp()
        save_groups()

        formatted_date = expiry_date.strftime("%Y-%m-%d %H:%M:%S UTC")
        bot.reply_to(message, f"✅ تم تفعيل البوت في الجروب.\n\n🗓 المدة:{days} يوم\n⏳ ينتهي بتاريخ: {formatted_date}", parse_mode="Markdown")

    except ValueError:
        bot.reply_to(message, "❌ عدد الأيام يجب أن يكون رقماً.")
    except Exception as e:
        print(f"[SID_ERROR] {e}")
        bot.reply_to(message, "❌ حدث خطأ أثناء التفعيل.")

@bot.message_handler(commands=['stop'])
def stop_group_activation(message):
    if not is_admin(message):
        bot.reply_to(message, "🔒 هذا الأمر مخصص فقط لي @Picos0.")
        return

    if message.chat.type == 'private':
        bot.reply_to(message, "❌ لا يمكن إيقاف البوت في الدردشة الخاصة، يرجى استخدام هذا الأمر في المجموعة.")
        return
    
    if maintenance_mode:
        bot.reply_to(message, "⚙️ البوت في وضع الصيانة حالياً.\nسوف يتم إعادته بعد الانتهاء من الصيانة.\nنعتذر على الازعاج.", parse_mode="Markdown")
        return
    
    chat_id_str = str(message.chat.id)
    
    if chat_id_str in group_activations:
        del group_activations[chat_id_str]
        save_groups()
        bot.reply_to(message, "✅ تم إيقاف عمل البوت في هذه المجموعة بنجاح.")
    else:
        bot.reply_to(message, "⚠️ البوت غير مفعل بالفعل في هذه المجموعة.")

@bot.message_handler(commands=['leave_group'])
def leave_group_command(message):
    if not is_admin(message):
        bot.reply_to(message, "⚠️ هذا الأمر مخصص فقط لي @Picos0.")
        return
        
    if message.chat.type != 'private':
        bot.reply_to(message, "❌ يرجى استخدام هذا الأمر في الدردشة الخاصة مع البوت.")
        return
    
    try:
        parts = message.text.split()
        if len(parts) != 2:
            bot.reply_to(message, "❌ الاستخدام: /leave_group <ايدي_المجموعة>")
            return
            
        group_id = parts[1]
        
        # محاولة الخروج من المجموعة
        try:
            bot.leave_chat(group_id)
            bot.reply_to(message, f"✅ تم الخروج من المجموعة {group_id} بنجاح.")
            
            # حذف المجموعة من قائمة التفعيل إذا كانت موجودة
            if group_id in group_activations:
                del group_activations[group_id]
                save_groups()
                
        except Exception as e:
            bot.reply_to(message, f"❌ فشل الخروج من المجموعة: {e}")
            
    except Exception as e:
        print(f"[LEAVE_GROUP_ERROR] {e}")
        bot.reply_to(message, "❌ حدث خطأ أثناء محاولة الخروج من المجموعة.")

# استخدم هذا في النهاية بدلاً من bot.polling(none_stop=True)
print("🚀 بدء تشغيل البوت...")
bot.polling(none_stop=True, allowed_updates=['message', 'callback_query', 'inline_query'])