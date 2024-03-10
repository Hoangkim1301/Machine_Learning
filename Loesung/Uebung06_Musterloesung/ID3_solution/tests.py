import unittest
import pandas as pd


class TestID3(unittest.TestCase):
    data = {
        'col_1': ['3', '3', '3', '1'],
        'col_2': ['a', 'b', 'b', 'a'],
        'target_class': ['yes', 'yes', 'no', 'no']
    }

    df = pd.DataFrame.from_dict(data)
    df.to_csv("test.csv")

    def test_entropy(self):
        from ID3.ID3_solution import entropy
        self.assertEqual(1.0, entropy(self.data['target_class']))
        self.assertEqual(0.0, entropy(self.data['target_class'][:2]))
        self.assertAlmostEqual(0.918295834, entropy(self.data['target_class'][:3]))

    def test_get_split_attr(self):
        from ID3.ID3_solution import ID3
        id3 = ID3("test.csv")
        self.assertEqual("col_1", id3.get_split_attr(self.df, ["col_1", "col_2"]))

    def test_info_gain(self):
        from ID3.ID3_solution import ID3, entropy
        id3 = ID3("test.csv")
        info_gain = entropy(self.data['target_class']) - (0.5 * entropy([self.data['target_class'][0],
                                                                         self.data['target_class'][3]]) +
                                                          0.5 * entropy([self.data['target_class'][1],
                                                                         self.data['target_class'][2]]))
        self.assertEqual(info_gain, id3.info_gain(self.df, "col_2"))


if __name__ == '__main__':
    unittest.main()
