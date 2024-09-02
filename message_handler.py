from .database import SessionLocal
from .dispatcher_bot import dispatcher
from aiogram import filters, types
from .modeles import User 



@dispatcher.message(filters.CommandStart())
async def start_command(message: types.Message):
    #Функція яка починая сессію 
    session = SessionLocal()
    #Коли к боту звертаються вона починаеться
    user_telegram_id = message.from_user.id
    # Відсилати Id користувача
    user = session.query(User).filter_by(telegram_id= user_telegram_id).first()
    # Бот шукае юзера по Id щоб він розумів з ким працюе
    if user == None:
        # Юзер не знайдено
        new_user = User(
            user_name = message.from_user.first_name,
            telegram_id = user_telegram_id    
        )
        #Данні користувача які нам висилаються 
        session.add(new_user)
        # Додаемо нових користувачів
        session.commit()
        await message.answer(text= 'Ви успішно авторизовані')
    else:
        await message.answer(text= f'З поверненням до тестування {message.from_user.first_name}')
        # Відповіді на відправлені команди користувачем 
    
    session.close()
