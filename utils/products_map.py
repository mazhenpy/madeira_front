
def Mobile(phone_id):
    return {"TBM00000100A":"3",
            "TBM00000300A":"5",
            "TBM00000700A":"10",
            "TBM00001500A":"20",
            "TBM00005000A":"30",
            "TBM00010000A":"50",
            "TBM00020000A":"70",
            "TBM00030000A":"100",
            "TBM00040000A":"130",
            "TBM00060000A":"180",
            "TBM00110000A":"280",}.get(phone_id) or None

def Unicom(phone_id):
    return {"TBU00000200A":"3",
            "TBU00000500A":"6",
            "TBU00001000A":"10",
            "TBU00002000A":"15",
            "TBU00005000A":"30",
            "TBU00010000A":"100",}.get(phone_id) or None

def Telecom(phone_id):
    return {"TBC00000050B":"1",
            "TBC00000100B":"2",
            "TBC00000300B":"5",
            "TBC00000500B":"7",
            "TBC00001000B":"10",
            "TBC00002000B":"15",
            "TBC00005000B":"30",
            "TBC00010000B":"50",}.get(phone_id) or None