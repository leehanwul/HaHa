#-*-coding:utf-8-*-
import re

Exercise = ['squat','deadlift',"bench press"]

testString = [u'squat'.encode('unicode_escape'), u'deadlift'.encode('unicode_escape'),u'스쿼트'.encode('unicode_escape'),u'데드리프트'.encode('unicode_escape'),
		u"벤치 프레스".encode('unicode_escape'), u"밴치 프레스 ".encode('unicode_escape'), u"벤치".encode('unicode_escape'), u"bench_press".encode('unicode_escape')]


# 스쿼트
squat = (""
    + "squat|"
    + u"스쿼트".encode('unicode_escape') + "|"
    + u"스퀏".encode('unicode_escape')+ "|"
    + u"스쾉".encode('unicode_escape')
    )
squat = squat.replace('\\', '\\\\')

# 데드리프트    
deadlift = (""
    + "deadlift|"
    + u"데드리프트".encode('unicode_escape') + "|"
    + u"대드리프트".encode('unicode_escape') +"|"
    + u"데드".encode('unicode_escape') + "|"
    + u"대드".encode('unicode_escape')
    )
deadlift = deadlift.replace('\\','\\\\')
print "deadlift  : ", deadlift

# 벤치프레스
element = []
element.append("\\"+u"벤".encode('unicode_escape'))	# '벤'	0
element.append("\\" + u"밴".encode('unicode_escape'))	# '밴'	1
element.append("\\" + u"치".encode('unicode_escape'))	# '치'	2
element.append("\\" + u"프".encode('unicode_escape'))	# '프'	3
element.append("\\" + u"레".encode('unicode_escape'))	# '레'	4
element.append("\\" + u"래".encode('unicode_escape'))	# '래'	5
element.append("\\" + u"스".encode('unicode_escape'))	# '스'	6
bench_press = (""
	+ "bench\s*_?press|"
	+ "[" + element[0]  + "|" +  element[1] + "]"+"+" + element[2]  + "\s*" +"(" + element[3] + "[" + element[4] + "|" +  element[5]  +  "]"+"+" + element[6] +")?"
	#[벤|밴]+치\s*{프[래|레]+스}?
)
print "bench_press : " , bench_press


def what_exercise(testString):
    mRE = [squat, deadlift, bench_press]
    iterativeCount = 0
    for i in mRE:
        if(re.match(i,testString)):
	    #print "result : ",re.compile(i).findall(testString)
            return Exercise[iterativeCount]
        iterativeCount = iterativeCount + 1
    return None    

def main():
    for i in testString:
        print "i : " , i
        print "ExerciseType : " , (what_exercise(i))

if __name__=='__main__':
    main()
