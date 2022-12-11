import pyautogui as auto
from time import sleep
import pywhatkit


def send_message_inst():  # Отправляется сообщение в течение 15 сек по умолчанию
    mobile = input("Введите номер получателя: ")
    text_ = input("Введите текст сообщения: ")
    pywhatkit.sendwhatmsg_instantly(phone_no=mobile, )

    for i in range(20):
        auto.write("Wake up, Neo... \n")
        auto.write("The matrix has you...")
        auto.press('enter')
        sleep(0.4)


def main():
    send_message_inst()


if __name__ == "__main__":
    main()