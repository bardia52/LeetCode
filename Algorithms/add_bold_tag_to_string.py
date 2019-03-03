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