from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "☘️ Get started"),
            types.BotCommand("tolatin", "🔄 Convert to latin"),
            types.BotCommand("tocyril", "🔄 Convert to cyril"),
            types.BotCommand("about", "📜 About Us"),
        ]
    )
