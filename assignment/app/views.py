from django.shortcuts import render,redirect

def home_view(request):                           
	return render(request,'ui/home.html')

def addcountry(request):                                    
	mycountry = request.POST["country_name"]                        
	Country(country_name = mycountry).save()                      
	return redirect(request.META["HTTP_REFERER"])

def addstate(request):                                    
 	mystate = request.POST["state_name"]                        
 	Country(state_name = mystate).save()                      
 	return redirect(request.META["HTTP_REFERER"])

def addcity(request):                                    
 	mycity = request.POST["city_name"]                        
 	Country(city_name = mycity).save()                      
 	return redirect(request.META["HTTP_REFERER"])

def addlocation(request):                                    
 	mylocation = request.POST["location_name"]                        
 	Country(location_name = mylocation).save()                      
 	return redirect(request.META["HTTP_REFERER"])

def submit(request):
	return render(request,'ui/result.html')




