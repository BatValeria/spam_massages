import pywhatkit


def send_message_inst():  # Отправляется сообщение в течение 15 сек по умолчанию
    mobile = input("Введите номер получателя: ")
    text_ = input("Введите текст сообщения: ")
    pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=text_)


def main():
    send_message_inst()


if __name__ == "__main__":
    main()
