import pywhatkit


def send_message():  # Отправляется сообщение в течение заданного времени
    mobile = input("Введите номер получателя: ")
    text_ = input("Введите текст сообщения: ")
    hours_ = int(input("Введите часы: "))
    min_ = int(input("Введите минуты: "))
    pywhatkit.sendwhatmsg(phone_no=mobile, message=text_, time_hour=hours_, time_min=min_)


def main():
    send_message()


if __name__ == "__main__":
    main()
