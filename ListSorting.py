class Sort_The_List :
    def Sort(self, list, comparedIndex, length):
        return self.MergeSort(list, 0, length - 1, comparedIndex)

    def MergeSort(self, list, firstIndex, lastIndex, comparedIndex):
        if(firstIndex < lastIndex):
            middleIndex = (firstIndex + lastIndex) // 2
            list = self.MergeSort(list, firstIndex, middleIndex, comparedIndex)
            list = self.MergeSort(list, middleIndex + 1, lastIndex, comparedIndex)
            list = self.Merge(list, firstIndex, middleIndex, lastIndex, comparedIndex)

        return list

    def Merge(self, list, firstIndex, middleIndex, lastIndex, comparedIndex):
        result = []
        for isi in list:
            result.append(isi)
            
        p = firstIndex
        q = middleIndex + 1
        r = firstIndex
        while(p <= middleIndex) and (q <= lastIndex):
            if(list[p][comparedIndex] <= list[q][comparedIndex]):
                result[r] = list[p]
                p += 1
            else:
                result[r] = list[q]
                q += 1

            r += 1

        while(p <= middleIndex):
            result[r] = list[p]
            p += 1
            r += 1

        while(q <= lastIndex):
            result[r] = list[q]
            q += 1
            r += 1

        return result
