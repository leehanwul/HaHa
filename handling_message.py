#-*-coding:utf-8-*-
import re
import regularexpression

NEXT_RECORD = ""

service_type = ["start", "select", "recommend", "stop", "record", "chest", "back", "lower_body", "shoulder"]
basic_element = []
basic_element.append("\\"+u"운".encode('unicode_escape'))	# '운' 0
basic_element.append("\\"+u"동".encode('unicode_escape'))	# '동' 1

def unhandled():
	msg = ("----usage----\n"
		+ "1. " + u"운동 시작할래".encode('unicode_escape') + "\n"	# initiate
		+ "2. " + u"운동 부위 선택".encode('unicode_escape') + "\n"	# select exercise course
		+ "3. " + u"운동 추천 해줘".encode('unicode_escape') + "\n"	# recommend exercise
		+ "4. " + u"운동 그만할래".encode('unicode_escape') + "\n"	# stop exercise
		+ "5. " + u"운동 기록 조회".encode('unicode_escape') + "\n"	# exercise record
		+ "6. " + u"키워드--스쿼트/데드리프트/벤치프레스/etc".encode('unicode_escape') + "\n" 	# keyword searching
	)

	return msg


def get_service_type(message):
	#start keyword
	element = []
	element.append("\\"+u"시".encode('unicode_escape'))	# '시'	0
	element.append("\\"+u"작".encode('unicode_escape'))	# '작'	1
	start_keyword = (".*" +"(" + basic_element[0] +")" + "?" + ".*" + "("+basic_element[1]+")"+ "?" + ".*" + element[0] + "\w*" +element[1] +".*" )	# .*운?.*동?.*시\w*작.*

	#select keyword
	element = []
	element.append("\\"+u"선".encode('unicode_escape'))	# '선'	0
	element.append("\\"+u"택".encode('unicode_escape'))	# '택'	1
	select_keyword = (".*" +"(" + basic_element[0] +")" + "?" + ".*" + "("+basic_element[1]+")"+ "?" + ".*" + element[0] + "\w*" +element[1] +".*" )# .*운?.*동?.*선\w*택.*

	#recommend keyword
	element = []
	element.append("\\"+u"추".encode('unicode_escape'))	# '추'	0
	element.append("\\"+u"천".encode('unicode_escape'))	# '천'	1
	recommend_keyword = (".*" +"(" + basic_element[0] +")" + "?" + ".*" + "("+basic_element[1]+")"+ "?" + ".*" + element[0] + "\w*" +element[1] +".*|" +
			".*" + u"뭐하지".encode('unicode_escape').replace('\\','\\\\') +".*"
 )# .*운?.*동?.*추\w*천.*

	# stop keyword
	element = []
	element.append("\\"+u"그".encode('unicode_escape'))	# '그'	0
	element.append("\\"+u"만".encode('unicode_escape'))	# '만'	1
	stop_keyword = (".*" +"(" + basic_element[0] +")" + "?" + ".*" + "("+basic_element[1]+")"+ "?" + ".*" + element[0] + "\w*" +element[1] +".*" )# .*운?.*동?.*그\w*만.*
	
	# record keyword
	element = []
	element.append("\\"+u"기".encode('unicode_escape'))	# '기'	0
	element.append("\\"+u"록".encode('unicode_escape'))	# '록'	1
	record_keyword = (".*" +"(" + basic_element[0] +")" + "?" + ".*" + "("+basic_element[1]+")"+ "?" + ".*" + element[0] + "\w*" +element[1] +".*|" +
		"("+ u"최근에".encode('unicode_escape').replace('\\','\\\\') +")?" + ".*" + u"뭐했지".encode('unicode_escape').replace('\\','\\\\') +".*"+ "|" +
		".*" +u"뭐 했지".encode('unicode_escape').replace('\\','\\\\')			
	 )# .*운?.*동?.*기\w*록.*
	
	# exercise part expression

	chest = (""
	    + "chest|"
	    + u"가슴".encode('unicode_escape')
	    )
	chest = chest.replace('\\', '\\\\')
	back = (""
	    + "back|"
	    + u"등".encode('unicode_escape')
	    )
	back = back.replace('\\', '\\\\')
	lower_body = (""
	    + "lower\w?[_]?body|"
	    + u"하체".encode('unicode_escape') + "|"
	    + u"하채".encode('unicode_escape')
	    )
	lower_body = lower_body.replace('\\', '\\\\')
	shoulder = (""
	    + "shoulder|"
	    + u"어꺠".encode('unicode_escape') + "|"
	    + u"어께".encode('unicode_escape')+ "|"
	    + u"어깨".encode('unicode_escape')
	    )
	shoulder = shoulder.replace('\\', '\\\\')

	mRE = [start_keyword, select_keyword, recommend_keyword, stop_keyword, record_keyword, chest, back, lower_body, shoulder]
	iterativeCount = 0
	for i in mRE:
	  if(re.match(i,message)):
	    return service_type[iterativeCount]
	  iterativeCount = iterativeCount + 1


	return False

if __name__ == '__main__':
	test = [u"어깨".encode('unicode_escape'), u"등".encode('unicode_escape'),u"가슴".encode('unicode_escape'),
		u"하채".encode('unicode_escape'), u"하체".encode('unicode_escape')
	]

	for i in test:
		print i
		print get_service_type(i)
		
