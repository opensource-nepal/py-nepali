import re
from enum import Enum

_mobile_number_re = re.compile(r"^(?:\+977|977)?(?:-)?(?:98|97|96)\d{8}$")
_landline_number_re = re.compile(
    r"^(?:\+977|977)?(?:-)?(?:0)?(?:[01][1-9]|2[13-9]|[3-9]\d)\d{6,7}$"
)


class Operator(Enum):
    NEPAL_TELECOM = "Nepal Telecom"
    NCELL = "Ncell"
    SMART_CELL = "Smart Cell"
    UTL = "UTL"
    HELLO_MOBILE = "Hello Mobile"

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"<Operator: {self.value}>"


_OPERATOR_PREFIXES = {
    Operator.NEPAL_TELECOM: ["984", "985", "986", "974", "975", "976"],
    Operator.NCELL: ["980", "981", "982"],
    Operator.SMART_CELL: ["961", "962", "988"],
    Operator.UTL: ["972"],
    Operator.HELLO_MOBILE: ["963"],
}


class Area(Enum):
    # Koshi Province
    BHOJPUR = ("Bhojpur", "029")
    DHANKUTA = ("Dhankuta", "026")
    ILAM = ("Ilam", "027")
    JHAPA = ("Jhapa", "023")
    KHOTANG = ("Khotang", "036")
    MORANG = ("Morang", "021")
    OKHALDHUNGA = ("Okhaldhunga", "037")
    PANCHTHAR = ("Panchthar", "024")
    SANKHUWASABHA = ("Sankhuwasabha", "029")
    SOLUKHUMBU = ("Solukhumbu", "038")
    SUNSARI = ("Sunsari", "025")
    TAPLEJUNG = ("Taplejung", "024")
    TERHATHUM = ("Terhathum", "026")
    UDAYAPUR = ("Udayapur", "035")

    # Madhesh Province
    BARA = ("Bara", "053")
    DHANUSA = ("Dhanusa", "041")
    MAHOTTARI = ("Mahottari", "044")
    PARSA = ("Parsa", "051")
    RAUTAHAT = ("Rautahat", "055")
    SAPTARI = ("Saptari", "031")
    SARLAHI = ("Sarlahi", "046")
    SIRAHA = ("Siraha", "033")

    # Bagmati Province
    BHAKTAPUR = ("Bhaktapur", "01")
    CHITWAN = ("Chitwan", "056")
    DHADING = ("Dhading", "010")
    DOLAKHA = ("Dolakha", "049")
    KATHMANDU = ("Kathmandu", "01")
    KAVREPALANCHOK = ("Kavrepalanchok", "011")
    LALITPUR = ("Lalitpur", "01")
    MAKWANPUR = ("Makwanpur", "057")
    NUWAKOT = ("Nuwakot", "010")
    RAMECHHAP = ("Ramechhap", "048")
    RASUWA = ("Rasuwa", "010")
    SINDHUPALCHOK = ("Sindhupalchok", "011")
    SINDHULI = ("Sindhuli", "047")

    # Gandaki Province
    BAGLUNG = ("Baglung", "068")
    GORKHA = ("Gorkha", "064")
    KASKI = ("Kaski", "061")
    LAMJUNG = ("Lamjung", "066")
    MANANG = ("Manang", "066")
    MUSTANG = ("Mustang", "069")
    MYAGDI = ("Myagdi", "069")
    NAWALPUR = ("Nawalpur", "078")
    PARBAT = ("Parbat", "067")
    SYANGJA = ("Syangja", "063")
    TANAHU = ("Tanahu", "065")

    # Lumbini Provinc
    ARGHAKHANCHI = ("Arghakhanchi", "077")
    BANKE = ("Banke", "081")
    BARDIYA = ("Bardiya", "084")
    DANG = ("Dang", "082")
    GULMI = ("Gulmi", "079")
    KAPILVASTU = ("Kapilvastu", "076")
    PARASI = ("Parasi", "078")
    PALPA = ("Palpa", "075")
    PYUTHAN = ("Pyuthan", "086")
    ROLPA = ("Rolpa", "086")
    RUKUM_EAST = ("Rukum East", "088")
    RUPANDEHI = ("Rupandehi", "071")

    # Karnali Province
    DAILEKH = ("Dailekh", "089")
    DOLPA = ("Dolpa", "087")
    HUMLA = ("Humla", "019")
    JAJARKOT = ("Jajarkot", "089")
    JUMLA = ("Jumla", "087")
    KALIKOT = ("Kalikot", "087")
    MUGU = ("Mugu", "019")
    RUKUM_WEST = ("Rukum West", "088")
    SALYAN = ("Salyan", "088")
    SURKHET = ("Surkhet", "083")

    # Sudurpashchim Province
    ACHHAM = ("Achham", "097")
    BAITADI = ("Baitadi", "095")
    BAJHANG = ("Bajhang", "092")
    BAJURA = ("Bajura", "097")
    DADELDHURA = ("Dadeldhura", "096")
    DARCHULA = ("Darchula", "093")
    DOTI = ("Doti", "094")
    KAILALI = ("Kailali", "091")
    KANCHANPUR = ("Kanchanpur", "099")

    def __init__(self, area: str, area_code: str):
        self.area = area
        self.area_code = area_code

    def __str__(self):
        return f"{self.area}: {self.area_code}"

    @classmethod
    def get_by_area_code(cls, area_code: str = None) -> list[str]:
        if not area_code:
            return []
        results = [area.value[0] for area in cls if area.value[1] == area_code]
        return results


def is_mobile_number(number: str) -> bool:
    """
    Returns True is the input number is mobile number.

    >>> is_mobile = is_mobile_number(number)
    >>> if is_mobile:
    >>>     ...
    """
    try:
        return bool(_mobile_number_re.match(number))
    except Exception:
        return False


def is_landline_number(number: str) -> bool:
    """
    Returns True is the input number is landline number.

    >>> is_landline = is_landline_number(number)
    >>> if is_landline:
    >>>     ...
    """
    try:
        return bool(_landline_number_re.match(number))
    except Exception:
        return False


def is_valid(number: str) -> bool:
    return is_mobile_number(number) or is_landline_number(number)


def get_exact_number(number: str) -> str:
    # replacing start 977
    if number.startswith("977"):
        number = number.replace("977", "")
    # replacing +977 and all -
    return number.replace("+977", "").replace("-", "")


def parse(number: str):
    """
    Parse and returns the details of the phone number: `dict`.
    The return data may vary between mobile and landline numbers.
    If the number is invalid it returns `None`.

    If you want to make sure you get a valid response, please use
    `is_valid`, `is_mobile_number`, and `is_landline_number`.

    :return:
    {
        "type": "Mobile" | "Landline",
        "number": "XXXXXXX",
        ...
    }
    """
    if not number and not isinstance(number, str):
        return None

    number = number.replace("-", "")

    # checking if mobile number
    if is_mobile_number(number):
        return _parse_mobile_number(number)

    if is_landline_number(number):
        return _parse_landline_number(number)

    return None


def _get_operator(number: str) -> Operator | None:
    """
    Returns operator from the number.
    NOTE: The number should be 10digit mobile number.
    """
    starting_number = number[:3]
    for operator, prefixes in _OPERATOR_PREFIXES.items():
        if starting_number in prefixes:
            return operator
    return None


def _parse_mobile_number(number: str):
    """
    Parse and returns mobile number details.
    :return:
    {
        "type": "Mobile",
        "number": "98XXXXXXXX",
        "operator": <Operator>
    }
    """
    number = get_exact_number(number)
    operator = _get_operator(number)

    if not operator:
        return None

    detail = {
        "type": "Mobile",
        "number": number,
        "operator": operator,
    }
    return detail


def _get_area_code(number) -> str:
    """
    Returns area code of the number.
    NOTE: The number should be landline number without +977/977.
    """
    code = number[:3]

    # Kathmandu, Lalitpur, and Bhaktapur => 01
    if number.startswith("01") and code not in ["010", "011", "019"]:
        return "01"

    return code


def _parse_landline_number(number) -> dict:
    """
    Parse and returns landline number details.
    :return:
    {
        "type": "Landline",
        "number": "98XXXXXXXX",
        "area_code": <AreaCode>
        "area": list of areas/districts
    }
    """

    # adding zero
    if number[0] != "0":
        number = f"0{number}"

    number = get_exact_number(number)
    area_code = _get_area_code(number)
    area = _get_area(area_code)

    if not area:
        return None

    return {
        "type": "Landline",
        "number": number,
        "area_code": area_code,
        "area": area,
    }


def _get_area(area_code: str) -> list[str] | None:
    """
    Returns the details of the area code.
    """
    return Area.get_by_area_code(area_code)
