from random import randint
from app.scripts.factory.errors import FactoryRequirementVersionError
from string import ascii_letters, digits


SYM_IDS = ascii_letters + digits
SYM_LEN = len(SYM_IDS) - 1


def check_requirements(req: list):
    for name, n_ver, h_ver in req:
        if n_ver != int(h_ver):
            raise FactoryRequirementVersionError(name, n_ver, h_ver)


def generate_id(len_id: int = 8) -> str:
    result = "".join([SYM_IDS[randint(0, SYM_LEN)] for i in range(len_id)])
    return result
