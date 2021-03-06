from fake_useragent import UserAgent
import random


def get_user_agent(logger):
    THRESH = 0.5

    try:
        ua = UserAgent()
        if random.random() > THRESH:
            random_user_agent = ua.chrome
        else:
            random_user_agent = ua.firefox

    except FakeUserAgentError as error:
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1"]
        random_user_agent = random.choice(user_agents)
        logger.error('User agent did not work. Generating headers from pre-defined set. error: {}'.format(error))

    return random_user_agent
