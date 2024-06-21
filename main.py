import csv

from mrjob.job import MRJob
from mrjob.step import MRStep
from mr3px.csvprotocol import CsvProtocol


class TypeCounter(MRJob):

    def mapper(self, key, value):
        value_col = value.split(',')
        yield value_col[0], 1

    def reducer(self, key, values):
        yield None, (sum(values), key)

    def reducer_sorter(self, key, values):
        for count, key in sorted(values):
            yield count, key

    def steps(self):
        return [
            MRStep(
                mapper=self.mapper,
                reducer=self.reducer
            ),
            MRStep(
                reducer=self.reducer_sorter
            )
        ]


if __name__ == '__main__':
    TypeCounter.run()
    OUTPUT_PROTOCOL = CsvProtocol
# 1) call script using 'python main.py mbti.csv' in the command line from the project folder
# 2) call script using 'python main.py < "mbti.csv" > output.csv' in the command line
# from the project folder to export the outcome into a csv file
