from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Tambahkan ke Grup", url="https://t.me/UserSpyingbot?startgroup=true")]
    ])

    await update.message.reply_text(
        "🕵️ *Selamat datang di Telespy!*\n\n"
        "Bot ini bertugas sebagai *intel digital* di grup Telegram lo.\n"
        "Fungsinya:\n"
        "• Mendeteksi perubahan *username & nama user*\n"
        "• Memberi *laporan live* langsung di grup\n"
        "• Bantu admin *hindari spammer & penyusup identitas*\n\n"
        "📌 Telespy terinspirasi dari *Sangmata Bot*, pelacak identitas legendaris di Telegram yang udah lama eksis.\n"
        "Tapi versi ini dibuat lebih ringan, modular, dan bisa lo modifikasi sendiri 💼\n\n"
        "🔒 Bot harus dijadikan *admin* supaya bisa baca semua pesan dan aktifkan mode mata-mata.\n\n"
        "Klik tombol di bawah untuk langsung rekrut agen ini ke grup lo 👇",
        parse_mode="Markdown",
        reply_markup=keyboard
    )
