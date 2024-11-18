from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats, BotCommandScopeAllChatAdministrators
from aiogram.methods.set_my_commands import SetMyCommands


async def set_commands(bot):
    await bot(SetMyCommands(commands=[
        BotCommand(command="start", description="запустити бота"),
        BotCommand(command="profile", description="профіль користувача"),
        BotCommand(command="help", description="інструкція"),
        BotCommand(command="cancel", description="скасувати операцію"),
    ], scope=BotCommandScopeAllPrivateChats()))
