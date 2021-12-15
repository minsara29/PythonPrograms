import random
from tenacity import retry, stop_after_attempt, AsyncRetrying, RetryError

class NoisyChannel:


    async def send_message(self, message: str):

        try:
            async for attempt in AsyncRetrying(stop=stop_after_attempt(2)):
                with attempt:
                    print("Sending Message....")
                    error = random.choices([True, False], weights=[10, 1], k=1)


                    if error[0]:
                        raise IOError("Connection is broken")
        except RetryError as e:
            pass

def answer_with_message(msg: str):
    comm_interface = NoisyChannel()
    comm_interface.send_message(msg)
    return "message sent"

if __name__ == "__main__":
    msg = input("Enter your message: ")
    print(answer_with_message(msg))