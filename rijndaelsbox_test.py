import rijndaelsbox

# GNU General Public License Version 3

def test_multiplicativeinverse():
    assert rijndaelsbox.multiplicativeinverse(2) == bytes([0, 1])
    
    for number in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        mi = rijndaelsbox.multiplicativeinverse(number)
        assert mi[0] == 0
        for i in range(1, number):
            assert (i * mi[i]) % number == 1

def test_euclideanboth():
    for (a, b, r) in [(0, 0, 0), (1, 0, 1), (3, 5, 1), (54, 24, 6), (62, 36, 2), (42, 56, 14), (68, 92, 4), (280, 1100, 20)]:
        assert rijndaelsbox.euclideanrec(a, b) == r
        assert rijndaelsbox.euclideanrec(b, a) == r
        assert rijndaelsbox.euclideanloop(a, b) == r
        assert rijndaelsbox.euclideanloop(b, a) == r
