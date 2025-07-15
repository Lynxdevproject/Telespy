from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🕵️ Selamat datang di *Telespy*!\n\n"
        "Bot ini bertugas sebagai *intel digital* di grup Telegram lo.\n"
        "Fungsi utamanya:\n"
        "• Mendeteksi user yang *ganti username atau nama*\n"
        "• Memberi *laporan live* ke grup\n"
        "• Bantu admin *hindari spammer & penyusup*\n\n"
        "Bot ini aktif di background dan akan langsung lapor kalau ada perubahan identitas mencurigakan.\n\n"
        "🔒 Pastikan bot udah jadi *admin* biar bisa baca semua pesan.\n"
        "📡 Link bot: [@UserSpyingbot](http://t.me/UserSpyingbot)"
    )
