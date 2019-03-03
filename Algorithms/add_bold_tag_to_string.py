class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        inx_old = 0
        len_old = 0
        for d in dict:
            inx = s.find(d)
            l = len(d)
            if inx != -1:
                s1 = s[0:inx]
                if inx <= inx_old+len_old:
                    #merge
                    
                else:
                    #normal
                    s = s[0:inx]+'<b>'+d+'</b>'+s[inx+len(d):]
                print s
            inx_old = inx
            len_old = l
            print inx
        return s
"qrzjsorbkmyzzzvoqxefvxkcwtpkhzbakuufbpgdkykmojwuennrjeciqvvacpzrrczfhxnsmginzwinzihpomxtmweyyzzmgcoiupjnidphvzlnxtcogufozlenjfvokztghwckzyvmktduqkizixzxpanjwrdeudjyftxksjgdklwxrhmudhrtemuvelykqaafzlqmennttkighcdxfozdcoqkyshhajipnsdrljrnlwmyjuwxsebpqm"
["qr","zj","so","rb","km","yz","zz","vo","qx","ef","vx","kc","wt","pk"]

"qrzjsorbkmyzzzvoqxefvxkcwtpkhzbakuufbpgdkykmojwuennrjeciqvvacpzrrczfhxnsmgi"
["qr","zj","so","rb","km","yz","zz","vo","qx","ef","vx","kc","wt","pk"]

"qrzjsorbkmyzzzvo"
["qr","zj","so","rb","km","yz","zz","vo"]

class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        arr = [False] * len(s)
        inx = l = 0
        for d in dict:
            while True:
                temp = s[inx:]
                inx1 = s[inx:].find(d)
                l = len(d)
                if inx1 != -1:
                    arr[inx1+inx:inx1+inx+l] = [True]*l
                    print "case1 ", d, l, "temp=", temp, "inx=", inx, inx1
                    inx += inx1+l
                    #print "case1+", d, l, "temp=", temp, inx, inx1
                else:
                    print "case2 ", d, l, "temp=", temp, "inx=", inx, inx1
                    break
            #print arr
        print arr, len(arr)
        bias = 0
        if arr[0]:
            #print "case 1"
            s = '<b>' + s
            #print s
            bias += 3
        for ax in range(1,len(arr)):
            if arr[ax] and not arr[ax-1]:
                #print "case 2"
                s = s[0:bias+ax] + '<b>' + s[bias+ax:]
                #print s
                bias += 3
            if not arr[ax] and arr[ax-1]:
                #print "case 3"
                s = s[0:bias+ax] + '</b>' + s[bias+ax:]
                #print s
                bias += 4
        if arr[len(arr)-1]:
            #print "case 4"
            s = s + '</b>'
            #print s
        return s