import os
from dotenv import load_dotenv
from telegram import ChatMember
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ChatMemberHandler,
    ContextTypes,
    filters
)

# 📦 Import handler dari folder handlers/
from handlers import start, spy_handler

# 🔐 Load .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 🕵️ Handler auto-keluar jika bukan admin
async def member_check(update: ChatMember, context: ContextTypes.DEFAULT_TYPE):
    chat = update.chat
    bot_member = await chat.get_member(context.bot.id)

    if bot_member.status != ChatMember.ADMINISTRATOR:
        await context.bot.send_message(
            chat_id=chat.id,
            text="🚫 Bot tidak ditugaskan sebagai admin.\nSelamat tinggal 👋"
        )
        await context.bot.leave_chat(chat.id)

# 🚀 Entry point Telespy
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # 🧠 Handler /start untuk briefing user
    app.add_handler(CommandHandler("start", start))

    # 🕶️ Handler mata-mata yang mendeteksi perubahan username/nama
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, spy_handler))

    # 💣 Handler auto-keluar dari grup jika bukan admin
    app.add_handler(ChatMemberHandler(member_check, chat_member_types=["member"]))

    print("🕶️ Telespy aktif dan sedang menyelidiki...")
    app.run_polling()

if __name__ == "__main__":
    main()
