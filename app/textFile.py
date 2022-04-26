from .different import Different

class TextFile:

    @staticmethod
    def compare(pathname1: str, pathname2: str):
        error_data = Different()

        text1 = open(pathname1, "r").readlines()
        text2 = open(pathname2, "r").readlines()
        
        error_data.diff_length_lines(len(text1), len(text2))

        lines_more = abs(len(text1)-len(text2))

        maxx = []
        minn = []

        if text1 > text2:
            maxx = text1
            minn = text2
        else:
            maxx = text2
            minn = text1

        diffs = []

        ii = 0
        tam = max(len(maxx), len(minn))-1
        
        while( ii< tam ):
            if(maxx[ii] != minn[ii]):
                        
                    error_data.add(maxx[ii], minn[ii])
                    if lines_more > 0:
                        maxx.remove(maxx[ii])
                        lines_more-=1

            ii+=1

        while( ii< tam ):
            if(maxx[ii] != minn[ii]):
            ii+=1
            
        return error_data
