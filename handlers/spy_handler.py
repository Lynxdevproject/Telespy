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
            changes.append({
                "type": "username",
                "old": previous["username"],
                "new": username
            })
        if previous["first_name"] != first_name:
            changes.append({
                "type": "name",
                "old": previous["first_name"],
                "new": first_name
            })
    else:
        changes.append({
            "type": "new_user",
            "username": username,
            "name": first_name
        })

    # 📝 Update cache
    user_cache[user_id] = {"username": username, "first_name": first_name}

    if changes:
        report = "📋 *Laporan Perubahan Identitas:*\n"

        for change in changes:
            if change["type"] == "username":
                report += (
                    "\n👤 *Username Sebelumnya* : @" + change["old"] +
                    "\n🎯 *Username Sekarang*   : @" + change["new"]
                )
            elif change["type"] == "name":
                report += (
                    "\n📝 *Nama Sebelumnya*     : " + change["old"] +
                    "\n🆕 *Nama Sekarang*       : " + change["new"]
                )
            elif change["type"] == "new_user":
                report += (
                    f"\n📍 *User Baru Terdeteksi:*\n"
                    f"👤 Username : @{change['username']}\n"
                    f"📝 Nama     : {change['name']}"
                )

        await update.message.reply_text(report, parse_mode="Markdown")
