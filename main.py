import requests as rq
import logging

logger_200 = logging.getLogger('success_responses')
logger_200.setLevel(logging.INFO)
main_fh_200 = logging.FileHandler("success_responses.log", 'w', 'utf-8')
formatter_200 = logging.Formatter('%(message)s')
main_fh_200.setFormatter(formatter_200)
logger_200.addHandler(main_fh_200)

logger_not_200 = logging.getLogger('blocked_responses')
logger_not_200.setLevel(logging.WARNING)
main_fh_not_200 = logging.FileHandler("blocked_responses.log", 'w', 'utf-8')
formatter_not_200 = logging.Formatter('%(message)s')
main_fh_not_200.setFormatter(formatter_not_200)
logger_not_200.addHandler(main_fh_not_200)

logger_no_response = logging.getLogger('bad_responses')
logger_no_response.setLevel(logging.ERROR)
main_fh_no_response = logging.FileHandler("bad_responses.log", 'w', 'utf-8')
formatter_no_response = logging.Formatter('%(message)s')
main_fh_no_response.setFormatter(formatter_no_response)
logger_no_response.addHandler(main_fh_no_response)


sites = ['https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']


def print_primes():
    for site in sites:
        try:
            response_200 = rq.get(site, timeout=1)
            if response_200.status_code == 200:
                logger_200.info(f'INFO: {site}, response - {response_200.status_code}')
        except BaseException:
            print('logger_200')

        try:
            response_not_200 = rq.get(site, timeout=1)
            if response_not_200.status_code != 200:
                logger_not_200.warning(f'WARNING: {site}, response - {response_not_200.status_code}')
        except BaseException:
            print('logger_not_200')

        try:
            response_no_response = rq.get(site, timeout=1)
            if response_no_response.status_code == None:
                logger_no_response.error(f'ERROR: {site}, {response_no_response.status_code}')
        except BaseException:
            print(logger_no_response.error(f'ERROR: {site}, NO CONNECTION'))


if __name__ == '__main__':
    print_primes()
