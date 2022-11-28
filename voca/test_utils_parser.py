from django.test import TestCase
from voca import utils_parser


class Test(TestCase):

    def test_get_dataset_filepath(self):
        ret = utils_parser.get_dataset_filepath()

        self.assertNotEqual(len(ret), 0)

    def test_parse_parsed_data_english(self):
        full_filepath = str()

        for dataset in utils_parser.get_dataset_filepath():
            if dataset.find('english') == -1:
                continue

            full_filepath = dataset
            break

        ret = utils_parser.parse_csv_data(
            full_filepath=full_filepath,
        )

        self.assertNotEqual(len(ret), 0)

    def test_parse_parsed_data_japanese(self):
        full_filepath = str()

        for dataset_filename in utils_parser.get_dataset_filepath():
            if dataset_filename.find('japanese') == -1:
                continue

            full_filepath = dataset_filename
            break

        ret = utils_parser.parse_csv_data(
            full_filepath=full_filepath,
        )

        self.assertNotEqual(len(ret), 0)

    def test_parse_parsed_data_chinese(self):
        full_filepath = str()

        for dataset in utils_parser.get_dataset_filepath():
            if dataset.find('chinese') == -1:
                continue

            if dataset.find('classic') != -1:
                continue

            full_filepath = dataset
            break

        ret = utils_parser.parse_csv_data(
            full_filepath=full_filepath,
        )

        self.assertNotEqual(len(ret), 0)

    def test_parse_parsed_data_classic_chinese(self):
        full_filepath = str()

        for dataset in utils_parser.get_dataset_filepath():
            if dataset.find('classic_chinese') == -1:
                continue

            full_filepath = dataset
            break

        ret = utils_parser.parse_csv_data(
            full_filepath=full_filepath,
        )

        self.assertNotEqual(len(ret), 0)

    def test_parse_string_data(self):
        data = '''
invulnerable,불사신의|공격할 수 없는|반박할 수 없는
introspect,내성하다|자기 반성하다|내관하다
tug of war,줄다리기|세력 싸움|쟁탈전
stay in touch,"계속 연락하고 지내다, 소식을 주고받다"
'''
        ret = utils_parser.parse_string_data(
            raw_input=data,
        )

        self.assertNotEqual(len(ret), 0)

    def test_parse_word_data(self):
        ret = utils_parser.parse_word_data(
            raw_word='finish',
        )
        self.assertTrue(ret)

        ret = utils_parser.parse_word_data(
            raw_word='finish a job',
        )
        self.assertTrue(ret)

        ret = utils_parser.parse_word_data(
            raw_word='finish,complete',
        )
        self.assertFalse(ret)

        ret = utils_parser.parse_word_data(
            raw_word='finish|complete',
        )
        self.assertFalse(ret)

    def test_parse_meaning_data(self):
        ret = utils_parser.parse_meaning_data(
            raw_meanings='fish',
        )
        self.assertEqual(len(ret), 0)

        ret = utils_parser.parse_meaning_data(
            raw_meanings='물고기',
        )
        self.assertEqual(len(ret), 1)

        ret = utils_parser.parse_meaning_data(
            raw_meanings='물고기를 잡다',
        )
        self.assertEqual(len(ret), 1)
        self.assertEqual(len(ret[0]), 7)

        ret = utils_parser.parse_meaning_data(
            raw_meanings='…에 대한 걱정. ',
        )
        self.assertEqual(len(ret), 1)
        self.assertEqual(len(ret[0]), 8)

        ret = utils_parser.parse_meaning_data(
            raw_meanings='막~하려하다;',
        )
        self.assertEqual(len(ret), 1)
        self.assertEqual(len(ret[0]), 6)

        ret = utils_parser.parse_meaning_data(
            raw_meanings=' 나는[부정문]~할 생각은 없다',
        )
        self.assertEqual(len(ret), 1)
        self.assertEqual(len(ret[0]), 11)

        ret = utils_parser.parse_meaning_data(
            raw_meanings=' 악수하다[with ‥] ',
        )
        self.assertEqual(len(ret), 1)
        self.assertEqual(len(ret[0]), 4)

        ret = utils_parser.parse_meaning_data(
            raw_meanings='~에 대한 걱정. ',
        )
        self.assertEqual(len(ret), 1)
        self.assertEqual(len(ret[0]), 8)

        ret = utils_parser.parse_meaning_data(
            raw_meanings='우리…하지 않겠어요? ',
        )
        self.assertEqual(len(ret), 1)
        self.assertEqual(len(ret[0]), 11)

        ret = utils_parser.parse_meaning_data(
            raw_meanings='물고기|어류',
        )
        self.assertEqual(len(ret), 2)

        ret = utils_parser.parse_meaning_data(
            raw_meanings='"결심하다, 결단을 내리다 "',
        )
        self.assertEqual(len(ret), 2)

        ret = utils_parser.parse_meaning_data(
            raw_meanings='물고기.어류',
        )
        self.assertEqual(len(ret), 2)

        ret = utils_parser.parse_meaning_data(
            raw_meanings='물고기;어류',
        )
        self.assertEqual(len(ret), 2)

        ret = utils_parser.parse_meaning_data(
            raw_meanings='물고기|어류|',
        )
        self.assertEqual(len(ret), 2)

        ret = utils_parser.parse_meaning_data(
            raw_meanings='"물고기|어류,생선.물고기를 잡다;어업의"',
        )
        self.assertEqual(len(ret), 5)
