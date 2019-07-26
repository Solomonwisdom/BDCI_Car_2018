import codecs
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
f_example = codecs.open(BASE_DIR + "test_public_2.csv", encoding='utf-8').readlines()
fw = codecs.open(BASE_DIR + "submit2.csv", 'w', encoding='utf-8')
f_aspect = codecs.open(BASE_DIR + "test_predict_aspect_ensemble.txt", encoding='utf-8').readlines()
f_polarity = codecs.open(BASE_DIR + "test_predict_polarity_ensemble.txt", encoding='utf-8').readlines()

fw.write("content_id,subject,sentiment_value,sentiment_word\r\n")

f_ids = f_example[1:]
assert len(f_ids) == len(f_aspect)

count_a = 0
for i, (aspects, id) in enumerate(zip(f_aspect, f_ids)):
    aspect = aspects.strip('\r\n').split('|')
    content_id = id.split(',')[0]
    for asp in aspect:
        ap = f_polarity[count_a].strip('\n')
        a, p = ap.split(',')
        assert a == asp
        fw.write(content_id+','+asp+','+p+','+'\n')
        count_a += 1

