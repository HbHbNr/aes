import rijndaelsbox

# GNU General Public License Version 3

def test_multiplicativeinverse():
    assert rijndaelsbox.multiplicativeinverse(2) == bytes([0, 1])
    
    for number in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        mi = rijndaelsbox.multiplicativeinverse(number)
        assert mi[0] == 0
        for i in range(1, number):
            assert (i * mi[i]) % number == 1
