class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        kuchupuchu=[]
        for i in words:
            fhg=0
            for vfih in i:
                fhg+=weights[ord(vfih)-ord("a")]
            ytr= fhg%26
            kuchupuchu.append(chr(ord("z")-ytr))
        phre= "".join(kuchupuchu)
        return phre