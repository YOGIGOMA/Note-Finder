import unittest
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import word_normalization as wn


class PeopleNameNormalizationUnitTests(unittest.TestCase):

    ##def setUp(self):

    ##def tearDown(self):

    ################################################################
    # 의사이름 패턴
    ################################################################
    def test_DoctorPattern1(self):
        result = wn.word_normalization("DR.홍길동")
        self.assertEqual(result, "의사이름")

    def test_DoctorPattern2(self):
        result = wn.word_normalization("dr. 길동")
        self.assertEqual(result, "의사이름")

    def test_DoctorPattern3(self):
        result = wn.word_normalization("dR. 길동")
        self.assertEqual(result, "의사이름")

    def test_DoctorPattern4(self):
        result = wn.word_normalization("R. 길동")
        self.assertEqual(result, "의사이름")   

    def test_DoctorPattern5(self):
        result = wn.word_normalization("r2둘리")
        self.assertEqual(result, "의사이름")  

    def test_DoctorPattern5(self):
        result = wn.word_normalization("r4. 도레미")
        self.assertEqual(result, "의사이름")        

    def test_DoctorPattern10(self):
        result = wn.word_normalization("의사 김아무개")
        self.assertEqual(result, "의사이름")        

    def test_ProfPattern1(self):
        result = wn.word_normalization("pf.홍길동")
        self.assertEqual(result, "의사이름")

    def test_ProfPattern2(self):
        result = wn.word_normalization("prof. james")
        self.assertEqual(result, "의사이름")

    def test_ProfPattern3(self):
        result = wn.word_normalization("prof. 홍길동")
        self.assertEqual(result, "의사이름")

    def test_ProfPattern4(self):
        result = wn.word_normalization("prof. 홍길")
        self.assertEqual(result, "의사이름")

    def test_ProfPattern5(self):
        result = wn.word_normalization("prof. 홍")
        self.assertEqual(result, "의사이름")    

    def test_ProfPattern6(self):
        result = wn.word_normalization("PROF 홍")
        self.assertEqual(result, "의사이름")      

    def test_ProfPattern7(self):
        result = wn.word_normalization("prof고길동")
        self.assertEqual(result, "의사이름")     

    def test_ProfPattern8(self):
        result = wn.word_normalization("pro 홍말자")
        self.assertEqual(result, "의사이름")               
    
if __name__ == '__main__':
    unittest.main()