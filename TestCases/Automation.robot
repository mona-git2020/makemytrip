*** Setting ***
Library		Selenium2Library
Library		String
Variables	Variables/Variables.py
Resource	../Common/Common_Variables.txt

suite setup		open makemytrip

*** Test Cases ***
search hotels functionality
	set selenium speed	2 seconds
	search hotels for destination

*** Keywords ***
open makemytrip
	open browser	${url}		${browser}
	maximize browser window
	
search hotels for destination
	click element	${loginButton}
	click element	${hotelButton}
	click element	${destiName}
#	click element	${hotelButton}
	input text		${enterDesti}	${Destination}
	click element	${selectDesti}
	click element	${checkinDate}
	click element	${checkoutDate}
	click element	${roomGuest}
	${numa}=	convert to string	${adultsnum}
	${Adults}=	replace string	${adults}	NUMA	${numa}
	click element	${Adults}
	${numc}=	convert to string	${childsnum}
	${Childs}=	replace string	${childs}	NUMC	${numc}	
	click element	${childs}
	: FOR	${child_num}	IN RANGE	0	${childsnum}	
	\	${child}=	convert to string	${child_num}
	\	${ChildAge}=	replace string	${childAge}		CHILD		${child}
	\	${age}=		convert to string	${age${child_num}}
	\	${ChildAgeValue}=	replace string	${childAgeValue}	AGE		${age}
	\	${ChildAgeValue}=	replace string	${ChildAgeValue}	CHILD		${child}	
	\	click element	${ChildAge}
	\	click element   ${ChildAgeValue}
	\	${child_num}=	evaluate	${child_num} + 1
	click element	${apply}
	click element	${travellingReason}
	click element	${travellingForLeisure}
	click element	${serachButton}