# 📚 SwapShelf Bot

**SwapShelf** — foydalanuvchilar o'rtasida kitob almashish imkonini beruvchi peer-to-peer Telegram boti.

Foydalanuvchi o'z kitoblarini shelfga qo'shadi, bot ularni kanalga chop etadi. Boshqa foydalanuvchilar kitobni ko'rib, so'rov yuborishadi. Egasi qabul qilsa — swap boshlanadi.

---

## ⚙️ Texnologiyalar

| Texnologiya | Versiya | Maqsad |
|---|---|---|
| python-telegram-bot | 13.15 | Bot framework |
| PostgreSQL | 14+ | Ma'lumotlar bazasi |
| psycopg2-binary | 2.9.9 | PostgreSQL driver |
| python-dotenv | 1.0.0 | Environment variables |

---

## 🗂 Loyiha strukturasi

```
swapshelf/
├── bot.py                  # Entry point, handlerlar ro'yxatga olinadi
├── config.py               # BOT_TOKEN, CHANNEL_ID, DB sozlamalari
├── requirements.txt
├── .env.example
│
├── db/
│   ├── schema.sql          # Barcha jadvallar va seed data
│   ├── connection.py       # Connection pool va execute() helper
│   ├── users.py            # Users CRUD
│   ├── books.py            # Books CRUD
│   ├── requests.py         # Swap requests CRUD
│   └── swaps.py            # Swaps va reviews CRUD
│
├── handlers/
│   ├── start.py            # /start, ro'yxatdan o'tish
│   ├── shelf.py            # Kitob qo'shish, ko'rish, o'chirish
│   ├── request.py          # Browse, so'rov yuborish va qabul qilish
│   ├── swap.py             # Qaytarish va review
│   └── profile.py          # Foydalanuvchi profili
│
├── keyboards/
│   └── inline.py           # Barcha inline va reply klaviaturalar
│
└── utils/
    ├── states.py           # ConversationHandler state konstantalari
    └── channel.py          # Kanalga publish qilish
```

---

## 🗄 Ma'lumotlar bazasi

```
users ──────────────< books          (bir user ko'p kitob qo'sha oladi)
users ──────────────< swap_requests  (bir user ko'p so'rov yuboradi)
books ──────────────< swap_requests  (bir kitobga ko'p so'rov kelishi mumkin)
swap_requests ───── swaps            (qabul qilingan so'rov → swap)
swaps ──────────────< reviews        (har swap tugaganda ikkala tomon review qoldiradi)
genres ─────────────< books          (janr bo'yicha kategoriya)
```

**Jadvallar:**
- `users` — telegram foydalanuvchilari, reyting
- `genres` — kitob janrlari (seed: Roman, Ilmiy, Fantastika va boshqalar)
- `books` — shelfga qo'shilgan kitoblar, holati, turi
- `swap_requests` — yuborilgan so'rovlar (pending / accepted / rejected)
- `swaps` — faol va tugatilgan almashishlar, qaytarish muddati
- `reviews` — swap tugagandan so'ng ikkala tomon uchun reyting va izoh

---

## 🔄 Bot ishlash tartibi

```
/start
  └─ Ro'yxatdan o'tganmi?
       YO'Q → Ism → Telefon → ✅ Ro'yxatdan o'tdi
       HA   → Asosiy menyu

Asosiy menyu:
  📚 My Shelf      → O'z kitoblarim
  ➕ Add Book      → Kitob qo'shish
  🔍 Browse Books  → Mavjud kitoblar
  📬 Requests      → Kelgan / yuborilgan so'rovlar
  🔄 My Swaps      → Faol almashishlar
  ⭐ My Profile    → Profil va reyting

ADD BOOK:
  Nomi → Muallif → Janr → Holat → Tur (borrow/permanent/both)
  → Tavsif → Rasm → Tasdiqlash → DB + Kanal publish ✅

BROWSE + REQUEST:
  Janr tanlash → Kitoblar ro'yxati →
  "📩 Send Request" → Borrow yoki Permanent →
  Xabar → So'rov egasiga yuboriladi

REQUEST qabul qilish (egasi tomonidan):
  [✅ Accept] → Swap yaratiladi
               → Kitob "unavailable" bo'ladi
               → Ikkalasiga contact info yuboriladi
  [❌ Reject] → So'rovchiga xabar yuboriladi

RETURN (faqat borrow uchun):
  My Swaps → "📦 Mark as Returned" →
  Egasi tasdiqlaydi → Kitob yana available →
  Ikkalasiga ⭐ review so'raladi
```

---

## 🚀 O'rnatish va ishga tushirish

### 1. Reponi clone qiling
```bash
git clone https://github.com/yourname/swapshelf.git
cd swapshelf
```

### 2. Virtual environment va dependencylar
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. PostgreSQL database yarating
```sql
CREATE DATABASE swapshelf;
```

### 4. `.env` fayl yarating
```bash
cp .env.example .env
```

`.env` faylini to'ldiring:
```
BOT_TOKEN=your_bot_token_here
CHANNEL_ID=@your_channel_username
ADMIN_IDS=123456789
DB_HOST=localhost
DB_PORT=5432
DB_NAME=swapshelf
DB_USER=postgres
DB_PASSWORD=your_password
```

### 5. Botni ishga tushiring
```bash
python bot.py
```

DB schema birinchi ishga tushirishda avtomatik yaratiladi.

---

## 📢 Kanal sozlamalari

1. Telegram kanalini yarating (public yoki private)
2. Botni kanalga **admin** sifatida qo'shing
3. Admin huquqlari: **"Post Messages"** yoqilgan bo'lishi shart
4. `CHANNEL_ID` ga `@kanal_nomi` yoki `-100xxxxxxxxxx` formatida yozing

---

## 📋 Kitob holatlari va turlari

| Holat | Ma'nosi |
|---|---|
| 🆕 New | Yangi, ishlatilmagan |
| 👍 Good | Yaxshi holat |
| 👌 Fair | O'rtacha holat |
| 📄 Worn | Ko'p ishlatilgan |

| Tur | Ma'nosi |
|---|---|
| 🔄 Borrow | Vaqtincha (30 kun muddatli) |
| 🎁 Permanent | Doimiy berib yuborish |
| 🔀 Both | Ikkalasi ham mumkin |

---

## ⭐ Reyting tizimi

- Har bir swap tugagandan so'ng ikkala tomon bir-biriga 1–5 yulduz va izoh qoldiradi
- Foydalanuvchi reytingi barcha olingan baholaming o'rtachasi
- Profilda ko'rinadi va browse sahifasida egasining reytingi ko'rsatiladi
