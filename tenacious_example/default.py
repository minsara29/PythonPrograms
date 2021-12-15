import random

class NoisyChannel:

    def send_message(self, message: str):
        if random.choice([True, False]):
            raise Exception("Connection is broken")


def answer_with_message(msg: str):
    comm_interface = NoisyChannel()
    comm_interface.send_message(msg)
    return "message sent"

if __name__ == "__main__":
    msg = input("Enter your message: ")
    print(answer_with_message(msg))