def totalScore(s1,s2,s3):
    return s1+s2+s3
    
def averageScore(s1,s2,s3):
    return (s1+s2+s3)/3

def passfail(s1,s2,s3):
    avg=(s1+s2+s3)/3
    if avg >=60 and s1 >40 and s2>40 and s3 >=40:
        return 'Pass'
    else:
        return 'Fail'
