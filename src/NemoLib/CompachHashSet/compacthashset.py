
#import java.io.Serializable
#import java.lang.IllegalStateException
#import java.util.NoSuchElementException

class CompactHashSet(Serializable):#check on this, not 100% sure
    DEFAULT_CAPACITY = 29
    STARTING_BUCKET_SIZE = 4
    NULL_ELEMENT = -1
    table = []
    size = int()

    @overloaded
    def __init__(self):
        super(CompactHashSet, self).__init__()
        self.__init__(self.DEFAULT_CAPACITY)

    @__init__.register(object, int)
    def __init___0(self, tableSize):
        super(CompactHashSet, self).__init__()
        if tableSize < 0:
            raise IllegalArgumentException("Argument out of range (must be non-negative).")
        self.size = 0
        self.table = [None]*(1 if tableSize == 0 else tableSize)
        i = 0
        while i < table.length:
            self.table[i] = None
            i += 1

    def copy(self):
        copy = CompactHashSet(self.table.length)
        iter = iterator()
        while iter.hasNext():
            copy.add(iter.next())
        return copy

    def size(self):
        return self.size

    def isEmpty(self):
        return len(self) == 0

    def add(self, element):
        if element < 0:
            raise IllegalArgumentException("Argument out of range (must be non-negative).")
        bucket = hash(element) % table.length
        if self.table[bucket] == None:
            #  create a bucket if it does not exist
            self.table[bucket] = [None]*STARTING_BUCKET_SIZE
            #  create a bucket if it does not exist
            while i < table[bucket].length:
                #  create a bucket if it does not exist
                self.table[bucket][i] = NULL_ELEMENT
                i += 1
            #  addSubgraph element to bucket
            self.table[bucket][0] = element
            self.size += 1
            return
        #  create a bucket if it does not exist
        #  addSubgraph element to bucket
        #  check bucket if element already exists
        i = 0
        while i < table[bucket].length:
            #  create a bucket if it does not exist
            #  addSubgraph element to bucket
            #  check bucket if element already exists
            if self.table[bucket][i] == element:
                return
            i += 1
        #  create a bucket if it does not exist
        #  addSubgraph element to bucket
        #  check bucket if element already exists
        #  try to addSubgraph element if there is space
        i = 0
        while i < table[bucket].length:
            #  create a bucket if it does not exist
            #  addSubgraph element to bucket
            #  check bucket if element already exists
            #  try to addSubgraph element if there is space
            if self.table[bucket][i] == NULL_ELEMENT:
                self.table[bucket][i] = element
                self.size += 1
                return
            i += 1
        previousLength = self.table[bucket].length
        grow(bucket)
        self.table[bucket][previousLength] = element
        self.size += 1

    def contains(self, element):
        if element < 0:
            return False
        bucket = hash(element) % table.length
        if self.table[bucket] == None:
            return False
        else:
            #  create a bucket if it does not exist
            #  addSubgraph element to bucket
            #  check bucket if element already exists
            #  try to addSubgraph element if there is space
            #  otherwise grow the bucket and addSubgraph to first new position
            while index < table[bucket].length:
                #  create a bucket if it does not exist
                #  addSubgraph element to bucket
                #  check bucket if element already exists
                #  try to addSubgraph element if there is space
                #  otherwise grow the bucket and addSubgraph to first new position
                if self.table[bucket][index] == element:
                    return True
                index += 1
            return False

    def remove(self, element):
        if element < 0:
            return False
        bucket = hash(element) % table.length
        if self.table[bucket] == None:
            return False
        else:
            #  create a bucket if it does not exist
            #  addSubgraph element to bucket
            #  check bucket if element already exists
            #  try to addSubgraph element if there is space
            #  otherwise grow the bucket and addSubgraph to first new position
            while index < table[bucket].length:
                #  create a bucket if it does not exist
                #  addSubgraph element to bucket
                #  check bucket if element already exists
                #  try to addSubgraph element if there is space
                #  otherwise grow the bucket and addSubgraph to first new position
                if self.table[bucket][index] == element:
                    self.table[bucket][index] = NULL_ELEMENT
                    self.size -= 1
                    return True
                index += 1
            return False

    def grow(self, bucketIndex):
        newBucket = [None]*table[bucketIndex].length * 2
        index = 0
        #  create a bucket if it does not exist
        #  addSubgraph element to bucket
        #  check bucket if element already exists
        #  try to addSubgraph element if there is space
        #  otherwise grow the bucket and addSubgraph to first new position
        #  increase the getSize of the bucket at the given index
        #  double the bucket getSize
        while index < table[bucketIndex].length:
            #  create a bucket if it does not exist
            #  addSubgraph element to bucket
            #  check bucket if element already exists
            #  try to addSubgraph element if there is space
            #  otherwise grow the bucket and addSubgraph to first new position
            #  increase the getSize of the bucket at the given index
            #  double the bucket getSize
            newBucket[index] = table[bucketIndex][index]
            index += 1
        #  create a bucket if it does not exist
        #  addSubgraph element to bucket
        #  check bucket if element already exists
        #  try to addSubgraph element if there is space
        #  otherwise grow the bucket and addSubgraph to first new position
        #  increase the getSize of the bucket at the given index
        #  double the bucket getSize
        while index < newBucket.length:
            #  create a bucket if it does not exist
            #  addSubgraph element to bucket
            #  check bucket if element already exists
            #  try to addSubgraph element if there is space
            #  otherwise grow the bucket and addSubgraph to first new position
            #  increase the getSize of the bucket at the given index
            #  double the bucket getSize
            newBucket[index] = NULL_ELEMENT
            index += 1
        self.table[bucketIndex] = newBucket


    def hash(self, element):
        return element

    def iterator(self):
        return Iter(self)

    #toString
    def __str__(self):
        s = "["
        iter = self.iterator()
        while iter.hasNext():
            s = s + iter.next() + ", "
        s = s + "]"
        return s

    class Iter(object):
        set = CompactHashSet()
        row = int()
        col = int()
        prevCol = int()
        prevRow = int()

        def __init__(self, set):
            self.set = set
            self.row = 0
            self.col = -1
            self.prevRow = row
            self.prevCol = col
            moveToNext()

        def moveToNext(self):
            self.col += 1
            while self.row < set.table.length:
                if self.set.table[self.row] != None and self.col < set.table[row].length:
                    #  create a bucket if it does not exist
                    #  addSubgraph element to bucket
                    #  check bucket if element already exists
                    #  try to addSubgraph element if there is space
                    #  otherwise grow the bucket and addSubgraph to first new position
                    #  increase the getSize of the bucket at the given index
                    #  double the bucket getSize
                    while self.col < set.table[row].length:
                        #  create a bucket if it does not exist
                        #  addSubgraph element to bucket
                        #  check bucket if element already exists
                        #  try to addSubgraph element if there is space
                        #  otherwise grow the bucket and addSubgraph to first new position
                        #  increase the getSize of the bucket at the given index
                        #  double the bucket getSize
                        if self.set.table[self.row][self.col] != NULL_ELEMENT:
                            return
                        self.col += 1
                self.col = 0
                self.row += 1
                
        def hasNext(self):
            return self.row < set.table.length
        
        def next(self):
            if not self.hasNext():
                raise NoSuchElementException()
            self.prevRow = row
            self.prevCol = col
            self.moveToNext()
            return self.set.table[self.prevRow][self.prevCol]

        def remove(self):
            if self.prevCol == -1 or self.set.table[self.prevRow][self.prevCol] == NULL_ELEMENT:
                raise IllegalStateException()
            self.set.table[self.prevRow][self.prevCol] = NULL_ELEMENT
            self.set.size -= 1





            
        
