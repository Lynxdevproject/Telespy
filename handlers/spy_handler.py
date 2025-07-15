from telegram import Update
from telegram.ext import ContextTypes

# 🧠 Cache RAM buat nyimpan identitas user
user_cache = {}

async def spy_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = str(user.id)
    username = user.username or "NoUsername"
    first_name = user.first_name or "NoName"

    previous = user_cache.get(user_id)
    changes = []

    if previous:
        if previous["username"] != username:
            changes.append(f"🔁 Username berubah: @{previous['username']} → @{username}")
        if previous["first_name"] != first_name:
            changes.append(f"🔁 Nama berubah: {previous['first_name']} → {first_name}")
    else:
        changes.append(f"📍 User baru terdeteksi: @{username} ({first_name})")

    # 📝 Update cache
    user_cache[user_id] = {"username": username, "first_name": first_name}

    if changes:
        await update.message.reply_text(
            "🕵️ *Telespy Report:*\n" + "\n".join(changes),
            parse_mode="Markdown"
        )
