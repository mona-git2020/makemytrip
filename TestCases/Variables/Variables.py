#*** Variables ***

browser = 'FireFox'
url = 'https://www.makemytrip.com/hotels/hotel-listing/?checkin=07102020&checkout=07122020&locusId=CTDIU&locusType=city&city=CTDIU&country=IN&searchText=Diu%2C%20Daman%20and%20Diu%2C%20India&roomStayQualifier=2e2e11e5e&_uCurrency=INR&reference=hotel&type=city'


destination = 'Diu'
checkin = 'Thu Jul 10 2020'
checkout = 'Thu Jul 12 2020'
adultsnum = 2
childsnum = 2
age0 = 10
age1 = 5
allFilters = ["Popular", "Locality", "Star Category", "User Rating", "Property Types", "Ficility"]

popularFiltersList = ["MMT Assured", "MySafety - Safe and Hygienic Stays", "Pay @ Hotel Available", "EMI Deals Available", "LOW_COST_EMI", "Free Breakfast", "Free Cancellation, Zero Payment Now", "Free Cancellation"]

localityFilterList = ["Diu Airport", "Diu Fort", "Nagoa Beach", "Bandar Chowk"]

starCategoryList = ["Unrated", "4 Star", "3 Star", "2 Star", "1 Star"]

userRatingList = ["4.5", "4.0", "3.0"]

#propertyTypeList = ["Hotel", "RESORT", "HOMESTAY", "APART-HOTEL", "GUEST HOUSE", "Camp", "Farm House"]
propertyTypeList = []

#facilityFilterList = ["Caretaker", "Cafe", "Kitchenette", "Elevator/Lift", "Spa", "Restaurant", "Bar", "Indoor Games", "Parking", "Balcony/Terrace", "Living Room", "Bonfire", "Facilities for Guests with Disabilities", "Swimming Pool", "Wi-Fi", "Barbeque", "Fireplace", "Room Service"]
facilityFilterList = []