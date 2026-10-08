from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton, 
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)


reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Python")], [KeyboardButton(text="Java")], [KeyboardButton(text="JavaScript")]
])


inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Python", url="https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://docs.python.org/&ved=2ahUKEwiXxYi_8qqXAxVJVfEDHQ6nGX8QFnoECBAQAQ&usg=AOvVaw0eRfv-QpH-JIna_jepcnW7")],
    [InlineKeyboardButton(text="Java", url="https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://translate.google.com/translate%3Fu%3Dhttps://docs.oracle.com/en/java/%26hl%3Dru%26sl%3Den%26tl%3Dru%26client%3Dsearch&ved=2ahUKEwjziKbS8qqXAxUNXvEDHTRhGgYQ7gF6BAgPEAo&usg=AOvVaw2G9vnsyRx0mvadBBNarWwD")],
    [InlineKeyboardButton(text="JavaScript", url="https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://developer.mozilla.org/ru/docs")]
])