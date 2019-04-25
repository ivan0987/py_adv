import logging
from server.settings import ENCODING

logger = logging.getLogger('client')

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

handler = logging.FileHandler('info.log', encoding=ENCODING)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
