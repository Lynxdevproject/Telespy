from telegram import Update
from telegram.ext import ContextTypes
from handlers.spy_handler import user_cache  # Ambil cache dari spy_handler

async def history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        await update.message.reply_text("📌 Balas pesan dari user yang mau diselidiki dulu.")
        return

    target_user = update.message.reply_to_message.from_user
    user_id = str(target_user.id)

    data = user_cache.get(user_id)

    if data:
        username = data["username"]
        first_name = data["first_name"]

        report = (
            "📂 *Riwayat Identitas Tersimpan:*\n\n"
            f"👤 *Username* : @{username}\n"
            f"📝 *Nama*     : {first_name}"
        )
        await update.message.reply_text(report, parse_mode="Markdown")
    else:
        await update.message.reply_text("🚫 Tidak ditemukan riwayat identitas untuk user ini.")
