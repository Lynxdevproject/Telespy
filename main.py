import os
from dotenv import load_dotenv
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ChatMemberHandler,
    ContextTypes,
    filters
)
from telegram import ChatMemberUpdated

# 📦 Import handler dari folder handlers/
from handlers import start, spy_handler, history

# 🔐 Load BOT_TOKEN dari file .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 🕵️ Handler: bot keluar kalau ditambahkan tapi bukan admin
async def member_check(update: ChatMemberUpdated, context: ContextTypes.DEFAULT_TYPE):
    member_update = update.my_chat_member
    chat = member_update.chat
    status = member_update.new_chat_member.status

    if status != "administrator":
        await context.bot.send_message(
            chat_id=chat.id,
            text="🚫 Bot tidak ditugaskan sebagai admin.\nSelamat tinggal 👋"
        )
        await context.bot.leave_chat(chat.id)

# 🚀 Entry point Telespy
def main():
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN tidak ditemukan di .env. Pastikan sudah diatur.")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    # ✅ Handler /start untuk briefing user
    app.add_handler(CommandHandler("start", start))

    # ✅ Handler mata-mata identitas user
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, spy_handler))

    # ✅ Handler /history untuk selidiki user via reply
    app.add_handler(CommandHandler("history", history))

    # ✅ Handler auto-keluar jika bukan admin (pakai my_chat_member)
    app.add_handler(ChatMemberHandler(member_check, chat_member_types=["my_chat_member"]))

    # 🛠️ Optional: Tambahkan error handler biar gak buang stacktrace ke log
    async def error_handler(update, context):
        print(f"[ERROR] {context.error}")
    app.add_error_handler(error_handler)

    print("🕶️ Telespy aktif dan menyelidiki grup...")
    app.run_polling()

if __name__ == "__main__":
    main()
