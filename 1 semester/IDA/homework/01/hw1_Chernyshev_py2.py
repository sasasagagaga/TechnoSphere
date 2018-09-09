
import json
import csv
import random
import os


class SuperDict:
    def __init__(self, d):
        self.data = {}

        if type(d) is str:
            if d.endswith('.json'):
                with open(d) as json_file:
                    self.data = json.load(json_file)
            elif d.endswith('.csv'):
                with open(d) as csv_file:
                    reader = csv.reader(csv_file, delimiter=',')
                    for line in reader:
                        if len(line) != 2:
                            print 'Incorrect line in csv file'
                        else:
                            self.data[line[0]] = line[1]
        elif type(d) is dict:
            self.data = d.copy()
        else:
            print 'No available constructor'

    def __getitem__(self, item):
        return self.data[item]

    def clear(self):
        self.data.clear()

    def items(self):
        return self.data.items()
    
    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def iteritems(self):
        return self.data.iteritems()

    def iterkeys(self):
        return self.data.iterkeys()

    def itervalues(self):
        return self.data.itervalues()

    def __iter__(self):
        return self

    def __eq__(self, another):
        return self.data == another.data

    def __len__(self):
        return len(self.data)

    def get_random_key(self):
        return random.choice(self.data.keys())

    def get_max_key_len(self):
        return len(max(self.data.keys()))

    def __add__(self, another):
        d = self.data.copy()
        d.update(another)
        return SuperDict(d)

    def to_csv(self, path):
        with open(path, 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for key, value in self.data.iteritems():
                writer.writerow([key, value])

    def to_json(self, path):
        with open(path, 'w') as json_file:
            json.dump(self.data, json_file)

    def get_key_starts_from(self, s):
        return [x for x in self.data.iterkeys() if x.startswith(s)]


## There are some tests for SuperDict class
#if __name__ == '__main__':
#    if not os.path.exists('files'):
#        os.makedirs('files')
#
#    with open('files/in.csv', 'w') as csv_file:
#        writer = csv.writer(csv_file, delimiter=',')
#        writer.writerow(['a', 1])
#        writer.writerow(['b', 3])
#
#    d1 = {'q': 12, 'e': 3, 'a': -1, 'test1': 22, 'test2': 34}
#    with open('files/in.json', 'w') as json_file:
#        json.dump(d1, json_file)
#
#    # Checking constructors
#    sd1 = SuperDict('files/in.csv')
#    sd2 = SuperDict('files/in.json')
#    sd3 = SuperDict(d1)
#
#    # Checking __eq__
#    print 'sd2 == sd3: %d' % (sd2 == sd3)
#
#    # Checking __len__
#    print 'len(sd1): %d' % len(sd1)
#
#    # Checking keys
#    print 'sd2.keys(): {}'.format(sd2.keys())
#
#    # Checking get_random_key
#    print 'Random key from sd2: {}'.format(sd2.get_random_key())
#
#    # Checking __add__
#    sd4 = sd1 + sd2
#    print sd4.items()
#
#    # Checking save
#    sd1.to_csv('files/sd1.csv')
#    sd2.to_json('files/sd2.json')
#    sd3.to_csv('files/sd3.csv')
#    sd4.to_json('files/sd4.json')
#
#    # Checking get_key_starts_from
#    print sd3.get_key_starts_from('tes')



def file_tree(path, file_filter=None, level=-1, to=None):
    if os.path.isdir(path):
        if to is not None:
            print '  ' * level + to

        for to in os.listdir(path):
            file_tree(os.path.join(path, to), file_filter, level + 1, to)
    elif os.path.isfile(path) and (file_filter is None or os.path.basename(path).endswith(file_filter)):
        print '  ' * level + os.path.basename(path)


## There are some tests for file_tree function
#if __name__ == "__main__":
#    file_tree('./', '.py')
#
#    print '\n' + '-' * 32 + '\n'
#    file_tree('./', '.cpp')
#
#    print '\n' + '-' * 32 + '\n'
#    file_tree('hw1_Chernyshev_py2.py')
