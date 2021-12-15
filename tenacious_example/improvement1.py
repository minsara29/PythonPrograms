import random
from tenacity import retry, stop_after_attempt

class NoisyChannel:

    # @retry
    @retry(stop=stop_after_attempt(4))
    # @retry(stop=stop_after_delay(10))
    # @retry(stop=stop_after_delay(10) | stop_after_attempt(4)))
    # @retry(wait=wait_exponential(multiplier=1, min=4, max=10))
    # @retry(retry=retry_if_exception_type(IOError))
    # @retry(retry=(retry_if_result(None)))
    def send_message(self, message: str):
        print("Sending Message....")
        error = random.choices([True, False], weights=[10, 1], k=1)
        print(error)

        if error[0]:
            raise IOError("Connection is broken")


def answer_with_message(msg: str):
    comm_interface = NoisyChannel()
    comm_interface.send_message(msg)
    return "message sent"

if __name__ == "__main__":
    msg = input("Enter your message: ")
    print(answer_with_message(msg))