import os
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters
)

# =========================================
# TOKEN BOT
# =========================================
TOKEN = os.getenv("TOKEN")

# =========================================
# ID TELEGRAM ADMIN
# DAPAT DARI @userinfobot
# =========================================
ADMIN_ID = 8172840050

# =========================================
# LINK PRODUK
# =========================================
LINK_BASIC = "https://t.me/+LyJ-fL0ZUeVmMTM1"
LINK_PREMIUM = "https://t.me/+LyJ-fL0ZUeVmMTM1"
LINK_VIP = "https://t.me/+LyJ-fL0ZUeVmMTM1"

# =========================================
# MENYIMPAN DATA ORDER USER
# =========================================
user_orders = {}

# =========================================
# MENU UTAMA
# =========================================
main_keyboard = [
    ["🎥 PREVIEW GRATIS", "ℹ️ INFORMASI PAKET"],
    ["⭐ TESTIMONI", "❓ FAQ"],
    ["🛒 BELI SEKARANG"]
]

main_markup = ReplyKeyboardMarkup(
    main_keyboard,
    resize_keyboard=True
)

# =========================================
# MENU PEMBELIAN
# =========================================
buy_keyboard = [
    ["🥉 BASIC", "🥈 PREMIUM"],
    ["🥇 VIP PRIVATE"],
    ["⬅️ KEMBALI"]
]

buy_markup = ReplyKeyboardMarkup(
    buy_keyboard,
    resize_keyboard=True
)

# =========================================
# START
# =========================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    teks = (
        "Halo! 👋\n\n"
        "Selamat datang di Movies Digital Bot 🎬\n\n"
        "Silakan pilih menu di bawah ini 👇"
    )

    await update.message.reply_text(
        teks,
        reply_markup=main_markup
    )

# =========================================
# HANDLE TEXT
# =========================================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    user_id = update.message.from_user.id

    # =====================================
    # PREVIEW GRATIS
    # =====================================
    if text == "🎥 PREVIEW GRATIS":

        await update.message.reply_video(
            video=open("preview.mp4", "rb"),
            caption="🎥 Preview Gratis\n"
        )

    # =====================================
    # INFORMASI PAKET
    # =====================================
    elif text == "ℹ️ INFORMASI PAKET":

        await update.message.reply_text(
            "📦 INFORMASI PAKET\n\n"

            "🥉 BASIC : Rp 50.000\n"
            "✅ Harga lebih murah\n"
            "✅ Cocok untuk penggunaan pribadi\n"
            "✅ Akses film & series pilihan\n\n"

            "🥈 PREMIUM : Rp 100.000\n"
            "✅ Kualitas Full HD\n"
            "✅ Update film terbaru\n"
            "✅ Akses lebih lengkap\n"
            "✅ Bisa login di beberapa device\n\n"

            "🥇 VIP PRIVATE : Rp 150.000\n"
            "✅ Akun private full akses\n"
            "✅ Anti gangguan pengguna lain\n"
            "✅ Streaming lebih nyaman\n"
            "✅ Support prioritas"
        )

    # =====================================
    # TESTIMONI
    # =====================================
    elif text == "⭐ TESTIMONI":

        await update.message.reply_photo(
            photo=open("testimoni.jpg", "rb"),
            caption="⭐ TESTIMONI CUSTOMER"
        )

    # =====================================
    # FAQ
    # =====================================
    elif text == "❓ FAQ":

        await update.message.reply_text(
            "❓ FAQ\n\n"

            "🎬 Apakah film bisa ditonton selamanya?\n"
            "✅ Tergantung paket yang dipilih.\n\n"

            "📱 Bisa ditonton di HP?\n"
            "✅ Bisa di HP, Laptop, maupun Smart TV.\n\n"

            "⏳ Berapa lama proses pengiriman akun?\n"
            "✅ Estimasi 1-10 menit setelah pembayaran.\n\n"

            "💳 Pembayaran via apa?\n"
            "✅ QRIS.\n\n"

            "🛒 Cara order bagaimana?\n"
            "✅ Klik menu BELI SEKARANG."
        )

    # =====================================
    # BELI SEKARANG
    # =====================================
    elif text == "🛒 BELI SEKARANG":

        await update.message.reply_text(
            "🛒 Silakan pilih paket:",
            reply_markup=buy_markup
        )

    # =====================================
    # BASIC
    # =====================================
    elif text == "🥉 BASIC":

        user_orders[user_id] = "BASIC"

        caption = (
            "🥉 BASIC\n\n"

            "Nominal:\n"
            "Rp 50.000\n\n"

            "Format Konfirmasi:\n"
            "Paket: BASIC\n"

            "*Upload bukti pembayaran ke bot ini."
        )

        await update.message.reply_photo(
            photo=open("qris.jpg", "rb"),
            caption=caption
        )

    # =====================================
    # PREMIUM
    # =====================================
    elif text == "🥈 PREMIUM":

        user_orders[user_id] = "PREMIUM"

        caption = (
            "🥈 PREMIUM\n\n"

            "Nominal:\n"
            "Rp 100.000\n\n"

            "Format Konfirmasi:\n"
            "Paket: PREMIUM\n"

            "*Upload bukti pembayaran ke bot ini."
        )

        await update.message.reply_photo(
            photo=open("qris.jpg", "rb"),
            caption=caption
        )

    # =====================================
    # VIP PRIVATE
    # =====================================
    elif text == "🥇 VIP PRIVATE":

        user_orders[user_id] = "VIP PRIVATE"

        caption = (
            "🥇 VIP PRIVATE\n\n"

            "Nominal:\n"
            "Rp 150.000\n\n"

            "Format Konfirmasi:\n"
            "Paket: VIP PRIVATE\n"

            "*Upload bukti pembayaran ke bot ini."
        )

        await update.message.reply_photo(
            photo=open("qris.jpg", "rb"),
            caption=caption
        )

    # =====================================
    # KEMBALI
    # =====================================
    elif text == "⬅️ KEMBALI":

        await update.message.reply_text(
            "Menu utama 👇",
            reply_markup=main_markup
        )

# =========================================
# HANDLE FOTO PEMBAYARAN
# =========================================
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user
    user_id = user.id

    # =====================================
    # CEK APAKAH SUDAH PILIH PAKET
    # =====================================
    if user_id not in user_orders:

        await update.message.reply_text(
            "❌ Silakan pilih paket terlebih dahulu."
        )

        return

    paket = user_orders[user_id]

    # =====================================
    # AMBIL FOTO
    # =====================================
    photo = update.message.photo[-1].file_id

    # =====================================
    # BUTTON ADMIN
    # =====================================
    keyboard = [
        [
            InlineKeyboardButton(
                "✅ APPROVE",
                callback_data=f"approve_{user_id}"
            ),

            InlineKeyboardButton(
                "❌ REJECT",
                callback_data=f"reject_{user_id}"
            )
        ]
    ]

    admin_markup = InlineKeyboardMarkup(keyboard)

    # =====================================
    # KIRIM FOTO KE ADMIN
    # =====================================
    caption = (
        f"📥 PEMBAYARAN MASUK\n\n"
        f"👤 Username: @{user.username}\n"
        f"🆔 User ID: {user_id}\n"
        f"📦 Paket: {paket}"
    )

    await context.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=photo,
        caption=caption,
        reply_markup=admin_markup
    )

    # =====================================
    # PESAN KE USER
    # =====================================
    await update.message.reply_text(
        "✅ Bukti pembayaran berhasil dikirim.\n\n"
        "Silakan tunggu konfirmasi admin."
    )

# =========================================
# HANDLE APPROVE / REJECT
# =========================================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    data = query.data

    # =====================================
    # APPROVE
    # =====================================
    if data.startswith("approve_"):

        user_id = int(data.split("_")[1])

        paket = user_orders.get(user_id)

        # =================================
        # PILIH LINK BERDASARKAN PAKET
        # =================================
        if paket == "BASIC":
            link = LINK_BASIC

        elif paket == "PREMIUM":
            link = LINK_PREMIUM

        elif paket == "VIP PRIVATE":
            link = LINK_VIP

        else:
            link = "Link tidak tersedia"

        # =================================
        # KIRIM KE USER
        # =================================
        await context.bot.send_message(
            chat_id=user_id,
            text=(
                "✅ Pembayaran berhasil dikonfirmasi.\n\n"
                "🎬 Berikut link akses kamu:\n\n"
                f"{link}"
            )
        )

        # =================================
        # UPDATE STATUS ADMIN
        # =================================
        await query.edit_message_caption(
            caption=query.message.caption + "\n\n✅ APPROVED"
        )

    # =====================================
    # REJECT
    # =====================================
    elif data.startswith("reject_"):

        user_id = int(data.split("_")[1])

        await context.bot.send_message(
            chat_id=user_id,
            text=(
                "❌ Mohon cek kembali bukti pembayaran anda."
            )
        )

        await query.edit_message_caption(
            caption=query.message.caption + "\n\n❌ REJECTED"
        )

# =========================================
# MAIN
# =========================================
def main():

    app = ApplicationBuilder().token(TOKEN).build()

    # COMMAND
    app.add_handler(CommandHandler("start", start))

    # TEXT
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message
        )
    )

    # FOTO
    app.add_handler(
        MessageHandler(
            filters.PHOTO,
            handle_photo
        )
    )

    # BUTTON
    app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    print("Bot berjalan...")
    app.run_polling()

# =========================================
# RUN
# =========================================
if __name__ == "__main__":
    main()
