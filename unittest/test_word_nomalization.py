import unittest
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import word_normalization as wn


class WordNormalizationUnitTests(unittest.TestCase):

    ##def setUp(self):

    ##def tearDown(self):

    ################################################################
    # 의사이름 패턴
    ################################################################
    

    ################################################################
    # 날짜 패턴 시험
    # COMMENT: 날짜패턴에서 종료문자가 빈칸을 허용하는것과 아닌것을 패턴으로 구분한 이유는?
    ################################################################
    def test_DatePattern1(self):
        result = wn.word_normalization("2022.1.25.")
        self.assertEqual(result, "날짜")

    def test_DatePattern2(self):
        result = wn.word_normalization("2022/01/25 ")
        self.assertEqual(result, "날짜")

    def test_DatePattern3(self):
        result = wn.word_normalization("2022-73-10 ")
        self.assertEqual(result, "날짜")      

    def test_DatePattern4(self):
        result = wn.word_normalization("01/01/1044")
        self.assertEqual(result, "날짜")          

    def test_DatePattern5(self):
        result = wn.word_normalization("9/1/1044")
        self.assertEqual(result, "날짜") 

    ################################################################
    # 시간 패턴 시험
    ################################################################
    def test_TimePattern1(self):
        result = wn.word_normalization("12:12")
        self.assertEqual(result, "시간")  

    def test_TimePattern2(self):
        result = wn.word_normalization("1:5")
        self.assertEqual(result, "시간")                 

    def test_TimePattern3(self):
        result = wn.word_normalization("2am")
        self.assertEqual(result, "시간")   

    def test_TimePattern4(self):
        result = wn.word_normalization("12AM")
        self.assertEqual(result, "시간") 

    def test_TimePattern5(self):
        result = wn.word_normalization("7pM")
        self.assertEqual(result, "시간")                          
    
if __name__ == '__main__':
    unittest.main()