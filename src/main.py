import os

import vk_api
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType

from src.ml import inference
from src.schemas import RequestModel
from src.utils import get_random_int32


def main() -> None:
    load_dotenv()
    login, password = os.getenv("LOGIN"), os.getenv("PASSWORD")
    vk_session = vk_api.VkApi(login, password, app_id=6287487)
    vk_session.auth()

    long_poll = VkLongPoll(vk_session)
    vk = vk_session.get_api()

    for event in long_poll.listen():
        if (
                event.type == VkEventType.MESSAGE_NEW
                and event.to_me
                and event.from_user
        ):
            if text := event.text:
                print(text)
                print(type(text))
                predict = inference(RequestModel(text=text))
                tags = '\n'.join(predict.tags)
                vk.messages.send(
                    user_id=event.user_id,
                    message=f"Теги:\n{tags}",
                    random_id=get_random_int32(),
                )


if __name__ == "__main__":
    main()
