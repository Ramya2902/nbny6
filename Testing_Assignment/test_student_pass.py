from test_pass import existing, Studentid

def test():
    passorfail = 1
    digits = len(str(existing))

    if (digits != 5):
        passorfail = 0
        assert passorfail == 1

    if existing in Studentid:
        numberinList = 1
    else:
        numberinList = 0
    
    assert numberinList == 1
