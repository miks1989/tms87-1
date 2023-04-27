# class MyRange:
#
#     def __init__(self, start, stop, step):
#         self.start = start
#         self.stop = stop
#         self.step = step
#         self.value = self.start
#
#     def __next__(self):
#         if self.value < self.stop:
#             self.value += self.step
#             return self.value
#         else:
#             raise StopIteration
#
#
# r = MyRange(0, 3, 0.5)
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))


# V2
class MyRange:

    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start
        return self

    def __next__(self):
        if self.value < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


a = MyRange(0, 3, 0.5)
for i in a:
    print(i)
