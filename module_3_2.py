def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if '@' not in recipient or ('.com' not in recipient and '.ru' not in recipient and '.net' not in recipient):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    if sender == recipient:
        print(f'Нельзя отправить письмо самому себе!')
        return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')