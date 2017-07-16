import unittest
import io

from seqfiletk.sample import sample, get_number_sequences


class TestSample(unittest.TestCase):
    def setUp(self):
        self.input_str=""">test0
aaaaaaaaaaaaaaaa
>test1
cccccccccccccccc
>test2
dddddddddddddddd
>test3
tttttttttttttttt
        """

        self.input=io.StringIO(self.input_str)
        self.output=io.StringIO()

    def test_get_number_sequences(self):
        c = get_number_sequences(self.input, 'fasta')
        self.assertEqual(4, c)

    def test_sample(self):
        sample(self.input, self.output, number_sequences=2, seed=0)
        sampled_file_str = self.output.getvalue()

        ans_file_str = """>test2
dddddddddddddddd
>test3
tttttttttttttttt
"""
        self.assertEqual(ans_file_str, sampled_file_str)

if __name__ == '__main__':
    unittest.main()
